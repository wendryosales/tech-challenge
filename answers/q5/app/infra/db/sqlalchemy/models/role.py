from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infra.db.sqlalchemy.base import Base


class RoleModel(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(String, nullable=False)
