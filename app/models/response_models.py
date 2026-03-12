from pydantic import BaseModel
from typing import Dict


class AnalyzeResponse(BaseModel):
    summary: Dict
    insights: str