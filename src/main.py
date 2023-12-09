import asyncio
from queries.core import Core, AsyncCore
from queries.orm import ORM

ORM.create_tables()
ORM.insert_employers()
ORM.update_employers()
ORM.select_employers()
