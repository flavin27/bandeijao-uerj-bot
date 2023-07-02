import requests
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session
import os
import json
from scraper import Scraper
from datetime import datetime

data_hoje = datetime.now()
dia_hoje = data_hoje.weekday()
dias_da_semana = ['Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo']
data_formatada = data_hoje.strftime("%d/%m/%Y")


load_dotenv()

consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET_KEY")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)




if dia_hoje < 5:
    scraper = Scraper()
    cardapio = scraper.getCardapioDia()

    payload = {"text": f"{dias_da_semana[dia_hoje]} - {data_formatada} \n Saladas: {cardapio[0]} \n Prato Principal: {cardapio[1]} \n Ovolactovegetariano: {cardapio[2]} \n Guarnição: {cardapio[3]} \n Acompanhamentos: {cardapio[4]} \n Sobremesas: {cardapio[5]}"}
    
    response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
)

    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )
    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))
else:
    print("oi")
