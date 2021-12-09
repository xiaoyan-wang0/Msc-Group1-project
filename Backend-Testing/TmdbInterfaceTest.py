import unittest
import requests
from jsonpath import jsonpath
from tmdbv3api import TMDb
from tmdbv3api import Movie
import timeit

tmdbId = '49026'

response1 = requests.get('https://api.themoviedb.org/3/movie/' + tmdbId + '/reviews?api_key=11fd5ef69d961d91f0f010d0407fd094&language=en-US&page=1')
reviews = jsonpath(response1.json(),'$..content')
authors = jsonpath(response1.json(),'$..author')
urls = jsonpath(response1.json(),'$..url')

start = timeit.default_timer()
response1_2 = requests.get('http://127.0.0.1:5000/movieTmdb/movieTmdbReviews?movieId=' + tmdbId)
reviews2 = jsonpath(response1_2.json(),'$..content')
authors2 = jsonpath(response1_2.json(),'$..author')
urls2 = jsonpath(response1_2.json(),'$..url')
stop = timeit.default_timer()
Time1 = stop - start
print(Time1)

tmdb = TMDb()
tmdb.language = 'en'
tmdb.debug = True
tmdb.api_key = '11fd5ef69d961d91f0f010d0407fd094'
movie = Movie()

m = movie.details(tmdbId)
imdb_id = m.imdb_id
title = m.title
overview = m.overview
poster = m.poster_path
vote_average = m.vote_average
year = m.release_date
runtime = m.runtime
popularity = m.popularity

response2_2 = requests.get('http://127.0.0.1:5000/movieTmdb/movieTmdbInfo?movieId=' + tmdbId)
title2 = jsonpath(response2_2.json(),'$..title')
overview2 = jsonpath(response2_2.json(),'$..overview')
date2 = jsonpath(response2_2.json(),'$..release date')
popularity2 = jsonpath(response2_2.json(),'$..popularity')
runtime2 = jsonpath(response2_2.json(),'$..runtime') 
imdb_id2 = jsonpath(response2_2.json(),'$..imdb Id') 


class TestStringMethods(unittest.TestCase):

#Testing movieTmdbReviews part of the Interface:

    def test_movieTmdbReviews1(self):
        self.assertEqual(reviews[0], reviews2[0])

    def test_movieTmdbReviews2(self):
        self.assertEqual(reviews[3], reviews2[3])

    def test_movieTmdbReviews3(self):
        self.assertEqual(reviews[5], reviews2[5])

    def test_movieTmdbReviews4(self):
        self.assertEqual(reviews[1], reviews2[1])

    def test_movieTmdbReviews5(self):
        self.assertEqual(reviews[4], reviews2[4])

    def test_movieTmdbReviews6(self):
        self.assertEqual(authors[0], authors2[0])

    def test_movieTmdbReviews7(self):
        self.assertEqual(authors[2], authors2[2])

    def test_movieTmdbReviews8(self):
        self.assertEqual(authors[1], authors2[1])

    def test_movieTmdbReviews9(self):
        self.assertEqual(urls[0], urls2[0])

    def test_movieTmdbReviews10(self):
        self.assertEqual(urls[1], urls2[1])

# Testing movieTmdbInfo part of the Interface: 

    def test_movieTmdbInfo1(self):
        self.assertEqual(title, title2[0])

    def test_movieTmdbInfo2(self):
        self.assertEqual(overview, overview2[0])

    def test_movieTmdbInfo3(self):
        self.assertEqual(year, date2[0])

    def test_movieTmdbInfo4(self):
        self.assertEqual(popularity, popularity2[0])

    def test_movieTmdbInfo5(self):
        self.assertEqual(runtime, runtime2[0]) 
        
    def test_movieTmdbInfo6(self):
        self.assertEqual(imdb_id, imdb_id2[0])   

# Performance testing in terms of runtime

    def test_TmdbReviewRuntime(self):
        self.assertLessEqual(Time1, 5) 


if __name__ == '__main__':
    unittest.main()