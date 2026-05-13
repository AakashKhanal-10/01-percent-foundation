import logging
import requests
from bs4 import BeautifulSoup
from schema import JobOpportunity
from models import Session, JobMatch, init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AI-Scout")

class JobScout:
    def __init__(self, targets: list):
        self.targets = targets
        self.findings = []
        logger.info(f"Scout initialized with {len(targets)} targets.")

    def analyze_match(self, tech_stack: list):
        """Logic to compare job requirements with Aakash's skills."""
        my_skills = {"python", "data science", "docker", "git", "machine learning"}
        match_count = len(set(tech_stack).intersection(my_skills))   
        return (match_count / len(my_skills)) * 100

    def scan_for_keywords(self, soup, keywords):
        # 1. Get all text from the website and make it lowercase
        page_text = soup.get_text().lower()
        
        found = []
        for word in keywords:
            # 2. Check if the keyword exists in the text
            if word.lower() in page_text:
                found.append(word)
        
        return found


    def harvest(self, url: str):
        
        try:
            # Send a request to the website
            response = requests.get(url, timeout=10)
            
            # Instead of returning just the title text, we return the whole Soup object
            
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            logger.error(f"Error reaching {url}: {e}")
            return None

    def patrol(self, my_skills: list):

        # Initialize the database(creates the file if it doesnot exist)
        init_db()
        session = Session()


        logger.info("--- 🚀 STARTING DEEP SCAN PATROL ---")
        

        
        for target in self.targets:
            # 1. Get the Eyes (The Soup)
            soup = self.harvest(target)
            
            if soup:
                # 2. Use the Brain (Scan for keywords)
                found = self.scan_for_keywords(soup, my_skills)
                
                # 3. Calculate Score
                score = (len(found) / len(my_skills)) * 100 if my_skills else 0

                # 1 Create a new databse record for the job match
                match_record=JobMatch(
                    company=target,
                    score=score,
                    keywords_found=", ".join(found),# Turn the list of found keywords into a comma-separated string
                  
                )
                #2 Save it tp a database
                session.add(match_record)
                session.commit()
                # 4. Report Back
                logger.info(f"Target: {target} | Match Results: {found} | Score: {score:.1f}%")
                
                if score >= 50: # Lowered to 50% for now so you see results!
                    logger.info(f"   🎯 STRONG MATCH FOUND at {target}")
            else:
                logger.warning(f"   ⚠️ Could not reach {target}")

if __name__ == "__main__":
    hit_list = ["Leapfrog", "Logpoint", "CloudFactory", "Fusemachines"]
    scout = JobScout(targets=hit_list)
    
    # Simulation of a finding
    sample_job = JobOpportunity(
        company_name="Leapfrog",
        job_title="Data Science Intern",
        tech_stack=["Python", "SQL", "Pandas"],
        link="https://career.lftechnology.com"
    )
    
    score = scout.analyze_match(sample_job.tech_stack)
    logger.info(f"Target: {sample_job.company_name} | Match Score: {score}%")