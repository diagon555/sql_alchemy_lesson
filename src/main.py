import sys
from pathlib import Path
sys.path.insert(1, str(Path(sys.path[0]) / '..'))

from queries.core import create_tables, insert_data

create_tables()
insert_data()
