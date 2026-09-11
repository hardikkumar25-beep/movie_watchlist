from typing import List, Optional,Dict
from datetime import datetime
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, HttpUrl, EmailStr,Field

router = APIRouter(prefix="/watchlist", tags=["Watchlist"])

class WatchlistCreate(BaseModel):
    user_id:int
    movie_id:int
    watched:bool=False
    user_rating: Optional[int] = Field(None, ge=1, le=10)

class WatchlistResponse(BaseModel):
    movie_id: int
    watched: bool
    user_rating: Optional[int]
    added_at: str

watchlist_db: Dict[int, List[dict]] = {}

@router.post("", response_model=WatchlistResponse, status_code=status.HTTP_201_CREATED)
def add_to_watchlist(item: WatchlistCreate):
    if item.user_id not in watchlist_db:
        watchlist_db[item.user_id] = []
        
    user_list = watchlist_db[item.user_id]
    if any(m["movie_id"] == item.movie_id for m in user_list):
        raise HTTPException(status_code=400, detail="Movie is already in your watchlist")

    new_entry = {
        "movie_id": item.movie_id,
        "watched": item.watched,
        "user_rating": item.user_rating,
        "added_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    user_list.append(new_entry)
    return new_entry

@router.get("",response_model=List[WatchlistResponse])
def get_watchlist(user_id:int):
    return watchlist_db.get(user_id,[])

@router.delete("/{movie_id}")
def remove_from_watchlist(user_id: int, movie_id: int):
    if user_id not in watchlist_db:
        raise HTTPException(status_code=404,detail="Watchlist not found for this user")
    user_list=watchlist_db[user_id]
    initial_len=len(user_list)
    watchlist_db[user_id]=[m for m in user_list if m["movie_id"]!= movie_id]
    if len(watchlist_db[user_id])==initial_len:
        raise HTTPException(status_code=404,detail="Movie not found in watchlist")
    return {"message": f"Movie {movie_id} successfully removed from watchlist"}