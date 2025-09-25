from app.use_cases.create_user import CreateUserResult

from .dto import UserResponseDTO


class UserPresenter:
    @staticmethod
    def toHTTP(result: CreateUserResult) -> dict:
        response = UserResponseDTO(
            id=result.user_id,
            name=result.name,
            email=result.email,
            role_id=result.role_id,
            created_at=result.created_at,
            generated_password=result.generated_password,
        )
        return response.model_dump()
