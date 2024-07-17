# -*- coding: utf-8 -*-
from sqlalchemy import Column, DateTime, ForeignKey, Text, Boolean, String, BigInteger, SmallInteger, Time, Date, UUID
from sqlalchemy import func, select, update, insert, case, desc, delete, null, or_, and_, text
from typing import AsyncGenerator
from contextlib import asynccontextmanager
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncAttrs, AsyncSession
import main.config as config
from datetime import datetime, time, timedelta
from typing import Type


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Tokens(Base):
    __tablename__ = 'tokens'
    id = Column(BigInteger, primary_key=True)
    token = Column(UUID(as_uuid=False), unique=True, nullable=False, index=True, server_default=text('uuid_generate_v4()'))
    datetime_create = Column(
        DateTime,
        default=func.now(),
        server_default=text('(now() AT TIME ZONE \'Asia/Novosibirsk\')'),
        nullable=False
    )
    ip = Column(String(length=255), nullable=False)
    user_agent = Column(String(length=255), nullable=False)

    @classmethod
    async def del_(cls, token: str | None = None, ip: str | None = None):
        where_ = []
        if token is not None:
            where_.append(cls.token == token)
        if ip is not None:
            where_.append(cls.ip == ip)
        async with get_async_session() as session:
            await session.execute(delete(cls).where(*where_))
            await session.commit()

    @classmethod
    async def add_(cls, token: str, ip: str, user_agent: str):
        async with get_async_session() as session:
            await session.execute(insert(cls).values(token=token, ip=ip, user_agent=user_agent))
            await session.commit()

    @classmethod
    async def get_(cls, token: str | None = None, ip: str | None = None, user_agent: str | None = None):
        where_ = []
        if token is not None:
            where_.append(cls.token == token)
        if ip is not None:
            where_.append(cls.ip == ip)
        if user_agent is not None:
            where_.append(cls.user_agent == user_agent)

        async with get_async_session() as session:
            result = await session.execute(select(cls).where(*where_))
            result = result.first()
        if result is None:
            return False
        return result[0]


class Feedbacks(Base):
    __tablename__ = 'feedbacks'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(length=255), nullable=False)
    tel_number = Column(String(length=255), nullable=False)
    email = Column(String(length=255), nullable=False)
    comment = Column(Text, nullable=True)
    user_agent = Column(Text, nullable=False)
    datetime_create = Column(
        DateTime,
        default=func.now(),
        server_default=text('(now() AT TIME ZONE \'Asia/Novosibirsk\')'),
        nullable=False
    )
    viewed = Column(Boolean, default=False, server_default=text('False'), nullable=False)

    @classmethod
    async def get_(cls):
        async with get_async_session() as session:
            result = await session.execute(select(cls).where(cls.viewed == False))
            result = result.all()
        if result is None:
            return False
        return [x for x in result]

    @classmethod
    async def add_(cls, name: str, tel_number: str, email: str, comment: str, user_agent: str):
        async with get_async_session() as session:
            query = insert(cls).values(
                name=name,
                tel_number=tel_number,
                email=email,
                comment=comment,
                user_agent=user_agent
            )
            await session.execute(query)
            await session.commit()


engine = create_async_engine(
        f'postgresql+asyncpg://{config.DATABASE_USER}'
        f':{config.DATABASE_PASSWORD}'
        f'@{config.DATABASE_IP}:{config.DATABASE_PORT}'
        f'/{config.DATABASE_NAME}',
        echo=False,
        pool_recycle=300,
        query_cache_size=0,
        pool_pre_ping=True,
        pool_size=10,
        max_overflow=2,
        pool_use_lifo=True
    )

# CREATE EXTENSION "uuid-ossp"
# alembic init -t async main/alembic
# alembic revision --autogenerate -m "Init Alembic"
# alembic upgrade head

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


@asynccontextmanager
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.commit()
            await session.close()
