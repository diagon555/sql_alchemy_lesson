from sqlalchemy import text, insert

from models import metadata_obj
from database import session_factory, engine, engine_async

from src.models import workers_table


def create_tables():
    engine.echo = False
    metadata_obj.drop_all(engine)
    metadata_obj.create_all(engine)
    engine.echo = True

# with engine.begin() as conn:
#     res = conn.execute(text('select 1,2,3 union select 3,4,5'))
#     print(f'{res.all()=}')


async def get_db_version():
    async with engine_async.begin() as conn:
        res = await conn.execute(text('select 1,2,3 union select 3,4,5'))
        print(f'{res.all()=}')


def insert_data():
    with engine.connect() as conn:
#         stmt = """INSERT INTO employers (username) VALUES
# ('AO Bobr'),
# ('OOO Viktor');"""
        stmt = insert(workers_table).values(
            [
                {'username': 'Bobr'},
                {'username': 'VOLK'}
            ]
        )
        conn.execute(stmt)
        conn.commit()
