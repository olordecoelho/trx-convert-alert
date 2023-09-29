      ##scraping##

import urllib.request #biblioteca para fazer as requisições no site
from bs4 import BeautifulSoup #biblioteca para pegar valores nas tags HTML

##Libs adicionais##
import threading #Biblioteca para criar o loop com intervalos
import sys #Só utilizei essa para parar o loop

##Criei um loop com intervalos##
def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def foo():
    wiki = "https://dolarhoje.com/tron-hoje/" #link do site para o scraping
    page = urllib.request.urlopen(wiki) #Fazendo uma requisição na pagina do site
    soup = BeautifulSoup(page, 'html5lib') #Recomendo instalar essa lib usando pip install html5lib
    div = soup.find('span', class_='cotMoeda nacional') #Encontrando tag a partir da classe
    valor = div.find('input') #Buscando tag filha
    valorf = float(valor['value'].replace(',', '.')) #Pegando o valor e convertendo para tipo float

    if valorf >= 1.0: #condição para o envio do email
        import alertmail #importando o arquivo.py que irá enviar o email 
        sys.exit() #Fim do loop

setInterval(foo, 3600) #intervalo de uma(1) hora para cada request no site
