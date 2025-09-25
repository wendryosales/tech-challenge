from fastapi import FastAPI

from .core.logging import setup_logging
from .infra.http.health.controller import router as health_router
from .infra.http.users.controller import router as users_router

setup_logging()
app = FastAPI(title="Q5 User API", version="0.1.0", docs_url="/docs", redoc_url="/redoc")
app.include_router(users_router)
app.include_router(health_router)
