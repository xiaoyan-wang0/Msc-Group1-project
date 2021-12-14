import unittest
import requests
from jsonpath import jsonpath
import tweepy
import timeit


movieName = 'Batman dark knight rises'

consumer_key="BtNMua2cnczTyaCIQ0ZKA01xV"
consumer_secret="dWWqv17X6XKVYm9SrfLr10WrJQHYCYhUjAhxw8DBKdoHBqaTTZ"
access_token="1444319826399408130-F8gWnTYETTKv5pEXlNSkPoGgDOc0dm"
access_token_secret="8D4vBQZrcsN3g1wPyfxUItcybcOctf8fioTtbuyfxEfKz"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

cursor = tweepy.Cursor(api.search_tweets, q=str(movieName), tweet_mode="extended", lang='en').items(20)

list = []

for c in cursor:
    list.append(c.full_text)


start = timeit.default_timer()
response1 = requests.get('http://127.0.0.1:5000/movieTwitter/movieTwitterReviews?movieName=' + str(movieName))
reviews = jsonpath(response1.json(),'$..content')
stop = timeit.default_timer()
Time1 = stop - start

print(Time1)


class TestStringMethods(unittest.TestCase):

#Testing movieTwitterReviews part of the Interface:

    def test_Twitter1(self):
        self.assertEqual(list[0], reviews[0])

    def test_Twitter2(self):
        self.assertEqual(list[1], reviews[1])

    def test_Twitter3(self):
        self.assertEqual(list[2], reviews[2])

    def test_Twitter4(self):
        self.assertEqual(list[3], reviews[3])

    def test_Twitter5(self):
        self.assertEqual(list[4], reviews[4])

    def test_Twitter6(self):
        self.assertEqual(list[5], reviews[5])

    def test_Twitter7(self):
        self.assertEqual(list[6], reviews[6])

    def test_Twitter8(self):
        self.assertEqual(list[7], reviews[7])

    def test_Twitter9(self):
        self.assertEqual(list[8], reviews[8])

    def test_Twitter10(self):
        self.assertEqual(list[9], reviews[9])


#Performance test in terms of runtime

    def test_ImdbReviewRuntime(self):
        self.assertLessEqual(Time1, 15) 


if __name__ == '__main__':
    unittest.main()
