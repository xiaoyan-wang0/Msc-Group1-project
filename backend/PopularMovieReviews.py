# I am using a Python Library for the TMDB API which is very convinient and easy to use.
from tmdbv3api import TMDb
from tmdbv3api import Movie
import requests
import json
from jsonpath import jsonpath
tmdb = TMDb()
tmdb.language = 'en'
tmdb.debug = True
tmdb.api_key = '11fd5ef69d961d91f0f010d0407fd094'
movie = Movie()

movieids = []
# Gets id's of 20 most popular movies and puts them into a list. This list gets updated everyday.
popular = movie.popular()
for p in popular:
    movieids.append(str(p.id)) 
   
# IMPORTANT: This is a dictionary that keeps popular movie reviews, i assigned the reviews of the movie to the movie id so that using the movie id we can reach to its reviews,
# i can also use the movie name as a key if needed.
reviewDictionary = {}

for t in movieids:
    res8 = requests.get('https://api.themoviedb.org/3/movie/' + t + '/reviews?api_key=11fd5ef69d961d91f0f010d0407fd094&language=en-US&page=1')
    reviews = jsonpath(res8.json(),'$..content')
    reviewDictionary[t] = reviews

print(reviewDictionary)















