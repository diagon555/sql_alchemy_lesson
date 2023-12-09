from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine

from config import settings

engine = create_engine(
    url=settings.database_url_psycopg,
    echo=True,
)

engine_async = create_async_engine(
    url=settings.database_url_asyncpg,
    echo=True,
)
