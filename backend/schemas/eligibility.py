from pydantic import BaseModel


class EligibilityRequest(BaseModel):
    startup_profile: dict
    grant: dict