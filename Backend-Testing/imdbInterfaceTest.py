import unittest
import requests
from jsonpath import jsonpath
import timeit

imdbId = 'tt0096895'

response1 = requests.get('https://imdb-api.com/en/API/Reviews/k_ds7a1ynu/' + imdbId)
year = jsonpath(response1.json(),'$..year')
title = jsonpath(response1.json(),'$..fullTitle')
type1 = jsonpath(response1.json(),'$..type')

response1_2 = requests.get('http://127.0.0.1:5000/movieImdb/movieImdbInfo?movieId=' + imdbId)
year2 = jsonpath(response1_2.json(),'$..year')
title2 = jsonpath(response1_2.json(),'$..title')
type2 = jsonpath(response1_2.json(),'$..type') 
ImdbRating2 = jsonpath(response1_2.json(),'$..Imdb Rating')

response2 = requests.get('https://imdb-api.com/en/API/Ratings/k_ds7a1ynu/' + imdbId)
ImdbRating = jsonpath(response2.json(),'$..imDb')

response3 = requests.get('https://imdb-api.com/en/API/Title/k_ds7a1ynu/' + imdbId)
plot = jsonpath(response3.json(),'$..plot')

response3_2 = requests.get('http://127.0.0.1:5000/movieImdb/movieImdbInfo?movieId=' + imdbId)
plot2 = jsonpath(response3_2.json(),'$..plot')

response4 = requests.get('https://imdb-api.com/en/API/FullCast/k_ds7a1ynu/' + imdbId)
cast = jsonpath(response4.json(),'$..actors')

response4_2 = requests.get('http://127.0.0.1:5000/movieImdb/movieImdbInfo?movieId=' + imdbId)
cast2 = jsonpath(response4_2.json(),'$..cast (actors)')

response5 = requests.get('https://api.themoviedb.org/3/movie/' + imdbId + '?api_key=11fd5ef69d961d91f0f010d0407fd094&language=en-US&page=1')
tmdbId = jsonpath(response5.json(),'$.belongs_to_collection..id')

response5_2 = requests.get('http://127.0.0.1:5000/movieImdb/movieImdbInfo?movieId=' + imdbId)
tmdbId2 = jsonpath(response5_2.json(),'$..Tmdb Id')


response6 = requests.get('https://imdb-api.com/en/API/Reviews/k_ds7a1ynu/' + imdbId)
reviews = jsonpath(response6.json(),'$.items..content')
#reviews = response6.json()

start = timeit.default_timer()
response6_2 = requests.get('http://127.0.0.1:5000/movieImdb/movieImdbReviews?movieId=' + imdbId)
reviews2 = jsonpath(response6_2.json(),'$..content')
stop = timeit.default_timer()
Time1 = stop - start
print('Time: ', Time1) 

start = timeit.default_timer()
response7 = requests.get('http://127.0.0.1:5000/movieImdb/movieImdbBottomInfo?numberOfMovies=10')
titles = jsonpath(response7.json(),'$..movie_title')
imdbRatings = jsonpath(response7.json(),'$..Imdb_Rating')
years = jsonpath(response7.json(),'$..year')
posters = jsonpath(response7.json(),'$..posters')
stop = timeit.default_timer()
Time2 = stop - start
print('Time: ', Time2) 

response8 = requests.get('http://127.0.0.1:5000/movieImdb/movieImdbLoadWorstComments?movieId=tt0096895')
reviewsWorst = jsonpath(response8.json(),'$..review')
usernamesWorst = jsonpath(response8.json(),'$..username')  
ratingsWorst = jsonpath(response8.json(),'$..rating')
theReviewToCompare = "I know back in 1989 , this was considered the bomb of comic book character movies. I never did like the casting choices ,short shi* Michael Keaton as a rather dull Bruce Wayne and the annoying Kim Basinger as Vicki Vale. The action and backdrops are all so cartoonish as if the director and producers were thinking product placement for kids rather than a dark and serious movie. Nicholson is sorely miscast as the Joker too - too old for starters and the hammy overacting is just awful. The movie degenerates into bad one liners and stagnant scenes of the characters just looking at each other as if saying I'm so bored lets just get this scene over with already. I've watched this movie several times and each time I see just how bad it is."


class TestStringMethods(unittest.TestCase):

#Testing movieImdbInfo part of the Interface:

    def test_year(self):
        self.assertEqual(year, year2[0])

    def test_title(self):
        self.assertEqual(title, title2[0])

    def test_type(self):
        self.assertEqual(type1, type2[0])

    def test_imdbRating(self):
        self.assertEqual(ImdbRating, ImdbRating2[0])

    def test_plot(self):
        self.assertEqual(plot[0], plot2[0])

    def test_cast(self):
        self.assertEqual(cast, cast2[0])    

    def test_tmdbId(self):
        self.assertEqual(tmdbId, tmdbId2[0])   

#Testing movieImdbReview part of the Interface:

    def test_reviews1(self):
        self.assertEqual(reviews[0], reviews2[0]) 

    def test_reviews2(self):
        self.assertEqual(reviews[1], reviews2[1]) 

    def test_reviews3(self):
        self.assertEqual(reviews[10], reviews2[10]) 

    def test_reviews4(self):
        self.assertEqual(reviews[7], reviews2[7]) 

#Testing movieImdbBottomInfo part of the Interface

    def test_bottom1(self):
        self.assertEqual(titles[2], 'Kod Adi KOZ') 

    def test_bottom2(self):
        self.assertEqual(titles[3], 'Manos: The Hands of Fate') 

    def test_bottom3(self):
        self.assertEqual(titles[7], 'House of the Dead') 

    def test_bottom4(self):
        self.assertEqual(imdbRatings[0][0], '1.9')

    def test_bottom5(self):
        self.assertEqual(years[1], '2004')

    def test_bottom6(self):
        self.assertEqual(years[2], '2015')

    def test_bottom7(self):
        self.assertEqual(years[7], '2003')

#Testing movieImdbLoadWorstComments part of the Interface

    def test_worst1(self):
        self.assertEqual(reviewsWorst[3], theReviewToCompare)

    def test_worst2(self):
        self.assertEqual(usernamesWorst[2], 'johnhenrik') 
        
    def test_worst2(self):
        self.assertEqual(ratingsWorst[3], '1/10')   

#Testing performance of movieImdbReview part of the Interface in terms of runtime.

    def test_ImdbReviewRuntime(self):
        self.assertLessEqual(Time1, 12) 

#Testing performance of worst raated movies part of the Interface in terms of runtime.

    def test_worstRuntime(self):
        self.assertLessEqual(Time2, 10) 


if __name__ == '__main__':
    unittest.main()