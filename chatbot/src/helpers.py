from nltk import TweetTokenizer as tokenizer
from nltk.tokenize import word_tokenize

def get_ngrams(n, s):
	return [' '.join(s[i:i+n]) for i in range(len(s) - n + 1)]

def clean_string(s, sw):
	return [tkn.lower() for tkn in s if tkn not in sw]

def tokenize_string(s):
	return tokenizer().tokenize(s)

def unibigrams(input_list):
	tokenized = []
	uni = []
	bi = []
	tri = []

	for x in input_list:
		tokenized.append(word_tokenize(x))

	for x in tokenized:
		if len(x) == 1:
			for i in x:
				uni.append(i)
		if len(x) == 2:
			bi.append(x)
			if len(x) == 3:
				tri.append(x)

	results = {
		'unigrams': uni,
		'bigrams': bi,
		'trigrams': tri
	}

	return results

def hasNumbers(s):
    return any(c.isdigit() for c in s)

def print_recipe(steps):
	for n, step in enumerate(steps, 1):
		print('Step {}:'.format(n))

		print('\tIngredients:')
		for ingredient in step['ingredients']:
			print('\t\t{} {} {} {}{}'.format(
				ingredient['quantity'],
				ingredient['measurement'] if ingredient['measurement'] else '',
				', '.join(ingredient['descriptor']),
				ingredient['name'],
				', ' + ', '.join(ingredient['preparation']) if len(ingredient['preparation']) else ''
			))

		print('\tMethods:')
		for method in step['methods']:
			print('\t\t' + method)

		print('\tTools:')
		for tool in step['tools']:
			print('\t\t' + tool)

		if step['time']:
			print('\tTime:')
			print('\t\t{} {}'.format(step['time']['duration'], step['time']['unit']))

def prune_list(l):
	clean = []
	for i in l:
		if i not in clean:
			clean.append(i)
	return clean

def custom_replace_name(arr, old, new):
	for n in range(len(arr)):
		if arr[n]['name'] == old:
			arr[n]['name'] = new

def custom_replace_quantity(arr, old, new):
	for n in range(len(arr)):
		if arr[n]['quantity'] == old:
			arr[n]['quantity'] = new
			break
