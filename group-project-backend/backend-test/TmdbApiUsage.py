# I am using a Python Library for the TMDB API which is very convinient and easy to use.
# initializes TMDB object:
from tmdbv3api import TMDb
tmdb = TMDb()
tmdb.api_key = '11fd5ef69d961d91f0f010d0407fd094'

tmdb.language = 'en'
tmdb.debug = True

from tmdbv3api import Movie
movie = Movie()

# Gets recommendations for a given movie:
recommendations = movie.recommendations(movie_id=111)

for recommendation in recommendations:
    print(recommendation.title)
    print(recommendation.overview)


# Gets list of popular movies
popular = movie.popular()

for p in popular:
    print(p.id)
    print(p.title)
    print(p.overview)
    print(p.poster_path)

# To get primary information about a movie:
m = movie.details(343611)

print(m.title)
print(m.overview)
print(m.popularity)

# To search a movie by title:
search = movie.search('Mad Max')

for res in search:
    print(res.id)
    print(res.title)
    print(res.overview)
    print(res.poster_path)
    print(res.vote_average)

# To get similar movies to a specidif movie id:
similar = movie.similar(777)

for result in similar:
    print(result.title)
    print(result.overview)











