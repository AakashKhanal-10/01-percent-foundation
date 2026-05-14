from pydantic import BaseModel, Field, field_validator
from typing import List, Optional

class JobOpportunitySchema(BaseModel):
    # These match our dataclass fields but with Pydantic Power
    company_name: str
    job_title: str
    tech_stack: List[str]
    link: str
    location: str = "Kathmandu"
    match_score: float = 0.0
    visa_sponsorship: bool = False
    salary_estimate: Optional[str] = "Negotiable"
    tags: List[str] = []

    # This replaces the __post_init__ logic
    @field_validator('company_name')
    @classmethod
    def sanitize_company_name(cls, v: str) -> str:
        return v.strip().title()

    # This automatically generates tags from the tech_stack
    @field_validator('tags', mode='before')
    @classmethod
    def generate_tags(cls, v, info):
        # info.data contains the other fields like 'tech_stack'
        if not v and 'tech_stack' in info.data:
            return [t.lower() for t in info.data['tech_stack']]
        return v

    class Config:
        from_attributes = True # Critical for connecting to your Database models and the bridge to SQLALchemy	