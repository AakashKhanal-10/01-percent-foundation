import logging
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from models import JobMatch, init_db # Removed local Session import here

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AI-Scout")

class JobScout:
    def __init__(self, targets: list):
        self.targets = targets
        logger.info(f"Scout initialized with {len(targets)} targets.")

    def scan_for_keywords(self, soup, keywords):
        page_text = soup.get_text().lower()
        return [word for word in keywords if word.lower() in page_text]

    def harvest(self, url: str):
        try:
            # Added a User-Agent: US clients/sites often block scripts without one
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            response = requests.get(url, headers=headers, timeout=10)
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            logger.error(f" Error reaching {url}: {e}")
            return None

    def patrol(self, my_skills: list, db):
        """
        FIXED: We pass 'db' (the session) from app.py.
        This ensures the API and the Scout share the same connection 'lifecycle'.
        """
        logger.info("--- 🚀 STARTING DEEP SCAN PATROL ---")
        
        for target in self.targets:
            soup = self.harvest(target)
            
            if soup:
                found = self.scan_for_keywords(soup, my_skills)
                score = (len(found) / len(my_skills)) * 100 if my_skills else 0

                # Create a new database record
                match_record = JobMatch(
                    company=target,
                    score=score,
                    keywords_found=", ".join(found),
                    timestamp=datetime.utcnow() # Always track WHEN data was found
                )
                
                try:
                    db.add(match_record)
                    db.commit() # Save to Vault
                    logger.info(f"Target: {target} | Score: {score:.1f}% | SAVED")
                except Exception as e:
                    logger.error(f" Failed to save {target}: {e}")
                    db.rollback() # The safety net
                
                if score >= 50:
                    logger.info(f"   🎯 STRONG MATCH FOUND at {target}")
            else:
                logger.warning(f"   ⚠️ Skipping {target}")