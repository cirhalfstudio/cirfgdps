from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .app.core.config import Config
from .app.core.di import container
from .app.core.services.players.presentation.api.routers.cirf import players_router
from .app.core.services.players.presentation.api.routers.gd import accounts_router
from .app.core.shared.utils import TraceIDMiddleware, lifespan

app = FastAPI(
    lifespan=lifespan,
    title=Config.APP_NAME,
    description=Config.APP_DESCRIPTION,
    version=Config.APP_VERSION,
    docs_url="/docs" if Config.ENABLE_API_DOCS else None,
    redoc_url="/redoc" if Config.ENABLE_API_DOCS else None,
    openapi_url="/openapi.json" if Config.ENABLE_API_DOCS else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.add_middleware(TraceIDMiddleware)

app.include_router(players_router)
app.include_router(accounts_router)

setup_dishka(container=container, app=app)
