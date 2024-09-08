import requests
from bs4 import BeautifulSoup
from fastapi import APIRouter
from client import db
from models import NewsSource
from datetime import date


router = APIRouter(prefix="/scraping", tags=["Web Scraping"])

news_collection = db.news
source_collection = db.sources


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


@router.post("/source/")
def new_source(source: NewsSource):
    new = source_collection.insert_one(
        {
            "link": source.link,
            "name": source.name,
            "title_tag": source.title_tag,
            "title_class": source.title_class,
            "content_tag": source.content_tag,
            "content_class": source.content_class,
        }
    )
    return {"message": "success", "id": str(new.inserted_id)}


# titlesfromwebsite("https:///elpais.com/america/", "h2", "El Pais)             SHECK
# titlesfromwebsite("https://cnnespanol.cnn.com/", "h2", "CNN Español")         SHECK
# titlesfromwebsite("https://www.bbc.com/mundo", "h3", "BBC")                   SHECK
# titlesfromwebsite("https://www.elmundo.es/", "h2", "El Mundo")                SHECK


@router.get("/elpais")
def webscrapping():
    getter = requests.get("https://elpais.com/america/")
    soup = BeautifulSoup(getter.content, "html.parser")
    print(soup)
    article_urls = []
    for a in soup.find_all("h2"):
        try:
            hr = a.find("a")
            article_urls.append(hr["href"])
        except: pass
    articles = []
    for url in article_urls:
        article_getter = requests.get(url)
        article_soup = BeautifulSoup(article_getter.content, "html.parser")
        if len(articles) == 25:
            break
        try:
            article_title = article_soup.find(
                "h1", {"class": "a_t"}
            ).text
            article_content = article_soup.find(
                "h2", {"class": "a_st"}
            ).text
            print({"url": url, "title": article_title, "content": article_content})
            articles.append(
                {"url": url, "title": article_title.strip(), "content": article_content.strip()}
            )
        except:
            pass
    news_collection.insert_one(
        {"website": "El País", "articles": articles, "time": str(date.today()), "sentiment": None}
    )
    return {"website": "El País", "articles": articles}

@router.get("/bbcmundo")
def webscrapping():
    getter = requests.get("https://www.bbc.com/mundo")
    soup = BeautifulSoup(getter.content, "html.parser")

    article_urls = []
    for a in soup.find_all("h3"):
        try:
            hr = a.find("a")
            article_urls.append(hr["href"])
        except: pass
    articles = []
    for url in article_urls:
        article_getter = requests.get(url)
        article_soup = BeautifulSoup(article_getter.content, "html.parser")
        if len(articles) == 25:
            break
        try:
            article_title = article_soup.find(
                "h1", {"class": "bbc-14gqcmb e1p3vdyi0"}
            ).text
            article_content = article_soup.find(
                "p", {"class": "bbc-hhl7in e17g058b0"}
            ).text
            print({"url": url, "title": article_title, "content": article_content})
            articles.append(
                {"url": url, "title": article_title.strip(), "content": article_content.strip()}
            )
        except:
            pass
    news_collection.insert_one(
        {"website": "BBC Mundo", "articles": articles, "time": str(date.today()), "sentiment": None}
    )
    return {"website": "BBC Mundo", "articles": articles}

@router.get("/ceñeeñe")
def webscrapping():
    getter = requests.get("https://cnnespanol.cnn.com/")
    soup = BeautifulSoup(getter.content, "html.parser")

    article_urls = []
    for a in soup.find_all("h2", {"class": "news__title"}):
        try:
            hr = a.find("a")
            article_urls.append(hr["href"])
        except: pass
    articles = []
    for url in article_urls:
        article_getter = requests.get(url)
        article_soup = BeautifulSoup(article_getter.content, "html.parser")
        if len(articles) == 25:
            break
        try:
            article_title = article_soup.find(
                "h1", {"class": "storyfull__title"}
            ).text
            
            article_content = ""
            for p in article_soup.find_all("p"):
                strong_tag = p.find('strong')
                if strong_tag and strong_tag.next_sibling and isinstance(strong_tag.next_sibling, str):
                    article_content = p.get_text(separator=' ')
            
            print({"url": url, "title": article_title, "content": article_content})
            articles.append(
                {"url": url, "title": article_title.strip(), "content": article_content.strip(), "sentiment": None}
            )
        except:
            pass
    news_collection.insert_one(
        {"website": "CNN Español", "articles": articles, "time": str(date.today())}
    )
    return {"website": "CNN Español", "articles": articles}


