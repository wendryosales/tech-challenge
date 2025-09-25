import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context

# Importa Base e models para autogenerate
from app.infra.db.sqlalchemy.base import Base
from app.infra.db.sqlalchemy.models import claim as _claim  # noqa: F401
from app.infra.db.sqlalchemy.models import role as _role  # noqa: F401
from app.infra.db.sqlalchemy.models import user as _user  # noqa: F401
from app.infra.db.sqlalchemy.models import user_claim as _user_claim  # noqa: F401

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Base.metadata para autogenerate
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    url = os.getenv("ALEMBIC_DATABASE_URL", config.get_main_option("sqlalchemy.url"))
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    configuration = config.get_section(config.config_ini_section, {})
    configuration["sqlalchemy.url"] = os.getenv("ALEMBIC_DATABASE_URL", configuration.get("sqlalchemy.url"))

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
