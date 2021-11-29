import unittest
import requests
from jsonpath import jsonpath

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

response1_2 = requests.get('http://127.0.0.1:5000/movieYoutube/movieYoutubeReviews?movieName=' + str(movieName))
reviews2 = jsonpath(response1_2.json(),'$..review')
names2 = jsonpath(response1_2.json(),'$..username')
profileImages2 = jsonpath(response1_2.json(),'$..profile_picture')
times2 = jsonpath(response1_2.json(),'$..time')



class TestStringMethods(unittest.TestCase):

#Testing movieYoutubeReviews part of the Interface:

    def test_Youtube1(self):
        self.assertEqual(reviews, reviews2)

    def test_Youtube2(self):
        self.assertEqual(names, names2)

    def test_Youtube3(self):
        self.assertEqual(profileImages, profileImages2)

    def test_Youtube4(self):
        self.assertEqual(times, times2)



if __name__ == '__main__':
    unittest.main()