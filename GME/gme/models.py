# coding:utf-8

from django.db import models
from mongoengine import *
import json
from bson import ObjectId

# Create your models here.


# class Z3_EQUITY_HISTORY(Document):
#     """
#     大框表的模型字段
#     """
#     def __init__(self):
#         pass

class JSONEncoder(json.JSONEncoder):
    """
    用于将机器码objectid转化成程序可以输出的字符串
    """
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class Other(EmbeddedDocument):
    hobby = StringField(max_length=50)
    height = IntField(required=True)


class Z3_EQUITY_HISTORY(Document):
    _id = StringField(max_length=100)
    name = StringField(max_length=20)
    age = IntField(required=True)
    other = ListField(EmbeddedDocumentField(Other))

    meta = {"collection":"Z3_EQUITY_HISTORY"}