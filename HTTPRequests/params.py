# demo programmatically using query string w/ params

import requests

url = "https://icanhazdadjoke.com/search"

res = requests.get(url,
                   headers={
                       'Accept': 'application/json'
                   },
                   params={
                       'term': 'dog',
                       'limit': 1
                   }
                   )
print(res.json()['results'][0]['joke'])
