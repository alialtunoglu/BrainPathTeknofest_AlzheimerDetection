from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import predict, train, mrpredict, multipredict

app = FastAPI(
    title="Alzheimer Detection API",
    description="API for Alzheimer's disease detection using machine learning",
    version="1.0.0"
)

# CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Production'da spesifik domainler belirtilmeli
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route'ları ekle
app.include_router(predict.router, prefix="/api/v1", tags=["predictions"])
app.include_router(train.router, prefix="/api/v1", tags=["training"])
app.include_router(mrpredict.router, prefix="/api/v1", tags=["mr_predictions"])
app.include_router(multipredict.router, prefix="/api/v1", tags=["ensemble_predictions"])

# Ana sayfa
@app.get("/")
async def root():
    return {
        "message": "Alzheimer Detection API",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 