import joblib
import pickle
from pathlib import Path
from catboost import CatBoostClassifier
from datetime import datetime

class ModelManager:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.model_dir = self.base_dir / "saved"
        self.model_dir.mkdir(parents=True, exist_ok=True)
        
        # En son modeli yükle
        self.model = self._load_latest_model()
        self.scaler = self._load_component("scaler.pkl")
        self.pca = self._load_component("pca.pkl")
        self.low_variance_features = self._load_component("low_variance_features.pkl")
    
    def _load_latest_model(self):
        """En son kaydedilen modeli yükle"""
        try:
            return joblib.load(self.model_dir / "best_model.pkl")
        except:
            return CatBoostClassifier(verbose=0)
    
    def _load_component(self, filename):
        """Modelin bileşenlerini yükle"""
        try:
            with open(self.model_dir / filename, "rb") as f:
                return pickle.load(f)
        except:
            return None
    
    def save_model(self, model, scaler, pca, low_variance_features):
        """Modeli ve bileşenlerini kaydet"""
        # Yeni model versiyonu oluştur
        version = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Ana modeli kaydet
        joblib.dump(model, self.model_dir / "best_model.pkl")
        joblib.dump(model, self.model_dir / f"model_v{version}.pkl")
        
        # Bileşenleri kaydet
        with open(self.model_dir / "scaler.pkl", "wb") as f:
            pickle.dump(scaler, f)
        
        with open(self.model_dir / "pca.pkl", "wb") as f:
            pickle.dump(pca, f)
            
        with open(self.model_dir / "low_variance_features.pkl", "wb") as f:
            pickle.dump(low_variance_features, f)
        
        # Sınıf değişkenlerini güncelle
        self.model = model
        self.scaler = scaler
        self.pca = pca
        self.low_variance_features = low_variance_features
        
        return version
    
    def get_model(self):
        """Güncel modeli ve bileşenlerini döndür"""
        return {
            "model": self.model,
            "scaler": self.scaler,
            "pca": self.pca,
            "low_variance_features": self.low_variance_features
        }

# Singleton model manager instance
model_manager = ModelManager() 