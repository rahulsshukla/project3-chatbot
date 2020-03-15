import requests
from bs4 import BeautifulSoup
from nltk.tokenize import TweetTokenizer
import re
import nltk
import fractions

from src.helpers import *

def make_veg(steps):
    meat = ['beef', 'chicken', 'pork', 'salmon', 'tuna', 'sausage', 'veal', 'turkey', 'duck', 'goat', 'lamb', 'meatball',
            'shrimp', 'crab', 'lobster', 'hot dog', 'bacon', 'ham', 'burger', 'patty', 'pork', 'meat', 'ground beef', 'ground pork',
            'ground turkey']
     
    for step in steps:
        for i in step['ingredients']:
            for m in meat:
                if m == i['name']:
                    custom_replace_name(step['ingredients'], i['name'], 'tofu')

def double_amount(steps):
    for step in steps:
        for i in step['ingredients']:
            quantity = str(i['quantity'])
            if '/' in quantity:
                fraction_obj = sum(map(fractions.Fraction, quantity.split()))
                doubled = fraction_obj + fraction_obj
                n = doubled.numerator
                d = doubled.denominator
                if str(n) == str(d):
                    amount = '1'
                else:
                    amount = str(n) + str('/') + str(d)

                custom_replace_quantity(step['ingredients'], i['quantity'], amount)

            elif quantity.isnumeric():
                amount = int(i['quantity']) * 2
                custom_replace_quantity(step['ingredients'], i['quantity'], amount)

def make_meat(steps):
    subs = ['tofu', 'eggplant', 'seitan', 'jackfruit']

    for step in steps:
        updated = False
        for i in step['ingredients']:
            for s in subs:
                if s == i['name']:
                    custom_replace_name(step['ingredients'], i['name'], 'chicken')
                    updated = True
        if not updated:
            step['ingredients'].append({
                'name': 'chicken',
                'quantity': '1',
                'measurement': 'pound',
                'descriptor': [],
                'preparation': []
            })
