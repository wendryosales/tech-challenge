from datetime import date, datetime

from sqlalchemy import BigInteger, Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infra.db.sqlalchemy.base import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column("name", String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)
    created_at: Mapped[date] = mapped_column(Date, nullable=False, default=lambda: datetime.utcnow().date())
    updated_at: Mapped[date | None] = mapped_column(Date, nullable=True)

    role = relationship("RoleModel")
