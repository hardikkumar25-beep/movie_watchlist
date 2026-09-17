from fastapi import APIRouter, HTTPException,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schema import UserCreate, UserResponse
from ..model import User

router=APIRouter(prefix="/users",tags=["Users"])

@router.post("/",response_model=UserResponse)
def create_user(user:UserCreate, db: Session=Depends(get_db)):
    new_user=User(username=user.username,email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
