import os
import logging
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from scout import JobScout 
import models, schema, database

# Professional Logging Configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("Foundation-Core")

# 1. Initialize the CEO (The API)
app = FastAPI(title="Aakash's 0.1% Job Scout")

# Create database tables if they don't exist
models.Base.metadata.create_all(bind=database.engine)

# 2. Dependency: Get the DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 3. ENDPOINT: Trigger the Scout (The "Action")
@app.post("/scout/run", status_code=202)
def run_scout_patrol(background_tasks: BackgroundTasks):
    """
    Triggers the JobScout to patrol the hit_list.
    We use BackgroundTasks so the API doesn't 'hang' while scraping.
    """
    hit_list = [
        "https://www.lftechnology.com",
        "https://www.logpoint.com",
        "https://www.cloudfactory.com"
    ]
    my_skills = ['Python', 'Intern', 'Data', 'Engineering', 'Machine Learning']
    
    scout = JobScout(targets=hit_list)

    db=database.SessionLocal()
    
    # Run the mission in the background
    background_tasks.add_task(scout.patrol, my_skills,db)
    
    return {"message": "Mission initiated. Scout is now patrolling in the background."}

# 4. ENDPOINT: View the Results (The "Vault")
@app.get("/matches", response_model=list[schema.ScoutMatchResponse])
def get_matches(db: Session = Depends(get_db)):
    matches = db.query(models.JobMatch).all()
    return matches