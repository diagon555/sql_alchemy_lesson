from database import engine, session_factory, session_factory_async, Base
from models import EmployerOrm


def create_tables():
    # engine.echo = False
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    engine.echo = True

#
# def insert_data():
#     employer_bobr = EmployerOrm(username='Bobr')
#     employer_diagon = EmployerOrm(username='Diagon')
#     with session_factory() as session:
#         session.add_all([employer_bobr, employer_diagon])
#         session.commit()


async def insert_data():
    employer_bobr = EmployerOrm(username='BobrAS')
    employer_diagon = EmployerOrm(username='DiagonAS')
    async with session_factory_async() as session:
        session.add_all([employer_bobr, employer_diagon])
        await session.commit()
