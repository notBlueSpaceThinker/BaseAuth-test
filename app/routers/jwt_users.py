from fastapi import APIRouter, Depends
from app.schemas.user import UserInDB
from app.auth import authenticate_user
from app.security import create_jwt_token


router = APIRouter()

@router.post('/protected_login')
async def login(user: UserInDB = Depends(authenticate_user)):
    return {"access_token": create_jwt_token({"sub": UserInDB.username})}

@router.get("/protected_resource")
async def get_user():
    pass