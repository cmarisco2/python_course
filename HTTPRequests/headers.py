from urllib import response
import requests

url = "https://icanhazdadjoke.com/"

# returns HTML by defalut
# response = requests.get(url)
# print(response.text)


response = requests.get(
    url,
    headers={
        'Accept': 'application/json'
    }
)

data = response.json()

print(type(data))
print(data)
