import httpx
import os
from dotenv import load_dotenv
from ..schema import Movie
load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

genre_map = {
    28: "Action",
    12: "Adventure",
    16: "Animation",
    35: "Comedy",
    80: "Crime",
    18: "Drama",
    14: "Fantasy",
    27: "Horror",
    878: "Science Fiction",
    53: "Thriller",
}

async def search_movies(query: str):
    url = f"{BASE_URL}/search/movie"
    params = {"api_key": TMDB_API_KEY,"query": query}
    async with httpx.AsyncClient(verify=False,trust_env=False) as client:
        response = await client.get(url, params=params)
    response.raise_for_status()
    data=response.json()
    movies=[]
    for movie in data["results"]:
        release_date=movie.get("release_date")
        movie_data={"id":movie["id"],
                    "title":movie["title"],
                    "description":movie.get("overview",""),
                    "genres":[genre_map.get(genre_id,"Unknown")
                    for genre_id in movie.get("genre_ids",[])],
                    "release_year":int(release_date[:4]) if release_date else None,
                    "rating":movie.get("vote_average",0),
                    "poster_url": (f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
                if movie.get("poster_path") else None)}
        movies.append(Movie(**movie_data))
    return movies


async def get_movie_details(movie_id: int):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": TMDB_API_KEY}
    async with httpx.AsyncClient(verify=False,trust_env=False) as client:
        response = await client.get(url, params=params)
    response.raise_for_status()
    movie = response.json()
    release_date = movie.get("release_date")
    movie_data = {
        "id": movie["id"],
        "title": movie["title"],
        "description": movie.get("overview", ""),
        "genres": [genre["name"] for genre in movie.get("genres", [])],
        "release_year": int(release_date[:4]) if release_date else None,
        "rating": movie.get("vote_average", 0),
        "poster_url": (
            f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
            if movie.get("poster_path") else None)}
    return Movie(**movie_data)
