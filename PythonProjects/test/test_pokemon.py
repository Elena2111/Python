import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '9bb4b06f5154cb3714346467f1f84e17'
HEADER = {'Content-Type':'application/json','trainer_token': TOKEN}
TRAINER_ID = '17577'

def test_status_code():
    responce = requests.get(url = f'{URL}trainers')
    assert responce.status_code == 200

def test_part_of_response():
    responce_get = requests.get(url = f'{URL}trainers', params = {'trainer_id': TRAINER_ID})
    assert responce_get.json()["data"][0]["trainer_name"] == 'meanie'  