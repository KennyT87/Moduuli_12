import requests

def get_random_chuck_norris_joke():
    response = requests.get('https://api.chucknorris.io/jokes/random')
    joke = response.json()['value']
    print(joke)

get_random_chuck_norris_joke()