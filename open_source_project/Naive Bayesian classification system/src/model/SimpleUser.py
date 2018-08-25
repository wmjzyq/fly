from model.BaseModel import BaseModel
from peewee import CharField

class SimpleUser(BaseModel):
    username = CharField()
    password = CharField()