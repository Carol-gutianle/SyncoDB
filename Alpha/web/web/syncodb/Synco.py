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
            # 上一版错误路径：
            # operate_query = './web/syncodb/SqlVS.exe' + ' ' + dbname + ' "' + sqlquery + '"'

            # @bianying 修改之后的正确路径(\\) + 参数格式(必须要有"",否则非内置命令无法识别，会报错：)
            operate_query = 'web\\syncodb\\SqlVS.exe' + ' ' + dbname + ' "' + sqlquery + '"'

            print('TEST:1')
            print(operate_query)
            operate_query = operate_query.replace('\n','')
            print('TEST:2')
            print(operate_query)
            result = os.system(operate_query)
            print('Result:')
            print(result)
            if(result == 0):
                return "success"
            else:
                return "failed" 
        #查询操作
        else:
            # 测试之后还是有问题，报错LOG在 [后端测试v1]
            # operate_query = '.\SqlVS.exe' + ' ' + dbname + ' "' + sqlquery + '"'

            # @bianying 改用如下方法可以正常使用
            operate_query = 'web\\syncodb\\SqlVS.exe' + ' ' + dbname + ' "' + sqlquery + '"'
            operate_query = operate_query.replace('\n','')
            # os.chdir('web/syncodb')
            result = os.popen(operate_query).readlines()
            print("select result:")
            print(result)
            for i in range(len(result)):
                result[i] = result[i].split('|')

            # @bainying: 不识别格式会报错：TypeError: Object of type DataFrame is not JSON serializable
            # 目前直接返回的是list
            # result = pd.DataFrame(result)
            return result
