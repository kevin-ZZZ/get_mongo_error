# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.conf import settings
from .field_list import fieldFir, perf_idx, val_idx, fin_idx, fcst_idx, mkt2_idx, mkt_idx, signal_normal, candle_charts


# Create your views here.

def index(request):
    """
    返回主页信息
    :param request:
    :return:
    """
    return render(request, "index.html")


def submit(request):
    """
    接收上传的参数
    :param request:
    :return:
    """
    dict = request.POST
    if dict:
        skd = dict.get("skd")
        field = dict.get("field")
        print("std:{arg}".format(arg=skd))
        print("field:{arg}".format(arg=field))
    return JsonResponse({"name": "zhang"})


def query(skd, field):
    """
    通过类似ORM映射的方式用mongoengine进行查询
    :param skd:
    :param field:
    :return:
    """
    if field in fieldFir:
        pass


def rawQuery(skd, field):
    """
    不通过mongoengine提供的orm层,直接调用pymongo包查询.
    :param skd:
    :param field:
    :return:
    """
    # 通过pymongo连接数据库,进行操作
    from pymongo import MongoClient
    # 需要认证操作的mongo客户端
    # uri = "mongodb://user:password@example.com/the_database?authMechanism=SCRAM-SHA-1"
    # 不需要密码认证的本地mongo
    uri = "mongodb://0.0.0.0:27017/z3bus"
    conn = MongoClient(uri)
    # 连接到目标数据库
    db = conn.z3bus

    # 对skd进行操作
    if skd.startswith("0") or skd.startswith("3"):
        skd += ".SZ"
    elif skd.startswith("6"):
        skd += ".SH"
    else:
        return None

    # 对field字段进行操作
    listUp = [perf_idx, val_idx, fin_idx, fcst_idx, mkt2_idx, mkt_idx, signal_normal, candle_charts]
    if field in fieldFir:
        pass
    else:
        for listDown in listUp:
            if field in listDown:
                field = listDown + '.' + field
                print field
                break
        else:
            return None

    # 通过句柄db进行操作
    res = db.Z3_EQUITY_HISTORY.find({"innoCode":skd,field:None}).count()
    print res
    cursor = db.Z3_EQUITY_HISTORY.find({}, {"_id": 0, "name": 1})
    print(JSONEncoder().encode(list(cursor)))
    return {"count": res, }


def index2(request):
    """
    用来测试mongo与django连接的方法
    :param request:
    :return:
    """
    dict = Z3_EQUITY_HISTORY.objects.filter(age__gte=30).filter(other__hobby="soccer")
    print 'dict的个数为%s' % len(dict)
    context = {"name": dict}
    return render(request, "index2.html", context)
