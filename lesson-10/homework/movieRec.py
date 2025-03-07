import requests
import random

# Your TMDb API Key
API_KEY = "49a7238fe7c13bc0865a98eb92e8d7b8"

# Base URLs
GENRE_URL = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=en-US"
MOVIE_URL = "https://api.themoviedb.org/3/discover/movie"

# Fetch available genres
response = requests.get(GENRE_URL)
if response.status_code != 200:
    print("Error fetching genres:", response.json())
    exit()

genres = response.json()["genres"]
genre_dict = {genre["name"].lower(): genre["id"] for genre in genres}

# Ask the user for a genre
user_genre = input("Enter a movie genre (e.g., Action, Comedy, Horror): ").strip().lower()

if user_genre not in genre_dict:
    print("Genre not found. Please try again.")
    exit()

# Get movies in the selected genre
params = {
    "api_key": API_KEY,
    "with_genres": genre_dict[user_genre],
    "language": "en-US",
    "sort_by": "popularity.desc"
}

response = requests.get(MOVIE_URL, params=params)
if response.status_code != 200:
    print("Error fetching movies:", response.json())
    exit()

movies = response.json()["results"]
if not movies:
    print("No movies found for this genre.")
    exit()

# Pick a random movie
movie = random.choice(movies)
print(f"🎬 Recommended Movie: {movie['title']} ({movie['release_date'][:4]})")
print(f"⭐ Rating: {movie['vote_average']}/10")
print(f"📖 Overview: {movie['overview']}")
