from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://username:password@localhost/database"
DATABASE_URL = "postgresql+psycopg2://postgres:1@localhost/postgres"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


Base = declarative_base()

