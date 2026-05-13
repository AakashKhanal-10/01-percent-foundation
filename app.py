import os
import logging
from scout import JobScout 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("Foundation-Core")

def start():
    engineer = os.getenv("ENGINEER_NAME", "Aakash")
    logger.info(f"--- 🚀 SYSTEM BOOT SEQUENCE INITIATED ---")
    print(f"\n[SUCCESS]: Connection established. Welcome to the 0.1%, {engineer}.\n")
    
    # 1. THE DATA: Define where we are looking
    hit_list = [
        "https://www.lftechnology.com",
        "https://www.logpoint.com",
        "https://www.cloudfactory.com"
    ]
    
    # 2. THE REQUIREMENTS: Define WHAT we are looking for
    # We add this line so the program knows what 'my_skills' is
    my_skills = ['Python', 'Intern', 'Data', 'Engineering', 'Machine Learning']
    
    # 3. THE WORKER: Initialize the Scout
    scout = JobScout(targets=hit_list)
    
    # 4. THE ACTION: Pass the requirements to the worker
    scout.patrol(my_skills) 

    logger.info("--- 📊 SCOUT DATABASE REPORT ---")

if __name__ == "__main__":
    start()