import pandas as pd
from sklearn.preprocessing import LabelEncoder
from typing import Tuple, Any
import os
from pathlib import Path
import aiofiles

async def save_upload_file(upload_file: Any, destination: Path) -> Path:
    """Yüklenen dosyayı geçici klasöre kaydet"""
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        
        # Dosyayı oku
        contents = await upload_file.read()
        
        # Dosyayı asenkron olarak kaydet
        async with aiofiles.open(str(destination), 'wb') as out_file:
            await out_file.write(contents)
            
        return destination
    finally:
        await upload_file.close()

def clean_old_files(directory: Path, max_files: int = 10):
    """Geçici klasördeki eski dosyaları temizle"""
    files = list(directory.glob("*.csv"))
    if len(files) > max_files:
        # Dosyaları oluşturulma tarihine göre sırala
        files.sort(key=lambda x: x.stat().st_ctime)
        # En eski dosyaları sil
        for file in files[:-max_files]:
            file.unlink()

def preprocess_data(data: pd.DataFrame, is_training: bool = False) -> Tuple[pd.DataFrame, Any]:
    """Veriyi ön işleme"""
    # ID sütununu kaldır
    if 'ID' in data.columns:
        data = data.drop('ID', axis=1)
    
    # Eğitim modunda class sütununu ayır
    y = None
    if is_training:
        if 'class' not in data.columns:
            raise ValueError("Eğitim verisi 'class' sütunu içermelidir")
        
        y = data['class']
        # Sınıf etiketlerini sayısal formata dönüştür
        le = LabelEncoder()
        y = le.fit_transform(y)
        data = data.drop('class', axis=1)
    else:
        # Tahmin modunda class sütunu varsa kaldır
        if 'class' in data.columns:
            data = data.drop('class', axis=1)
    
    return data, y

def validate_data(data: pd.DataFrame, is_training: bool = False) -> bool:
    """Veri doğrulama"""
    # Gerekli sütunların varlığını kontrol et
    if is_training and 'class' not in data.columns:
        raise ValueError("Eğitim verisi 'class' sütunu içermelidir")
    
    try:
        # Sayısal olmayan sütunları sayısala çevirmeye çalış
        for col in data.columns:
            if col != 'class' and col != 'ID':
                data[col] = pd.to_numeric(data[col])
    except Exception as e:
        raise ValueError(f"Sayısal dönüşüm hatası: {str(e)}")
    
    # Eksik değerleri kontrol et
    if data.isnull().any().any():
        raise ValueError("Veri seti eksik değerler içermemelidir")
    
    return True 