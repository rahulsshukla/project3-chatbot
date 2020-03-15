import sys
import random
from nltk.tokenize import word_tokenize

from src.helpers import *

def to_mediterranean(steps):
    cheeses = [line.strip() for line in open('data/cheeses.txt')]
    dressings = [line.strip() for line in open('data/dressings.txt')]
    red_meats = [line.strip() for line in open('data/red_meats.txt')]
    meats = [line.strip() for line in open('data/meats.txt')]
    breads = [line.strip() for line in open('data/breads.txt')]
    sauces = [line.strip() for line in open('data/sauces.txt')]
    dressings = [line.strip() for line in open('data/dressings.txt')]
    spices = [line.strip() for line in open('data/spices.txt')]
    veggies = ['onion','red pepper','tomato','peppers','green pepper','roasted vegetables']
    ans_veggies = unibigrams(veggies)
    ans_spices = unibigrams(spices)
    ans_sauces = unibigrams(sauces)
    ans_cheeses = unibigrams(cheeses)
    ans_meats = unibigrams(meats)
    ans_rm = unibigrams(red_meats)
    ans_breads = unibigrams(breads)
    ans_dressings = unibigrams(dressings)
    med = ["lamb", "chicken", "falafel"]
    med_sauces = ["Tahini sauce","Tzatziki sauce","Chermoula","Harissa","Toum"]
    c_f = ['chicken','falafel']
    med_spices = ['za\'atar','rosemary','sage','basil']

    for step in steps:
        for i in step['ingredients']:
            name = i['name']
            if name in spices:
                custom_replace_name(step['ingredients'], i['name'], random.choice(med_spices))
            elif name in breads:
                custom_replace_name(step['ingredients'], i['name'], 'pita')
            elif name in sauces:
                custom_replace_name(step['ingredients'], i['name'], random.choice(med_sauces))
            elif name in cheeses:
                custom_replace_name(step['ingredients'], i['name'], 'feta cheese')
            elif name == 'butter':
                custom_replace_name(step['ingredients'], i['name'], 'olive oil')
            elif name in meats:
                if name in red_meats:
                    custom_replace_name(step['ingredients'], i['name'], 'lamb')
                else:
                    custom_replace_name(step['ingredients'], i['name'], random.choice(c_f))
            elif name in dressings:
                custom_replace_name(step['ingredients'], i['name'], 'greek dressing')
