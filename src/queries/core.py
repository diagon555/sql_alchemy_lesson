from sqlalchemy import text, insert, select, update, delete

from models import metadata_obj, workers_table
from database import session_factory, engine, engine_async


class Core:
    @staticmethod
    def create_tables():
        # engine.echo = False
        metadata_obj.drop_all(engine)
        metadata_obj.create_all(engine)
        engine.echo = True

    # with engine.begin() as conn:
    #     res = conn.execute(text('select 1,2,3 union select 3,4,5'))
    #     print(f'{res.all()=}')

    @staticmethod
    async def get_db_version():
        async with engine_async.begin() as conn:
            res = await conn.execute(text('select 1,2,3 union select 3,4,5'))
            print(f'{res.all()=}')

    @staticmethod
    def insert_employers():
        with engine.connect() as conn:
            stmt = insert(workers_table).values(
                [
                    {'username': 'Bobr'},
                    {'username': 'VOLK'}
                ]
            )
            conn.execute(stmt)
            conn.commit()

    @staticmethod
    def select_employers():
        with engine.connect() as conn:
            query = select(workers_table)
            result = conn.execute(query)
            employers = result.all()
            print(f'{employers=}')

    @staticmethod
    def update_employers(worker_id: int = 2, username: str = 'MishaT'):
        with engine.connect() as conn:
            # stmt = text('UPDATE employers SET username=:username WHERE id=:id')
            # stmt = stmt.bindparams(id=worker_id, username=username)
            stmt = (
                update(workers_table)
                .values(username=username)
                # .where(workers_table.c.id == worker_id)
                .filter_by(id=worker_id)
            )
            conn.execute(stmt)
            conn.commit()


class AsyncCore:
    pass
