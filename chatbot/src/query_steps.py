import json
from nltk.tokenize import word_tokenize

from src.helpers import *

def query_steps(ingredients, directions, tools, methods):
	time_units = ['second', 'seconds', 'minute', 'minutes', 'hour', 'hours', 'hr', 'hrs']

	with open('data/methods.json', 'r') as f:
		all_methods = json.load(f)

	steps = []

	for direc in directions:
		tkn_direc = [tkn.lower() for tkn in word_tokenize(direc)]

		if 'preheat' in tkn_direc:
			for tkn in tkn_direc:
				if tkn.isnumeric():
					steps.append({
						'time': 0,
						'tools': ['oven'],
						'ingredients': [],
						'methods': ['preheat to ' + tkn]
					})
					break
			continue

		step = {}

		time_index = -1
		for unit in time_units:
			if unit in tkn_direc:
				time_index = tkn_direc.index(unit)

		if time_index >= 0:
			if time_index > 0 and tkn_direc[time_index - 1].isnumeric():
				step['time'] = {
					'duration': tkn_direc[time_index - 1],
					'unit': tkn_direc[time_index]
				}
		else:
			step['time'] = 0

		step['tools'] = [tool for tool in tools if tool in direc]
		step['ingredients'] = []
		for w in tkn_direc:
			for i in ingredients:
				if w in i['name'].split(' '):
					step['ingredients'].append(i.copy())

		step['ingredients'] = prune_list(step['ingredients'])

		step['methods'] = [
			m for m in methods
			if m in tkn_direc or
				any([syn in tkn_direc for syn in all_methods[m]['synonyms']])
		]

		steps.append(step)

	return steps
