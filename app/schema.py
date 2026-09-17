from typing import List, Optional
from pydantic import BaseModel, HttpUrl

class UserCreate(BaseModel):
    username: str
    email: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    model_config = {"from_attributes": True}

class Movie(BaseModel):
    id: int
    title: str
    description: str
    genres: List[str]
    release_year: Optional[int]
    rating: float
    poster_url: Optional[HttpUrl]