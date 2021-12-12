# built-in modules
import os

# third party modules
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql+asyncpg://{}:{}@{}/{}".format(
    os.environ['POSTGRES_USER'],
    os.environ['POSTGRES_PASSWORD'],
    os.environ['DB_HOST'],
    os.environ['POSTGRES_DB'],
)

engine = create_async_engine(DATABASE_URL, echo=True, future=True)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session