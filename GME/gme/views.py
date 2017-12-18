# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.conf import settings
from .field_list import fieldFir, perf_idx, val_idx, fin_idx, fcst_idx, mkt2_idx, mkt_idx, signal_normal, candle_charts
from manage import db
import time
from threading import Lock



def index(request):
    """
    返回主页信息
    :param request:
    :return:
    """
    return render(request, "index.html")

"""
def rawQuery(skd, field):

    不通过mongoengine提供的orm层,直接调用pymongo包查询.
    :param skd:
    :param field:
    :return:

    # 通过句柄db进行操作
    res = db.Z3_EQUITY_HISTORY.find({"innoCode": skd, field: None}).count()
    print res
    cursor = db.Z3_EQUITY_HISTORY.find({}, {"_id": 0, "name": 1})
    print(JSONEncoder().encode(list(cursor)))
    return {"count": res, }
"""

def index2(request):
    """
    用来测试mongo与django连接的方法
    :param request:
    :return:
    """
    # 接收ajax 数据请求
    dict = request.POST
    if not dict:
        return render(request, None)
    skd = dict.get("skd")
    field = dict.get("field")
    if not (skd and field):
        return render(request, None)

    # 将输入的skd变成带后缀的股票代码
    if skd.startswith("3") or skd.startswith("0"):
        skd += ".SZ"
    elif skd.startswith("6"):
        skd += ".SH"
    else:
        return render(request, None)

    data = readKeySet()
    # 将简略的字段变成全长字段,如"expr_enddate"变为"perf_idx.expr_enddate",便于查询
    if field in data:
        res = db.Z3_EQUITY_HISTORY.find({"innerCode": skd, field: None}, {"_id": 0, "innerCode": 1, "trade_date": 1})
        count = db.Z3_EQUITY_HISTORY.find({"innerCode": skd, field: None}).count()
    else:
        for i in data:
            if field in i:
                res = db.Z3_EQUITY_HISTORY.find({"innerCode": skd, i: None},
                                                {"_id": 0, "innerCode": 1, "trade_date": 1})
                count = db.Z3_EQUITY_HISTORY.find({"innerCode": skd, i: None}).count()
            else:
                return render(request, None)

    context = {"res": res}
    return render(request, context)


def readKeySet():
    """
    用于取出文件中的字符串,并且处理成集合模式
    :return:
    """
    data = set()
    f = open("/home/python/Desktop/keySet.py" , "r")
    oriData = f.read()
    f.close()
    data = set(oriData.split(","))
    return data


def connectMongod():
    # 不使用mongoengin进行操作
    # 通过pymongo连接数据库,进行操作
    from pymongo import MongoClient
    # 需要认证操作的mongo客户端
    uri = "mongodb://z3dbusadmin:z3dbusadmin@10.77.4.37:27017/z3dbus?authMechanism=SCRAM-SHA-1"
    # 不需要密码认证的本地mongo
    # uri = "mongodb://0.0.0.0:27017/z3bus"
    conn = MongoClient(uri)
    # 连接到目标数据库
    db = conn.z3dbus
    return db


