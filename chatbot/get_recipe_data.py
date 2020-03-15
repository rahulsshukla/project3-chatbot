import sys
import requests
import nltk
import itertools
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from string import punctuation

def step_dict(lst):
	a = {}
	for i in range(1, len(lst) + 1):
		a[i] = lst[i-1]
	return a


def get_recipe_data(url):
	sw = stopwords.words('english')
	punc = [p for p in punctuation]
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')

	recipe_data = {
		'title': soup.find('h1', {'class': 'recipe-summary__h1'}).text,
		'ingredients': [],
		'directions': []
	}

	try:
		directions = [span.text for span in soup.find('ul', {'class': 'instructions-section'}).find_all('p')]
	except AttributeError:
		directions = [span.text for span in soup.find('ol', {'class': 'recipe-directions__list'}).find_all('span', {'class': 'recipe-directions__list--item'})]
		ingredients_html = soup.findAll(class_ = 'checkList__line')

	for d in directions:
		i = len(d) - 1
		while i >= 0 and d[i] in [' ', '\\', 'n']:
			i -= 1

		recipe_data['directions'].append(d[:i])

	for i in ingredients_html:
		try:
			mystr = str(i)
			recipe_data['ingredients'].append(mystr.split('title=')[1].split('>')[0].strip('"'))
		except:
			pass

	return recipe_data
