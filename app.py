import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("Foundation-Core")

def start():
    engineer = os.getenv("ENGINEER_NAME", "Aakash")
    logger.info(f"--- 🚀 SYSTEM BOOT SEQUENCE INITIATED ---")
    print(f"\n[SUCCESS]: Connection established. Welcome to the 0.1%, {engineer}.\n")

if __name__ == "__main__":
    start()