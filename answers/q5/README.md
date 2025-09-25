# Questão 5 — API de Criação de Usuário

Arquitetura DDD/Hexagonal com ports & adapters.

Mesmo sendo só criação de usuário, optei por explorar possibilidades para trazer mais insumo para discussão. E para mostrar um pouco de como o projeto pode crescer. Em um projeto real, essa não seria a abordagem adotada para coisas pequenas e simples.

Estrutura principal:
- `infra/http`: controllers por recurso, DTOs, mappers e presenters
- `use_cases`: casos de uso (ex.: `create_user.py`)
- `domain`: entidades, value objects e portas (ex.: `UserEntity`, `Email`, `UserRepositoryPort`, `PasswordHasherPort`)
- `infra/db/sqlalchemy`: models, repositories e mappers (ex.: `UserModel`, `SqlAlchemyUserRepository`, `UserMapper`)
- `core`: utilidades (ex.: `PasswordGenerator`)

## Como executar
1. cp .env.example .env
2. poetry install --with dev
3. docker compose up -d db
4. export ALEMBIC_DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/tech_challenge
5. make alembic-rev
6. make alembic-up
7. make seed-roles  # Para criar algumas roles padrão
8. make run

Env var principal: `DATABASE_URL`. Para autogenerate do Alembic, também pode usar `ALEMBIC_DATABASE_URL`.

Testes e lint:
- `make test` para executar os testes
- `make format` e `make lint` para formatar e checar

## Endpoint
- POST `/v1/users`
  - body: `{ name, email, role_id, password? }`
  - 201 com `generated_password` se criada automaticamente

## Decisões

Arquitetura:
- Camadas com ports & adapters: domínio independente de frameworks.
- Use cases recebem portas por injeção (ex.: `UserRepositoryPort`, `PasswordHasherPort`).

Hash de senha:
- BCrypt via Passlib (padrão).
- Geração de senha temporária com `PasswordGenerator` (interno), length configurável em `settings.password_length`.

```



