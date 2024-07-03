import requests
import pydantic
import json
from bs4 import BeautifulSoup
from fastapi import FastAPI
from client import db
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

news_collection = db.news
origins = [
    "http://localhost:3000",
    "localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def titlesfromwebsite(url, htmltag, doctitle):
    getter = requests.get(url)
    soup = BeautifulSoup(getter.content, "html.parser")
    titles = [i.text for i in soup.find_all(htmltag)]
    txtstring = ""
    for i in titles:
        txtstring += f"{i}\n"
    with open(f"{doctitle}.txt", "w", encoding="utf-8") as file:
        file.write(txtstring)
    return txtstring


# @app.get("/webscrapping/{link}/{tag}/{name}")
# def webscrapping(link, tag, name):
#     getter = requests.get(link.replace("-", "/"))
#     soup = BeautifulSoup(getter.content, 'html.parser')
#     titles = [i.text for i in soup.find_all(tag)]
#     return {"website": name, "urls": titles}


@app.get("/webscrapping/{link}/{tag}/{name}")
def webscrapping(link, tag, name):
    getter = requests.get(link.replace("-", "/"))
    soup = BeautifulSoup(getter.content, "html.parser")

    article_urls = []
    for a in soup.find_all(tag):
        hr = a.find("a")
        # print(hr['href'])
        article_urls.append(hr["href"])
    # article_urls = [a['href'] for a in soup.find_all(tag, href=True)]
    articles = []
    for url in article_urls:
        article_getter = requests.get(url)
        article_soup = BeautifulSoup(article_getter.content, "html.parser")
        try:
            article_title = article_soup.find("h1", {"class": "a_t"}).text
            article_content = article_soup.find("h2", {"class": "a_st"}).text
            # article_content = article_soup.find('div', {'class': 'a_c clearfix'}).text
            print({"url": url, "title": article_title, "content": article_content})
            articles.append(
                {"url": url, "title": article_title, "content": article_content}
            )
        except:
            pass
    news_collection.insert_one({"website": name, "articles": articles})
    return {"website": name, "articles": articles}


# titlesfromwebsite("https:--elpais.com-america-", "h2", "El Pais")
# titlesfromwebsite("https://www.prensalibre.com/", "h1", "Prensa Libre")
# titlesfromwebsite("https://cnnespanol.cnn.com/", "h2", "CNN Español")
# titlesfromwebsite("https://www.bbc.com/mundo", "h3", "BBC")
# titlesfromwebsite("https://www.elmundo.es/", "h2", "El Mundo")

if __name__ == "__main__":
    uvicorn.run(app="app :app", host="0.0.0.0", port=8000, reload=True)
