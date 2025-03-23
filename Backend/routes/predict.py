from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import io
from pathlib import Path
from datetime import datetime

from models.model import model_manager
from utils.preprocess import save_upload_file, validate_data, preprocess_data, clean_old_files

router = APIRouter()

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Dosya uzantısını kontrol et
        if not file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, detail="Sadece CSV dosyaları kabul edilir")
        

         # Dosya içeriğini belleğe al
        contents = await file.read()  # bytes
        
        # Bellekten oku (decode -> StringIO -> pandas)
        data = pd.read_csv(io.StringIO(contents.decode('utf-8')))
        
        # Dosyayı geçici olarak kaydet
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        '''
        upload_dir = Path("data/uploaded_files")
        file_path = upload_dir / f"predict_{timestamp}.csv"
        await save_upload_file(file, file_path)
        
        # Eski dosyaları temizle
        clean_old_files(upload_dir)
        
        # Veriyi oku
        data = pd.read_csv(file_path)
        '''
        # Veriyi doğrula
        validate_data(data, is_training=False)
        
        # Veriyi ön işle
        data, _ = preprocess_data(data, is_training=False)
        
        # Model bileşenlerini al
        components = model_manager.get_model()
        
        # Low variance özelliklerini kaldır
        data = data.drop(columns=components["low_variance_features"])
        
        # Özellikleri ölçeklendir
        scaled_features = components["scaler"].transform(data)
        
        # PCA dönüşümü uygula
        pca_features = components["pca"].transform(scaled_features)
        
        # Tahmin yap
        prediction = components["model"].predict(pca_features)
        #print(prediction)
        proba = components["model"].predict_proba(pca_features)
        probability = proba[:, 1]
        print(probability[0])

        prediction_proba = components["model"].predict_proba(pca_features)
        
        # Sonuçları hazırla
        prediction = int(prediction[0])
        #probability = float(max(prediction_proba[0]))
        if prediction == 0 :
            status=f"{(proba[:, 0][0])*100:.2f} Doğrulukla Sağlıklı"
        else:
            status=f"{(proba[:, 1][0])*100:.2f} Doğrulukla Hasta"


        return JSONResponse({
            "prediction": status,
            "probability": probability[0],
            "timestamp": timestamp
        })
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 