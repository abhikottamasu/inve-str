from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict

@dataclass
class Tweet:
    id: str
    text: str
    author: str
    timestamp: datetime
    category: str = None

@dataclass
class DigestConfiguration:
    authors: List[str]
    categories: List[str]
    user_id: str

    def __init__(self, authors: List[str], categories: List[str]):
        self.authors = authors
        self.categories = categories