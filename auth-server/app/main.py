import email
from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.config import settings
from app.db.database import get_db
from app.models import User

from app.routers.auth import router as auth_router

app=FastAPI(title=settings.APP_NAME)

app.include_router(auth_router)

@app.get("/health")
def check():
    return {"status":"ok"}

#Depends(get_db) means:"FastAPI, give this route a database session using get_db()."
@app.get("/db-test")
def db_test(db: Session=Depends(get_db)):
    user=User(
        email="test@gmail.com",
        password_hash="dummy_hash"
    )#Creates a Python User object.
    db.add(user)#I want to insert this object into the database.
    db.commit()#Actually saves the change to PostgreSQL.
    db.refresh(user)#Gets the updated database values back into the Python object — especially the automatically generated id.

    return {
        "id":user.id,
        "email":user.email
        }
