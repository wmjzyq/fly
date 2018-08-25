from model.BaseModel import BaseModel
from peewee import CharField

class Admin(BaseModel):
    username = CharField()
    password = CharField()