from pydantic import BaseModel
from typing import Optional


class Post(BaseModel):
    title: str
    body: str
    rating: Optional[int] = None
    published: Optional[bool] = True

