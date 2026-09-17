from fastapi import APIRouter, HTTPException, status,Depends
from sqlalchemy import Session
from ..database import get_db
from ..model import Watchlist
from ..schema import WatchlistCreate

router = APIRouter(prefix="/watchlist", tags=["Watchlist"])

@router.post("",status_code=status.HTTP_201_CREATED)
def add_to_watchlist(item:WatchlistCreate,db:Session=Depends(get_db)):
    existing=db.query(Watchlist).filter(Watchlist.user_id==item.user_id,Watchlist.movie_id==item.movie_id).first()
    if existing:
        raise HTTPException(status_code=400,detail="Movie is already in watchlist")
    new_entry=Watchlist(user_id=item.user_id,
                        movie_id=item.movie_id,
                        watched=item.watched,
                        user_rating=item.user_rating)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

