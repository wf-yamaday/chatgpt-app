from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import Response

from src.config.vite import ViteAssetsLoader

templates = Jinja2Templates(directory="assets/templates")

index_router = APIRouter()


@index_router.get("/", response_class=HTMLResponse)
def index(request: Request) -> Response:
    """
    Serves the main HTML page, injecting the Vite-generated CSS and JavaScript files.

    Args:
        request (Request): The incoming request object.

    Returns:
        Response: The rendered HTML response with injected Vite assets.
    """
    vite_assets = ViteAssetsLoader()
    vite_assets.load_manifest()
    css_file_name = vite_assets.generate_css_file_name()
    js_file_name = vite_assets.generate_js_file_name()

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "css_file": css_file_name, "js_file": js_file_name},
    )
