# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
import json
import os
import numpy as np
from django.views.decorators.csrf import csrf_exempt
from pylab import *
# mpl.rcParams['font.sans-serif'] = ['SimHei']
# titles=["图一反应条件：448K 1.0MPa","图二反应条件：453K 1.0MPa","图三反应条件：458K 1.0MPa","图四反应条件：463K 1.0MPa","图五反应条件：443K 1.0MPa 酯浓度0.002mol/m3","图六反应条件：443K 1.0MPa 酯浓度0.001mol/m3","图七反应条件：443K 1.0MPa 酯浓度0.004mol/m3"]

password="123456"
username="admin"
ip="127.0.0.1"
port="9000"


@csrf_exempt
def page1_check(request):
    request.encoding = 'utf-8'
    data = {}

    '''取出用户名，密码'''
    # 以可读方式打开文件
    fp = open("data.json", 'r')
    json_data = json.load(fp)
    global username,password,ip,port
    username = json_data["username"]
    password = json_data["pass"]
    fp.close()
    name_=request.GET.get('username','')
    pass_=request.GET.get('pwd','')
    ip_=request.GET.get('ip','')
    port_ = request.GET.get('port','')

    if (username==name_)==False:
        rescode=201  #用户名错误
    elif (password==pass_)==False:
        rescode = 202  # 密码错误
    elif (ip==ip_)==False:
        rescode = 203  # IP错误
    elif (port==port_)==False:
        rescode = 203  # port错误
    else :
        rescode=200

    data['res']=rescode
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




