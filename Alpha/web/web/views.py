# Create your views here.
from random import sample
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
import json
import os
from .syncodb.Synco import Synco
import numpy as np
from django.views.decorators.csrf import csrf_exempt
from pylab import *


@csrf_exempt
def page1_check(request):
    data = {}
    '''取出用户名，密码'''
    data = json.loads(request.body.decode('utf-8'))
    name_ = data.get('username')
    pass_ = data.get('pwd')

    #判断是否成功连接
    db = Synco()
    if(db.conn(name_,pass_)):
        rescode = 200#成功
    else :
        rescode = 201

    data['status']=rescode
    sample = json.dumps(data)  # json.dumps()把一个Python对象编，码转换成Json字符串。
    return HttpResponse(sample, content_type="application/json")  # 返回给前端

@csrf_exempt
def page2_getsql(request):
    request.encoding = 'utf-8'
    sql=request.GET.get('request','')
    data = {}
    res=''
    #调用c函数，将c函数返回的结果保存在res当中
    data['res'] = res
    HttpResponse(sample, content_type="application/json")  # 返回给前端

@csrf_exempt
def getCurrPath(request):
    data = {}
    res = ''
    db = Synco()
    res = db.currPath()
    data['res'] = res
    sample = json.dumps(data)
    return HttpResponse(sample, content_type="application/json")


@csrf_exempt
def getDatabase(request):
    data = {}
    db = Synco()
    res = db.getDatabase()
    data['datas'] = res
    sample = json.dumps(data)
    return HttpResponse(sample, content_type="application/json")

@csrf_exempt
def sqlExecute(request):
    '''取出操作数据库 sql语句内容'''
    ret = json.loads(request.body.decode('utf-8'))
    dbname = ret.get('dbname')
    sqlQuery = ret.get('sqlQuery')
    db = Synco()
    data = {}
    List = []
    Obj = {}
    Obj['操作'] = sqlQuery
    List.append(Obj)
    data['res1'] = List

    # dbname="user"
    # sqlQuery="SELECT * FROM user;"
    '''判断操作类型'''
    # @bianying: 修改为SELECT: Sqlite大小写敏感, 固定词必须全大写
    if sqlQuery[0:6] == "SELECT":
        res = db.SQLExecute(dbname,1,sqlQuery)
        data['res2'] = res
        # data['status'] = "success"
    else:
        status = db.SQLExecute(dbname,0,sqlQuery)
        data['res2']=status

    sample = json.dumps(data)  # json.dumps()把一个Python对象编，码转换成Json字符串。
    return HttpResponse(sample, content_type="application/json")  # 返回给前端



