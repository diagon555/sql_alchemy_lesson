import asyncio
from queries.orm import create_tables, insert_data

create_tables()
asyncio.run(insert_data())
