from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, EmailStr, Field, StringConstraints

NameStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class UserCreateDTO(BaseModel):
    name: NameStr
    email: EmailStr
    role_id: int
    password: str | None = Field(default=None, min_length=8)


class UserResponseDTO(BaseModel):
    id: int
    name: str
    email: EmailStr
    role_id: int
    created_at: datetime
    generated_password: str | None = None
