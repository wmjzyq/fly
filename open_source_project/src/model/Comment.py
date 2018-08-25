from model.BaseModel import BaseModel
from peewee import CharField, IntegerField

class Comment(BaseModel):
    articleId = IntegerField()
    name = CharField()
    content = CharField()
    time = CharField()