from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.repositories.user_repository import UserRepositoryPort
from app.infra.db.sqlalchemy.db import get_session
from app.infra.db.sqlalchemy.repositories.user_repository import SqlAlchemyUserRepository
from app.infra.security.bcrypt_hasher import BcryptPasswordHasher
from app.use_cases.create_user import CreateUser

from .dto import UserCreateDTO, UserResponseDTO
from .mappers import UserMapper
from .presenter import UserPresenter

router = APIRouter(prefix="/v1", tags=["users"])


def get_user_repo(session: AsyncSession = Depends(get_session)) -> UserRepositoryPort:
    return SqlAlchemyUserRepository(session)


@router.post("/users", response_model=UserResponseDTO, status_code=status.HTTP_201_CREATED)
async def create_user_endpoint(
    request: Request,
    body: UserCreateDTO,
    repo: UserRepositoryPort = Depends(get_user_repo),
):
    use_case = CreateUser(repo, BcryptPasswordHasher())
    try:
        command = UserMapper.to_command(body)
        result = await use_case.execute(command)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except PermissionError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except RuntimeError:
        raise HTTPException(status_code=409, detail="could not create user")

    return UserPresenter.toHTTP(result)
