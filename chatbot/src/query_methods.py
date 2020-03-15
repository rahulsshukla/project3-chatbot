import sys
import json
import itertools
from string import punctuation

import nltk
from nltk.corpus import stopwords as sw
from nltk.tokenize import TweetTokenizer as tokenizer

from src.helpers import *

def get_verb_vars(v):
	return [
		v + 'ing',
		v[:-1] + 'ing',
		v + 'ed',
		v + 'd',
		v + 's'
	]

def method_check(word, method, method_info):
	return (
		word == method or
		word in get_verb_vars(method) or
		any([
			word == syn or
			word in get_verb_vars(syn)
			for syn in method_info['synonyms']
		]) or
		word in method_info['tools']
	)

def query_methods(directions):
	with open('data/methods.json', 'r') as f:
		method_data = json.load(f)
	f.close()

	sws = [p for p in punctuation] + sw.words('english')

	jumble = [tkn for tkn in clean_string(tokenize_string(' '.join(directions)), sws) if tkn.isalpha() and len(tkn) > 1]

	# jumble = [j for j in clean_string(' '.join(directions).split(), sws) if j.isalpha() and len(j) > 1]

	counter = {}
	for word in jumble:
		for method in method_data:
			if method_check(word, method, method_data[method]):
				counter[method] = 1 if method not in counter else counter[method] + 1

	sorted_methods = [d for d in sorted(counter, key=counter.get, reverse=True)]

	return {
		'main': sorted_methods[0],
		'methods': sorted_methods
	}
