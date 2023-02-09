import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = None

# POSTGRE
# engine = create_engine(f'postgresql'
#                        f'://{os.environ["LOCAL_DB_USER"]}'
#                        f':{os.environ["LOCAL_DB_PASSWORD"]}'
#                        f'@{os.environ["LOCAL_DB_HOST"]}'
#                        f':{os.environ["LOCAL_DB_PORT"]}'
#                        f'/{os.environ["LOCAL_DB_DBNAME"]}')

# MSSQL
# engine = create_engine(f'mssql+pymssql'
#                        f'://{os.environ["LOCAL_DB_USER"]}'
#                        f':{os.environ["LOCAL_DB_PASSWORD"]}'
#                        f'@{os.environ["LOCAL_DB_HOST"]}'
#                        f':{os.environ["LOCAL_DB_PORT"]}'
#                        f'/{os.environ["LOCAL_DB_DBNAME"]}'
#                        f'?charset=utf8')

# SQLITE
# engine = create_engine("sqlite:///./sqlite3.db", connect_args={
#                        "check_same_thread": False})


SessionLocalDB = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

LocalDBBase = declarative_base()


def get_local_db():
    session = SessionLocalDB()
    try:
        yield session
    finally:
        session.close()
