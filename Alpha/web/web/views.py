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
    request.encoding = 'utf-8'
    data = {}
    '''取出用户名，密码'''
    name_ = request.POST.get('username','')
    pass_ = request.POST.get('pwd','')
    #判断是否成功连接
    db = Synco()
    if(db.conn(name_,pass_)):
        rescode = 201
    else :
        rescode = 200

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
    data['data'] = res
    sample = json.dumps(data)
    return HttpResponse(sample, content_type="application/json")

@csrf_exempt
def sqlExecute(request):
    request.encoding = 'utf-8'
    '''取出操作数据库 sql语句内容'''
    dbname = request.POST.get('dbname','')
    sqlQuery = request.POST.get('sqlQuery','')
    db = Synco()
    data = {}
    '''判断操作类型'''
    if sqlQuery[0:6] == "select":
        res = db.SQLExecute(dbname,1,sqlQuery)
        data['data'] = res
        data['status'] = "success"
    else:
        status = db.SQLExecute(dbname,0,sqlQuery)
        data['status'] = status
    sample = json.dumps(data)  # json.dumps()把一个Python对象编，码转换成Json字符串。
    return HttpResponse(sample, content_type="application/json")  # 返回给前端



