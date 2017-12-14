# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from django.conf import settings

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
    return JsonResponse({"name":"zhang"})

def query(skd,field):
    fieldFir = ["_id","innerCode","trade_date","symbol","name","sec_type","list_sec","chi_spel",
               "area_code","area_name","is_st","is_margin","list_date","act_date","div_year",
               "div_date","div_pct","mkt_num","a_mkt_num","totl_num","in_hld_pct","in_chng_pct",
               "mng_hld_pct","mng_chng_pct","perf_idx","val_idx","fin_idx","fcst_idx","mkt2_idx",
               "org_hld_pct","org_chng_pct","staff_num","sw_indu_name","sw_indu_code","cname",
               "com_brief","mkt_idx","signal_normal","candle_charts","exchange","pattern",
               "status_type","free_a_mkt_num"]
    if field in fieldFir:



def index2(request):
    """
    用来测试mongo与django连接的方法
    :param request:
    :return:
    """
    john = Employee(name="John Doe", age=25)
    john.save()

    res = Z3_EQUITY_HISTORY.objects.filter(name="zhang")
    print(res)
    zoe = Z3_EQUITY_HISTORY(name="John Doe", age=25)
    zoe.save()

    context = {"name":"li"}
    return render(request,"index2.html",context)