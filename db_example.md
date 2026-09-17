users:
  id PK
  email UNIQUE
  password_hash
  created_at

movies:
  id PK
  tmdb_id UNIQUE
  title
  poster_path
  release_date
  created_at

watchlist:
  id PK
  user_id FK
  movie_id FK
  added_at
  UNIQUE(user_id, movie_id)
