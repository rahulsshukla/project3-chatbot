from get_recipe_data import get_recipe_data
from src.query_methods import query_methods
from src.change_health import change_health
from get_recipe_data import step_dict
from nltk.tokenize import TweetTokenizer

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])

def ingreds_shower(lst):
	for i in lst:
		print('- ' + str(i) + '\n')

def rec_step(c, d, url):
	recipe_data = get_recipe_data(url)
	if c == 1:
		print('\nThe 1st step is: ' + str(step_dict(recipe_data['directions'])[1]))
		intro = input('Do you want to... \n'
			'[1] Go to the next step\n'
			'[2] Go to a specific step\n'
			'[3] Search a cooking technique on youtube\n'
			'[4] Search a tool on google\n'
			'[5] Quit\n')
		if intro == '1':
			rec_step(c+1, d, url)
		if intro == '2':
			print(str(list(d.keys())))
			intro = input('Which step number? \n')
			if intro.isnumeric():
				rec_step(int(intro), d, url)
		if intro == '3':
			intro = input('What technique do you want to search?\n')
			tknzr = TweetTokenizer()
			search_terms = intro.lower()
			tokens = tknzr.tokenize(search_terms)
			link = 'https://www.youtube.com/results?search_query=how+to+'
			b = 1
			for i in tokens:
				if b == len(tokens):
					link = link + i
					b = b + 1
				else:
					link = link + i + '+'
					b = b + 1
			print('I found a reference for you: ' + link)
			rec_step(c, d, url)
		if intro == '4':
			intro = input('What tool do you want to search?\n')
			tknzr = TweetTokenizer()
			search_terms = intro.lower()
			tokens = tknzr.tokenize(search_terms)
			link = 'https://www.google.com/search?q='
			b = 1
			for i in tokens:
				if b == len(tokens):
					link = link + i
					b = b + 1
				else:
					link = link + i + '%20'
					b = b + 1
			print('I found a reference for you: ' + link)
			rec_step(c, d, url)
		if intro == '5':
			print('\nBon Appetit!')
	else:
		print('\nThe ' + ordinal(c) + ' step is: ' + str(step_dict(recipe_data['directions'])[c]))
		intro = input('Do you want to... \n'
			'[1] Go to the next step\n'
			'[2] Go to the previous step\n'
			'[3] Go to a specific step\n'
			'[4] Search a cooking technique on youtube\n'
			'[5] Search on cooking tool on google\n'
			'[6] Quit\n')
		if intro == '1':
			if len(list(d.keys())) == c:
				print('At final step!')
			else:
				rec_step(c+1, d, url)
		if intro == '2':
			rec_step(c-1, d, url)
		if intro == '3':
			print(str(list(d.keys())))
			intro = input('Which step? \n')
			if intro.isnumeric():
				rec_step(int(intro), d, url)
		if intro == '4':
			intro = input('What technique do you want to search?\n')
			tknzr = TweetTokenizer()
			search_terms = intro.lower()
			tokens = tknzr.tokenize(search_terms)
			link = 'https://www.youtube.com/results?search_query=how+to+'
			b = 1
			for i in tokens:
				if b == len(tokens):
					link = link + i
					b = b + 1
				else:
					link = link + i + '+'
					b = b + 1
			print('I found a reference for you: ' + link)
			rec_step(c, d, url)
		if intro == '5':
			intro = input('What tool do you want to search?\n')
			tknzr = TweetTokenizer()
			search_terms = intro.lower()
			tokens = tknzr.tokenize(search_terms)
			link = 'https://www.google.com/search?q='
			b = 1
			for i in tokens:
				if b == len(tokens):
					link = link + i
					b = b + 1
				else:
					link = link + i + '%20'
					b = b + 1
			print('I found a reference for you: ' + link)
			rec_step(c, d, url)
		if intro == '6':
			print('\nBon Appetit!')
		
def main():
	print('Hi! My name is Mister Link!')
	print('I can help you with your recipes!')
	counter = 0

	url = input('Please enter the url of a recipe:\n>> ')

	recipe_data = get_recipe_data(url)

	print("Thanks! We're working with" + " " + str(recipe_data['title']))
	intro = input('What do you want to do? \n'
	'[1] Go over the ingredients list\n'
	'[2] Go over recipe steps\n')

	if intro == '1':
		print('The ingredients are: ')
		ingreds_shower(recipe_data['ingredients'])
		intro = input('What do you want to do? \n'
		'[1] Go over recipe steps\n'
		'[2] Exit :/\n')
		if intro == '2':
			print('\nBon Appetit!')
		elif intro == '1':
			counter = 1
			dct = step_dict(recipe_data['directions'])
			rec_step(1, dct, url)
	else:
		counter = 1
		dct = step_dict(recipe_data['directions'])
		rec_step(1, dct, url)



	
	methods = query_methods(recipe_data['directions'])


if __name__== '__main__':
	main()
