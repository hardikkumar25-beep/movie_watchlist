from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr

router=APIRouter(prefix="/users")

class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    id:int
    username:str
    email:EmailStr
user_db={}

@router.post("",response_model=UserResponse)
def create_user(user_data:UserCreate):
    for user in user_db.values():
        if user["username"]==user_data.username:
            raise HTTPException(status_code=400, detail="Username already registered")
        if user["email"]==user_data.email:
            raise HTTPException(status_code=400, detail="Email already registered")

    new_user_id=len(user_db)+1
    new_user={
        "id":new_user_id,
        "username":user_data.username,
        "email":user_data.email,
        "password":user_data.password
    }
    user_db[new_user_id]=new_user
    return new_user

