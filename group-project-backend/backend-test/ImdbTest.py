import requests
import json
from jsonpath import jsonpath

# Only gets 25 most helpful reviews for that movie, and most likely if its rated as helpful it may decrease its toxicity??? On the other hand result
# generall has low ratings... 

url = "https://imdb8.p.rapidapi.com/title/get-user-reviews"

# Movie ID
querystring = {"tconst":"tt2382320"}

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "c68de04b4emshb312359839eaa0ep162cdajsn508795a900ad"
    }

# Getting 25 most helpful reviews of a movie
response = requests.request("GET", url, headers=headers, params=querystring)
reviews = jsonpath(response.json(),'$..reviewText')

print(reviews)


querystring2 = {"tconst":"tt2382320","currentCountry":"US","purchaseCountry":"US"}
url2 = "https://imdb8.p.rapidapi.com/title/get-reviews"

# Getting overview of reviews like user review metacrtics etc, good stuff...
response2 = requests.request("GET", url2, headers=headers, params=querystring2)

#print(response2.text)

url3 = "https://imdb8.p.rapidapi.com/title/get-details"

response3 = requests.request("GET", url3, headers=headers, params=querystring)

#print(response3.text)

