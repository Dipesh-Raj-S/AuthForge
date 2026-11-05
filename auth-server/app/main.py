from fastapi import FastAPI
from app.config import settings

app=FastAPI(title=settings.app_name,description="OAuth 2.0 and OpenID Connect Authorization Server", version=settings.app_version)

@app.get("/health")
def health_check():
    return {
        "status":"healthy",
        "service":settings.app_name
    }