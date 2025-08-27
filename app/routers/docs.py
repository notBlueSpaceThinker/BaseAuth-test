from fastapi import APIRouter, Depends, Request
from fastapi.openapi.docs import get_swagger_ui_html
from app.schemas.user import User
from app.auth import authenticate_doc, hide_doc

router = APIRouter(tags=["docs"])

@router.get("/docs", include_in_schema=False, 
            dependencies=[Depends(hide_doc), Depends(authenticate_doc)])
async def docs_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="API Docs"
    )

@router.get("/openapi.json", include_in_schema=False,
            dependencies=[Depends(hide_doc), Depends(authenticate_doc)])
async def openapi_json(request: Request):
    return  request.app.openapi()