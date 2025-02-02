import requests
import json
import random
from datetime import timedelta, datetime

today = datetime.now()
tomorrow = datetime.now() + timedelta(days=1)
date = tomorrow.strftime('%m/%d')

url = 'https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/all/' + date
# whee 

# print(url)
def get_fun():
    response = requests.get(url)
    data = response.json()
    # print(data)
    we = list(data)
    bruh = random.choice(we)
    if(bruh != 'holidays'):
        e = data[bruh]
        we2 = random.choice(e)
        e = we2
        we2 = e.get('year')
        f = e.get('pages')
        f = random.choice(f)
        f = f['extract']
        # f = f.get('extract')
        # e = e.get('extract')
        return("year: " + str(we2) + " type: " + bruh + " - " + f)
    else:
        e = data[bruh]
        we2 = random.choice(e)
        e = we2
        # we2 = e.get('year')
        f = e.get('pages')
        f = f[0]
        f = f['extract']
        # f = f.get('extract')
        # e = e.get('extract')
        return( "HOLIDAY!! - " + f)
    # we = (random.choice(random.choice(list(data))))
    # return(we) # DONT USE YET

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
    quote = random.choice(data['quotes'])
    return (quote['text'] + " - " + quote['author']) 
# print(tell_joke())
print(get_quote())
print( get_fun())
