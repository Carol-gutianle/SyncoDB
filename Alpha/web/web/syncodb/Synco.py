import os
import pandas as pd
import plotly.express as px
import re
from datetime import datetime, date, timedelta
class Synco:
    #设置端口
    def __init__(self):
        self.program = 'SqlVS.exe'

    #连接数据库
    def conn(self,username,pwd):
        username = "\'" + username + "\'"
        pwd = "\'" + pwd + "\'"
        checkSQL = "select * from user where username = " + username + "and pwd = " + pwd
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
    def SQLExecute(self,sqlquery):
        #解析SQL语句
        return 1

    #输出执行时间
