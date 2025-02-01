

import requests
import json
import random
import datetime

today = datetime.datetime.now()
date = today.strftime('%m/%d')

url = 'https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/all/' + date
# whee 


def get_fun():
    response = requests.get(url)
    data = response.json()
    print(data) # DONT USE YET

def tell_joke():
    site = requests.get("https://icanhazdadjoke.com/",
                                headers={
                                    'Accept': 'application/json',
                                })
    data = site.json()
    return data['joke']

def get_quote():
    site = requests.get("https://thequoteshub.com/api/tags/tomorrow")
    data = site.json()
    return random.choice(data['quotes'])['text']
# get_fun()
print(tell_joke())
print(get_quote())
