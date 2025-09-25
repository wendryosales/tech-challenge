from dataclasses import dataclass
from datetime import datetime, timezone

from app.domain.value_objects.email import Email


@dataclass
class UserEntity:
    id: int
    name: str
    email: str
    role_id: int
    password: str | None
    created_at: datetime
    updated_at: datetime | None

    @staticmethod
    def create(*, name: str, email: str, role_id: int, now: datetime | None = None) -> "UserEntity":

        ts = now or datetime.now(timezone.utc)
        normalized_email = str(Email(email))
        # id is assigned by repository/DB; use 0 as placeholder
        return UserEntity(
            id=0,
            name=name.strip(),
            email=normalized_email,
            role_id=role_id,
            password=None,
            created_at=ts,
            updated_at=None,
        )
