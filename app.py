import os
import logging
from scout import JobScout 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("Foundation-Core")

def start():
    engineer = os.getenv("ENGINEER_NAME", "Aakash")
    logger.info(f"--- 🚀 SYSTEM BOOT SEQUENCE INITIATED ---")
    print(f"\n[SUCCESS]: Connection established. Welcome to the 0.1%, {engineer}.\n")
    
    # Initialize the Scout from within the Foundation-Core
    hit_list = ["https://www.lftechnology.com",
        "https://www.logpoint.com",
        "https://www.cloudfactory.com"]
    scout = JobScout(targets=hit_list)
    scout.patrol() 

if __name__ == "__main__":
    start()