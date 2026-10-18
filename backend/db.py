import os
from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo = True)

def create_db():
    SQLModel.metadata.create.all(engine)

def get():
    with Session(engine) as session:
        yield session