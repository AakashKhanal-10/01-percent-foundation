from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class JobOpportunity:
    company_name: str
    job_title: str
    tech_stack: List[str]
    link: str
    location: str = "Kathmandu"
    match_score: float = 0.0
    visa_sponsorship: bool = False
    salary_estimate: Optional[str] = "Negotiable"
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        # A 0.1% engineer always sanitizes data
        self.company_name = self.company_name.strip().title()
        self.tags = [t.lower() for t in self.tech_stack]