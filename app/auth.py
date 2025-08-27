from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.schemas.user import UserInDB
from app.security import hash_password, verify_password
from app.config import load_config


CONFIG = load_config()

security = HTTPBasic()
fake_users_db: list[UserInDB] = []

def search_user(username: str) -> UserInDB | None:
    for user in fake_users_db:
        if user.username == username:
            return user
    return None

def register_user(username: str, password: str) -> UserInDB:
    hashed = hash_password(password)
    user = UserInDB(username=username, hashed_password=hashed)
    fake_users_db.append(user)
    return user

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)) -> UserInDB:
    user = search_user(credentials.username)
    if user and verify_password(credentials.password, user.hashed_password):
        return user
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        headers={"WWW-Authenticate": "Basic"},
        detail="Invalid credentials"
    )


def authenticate_doc(credentials: HTTPBasicCredentials = Depends(security)) -> None:
    if credentials.username == CONFIG.DOCS_USER and credentials.password == CONFIG.DOCS_PASSWORD:
        return None
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        headers={"WWW-Authenticate": "Basic"},
        detail="Invalid credentials"
    )

def hide_doc() -> None:
    if CONFIG.MODE == 'PROD':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)