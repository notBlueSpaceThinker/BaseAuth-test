from passlib.context import CryptContext
from fastapi import status, HTTPException
import jwt 
from app.config import load_token_config

pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_jwt_token(data: dict) -> str:
    token_config = load_token_config()
    return jwt.encode(data, token_config.SECRET_KEY, algorithms=[token_config.ALGORITHM])

def get_user_from_token(token: str):
    token_config = load_token_config
    try:
        payload = jwt.decode(token, token_config.SECRET_KEY, algorithms=[token_config.ALGORITHM])
        return payload.get("sub")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e)
