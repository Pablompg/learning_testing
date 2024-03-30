from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///./db/database.db', connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


async def init_db():
    try:
        raw_conn = engine.raw_connection()
        with open("db/init_db.sql", "r") as file:
            sql_script = file.read()
            raw_conn.executescript(sql_script)

        raw_conn.close()
    except SQLAlchemyError as e:
        print(f"Error occurred during database initialization")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
