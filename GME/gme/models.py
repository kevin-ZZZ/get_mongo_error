# coding:utf-8
from mongoengine import *
import json
from bson import ObjectId

# Create your models here.

class JSONEncoder(json.JSONEncoder):
    """
    用于将机器码objectid转化成程序可以输出的字符串
    """
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


