import tweepy
import pandas as pd

consumer_key="BtNMua2cnczTyaCIQ0ZKA01xV"
consumer_secret="dWWqv17X6XKVYm9SrfLr10WrJQHYCYhUjAhxw8DBKdoHBqaTTZ"
access_token="1444319826399408130-F8gWnTYETTKv5pEXlNSkPoGgDOc0dm"
access_token_secret="8D4vBQZrcsN3g1wPyfxUItcybcOctf8fioTtbuyfxEfKz"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# cursor = tweepy.Cursor(api.user_timeline, id='elonmusk', tweet_mode="extended").items(1)

# for c in cursor:
#     #print(dir(c))
#     print(c.full_text)

cursor = tweepy.Cursor(api.search_tweets, q="Batman dark knight rises", tweet_mode="extended").items(30)

for c in cursor:
    print(c.full_text)
