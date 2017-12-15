# coding:utf-8
from .models import *
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

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

def index(request):
    # 使用模型类进行操作
    dic = Z3_EQUITY_HISTORY.objects.filter(age__gte=30)
    for i in dic:
        print dict(i)
    # print 'dic的个数为%s' % len(dic)
    context = {"name": "dict"}
    return render(request, "index2.html", context)

def query(skd, field):
    """
    通过类似ORM映射的方式用mongoengine进行查询
    :param skd:
    :param field:
    :return:
    """
    if field in fieldFir:
        pass