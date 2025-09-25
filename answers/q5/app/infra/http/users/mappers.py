from app.use_cases.create_user import CreateUserCommand

from .dto import UserCreateDTO


class UserMapper:
    @staticmethod
    def to_command(dto: UserCreateDTO) -> CreateUserCommand:
        return CreateUserCommand(name=dto.name, email=dto.email, role_id=dto.role_id, password=dto.password)
