import logging
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

    def patrol(self):
        logger.info("Patrol sequence started...")
        # Future Phase: We will add the BeautifulSoup/Playwright logic here
        pass

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