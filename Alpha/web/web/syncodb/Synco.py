import os
import pandas as pd
import plotly.express as px
import re
from datetime import datetime, date, timedelta
class Synco:
    #设置端口
    def __init__(self):
        self.program = '.\SqlVS.exe'

    #输出当前路径
    def currPath(self):
        return os.getcwd()

    #连接数据库
    def conn(self,username,pwd):
        username = "\'" + username + "\'"
        pwd = "\'" + pwd + "\'"
        checkSQL = "select * from user where username = " + username + "and pwd = " + pwd
        os.chdir('web/syncodb')
        result = os.popen('.\SqlVS.exe user.db \"' + checkSQL + '"').readline()
        if(len(result) == 0):
            return 0
        else:
            return 1

    #获取所有数据库
    def getDatabase(self):
        fileList = os.listdir('./web/syncodb/')
        dbList = []
        idx = 0
        for file in fileList:
            if ('.db' in file):
                fileObj = {}
                fileObj['id'] = idx
                fileObj['fileName'] = file
                dbList.append(fileObj)
                idx += 1
        return dbList

    #执行SQL语句
    def SQLExecute(self,dbname,optype,sqlquery):
        #非查询操作
        if optype == 0:
            operate_query = './web/syncodb/SqlVS.exe' + ' ' + dbname + ' "' + sqlquery + '"'
            operate_query = operate_query.replace('\n','')
            result = os.system(operate_query)
            if(result == 0):
                return "success"
            else:
                return "failed" 
        #查询操作
        else:
            operate_query = '.\SqlVS.exe' + ' ' + dbname + ' "' + sqlquery + '"'
            operate_query = operate_query.replace('\n','')
            os.chdir('web/syncodb')
            result = os.popen(operate_query).readlines()
            for i in range(len(result)):
                result[i] = result[i].split('|')
            result = pd.DataFrame(result)
            return result
