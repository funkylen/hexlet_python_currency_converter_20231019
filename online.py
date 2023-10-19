import requests

URL = "https://api.freecurrencyapi.com/v1/latest?apikey="
API_KEY = "fca_live_JQ6C4T6oLPhVV6ABYYqTEfvxplWY3YDqzRzdBpW8"


def get_currencies():
    response = requests.get(URL + API_KEY)
    return response.json()
