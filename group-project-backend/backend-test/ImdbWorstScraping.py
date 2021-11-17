from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.imdb.com/title/tt1213644/reviews?sort=userRating&dir=asc&ratingFilter=0'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

reviews = soup.select('div.text.show-more__control')
dates = soup.select('span.review-date')
displayNames = soup.select('span.display-name-link')

list = []

for index in range(0, len(reviews)):
	review = reviews[index].get_text()
	date = dates[index].get_text()
	displayName = displayNames[index].get_text()
	rating = "1/10"

	data = {"review": review,
			"date": date,
			"username": displayName,
			"rating": rating}
	list.append(data)

print(list)

