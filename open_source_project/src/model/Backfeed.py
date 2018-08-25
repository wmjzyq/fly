from model.BaseModel import BaseModel
from peewee import CharField, IntegerField

class Backfeed(BaseModel):
    content = CharField()