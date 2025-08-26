from fastapi import APIRouter, Depends
from app.schemas.user import User
from app.auth import register_user, authenticate_user


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register")
async def register(user: User):
    register_user(user.username, user.password)
    return {"message": f"User {user.username} successfully registered"}

@router.get("/login")
async def login(user: User = Depends(authenticate_user)):
    return {"message": f"Welcome, {user.username}"}
