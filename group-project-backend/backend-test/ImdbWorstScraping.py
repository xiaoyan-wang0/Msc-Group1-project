from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.imdb.com/title/tt1213644/reviews?sort=userRating&dir=asc&ratingFilter=0'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

reviews = soup.select('div.text.show-more__control')
displayNames = soup.select('span.display-name-link')

list = []

for index in range(0, len(reviews)):
	review = reviews[index].get_text()
	data = {"review": review}
	list.append(data)

for review in list:
	print(review['review'])

