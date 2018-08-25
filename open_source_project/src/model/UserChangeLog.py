from model.BaseModel import BaseModel
from peewee import IntegerField

class UserChangeLog(BaseModel):
    userId = IntegerField()
    operate = IntegerField()

    CHANGE_PASSWORD = 1
    USER_LOGIN = 2
    USRE_REGISTER = 3
    USER_LOGOUT = 4

    UPLOAD_ARTICLE = 5
    DELETE_ARTICLE = 6