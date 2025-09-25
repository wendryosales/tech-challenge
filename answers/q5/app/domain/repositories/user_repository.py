from abc import ABC, abstractmethod

from app.domain.entities.user import UserEntity


class UserRepositoryPort(ABC):
    @abstractmethod
    async def get_by_email(self, email: str) -> UserEntity | None: ...

    @abstractmethod
    async def role_exists(self, role_id: int) -> bool: ...

    @abstractmethod
    async def create(self, user: UserEntity) -> UserEntity: ...
