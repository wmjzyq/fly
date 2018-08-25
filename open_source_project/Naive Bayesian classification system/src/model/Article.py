from model.BaseModel import BaseModel
from peewee import CharField, TextField

class Article(BaseModel):
    title = CharField()
    content=TextField()
    detail_source=CharField()
    tag=CharField()
    time=CharField()
    img_url = CharField()