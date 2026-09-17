from fastapi import FastAPI
from .routers import users, movies

app=FastAPI()
app.include_router(users.router)
app.include_router(movies.router)


@app.get("/")
def root():
    return {"message": "Movie Watchlist API"}

