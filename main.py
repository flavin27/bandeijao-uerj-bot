from twitter import Twitter
from scraper import Scraper
from datetime import datetime
import time


def main():
    data_hoje = datetime.now()
    dia_hoje = data_hoje.weekday()
    dias_da_semana = ['Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo']
    data_formatada = data_hoje.strftime("%d/%m/%Y")

    if dia_hoje < 5:
        scraper = Scraper()
        cardapio = scraper.getCardapioDia()
        client = Twitter()

        payload = {"text": f"{dias_da_semana[dia_hoje]} - {data_formatada} \n Saladas: {cardapio[0]} \n Prato Principal: {cardapio[1]} \n Ovolactovegetariano: {cardapio[2]} \n Guarnição: {cardapio[3]} \n Acompanhamentos: {cardapio[4]} \n Sobremesas: {cardapio[5]}"}
        
        response = client.postTweet(payload)
        print(response)
    else:
        client = Twitter()
        text = {"text": "teste6"}
        resposta = client.postTweet(text)
        print(resposta)

main()