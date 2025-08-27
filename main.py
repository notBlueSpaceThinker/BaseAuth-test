from fastapi import FastAPI
from app.routers import users, docs
import uvicorn


app = FastAPI(docs_url=None, 
              redoc_url=None, 
              openapi_url=None
             )

app.include_router(users.router)
app.include_router(docs.router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True           
    )