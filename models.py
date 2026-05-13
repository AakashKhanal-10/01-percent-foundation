from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class JobMatch(Base):
    __tablename__ = 'job_matches'
    
    id = Column(Integer, primary_key=True)
    company = Column(String)
    score = Column(Float)
    keywords_found = Column(String) # We'll store this as a comma-separated string
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# Setup the database engine (creates a file called scout_memory.db)
engine = create_engine('sqlite:///scout_memory.db')
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)