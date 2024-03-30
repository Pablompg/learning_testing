from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, DeclarativeBase, MappedAsDataclass

engine = create_engine('sqlite:///./db/database.db', connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase, MappedAsDataclass):
    pass


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, init=False)
    username: Mapped[str] = mapped_column(String, unique=True)
    hashed_password: Mapped[str] = Column(String, nullable=False)


Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
