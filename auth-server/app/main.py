from fastapi import FastAPI

app=FastAPI(title="AuthForge",description="OAuth 2.0 and OpenID Connect Authorization Server", version="1.0.0")

@app.get("/health")
def health_check():
    return {
        "status":"healthy",
        "service":"AuthForge"
    }