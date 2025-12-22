from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#SQLite database file save in current folder fastapi.db
SQLALCHEMY_DATABASE_URL =  "sqlite:///./fastapi.db"
#create An engine represents the database connection.
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#This creates the base class for all your ORM models.
Base = declarative_base()
