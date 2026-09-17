from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field

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

class WatchlistCreate(BaseModel):
    user_id: int
    movie_id: int
    watched: bool = False
    user_rating: Optional[int] = Field(None, ge=1, le=10)