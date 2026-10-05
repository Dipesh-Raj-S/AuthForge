from sqlalchemy.orm import Session

from app.repositories.user_repository import get_user_by_email
from app.models import User
from app.security.password import hash_password
from app.security.password import verify_password


def create_user(
    db: Session,
    email: str,
    password: str
):
    existing_user = get_user_by_email(db, email)

    if existing_user:
        return None

    password_hash=hash_password(password)
    user = User(
        email=email,
        password_hash=password_hash
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def authenticate_user(
    db:Session,
    email=str,
    password=str
):
    user=get_user_by_email(db,email)

    if user is None:
        return None
    
    if not verify_password(password,user.password_hash):
        return None
    
    return user
