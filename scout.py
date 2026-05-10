import logging
import requests
from bs4 import BeautifulSoup
from schema import JobOpportunity

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


    def harvest(self, url: str):
        """The Scout reaches out to the URL and brings back the title."""
        try:
            # Send a request to the website
            response = requests.get(url, timeout=10)
            
            # Turn the messy HTML into a 'Soup' we can search
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the title of the website
            return soup.title.string if soup.title else "Untitled"
        except Exception as e:
            logger.error(f"Error reaching {url}: {e}")
            return None

    def patrol(self):
        logger.info("Patrol sequence started...")
        for target in self.targets:
        # Instead of 'google', we use the actual 'target' from the list
            title = self.harvest(target) 
            if title:
                logger.info(f"Target: {target} | Site Title: {title}")

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