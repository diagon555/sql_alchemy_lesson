import enum
from datetime import datetime, UTC
from typing import Optional, Annotated

from sqlalchemy import MetaData, Table, Integer, String, Column, ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base, str_255

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"),
                                               onupdate=lambda _: datetime.now(UTC))]


class EmployerOrm(Base):
    __tablename__ = 'employers'

    id: Mapped[intpk]
    username: Mapped[str]

    def __repr__(self):
        return self.username


class Workload(enum.Enum):
    parttime = 'parttime'
    fulltime = 'fulltime'


class ResumeOrm(Base):
    __tablename__ = 'resumes'

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    title: Mapped[str_255]
    salary: Mapped[Optional[int]]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey('employers.id', ondelete="CASCADE"))


metadata_obj = MetaData()
workers_table = Table(
    'employers',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('username', String),
)
resumes_table = Table(
    'resumes',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('username', String),
)
