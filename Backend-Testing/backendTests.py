import unittest
import requests
from jsonpath import jsonpath

imdbId = 'tt1375666'

response = requests.get('https://imdb-api.com/en/API/Reviews/k_ds7a1ynu/' + imdbId)
year = jsonpath(response.json(),'$..year')
title = jsonpath(response.json(),'$..fullTitle')
type1 = jsonpath(response.json(),'$..type')

response3 = requests.get('https://imdb-api.com/en/API/Ratings/k_ds7a1ynu/' + imdbId)
ImdbRating = jsonpath(response3.json(),'$..imDb')


response2 = requests.get('http://127.0.0.1:5000/movieImdb/movieImdbInfo?movieId=' + imdbId)
year2 = jsonpath(response2.json(),'$..year')
title2 = jsonpath(response2.json(),'$..title')
type2 = jsonpath(response2.json(),'$..type') 
ImdbRating2 = jsonpath(response2.json(),'$..Imdb Rating')

class TestStringMethods(unittest.TestCase):

    def test_year(self):
        self.assertEqual(year, year2[0])

    def test_title(self):
        self.assertEqual(title, title2[0])

    def test_type(self):
        self.assertEqual(type1, type2[0])

    def test_imdbRating(self):
        self.assertEqual(ImdbRating, ImdbRating2[0])


if __name__ == '__main__':
    unittest.main()