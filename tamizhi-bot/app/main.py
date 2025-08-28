from fastapi import FastAPI
from loguru import logger

from app.api.routes import router


def create_app() -> FastAPI:
    """Create and configure FastAPI application instance."""
    application = FastAPI(title="Tamizhi BOT", version="0.1.0")

    # Routers
    application.include_router(router)

    @application.get("/")
    async def root() -> dict:
        return {"message": "Tamizhi BOT API"}

    return application


app = create_app()

@app.on_event("startup")
async def on_startup() -> None:
    logger.info("Tamizhi BOT API starting up")

@app.on_event("shutdown")
async def on_shutdown() -> None:
    logger.info("Tamizhi BOT API shutting down")

