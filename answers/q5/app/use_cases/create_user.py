from dataclasses import dataclass
from datetime import datetime

from app.config import settings
from app.core.utils.passwords import PasswordGenerator
from app.domain.entities.user import UserEntity
from app.domain.repositories.user_repository import UserRepositoryPort
from app.domain.security.password_hasher import PasswordHasherPort


@dataclass(frozen=True)
class CreateUserCommand:
    name: str
    email: str
    role_id: int
    password: str | None = None


@dataclass(frozen=True)
class CreateUserResult:
    user_id: int
    name: str
    email: str
    role_id: int
    created_at: datetime
    generated_password: str | None


class CreateUser:
    def __init__(self, repository: UserRepositoryPort, hasher: PasswordHasherPort) -> None:
        self.repository = repository
        self.hasher = hasher

    async def execute(self, command: CreateUserCommand) -> CreateUserResult:
        if not await self.repository.role_exists(command.role_id):
            raise PermissionError("role not found")

        user = UserEntity.create(name=command.name, email=command.email, role_id=command.role_id)

        if await self.repository.get_by_email(user.email):
            raise RuntimeError("email already in use")

        raw_password = command.password or PasswordGenerator.generate(settings.password_length)
        password_hash = self.hasher.hash(raw_password)

        user.password = password_hash
        user = await self.repository.create(user)

        return CreateUserResult(
            user_id=user.id,
            name=user.name,
            email=user.email,
            role_id=user.role_id,
            created_at=user.created_at,
            generated_password=None if command.password else raw_password,
        )
