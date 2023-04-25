from typing import Any

from pydantic import BaseSettings
from sqlalchemy import delete, select, text, update
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

Base: Any = declarative_base()


class Settings(BaseSettings):
    db_driver: str = ''
    db_port: int = 5432
    db_host: str = ''
    db_database: str = ''
    db_username: str = ''
    db_password: str = ''


class Database:
    def __init__(self) -> None:
        self.settings = Settings()
        self.engine: AsyncEngine = self.get_engine()
        self.session: async_sessionmaker = async_sessionmaker(
            self.engine, expire_on_commit=False
        )

    def get_url(self) -> URL:
        return URL.create(
            drivername=self.settings.db_driver,
            username=self.settings.db_username,
            password=self.settings.db_password,
            host=self.settings.db_host,
            port=self.settings.db_port,
            database=self.settings.db_database,
        )

    def get_engine(self) -> AsyncEngine:
        return create_async_engine(
            url=self.get_url(),
            pool_pre_ping=True,
            echo=False,
            pool_recycle=300,
            pool_size=20,
            max_overflow=20,
        )

    async def create_tables(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def drop_tables(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    async def select_where(self, table, where) -> Any:
        async with self.session() as session:
            return (await session.execute(select(table).where(where))).fetchone()

    async def execute(self, query) -> None:
        async with self.session() as session:
            await session.execute(text(query))
            await session.commit()

    async def select_all(self, table, order) -> Any:
        async with self.session() as session:
            result = await session.execute(select(table).order_by(order))
            return result.scalars().all()

    async def select_all_where(self, table, where) -> Any:
        async with self.session() as session:
            result = await session.execute(select(table).where(where))
            return result.scalars().all()

    async def add(self, row) -> Any | None:
        async with self.session() as session:
            session.add(row)
            await session.commit()
            await session.refresh(row)
            return row

    async def update_where(self, table, values, where) -> None:
        async with self.session() as session:
            await session.execute(update(table).where(where).values(values))
            await session.commit()

    async def delete(self, table, where) -> None:
        async with self.session() as session:
            await session.execute(delete(table).where(where))
            await session.commit()
