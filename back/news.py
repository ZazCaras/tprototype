from typing import Literal
from bson import ObjectId
from fastapi import APIRouter
from client import db
from models import Sentiment

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
def sentiment(em: Literal["positive", "neutral", "negative"]):
    news = []
    for i in news_collection.find({
        "sentiment": em
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
    return {"code": 0, "news": sentiment(data.sentiment)['news']}
