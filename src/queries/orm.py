from sqlalchemy import select

from database import engine, session_factory, session_factory_async, Base
from models import EmployerOrm


class ORM:
    @staticmethod
    def create_tables():
        # engine.echo = False
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        engine.echo = True

    @staticmethod
    def insert_employers():
        employer_bobr = EmployerOrm(username='Bobr')
        employer_diagon = EmployerOrm(username='Diagon')
        with session_factory() as session:
            session.add_all([employer_bobr, employer_diagon])
            session.flush()
            # has id
            session.commit()

    @staticmethod
    def select_employers():
        with session_factory() as session:
            worker_id = 2
            worker_misha = session.get(EmployerOrm, worker_id)
            print(f'{worker_misha=}')

            query = select(EmployerOrm)
            result = session.execute(query)
            employers = result.scalars().all()
            print(f'{employers=}')

    @staticmethod
    def update_employers(worker_id: int = 2, username: str = 'MishaT'):
        with session_factory() as session:
            worker_michal = session.get(EmployerOrm, worker_id)
            worker_michal.username = username
            # session.expire(worker_michal)  # clear changes
            # session.expire_all()  # clear changes
            # session.refresh(worker_michal)
            session.commit()


class ORM_async:
    @staticmethod
    async def insert_data():
        employer_bobr = EmployerOrm(username='BobrAS')
        employer_diagon = EmployerOrm(username='DiagonAS')
        async with session_factory_async() as session:
            session.add_all([employer_bobr, employer_diagon])
            await session.commit()
