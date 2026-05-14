from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. The Connection String
engine = create_engine('sqlite:///scout_memory.db')

# 2. The Session Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. The Foundation for Models
Base = declarative_base()