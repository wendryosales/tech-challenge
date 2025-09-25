from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.infra.db.sqlalchemy.base import Base


class UserClaimModel(Base):
    __tablename__ = "user_claims"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    claim_id: Mapped[int] = mapped_column(ForeignKey("claims.id"), primary_key=True)
