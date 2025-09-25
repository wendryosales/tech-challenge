from passlib.context import CryptContext

from app.domain.security.password_hasher import PasswordHasherPort


class BcryptPasswordHasher(PasswordHasherPort):
    def __init__(self) -> None:
        self._ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash(self, raw: str) -> str:
        return self._ctx.hash(raw)

    def verify(self, raw: str, hashed: str) -> bool:
        return self._ctx.verify(raw, hashed)
