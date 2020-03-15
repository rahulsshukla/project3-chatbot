import requests
from bs4 import BeautifulSoup
from nltk.tokenize import TweetTokenizer
import re
import nltk
import fractions


#input is a url as a string
def get_ingredients(url):
    ingredients = scrape_ingredients(url)
    ingreds = {}
    for i in ingredients:
        tknzr = TweetTokenizer()
        t = tknzr.tokenize(i)
        if '/' in t[1]:
            quantity = t[0] + ' ' + t[1]
        
        elif not hasNumbers(t[0]):
            quantity = t[1]
        else:
            quantity = t[0]
        
        measurement = get_measurement(i)

        name = get_name(i)
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
            n = n + j + ' '

        pos = get_descriptor(name)

        prep = get_prep(name, i)

        ingreds[str(n)] = [str(quantity), str(measurement), pos, prep]
        
    #print('{name : [quantity, measurement, descriptor, preparation]}') 
    return ingreds

#helpers for get_ingredients
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def scrape_ingredients(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    ingredients_html = soup.findAll(class_ = 'checkList__line')
    ingredients = []
    for i in ingredients_html:
        try:
            mystr = str(i)
            ingredients.append(mystr.split('title=')[1].split('>')[0].strip('"'))
        except:
            pass
        
    return ingredients

def get_measurement(ingred):
    units = ['package','slice', 'container','litre', 'gallon', 'quart', 'stalk','cup', 'pint', 'jar', 'can', 'clove', 'ounce', 'spoon', 'gram', 'pound', 'pinch']
    tknzr = TweetTokenizer()
    t = tknzr.tokenize(ingred)
    for u in units:
        for w in t:
            if u in w:
                return w

def get_name(ingred):
    tknzr = TweetTokenizer()
    t = tknzr.tokenize(ingred)
    m = get_measurement(ingred)
    try:
        n = re.search(r'\d+', ingred).group()
        if (m and m != 'Not found' and m != 'None'):
            rest = ingred.split(m)[1]
            if ',' in rest:
                return rest.split(',')[0].lower()
            else:
                return rest.lower()
        else:
            rest = ingred.split(n)[1]
            if ',' in rest:
                return rest.split(',')[0].lower()
            else:
                return rest
    except:
        return ingred

def get_descriptor(name):
    descrip = []
    pos = nltk.pos_tag(name.split())
    for i in pos:
        if i[1] == 'JJ':
            descrip.append(i[0])
    return descrip
    
def get_prep(name, ingred):
    prep = []
    pos = nltk.pos_tag(name.split())
    for i in pos:
        if i[1] == 'VBN':
            prep.append(i[0])

    tknzr = TweetTokenizer()
    t = tknzr.tokenize(ingred)

    m = get_measurement(ingred)
    
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