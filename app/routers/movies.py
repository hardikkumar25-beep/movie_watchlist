from typing import List, Optional
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, HttpUrl, EmailStr
from app.services.movie_services import search_movies,get_movie_details

router = APIRouter(prefix="/movies",tags=["Movies"])

@router.get("")
async def get_movies(query:str):
    return await search_movies(query)

@router.get("/{movie_id}")
async def get_movie(movie_id: int):
    return await get_movie_details(movie_id)
