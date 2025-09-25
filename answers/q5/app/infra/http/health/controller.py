from fastapi import APIRouter, Depends, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.infra.db.sqlalchemy.db import get_session

from .presenter import HealthPresenter

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/", status_code=status.HTTP_200_OK)
async def health_root() -> dict[str, str]:
    return HealthPresenter.toHTTP_ok()


@router.get("/db", status_code=status.HTTP_200_OK)
async def health_db(session: AsyncSession = Depends(get_session)) -> dict[str, str]:
    await session.execute(text("SELECT 1"))
    return HealthPresenter.toHTTP_ok()
