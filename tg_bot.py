import pprint
import requests
token = '7192308389:AAEAYs4PUbuzLwvtYl0KpH2NSzCWSa8fjU0'
main_url = f'https://api.telegram.org/bot{token}'
#url = f'{main_url}/getMe'
#print(url)
#result = requests.get(url)
#print(result.json())

url = f'{main_url}/getupdates'
result = requests.get(url)
pprint.pprint(result.json())

messages = result.json()['result']
for message in messages:
    chat_id = message['message']['chat']['id']
    url = f'{main_url}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': 'Привет'
    }
    result = requests.post(url,params=params)