from model.BaseModel import BaseModel
from peewee import CharField

class ReporterUser(BaseModel):
    username = CharField()
    password = CharField()