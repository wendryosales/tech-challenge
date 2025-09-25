from app.domain.entities.user import UserEntity
from app.infra.db.sqlalchemy.models.user import UserModel


class UserMapper:
    @staticmethod
    def to_domain(row: UserModel) -> UserEntity:
        return UserEntity(
            id=row.id,
            name=row.name,
            email=row.email,
            role_id=row.role_id,
            password=None,
            created_at=row.created_at,
            updated_at=row.updated_at,
        )

    @staticmethod
    def to_persistence(entity: UserEntity) -> UserModel:
        return UserModel(
            name=entity.name,
            email=entity.email,
            password=entity.password or "",
            role_id=entity.role_id,
        )


