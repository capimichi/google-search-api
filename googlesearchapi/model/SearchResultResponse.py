from pydantic import BaseModel
from typing import List


class SearchResultResponse(BaseModel):
    query: str
    results: List[str]
