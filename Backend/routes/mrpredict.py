from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np
import io
import os
from pathlib import Path
from datetime import datetime
# TensorFlow log seviyesini ayarla
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

router = APIRouter()

# Model dosya yolu
MODEL_PATH = Path(__file__).parent.parent / "models" / "saved" / "mr_model" / "cnn_alzheimer.h5"

# Modeli yükle
model = load_model(str(MODEL_PATH))

class_names = ['Non Demented', 'Very Mild Demented']

def prepare_image(img_bytes):
    """Görseli modelin beklediği formata çevir"""
    img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
    img = img.resize((128, 128))  # modelin eğitim boyutuna göre
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalizasyon
    return img_array

@router.post("/mrpredict")
async def predict(file: UploadFile = File(...)):
    try:
        # Dosya uzantısını kontrol et
        if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            raise HTTPException(status_code=400, detail="Sadece PNG ve JPG dosyaları kabul edilir")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Görseli oku ve hazırla
        img_bytes = await file.read()
        img_array = prepare_image(img_bytes)

        # Tahmin yap
        predictions = model.predict(img_array)
        confidence = float(predictions[0][0])
        
        predicted_class = "Hasta" if confidence > 0.5 else "Sağlıklı"
        probability = float(confidence) if predicted_class == "Hasta" else float(1 - confidence)

        return JSONResponse(content={
            "prediction": predicted_class,
            "probability": f"{probability:.2%}",  # Yüzde formatında olasılık
            "timestamp": timestamp  # Ham olasılık değeri
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 