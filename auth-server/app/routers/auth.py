from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.services.user_service import create_user,authenticate_user
from app.schemas.auth import RegisterRequest,LoginRequest
 

router=APIRouter()

@router.post("/register")
def register(
    data:RegisterRequest,
    db: Session=Depends(get_db)
):
    user=create_user(
        db,data.email,data.password
    )
    if user is None:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )
        
        

    return{
        "id":user.id,
        "email":user.email
    }

@router.post("/login")
def login(
    data:LoginRequest,
    db:Session=Depends(get_db)
):
    user=authenticate_user(db,data.email,data.password)
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    return{
        "message":"Login successful",
        "user_id":user.id,
        "email":user.email
    }

