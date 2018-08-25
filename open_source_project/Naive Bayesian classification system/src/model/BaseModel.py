from playhouse.db_url import connect
from peewee import Model

db = connect('mysql://root:123456@localhost:3306/graduate')

class BaseModel(Model):
    class Meta:
        database = db