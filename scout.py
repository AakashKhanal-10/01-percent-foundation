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
    def calculate_match_score(self,job_description):
            # Convert the entire text to lowercase so matching is case-insensitive
            text=job_description.lower()
            #Map out our targeted tech skills to their respective scores
            skills_weights={
                
                # Core Data Science & Languages
                "python": 10,
                "pandas": 15,
                "numpy": 15,
                "sql": 10,
    
                # Machine Learning Frameworks
                "scikit-learn": 20,
                "sklearn": 20,
                "tensorflow": 15,
                "keras": 15,
                "machine learning": 25,
                "data science": 25,
    
                # AI & Agentic Infrastructure
                "ai": 20,
                "artificial intelligence": 20,
                "nlp": 20,
                "fastapi": 15,
                "api": 10,
    
                # DevOps & Operations Engineering
                "docker": 15,
                "container": 10,
                "git": 10,
                "linux": 10,
                 
            } 
            # Initialize our score counter at zero
            total_score=0
            # Loop through the dictionary keys and values at the same time
            for skill,weight in skills_weights.items():
                # Check if the skill keyword exists inside the job text
                if skill in text: # This is a membership operator check
                    total_score += weight
                # Intent priority filters(Intership Bonus)
                if "intern" in text or "intership" in text:
                    total_score += 50

                # Hand the final calculation back to the program
            return total_score

    def patrol(self, my_skills: list, db):
        """
        FIXED: We pass 'db' (the session) from app.py.
        This ensures the API and the Scout share the same connection 'lifecycle'.
        """
        logger.info("--- 🚀 STARTING DEEP SCAN PATROL ---")
        
        for target in self.targets:
            soup = self.harvest(target)
            
            if soup:
                raw_text= soup.get_text()
                # Split the text by whitespace words, then join them back with a single space to normalize it. This helps in better keyword matching and scoring.
                clean_snippet=" ".join(raw_text.split())
                #This is where the text comes from and gets passed to the engine!
                logger.info(f"--- EXTRACTED TEXT SNIPPET FOR {target}: {clean_snippet[:150]}...")
                
                
                score=self.calculate_match_score(raw_text) # Passed onto your scoring algorithm 
                found=self.scan_for_keywords(soup, my_skills)
                match_record = JobMatch(
                    company=target,
                    score=score,
                    keywords_found=", ".join(found),
                    timestamp=datetime.utcnow() # Always track WHEN data was found
                )
        
                try:
                    db.add(match_record)
                    db.commit() # Save to Vault
                    logger.info(f"Target: {target} | Score: {score} pts | SAVED")
                except Exception as e:
                    logger.error(f" Failed to save {target}: {e}")
                    db.rollback() # The safety net
                
                if score >= 50:
                    logger.info(f"   🎯 STRONG MATCH FOUND at {target}")
            else:
                logger.warning(f"   ⚠️ Skipping {target}")