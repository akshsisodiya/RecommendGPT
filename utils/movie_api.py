import requests
import os

token = os.environ.get('TMDB_API')
headers = {
    "accept":"application/json",
    "authorization":f"Bearer {token}"
}

url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
response = requests.get(url, headers=headers)

print(response.text)