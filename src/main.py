from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.chat.router import chat_router
from src.html.router import index_router

from .config.settings import STATIC_FILES_DIR


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        FastAPI: The configured FastAPI application instance.
    """
    app = FastAPI()

    # Mount static files directory
    app.mount("/static", StaticFiles(directory=STATIC_FILES_DIR), name="static")

    # Include routers for API and HTML endpoints
    app.include_router(chat_router)
    app.include_router(index_router)

    return app


app = create_app()
