import requests
import json
from jsonpath import jsonpath
 
response = requests.get('https://imdb-api.com/en/API/Title/k_ds7a1ynu/tt0110413')

print(response.text)


