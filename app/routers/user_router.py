from typing import List
from fastapi import APIRouter,HTTPException
from app.models.user_model import User, UserCreate

router = APIRouter(prefix="/users",tags=["Users"])

users = []

@router.post("",response_model=User)
def create_user(user:UserCreate):
    new_user = User(id=len(users)+1,**user.model_dump())
    users.append(new_user)
    return new_user

@router.get("/{user_id}",response_model=User)
def get_user(user_id:int):
    for user in users:
        if(user.id == user_id):
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.get("", response_model=List[User])
def get_all_users():
    return users
