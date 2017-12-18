#! /usr/bin/python2
# coding:utf-8
# 这个文件是需要定时执行的文件,在linux下定时开启命令


import sched
from threading import Lock
from pymongo import MongoClient
import time


def getDb():
    """
    获取操作数据库所用的句柄
    :return:
    """
    """
    # 需要认证操作的mongo客户端
    # uri = "mongodb://z3dbusadmin:z3dbusadmin@10.77.4.37:27017/z3dbus?authMechanism=SCRAM-SHA-1"
    conn = MongoClient(uri)
    db = conn.z3dbus
    """
    # 不需要密码认证的本地mongo
    uri = "mongodb://0.0.0.0:27017/z3dbus"
    conn = MongoClient(uri)
    db = conn.z3dbus
    print("已经连接到了数据库")
    # 连接到目标数据库
    return db


def getAverageKeySet():
    """
    # 随机找出3只股票,将字段求并集,每天定时执行一次
    :return:
    """
    db = getDb()
    mutex = Lock()
    mutex.acquire()
    keySet1 = getKeySet(db, "000027.SZ")
    keySet2 = getKeySet(db, "000046.SZ")
    keySet3 = getKeySet(db, "600120.SH")
    keySet = keySet1 | keySet2 | keySet3

    data = ",".join(list(keySet))
    writeData(data)
    print data
    print("今天天气很好")
    mutex.release()


def getKeySet(db, innerCode):
    """
    通过调用getKey函数,得到整个mongo表中所有的字段
    :param db:
    :return:
    """
    # 提取出mongo表中所有的字段
    tableKey = set()
    # result = db.Z3_EQUITY_HISTORY.find({"innerCode": innerCode})
    # 测试
    result = db.Z3_EQUITY_HISTORY.find({})
    for res in result:
        getKey(res, tableKey, "")
    # print db.Z3_EQUITY_HISTORY.find({"innerCode": innerCode}).count()
    # 测试
    print(db.Z3_EQUITY_HISTORY.find({}).count())
    return tableKey


def getKey(res, tableKey, pre):
    """
    将mongo中的所有字段当做嵌套字典解析,将结果存到集合中
    :param res:查询集中的一个Document
    :param tableKey: 用于盛放key的集合
    :return:
    """
    for key, value in res.items():
        if not isinstance(value, dict):
            tableKey.add(pre + key)
        else:
            if pre:
                content = pre + key + "."
            else:
                content = key + "."
            getKey(value, tableKey, content)


def writeData(data):
    """
    写入从mongo中提取出来的字符串
    :return:
    """
    f = open("/home/python/Desktop/keySet.py", "w")
    f.write(data)
    f.close()


if __name__ == '__main__':
    getAverageKeySet()
