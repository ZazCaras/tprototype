from pydantic import BaseModel

class NewsSource(BaseModel):
    link: str
    name: str
    home_tag: str
    title_tag: str  
    title_class: str
    content_tag: str
    content_class: str
