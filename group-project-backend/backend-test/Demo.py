import requests
import json
from jsonpath import jsonpath
 
# Gets information about top 250 movies on IMDB. 
response = requests.get('https://imdb-api.com/en/API/Top250Movies/k_ds7a1ynu')
movieIds = jsonpath(response.json(),'$..id')

# This is a dictionary that keeps Top 250 Movie Reviews, i assigned the reviews of the movie to the movie id so that 
# using the movie id we can reach to its reviews, i can also use the movie name as a key if needed.
top250MovieDictionary = {}

for id in movieIds:
    response2 = requests.get('https://imdb-api.com/en/API/Reviews/k_ds7a1ynu/tt1375666')
    reviews = jsonpath(response2.json(),'$..content')
    top250MovieDictionary[id] = reviews

with open('data.txt', 'w') as outfile:
    json.dump(top250MovieDictionary, outfile)

print(top250MovieDictionary)