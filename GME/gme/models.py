# coding:utf-8

from django.db import models
from mongoengine import *
# Create your models here.


# class Z3_EQUITY_HISTORY(Document):
#     """
#     大框表的模型字段
#     """
#     def __init__(self):
#         pass


class Employee(Document):
    name = StringField(max_length=50)
    age = IntField(required=False)


class Z3_EQUITY_HISTORY(Document):
    name = StringField(max_length=50)
    age = IntField(required=True)

    meta = {"collection":"Z3_EQUITY_HISTORY"}