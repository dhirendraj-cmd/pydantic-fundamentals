from pydantic import BaseModel, Field
from typing import List, Dict, Optional


class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    comments: Optional[str] = None
    imageUrl: Optional[str] = None

