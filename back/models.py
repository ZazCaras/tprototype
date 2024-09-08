from pydantic import BaseModel
from typing import Literal

class NewsSource(BaseModel):
    link: str
    name: str
    home_tag: str
    title_tag: str  
    title_class: str
    content_tag: str
    content_class: str

class Sentiment(BaseModel):
    sentiment: Literal["positive", "neutral", "negative"]