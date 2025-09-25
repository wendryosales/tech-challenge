import pytest

from app.domain.entities.user import UserEntity
from app.domain.repositories.user_repository import UserRepositoryPort
from app.domain.security.password_hasher import PasswordHasherPort
from app.use_cases.create_user import CreateUser, CreateUserCommand


class InMemoryRepo(UserRepositoryPort):
    def __init__(self) -> None:
        self.users: dict[str, UserEntity] = {}
        self.roles = {1}
        self._id = 0

    async def get_by_email(self, email: str):
        return self.users.get(email)

    async def role_exists(self, role_id: int) -> bool:
        return role_id in self.roles

    async def create(self, user: UserEntity) -> UserEntity:
        self._id += 1
        stored = UserEntity(
            id=self._id,
            name=user.name,
            email=user.email,
            role_id=user.role_id,
            created_at=__import__("datetime").datetime.utcnow(),
        )
        self.users[user.email] = stored
        return stored


class FakeHasher(PasswordHasherPort):
    def hash(self, raw: str) -> str:
        return "hashed:" + raw

    def verify(self, raw: str, hashed: str) -> bool:
        return hashed == "hashed:" + raw


@pytest.mark.asyncio
async def test_create_user_generates_password_when_missing():
    repo = InMemoryRepo()
    hasher = FakeHasher()
    uc = CreateUser(repo, hasher)
    res = await uc.execute(CreateUserCommand(name="A", email="a@a.com", role_id=1, password=None))
    assert res.user_id == 1
    assert res.generated_password is not None
