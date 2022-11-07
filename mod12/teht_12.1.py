import requests

ask_joke = "https://api.chucknorris.io/jokes/random"
joke = requests.get(ask_joke).json()
print(joke["value"])