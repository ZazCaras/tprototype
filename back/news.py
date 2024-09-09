from typing import Literal
from bson import ObjectId
from fastapi import APIRouter
from client import db
from models import Sentiment
from nn_utils import categorize

router = APIRouter(prefix="/news", tags=["DB News"])

news_collection = db.news

@router.get("/no_sentiment")
def no_sentiment():
    news = []
    for i in news_collection.find({
        "sentiment": None
    }):
        id = str(i["_id"])
        del[i["_id"]]
        i['id'] = id
        news.append(i)
    return {"code": 0, "news": news}


@router.get("/all/{sentiment}")
def news_by_sentiment(sentiment: Literal["positive", "neutral", "negative"]):
    news = []
    for i in news_collection.find({
        "sentiment": sentiment
    }):
        id = str(i["_id"])
        del[i["_id"]]
        i['id'] = id
        news.append(i)
    return {"code": 0, "news": news}


@router.put("/change/{newsId}")
def sentiment_change(newsId: str, data: Sentiment):
    news_collection.update_one(
        {
            "_id": ObjectId(newsId)
        },
        {
            "$set": {
                "sentiment": data.sentiment
            }
        }
    )
    return news_by_sentiment(data.sentiment)


@router.get("/fetch_and_categorize/{sentiment}")
def fetch_and_categorize(sentiment: Literal["positive", "neutral", "negative"]):
    format = []
    not_categorized = no_sentiment()['news']
    for i in not_categorized:
        format.append(f"{i['title']} {i['content']}".strip())
    
    if len(not_categorized) > 0:
        scores = categorize(format)
        
        for i, e in enumerate(scores):
            emotion = "neutral"
            if e < 0.25:
                emotion = "negative"
            elif e > 0.80:
                emotion = "positive"
            sentiment_change(not_categorized[i]["id"], Sentiment(sentiment=emotion))
    
    return news_by_sentiment(sentiment)