@router.get("/elmundo")
def webscrapping():
    getter = requests.get("https://www.elmundo.es/")
    soup = BeautifulSoup(getter.content, "html.parser")

    article_urls = []
    for a in soup.find_all("header", {"class": "ue-c-cover-content__headline-group"}):
        try:
            hr = a.find("a")
            article_urls.append(hr["href"])
        except: pass
    articles = []
    for url in article_urls:
        article_getter = requests.get(url)
        article_soup = BeautifulSoup(article_getter.content, "html.parser")
        if len(articles) == 25:
            break
        try:
            article_title = article_soup.find(
                "h1", {"class": "ue-c-article__headline js-headline"}
            ).text
            article_content = article_soup.find(
                "p", {"class": "ue-c-article__paragraph"}
            ).text
            print({"url": url, "title": article_title, "content": article_content})
            articles.append(
                {"url": url, "title": article_title.strip(), "content": article_content.strip(), "sentiment": None}
            )
        except:
            pass
    news_collection.insert_one(
        {"website": "El Mundo", "articles": articles, "time": str(date.today())}
    )
    return {"website": "El Mundo", "articles": articles}


@router.get("/nbcnews") #   WORKS
def webscrapping():
    getter = requests.get("https://www.nbcnews.com/world")
    soup = BeautifulSoup(getter.content, "html.parser")
    article_urls = []
    for a in soup.find_all("h2"):
        try:
            hr = a.find("a", href=True)
            article_urls.append(hr["href"])
        except: pass
    articles = []
    for url in article_urls:
        article_getter = requests.get(url)
        article_soup = BeautifulSoup(article_getter.content, "html.parser")
        if len(articles) == 10:
            break
        try:
            article_title = article_soup.find(
                "h1"
            ).text
            article_content = article_soup.find(
                "div", {"data-testid": "article-dek"}
            ).text
            # print({"url": url, "title": article_title, "content": article_content})
            articles.append(
                {"url": url, "title": article_title.strip(), "content": article_content.strip()}
            )
            news_collection.insert_one({
                "website": "NBC News", "title": article_title.strip(), "content": article_content.strip(), "date": str(date.today()), "sentiment": None
            })
        except:
            pass

    return {"website": "NBC News", "articles": articles}


@router.get("/cnn_news") #  WORKS
def webscrapping():
    getter = requests.get("https://edition.cnn.com/world")
    soup = BeautifulSoup(getter.content, "html.parser")
    article_urls = []
    for a in soup.find_all("div", {"data-created-updated-by": "true"}):
        try:
            hr = a.find("a", href=True)
            article_urls.append("https://edition.cnn.com" + hr["href"])
        except: pass
        
    print(article_urls)
    articles = []
    for url in article_urls:
        article_getter = requests.get(url)
        article_soup = BeautifulSoup(article_getter.content, "html.parser")
        if len(articles) == 10:
            break
        try:
            article_title = article_soup.find(
                "h1"
            ).text
            article_content = article_soup.find(
                "div", {"itemprop": "caption"}
            ).text
            # print({"url": url, "title": article_title, "content": article_content})
            articles.append(
                {"url": url, "title": article_title.strip(), "content": article_content.strip()}
            )
            news_collection.insert_one({
                "website": "CNN News", "title": article_title.strip(), "content": article_content.strip(), "date": str(date.today()), "sentiment": None
            })
        except:
            pass

    return {"website": "CNN News", "articles": articles}