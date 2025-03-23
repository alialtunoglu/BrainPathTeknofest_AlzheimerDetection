from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import numpy as np
import json
from datetime import datetime
from . import predict as handwriting_predict
from . import mrpredict as mr_predict

router = APIRouter()

def combine_predictions(handwriting_prob, mr_prob):
    """
    İki modelin tahminlerini birleştir
    Her iki model de "Hasta" sınıfı için olan olasılığı veriyor
    """
    threshold=0.5
    # Ensemble skoru hesapla (her iki modelin "Hasta" olasılıklarının ortalaması)
    ensemble_score = (handwriting_prob + mr_prob) / 2
    
    # Final tahmin
    predicted_class = "Alzheimer Riski Var" if ensemble_score > 0.5 else "Sağlıklı"
    
    status_mr = "Hasta" if mr_prob > threshold else "Sağlıklı"
    status_handwriting = "Hasta" if handwriting_prob > threshold else "Sağlıklı"

    
    return {
        "prediction": predicted_class,
        "probability": f"{(ensemble_score if ensemble_score > 0.5 else 1 - ensemble_score) * 100:.4f}%",
        "handwriting_probability": f"{(handwriting_prob if handwriting_prob > 0.5 else 1 - handwriting_prob) * 100:.4f}%, Tahmini: {status_handwriting}",
        "mr_probability": f"{(mr_prob if mr_prob > 0.5 else 1 - mr_prob) * 100:.4f}%, Tahmini: {status_mr}"
}

@router.post("/multipredict")
async def predict(
    handwriting_file: UploadFile = File(...),
    mr_file: UploadFile = File(...)
):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        

        # Handwriting tahmini
        hw_response = await handwriting_predict.predict(handwriting_file)
        hw_data = json.loads(hw_response.body.decode())
        hw_prob = hw_data["probability"]
        
        # MR tahmini
        mr_response = await mr_predict.predict(mr_file)
        mr_data = json.loads(mr_response.body.decode())
        mr_prob = mr_data["probability"]
        
        # Tahminleri birleştir
        combined_result = combine_predictions(hw_prob, mr_prob)
        combined_result["timestamp"] = timestamp
        
        return combined_result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 