import unittest
import requests
from jsonpath import jsonpath
import tweepy

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


response1 = requests.get('http://127.0.0.1:5000/movieTwitter/movieTwitterReviews?movieName=' + str(movieName))
reviews = jsonpath(response1.json(),'$..content')


class TestStringMethods(unittest.TestCase):

#Testing movieTwitterReviews part of the Interface:

    def test_Twitter1(self):
        self.assertEqual(list, reviews)



if __name__ == '__main__':
    unittest.main()