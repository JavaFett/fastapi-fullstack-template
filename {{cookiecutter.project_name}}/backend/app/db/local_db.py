import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine_local_db = create_engine(f'mssql+pymssql://{os.environ["LOCAL_DB_USER"]}:{os.environ["LOCAL_DB_PASSWORD"]}'
                                f'@{os.environ["LOCAL_DB_HOST"]}'
                                f':{os.environ["LOCAL_DB_PORT"]}/{os.environ["LOCAL_DB_DBNAME"]}'
                                f'?charset=utf8')

SessionLocalDB = sessionmaker(
    autocommit=False, autoflush=False, bind=engine_local_db)

LocalDBBase = declarative_base()


def get_local_db():
    session = SessionLocalDB()
    try:
        yield session
    finally:
        session.close()
