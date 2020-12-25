from starlette.requests import Request
from starlette.responses import RedirectResponse

from app.lib.config import configuration
from app.lib.authentication import get_client
from app.lib.image_service import base64_to_url
from app.models.image import ImageCreationResponse
from app.main import app

@app.get('/{url_path:path}', response_class=RedirectResponse)
async def get(request: Request, url_path="^((.*)(/))?$"):
    """
    Get an image
    Return static file
    """
    return RedirectResponse(url=f'/static/{url_path}')

from fastapi import Request, Depends, Response, Query

from fastapi.security import HTTPBearer
auth_scheme = HTTPBearer()

@app.post("/create", response_model=ImageCreationResponse)
async def post(request: Request, data: dict = {}, token: str = Depends(auth_scheme)):
    """
    Create an image
    Return URL
    """
    client_id = await get_client(token.credentials)

    return ImageCreationResponse(url=f"https://{configuration.service_domain}/{base64_to_url(data, client_id)}")


