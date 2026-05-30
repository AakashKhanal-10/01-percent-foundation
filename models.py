from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from database import Base, engine


class JobMatch(Base):
    __tablename__ = 'job_matches'
    
    id = Column(Integer, primary_key=True)
    company = Column(String)
    job_title = Column(String, default="Internship")
    score = Column(Float) # Storing as string for simplicity, can be changed to Float if needed
    keywords_found = Column(String) # We'll store this as a comma-separated string
    location = Column(String, default="Kathmandu")
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# Setup the database engine (creates a file called scout_memory.db)
engine = create_engine('sqlite:///scout_memory.db')
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.drop_all(engine)  # This will clear the database
    Base.metadata.create_all(engine)