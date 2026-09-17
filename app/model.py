from app.database import Base
from sqlalchemy.orm import mapped_column,Mapped
from sqlalchemy.sql import func
from sqlalchemy import String, Column, Integer, Float,ForeignKey,DateTime,Boolean

class User(Base):
    __tablename__="users"

    id: Mapped[int]=mapped_column(primary_key=True)
    username:Mapped[str]=mapped_column(String(50))
    email:Mapped[str]=mapped_column(String(100),unique=True)

class Movies(Base):
    __tablename__="movies"

    id=Column(Integer, primary_key=True)
    tmdb_id=Column(Integer,unique=True,nullable=False)
    title=Column(String,nullable=False)
    description=Column(String)
    release_year=Column(Integer)
    rating=Column(Float)
    poster_url=Column(String)

class Watchlist(Base):
    __tablename__ = "watchlist"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    watched = Column(Boolean, default=False)
    user_rating = Column(Integer, nullable=True)
    added_at = Column(DateTime, server_default=func.now())