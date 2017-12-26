# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import *
from django.conf import settings
import time
from threading import Lock


def index(request):
    """
    返回主页信息
    :param request:
    :return:
    """
    return render(request, "index.html")


def index2(request):
    """
    用来测试mongo与django连接的方法
    :param request:
    :return:
    """
    # 接收ajax 数据请求
    dict = request.POST
    if not dict:
        return HttpResponse(json.dumps({"code": "3", "show": "输入的股票代码有误!"}))
    skd = dict.get("skd")
    field = dict.get("field")

    # 将输入的skd变成带后缀的股票代码
    if (skd.startswith("3") or skd.startswith("0")) and len(skd) == 6:
        skd += ".SZ"
    elif skd.startswith("6") and len(skd) == 6:
        skd += ".SH"
    else:
        return HttpResponse(json.dumps({"code": "0", "show": "输入的股票代码有误!"}))

    # 取出保存在本地文件里面的数据(显示mongo嵌套结构的数据)
    data = readKeySet()
    db = connectMongod()

    # 将简略的字段变成全长字段,如"expr_enddate"变为"perf_idx.expr_enddate",便于查询
    if field in data:
        print("skd:%s" % skd)
        result = db.Z3_EQUITY_HISTORY.find({"innerCode": skd, field: None},
                                           {"_id": 0, "innerCode": 1, "trade_date": 1, field: 1})
        count = db.Z3_EQUITY_HISTORY.find({"innerCode": skd, field: None}).count()
    else:
        for i in data:
            if field in i:
                result = db.Z3_EQUITY_HISTORY.find({"innerCode": skd, i: None},
                                                   {"_id": 0, "innerCode": 1, "trade_date": 1, field: 1})
                count = db.Z3_EQUITY_HISTORY.find({"innerCode": skd, i: None}).count()
        else:
            return HttpResponse(json.dumps({"code": "0", "show": "输入的字段不存在"}))
    print count
    dataList = []
    if not count:
        return HttpResponse(json.dumps({"code": "2", "show": "查询到0个结果"}))
    else:
        for res in result:
            dataList.append({"innerCode": res["innerCode"], "trade_date": res["trade_date"], field: res[field]})
    # print context
    context = json.dumps({"code": "1", "innerCode": skd, "count": count, "context": dataList})
    return HttpResponse(context)


def connectMongod():
    """
    连接到mongo,返回db
    :return:
    """
    # 通过pymongo连接数据库,进行操作
    from pymongo import MongoClient
    # 需要认证操作的mongo客户端
    # uri = "mongodb://z3dbusadmin:z3dbusadmin@10.77.4.37:27017/z3dbus?authMechanism=SCRAM-SHA-1"
    # 不需要密码认证的本地mongo
    uri = "mongodb://0.0.0.0:27017/z3dbus"
    conn = MongoClient(uri)
    # 连接到目标数据库
    db = conn.z3dbus
    return db


def readKeySet():
    """
    用于取出文件中的字符串,并且处理成集合模式
    :return:
    """
    data = set()
    f = open("/home/python/Desktop/keySet.py", "r")
    oriData = f.read()
    f.close()
    data = set(oriData.split(","))
    return data
