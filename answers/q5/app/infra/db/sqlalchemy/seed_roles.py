import asyncio

from sqlalchemy import select

from app.infra.db.sqlalchemy.db import get_session
from app.infra.db.sqlalchemy.models.role import RoleModel

ROLES = ["admin", "manager", "user"]


async def seed_roles() -> None:
    async for session in get_session():
        existing = {r[0] for r in (await session.execute(select(RoleModel.description))).all()}
        created = 0
        for desc in ROLES:
            if desc in existing:
                continue
            role = RoleModel(description=desc)
            session.add(role)
            created += 1
        if created:
            await session.commit()
        print(f"seeded roles: +{created}, skipped: {len(ROLES) - created}")


if __name__ == "__main__":
    asyncio.run(seed_roles())
