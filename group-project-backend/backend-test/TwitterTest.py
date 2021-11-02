from pytwitter import Api
from searchtweets import collect_results
api = Api(bearer_token="AAAAAAAAAAAAAAAAAAAAAFZgUQEAAAAAsPd5Gbs79M%2BJ2YaDp8mgr1j9rzg%3DrXmBkxkCXT8gClftXtNB4YZnqsUDmLrV4W9RQ4xMDhyjxIyaxE")

x = api.get_following(user_id="2244994945", max_results=5)

