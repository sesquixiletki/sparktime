def get_quote():
    site = requests.get("https://thequoteshub.com/api/tags/tomorrow")
    data = site.json()
    return random.choice(data['quotes'])['text']
