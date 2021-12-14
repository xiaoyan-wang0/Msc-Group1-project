import unittest
import requests
from jsonpath import jsonpath
import timeit

movieName = 'Batman dark knight rises'
key = 'AIzaSyC6cz_fRdiwLhdlPBpkhyr0MXzF0PXMA4o'

response = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q=' + str(movieName) + ' trailer' + '&type=video&key=' + key)
trailerId = jsonpath(response.json(),'$..videoId')

trailerIdToString = str(trailerId)[2:13]

response1 = requests.get('https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=' + trailerIdToString + '&key=' + key)
reviews = jsonpath(response1.json(),'$..textDisplay')
names = jsonpath(response1.json(),'$..authorDisplayName')
profileImages = jsonpath(response1.json(),'$..authorProfileImageUrl')
times = jsonpath(response1.json(),'$..publishedAt')

start = timeit.default_timer()
response1_2 = requests.get('http://127.0.0.1:5000/movieYoutube/movieYoutubeReviews?movieName=' + str(movieName))
reviews2 = jsonpath(response1_2.json(),'$..review')
names2 = jsonpath(response1_2.json(),'$..username')
profileImages2 = jsonpath(response1_2.json(),'$..profile_picture')
times2 = jsonpath(response1_2.json(),'$..time')
stop = timeit.default_timer()
Time1 = stop - start
print(Time1)


class TestStringMethods(unittest.TestCase):

#Testing movieYoutubeReviews part of the Interface:

    def test_Youtube1(self):
        self.assertEqual(reviews[0], reviews2[0])

    def test_Youtube2(self):
        self.assertEqual(reviews[1], reviews2[1])

    def test_Youtube3(self):
        self.assertEqual(reviews[2], reviews2[2])

    def test_Youtube4(self):
        self.assertEqual(reviews[3], reviews2[3])

    def test_Youtube5(self):
        self.assertEqual(reviews[4], reviews2[4])

    def test_Youtube6(self):
        self.assertEqual(reviews[5], reviews2[5])

    def test_Youtube7(self):
        self.assertEqual(reviews[6], reviews2[6])

    def test_Youtube8(self):
        self.assertEqual(reviews[7], reviews2[7])

    def test_Youtube9(self):
        self.assertEqual(reviews[8], reviews2[8])

    def test_Youtube10(self):
        self.assertEqual(names[0], names2[0])

    def test_Youtube11(self):
        self.assertEqual(names[1], names2[1])

    def test_Youtube12(self):
        self.assertEqual(names[2], names2[2])

    def test_Youtube13(self):
        self.assertEqual(names[3], names2[3])

    def test_Youtube14(self):
        self.assertEqual(names[4], names2[4])

    def test_Youtube15(self):
        self.assertEqual(profileImages, profileImages2)

    def test_Youtube16(self):
        self.assertEqual(times[0], times2[0])

    def test_Youtube17(self):
        self.assertEqual(times[1], times2[1])

    def test_Youtube18(self):
        self.assertEqual(times[2], times2[2])

    def test_Youtube19(self):
        self.assertEqual(times[3], times2[3])

#Testing performance of Youtube interface in terms of runtime.

    def test_YoutubeRuntime(self):
        self.assertLessEqual(Time1, 15) 

if __name__ == '__main__':
    unittest.main()