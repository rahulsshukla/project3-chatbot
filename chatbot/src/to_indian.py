import requests
from bs4 import BeautifulSoup
import random
from src.helpers import *
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
import re
import fractions
import sys
import itertools
from nltk.corpus import stopwords
from string import punctuation
import random


def to_indian(steps):
    spices = [line.strip() for line in open('data/spices.txt')]
    sauces = [line.strip() for line in open('data/sauces.txt')]
    indian_spices = [line.strip() for line in open('data/indian_spices.txt')]
    indian_sauces = [line.strip() for line in open('data/indian_sauces.txt')]
    breads = [line.strip() for line in open('data/breads.txt')]
    cheeses = [line.strip() for line in open('data/cheeses.txt')]
    red_meats = [line.strip() for line in open('data/red_meats.txt')]
    ans_spices = unibigrams(spices)
    ans_sauces = unibigrams(sauces)
    ans_cheese = unibigrams(cheeses)
    ans_rm = unibigrams(red_meats)
    ans_breads = unibigrams(breads)
    
    for step in steps:
        for i in step['ingredients']:
            name = word_tokenize(i['name'])
            if len(name) == 1:
                if name[0] in spices:
                    custom_replace_name(step['ingredients'], i['name'], random.choice(indian_spices))
                elif name[0] in sauces:
                    custom_replace_name(step['ingredients'], i['name'], random.choice(indian_sauces))
                elif name[0] == 'rice':
                    custom_replace_name(step['ingredients'], i['name'], 'basmati rice')
                elif name[0] in breads:
                    custom_replace_name(step['ingredients'], i['name'], 'naan')
                elif name[0] in red_meats:
                    custom_replace_name(step['ingredients'], i['name'], 'chicken')
                elif name[0] in cheeses:
                    custom_replace_name(step['ingredients'], i['name'], 'paneer')
            elif len(name) == 2:
                if name in ans_spices['bigrams']:
                    custom_replace_name(step['ingredients'], i['name'], random.choice(indian_spices))
                elif name in ans_sauces['bigrams']:
                    custom_replace_name(step['ingredients'], i['name'], random.choice(indian_sauces))
                elif name in ans_breads['bigrams']:
                    custom_replace_name(step['ingredients'], i['name'], 'naan')
                elif name in ans_rm['bigrams']:
                    custom_replace_name(step['ingredients'], i['name'], 'chicken')
                elif name in ans_cheese['bigrams']:
                    custom_replace_name(step['ingredients'], i['name'], 'paneer')
            elif len(name) == 3:
                if name in ans_spices['trigrams']:
                    custom_replace_name(step['ingredients'], i['name'], random.choice(indian_spices))
                elif name in ans_sauces['trigrams']:
                    custom_replace_name(step['ingredients'], i['name'], random.choice(indian_sauces))
                elif name in ans_breads['trigrams']:
                    custom_replace_name(step['ingredients'], i['name'], 'naan')
                elif name in ans_rm['trigrams']:
                    custom_replace_name(step['ingredients'], i['name'], 'chicken')
                elif name in ans_cheese['trigrams']:
                    custom_replace_name(step['ingredients'], i['name'], 'paneer')
