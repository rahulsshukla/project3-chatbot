import re
import nltk
from nltk.tokenize import TweetTokenizer as tokenizer
from nltk.corpus import stopwords

from src.helpers import *

def parse_ingredients(ingredients):
	sw = set(stopwords.words('english'))

	parsed_ingredients = []
	for i in ingredients:
		tknzd = tokenizer().tokenize(i)

		if '/' in tknzd[1]:
			quantity = tknzd[0] + ' ' + tknzd[1]

		elif hasNumbers(tknzd[0]):
			quantity = tknzd[0]
		else:
			quantity = tknzd[1]

		measurement = get_measurement(tknzd, quantity)

		name = get_name(i, measurement)
		if not name:
			continue
		pos = nltk.pos_tag(name.split())
		nom = []
		for k in pos:
			if k[1] == 'NNS':
				nom.append(k[0])
			if k[1] == 'NN':
				nom.append(k[0])
			if k[0] == 'and':
				nom.append(k[0])
		n = ''
		for j in nom:
			if j not in sw:
				n = n + j + ' '

		pos = get_descriptor(name)

		prep = get_prep(name, i, measurement)

		parsed_ingredients.append({
			'name': n.strip(' '),
			'quantity': str(quantity),
			'measurement': measurement,
			'descriptor': pos,
			'preparation': prep
		})

	return parsed_ingredients

def get_measurement(ingred, quantity):
	units = ['package', 'slice', 'container', 'litre', 'gallon', 'quart', 'stalk', 'cup', 'pint', 'jar', 'can', 'clove', 'ounce', 'spoon', 'gram', 'pound', 'pinch', 'teaspoon', 'tablespoon', 'tsp', 'tbsp']

	for unit in units:
		for i in ingred:
			if unit in i:
				return i

def get_name(ingred, m):
	try:
		n = re.search(r'\d+', ingred).group()
		if m:
			rest = ingred.split(m)[1]
			if ',' in rest:
				ret = rest.split(',')[0].lower()
			else:
				ret = rest.lower()
		else:
			rest = ingred.split(n)[1]
			if ',' in rest:
				ret = rest.split(',')[0].lower()
			else:
				ret = rest
	except:
		ret = ingred
	return ret

def get_descriptor(name):
    descrip = []
    pos = nltk.pos_tag(name.split())
    for i in pos:
        if i[1] == 'JJ':
            descrip.append(i[0])
    return descrip

def get_prep(name, ingred, m):
	prep = []
	pos = nltk.pos_tag(name.split())
	for i in pos:
		if i[1] == 'VBN':
			prep.append(i[0])

	try:
		n = re.search(r'\d+', ingred).group()

		if (m and m != 'Not found' and m != 'None'):
			rest = ingred.split(m)[1]
			if ',' in rest:
				prep.append(rest.split(',')[1].lower())
		else:
			rest = ingred.split(n)[1]
			if ',' in rest:
				prep.append(rest.split(',')[1].lower())
		return prep
	except:
		return ''
