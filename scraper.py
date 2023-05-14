from bs4 import BeautifulSoup
import requests
import unicodedata
import re
from datetime import datetime

class Scraper:
    def __init__(self):
        self.url = "https://www.restauranteuniversitario.uerj.br/"


    def normalize_text(self, text):
        return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    
    def getDiaSemana(self):
        data_atual = datetime.now()
        dia_da_semana = data_atual.weekday()
        return dia_da_semana
    
    def scrape_data(self):
        response = requests.get(self.url)
        content = response.content.decode()
        normalized_content = self.normalize_text(content)

        soup = BeautifulSoup(normalized_content, "html.parser")

        colunas = soup.find('div', id='menu-1')
        teste = colunas.find_all(class_="et_pb_text_inner")

        p_array = []

        for element in teste:
            if element.find("p"):
                paragraph_tags = element.find_all("p")
                paragraphs = []
                for tag in paragraph_tags:
                    spans = tag.find_all("span")
                    for span in spans:
                        span.extract()
                    paragraphs.append(tag.get_text(separator=' ', strip=True).title())
                text = '/'.join(paragraphs)
                p_array.append(text)

        array_semana = []

        for i in range(0, len(p_array), 6):
            array_spliced = p_array[i:i+6]
            array_semana.append(array_spliced)

        array_strings = array_semana

        def remove_parentheses(text):
            return re.sub(r'\([^)]*\)', '', text)

        # Array atualizado sem as partes entre parênteses
        updated_array = [[remove_parentheses(string) for string in sublist] for sublist in array_strings]

        return updated_array
    def getCardapioDia(self):
        cardapio = self.scrape_data()
        dia_atual = self.getDiaSemana() 
        cardapio_do_dia = cardapio[dia_atual - 4]
        return cardapio_do_dia






