from typing import Annotated

from sqlalchemy import create_engine, String
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from config import settings

engine = create_engine(
    url=settings.database_url_psycopg,
    echo=True,
)

engine_async = create_async_engine(
    url=settings.database_url_asyncpg,
    echo=True,
)

session_factory = sessionmaker(engine)
session_factory_async = async_sessionmaker(engine_async)


str_255 = Annotated[str, 255]


class Base(DeclarativeBase):
    type_annotation_map = {
       str_255: String(255)
    }
