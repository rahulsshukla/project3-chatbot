import sys
import json

from src.helpers import *

def change_health(make_healthier, steps):
	with open('data/healthy.json', 'r') as f:
		health_json = json.load(f)
	f.close()

	health_data = {}
	if make_healthier:
		for pair in health_json:
			health_data[pair[0]] = pair[1]
	else:
		for pair in health_json:
			health_data[pair[1]] = pair[0]

	new_directions = []

	for step in steps:
		for i in step['ingredients']:
			if i['name'] in health_data.keys():
				custom_replace_name(step['ingredients'], i['name'], health_data[i['name']])
