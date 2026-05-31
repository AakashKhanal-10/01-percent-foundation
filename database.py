import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///scout_memory.db")
if SQLALCHEMY_DATABASE_URL.startswith("sqlite:////app/data/"):
    os.makedirs("/app/data", exist_ok=True)

#  The Engine Creator
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

#  The Session Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# The Foundation for Models
Base = declarative_base()