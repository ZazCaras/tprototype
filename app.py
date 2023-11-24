import requests
from bs4 import BeautifulSoup

def titlesfromwebsite(url, htmltag, doctitle):
    getter = requests.get(url)
    soup = BeautifulSoup(getter.content, 'html.parser')
    titles = [i.text for i in soup.find_all(htmltag)]
    txtstring = ''
    for i in titles: 
        txtstring += (f"{i}\n")
    with open (f"{doctitle}.txt", "w", encoding="utf-8") as file: 
        file.write(txtstring)
    return txtstring


titlesfromwebsite("https://elpais.com/america/", "h2", "El Pais")
titlesfromwebsite("https://www.prensalibre.com/", "h1", "Prensa Libre")
titlesfromwebsite("https://cnnespanol.cnn.com/", "h2", "CNN Español")
titlesfromwebsite("https://www.bbc.com/mundo", "h3", "BBC")
titlesfromwebsite("https://www.elmundo.es/", "h2", "El Mundo")