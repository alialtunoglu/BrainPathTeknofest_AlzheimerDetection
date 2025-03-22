from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from pathlib import Path
from datetime import datetime

from models.model import model_manager
from utils.preprocess import save_upload_file, validate_data, preprocess_data, clean_old_files

router = APIRouter()

@router.post("/retrain")
async def retrain(file: UploadFile = File(...)):
    try:
        # Dosya uzantısını kontrol et
        if not file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, detail="Sadece CSV dosyaları kabul edilir")
        
        # Dosyayı geçici olarak kaydet
        upload_dir = Path("data/uploaded_files")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = upload_dir / f"train_{timestamp}.csv"
        await save_upload_file(file, file_path)
        
        # Eski dosyaları temizle
        clean_old_files(upload_dir)
        
        # Veriyi oku
        data = pd.read_csv(file_path)
        
        # Veriyi doğrula
        validate_data(data, is_training=True)
        
        # Veriyi ön işle
        X, y = preprocess_data(data, is_training=True)
        
        # Model bileşenlerini al
        components = model_manager.get_model()
        
        # Low variance özelliklerini kaldır
        X = X.drop(columns=components["low_variance_features"])
        
        # Özellikleri ölçeklendir
        X_scaled = components["scaler"].fit_transform(X)
        
        # PCA dönüşümü uygula
        X_pca = components["pca"].fit_transform(X_scaled)
        
        # Modeli yeniden eğit
        components["model"].fit(X_pca, y)
        
        # Güncellenmiş modeli kaydet
        version = model_manager.save_model(
            model=components["model"],
            scaler=components["scaler"],
            pca=components["pca"],
            low_variance_features=components["low_variance_features"]
        )
        
        return JSONResponse({
            "message": "Model başarıyla güncellendi",
            "version": version,
            "timestamp": timestamp
        })
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 