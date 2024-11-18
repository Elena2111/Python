import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '9bb4b06f5154cb3714346467f1f84e17'
HEADER = {'Content-Type':'application/json','trainer_token': TOKEN}

body_create = {
    "name": "Булочка",
    "photo_id": 248
}

body_change = {
    "pokemon_id": "139007",
    "name": "Винчестер",
    "photo_id": 248
}

body_pokeball = {
    "pokemon_id": "139007"
}

response_create = requests.post(url = f'{URL}pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_change = requests.put(url = f'{URL}pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_pokeball = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text) 

message = response_create.json()['message']
print(message)