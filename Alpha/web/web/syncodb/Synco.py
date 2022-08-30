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

    def conn(self,username,pwd):
        username = "\'" + username + "\'"
        pwd = "\'" + pwd + "\'"
        checkSQL = "select * from u1 where username = " + username + "and pwd = " + pwd
        result = os.popen('web\\syncodb\\SqlVS.exe user.db \"' + checkSQL + '"').readlines()
        if(len(result) == 0):
            return 0
        else:
            return 1

    #获取所有数据库
    def getDatabase(self):
        fileList = os.listdir('./web/syncodb/')
        dbList = []
        idx = 1
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
            # @bianying 修改之后的正确路径(\\) + 参数格式(必须要有"",否则非内置命令无法识别，会报错：)
            operate_query = 'web\\syncodb\\SqlVS.exe' + ' ' + dbname + ' "' + sqlquery + '"'
            operate_query = operate_query.replace('\n','')
            result = os.system(operate_query+' 2>out.txt')
            f = open('out.txt')
            context = f.read()
            if(result == 0):
                res= "success"
            else:
                res= context

            List1 = []
            Obj1 = {}
            Obj1['运行结果'] = res
            List1.append(Obj1)
            return List1

        #查询操作
        else:
            # 测试之后还是有问题，报错LOG在 [后端测试v1]
            # operate_query = '.\SqlVS.exe' + ' ' + dbname + ' "' + sqlquery + '"'

            # @bianying 改用如下方法可以正常使用
            operate_query = 'web\\syncodb\\SqlVS.exe' + ' ' + dbname + ' "' + sqlquery + '"'
            operate_query = operate_query.replace('\n','')

            # os.chdir('web/syncodb')
            result = os.system(operate_query + ' 2>out.txt')

            List1 = []

            if (result == 0):
                res1 = os.popen(operate_query).readlines()#['22|12134\n', '22|12134\n', '22|12134\n', '22|12134\n']
                operate_query = 'web\\syncodb\\SqlVS.exe user \"PRAGMA table_info([user]);\"'
                operate_query = operate_query.replace('\n', '')
                res2=os.popen(operate_query).readlines()#获取表列名称和属性
                if len(res1)==0:
                    Obj1 = {}
                    Obj1['运行结果'] = '查询为空'
                    List1.append(Obj1)
                else:
                    for i in range(len(res1)):
                        res1[i] = res1[i].split('|')

                    for i in range(len(res2)):
                        res2[i] = res2[i].split('|')

                    sum = len(res2)
                    result = ""
                    for i in range(sum):
                        result += " \t        " + res2[i][1] + "(" + res2[i][2] + ")               "
                        Obj1 = {}
                    Obj1['运行结果'] = result
                    List1.append(Obj1)

                    for i in range(len(res1)):
                        Obj1 = {}
                        id = i + 1
                        result = str(id) + ":      "
                        for j in range(sum):
                            result += res1[i][j] + "               "

                        Obj1['运行结果'] = result
                        List1.append(Obj1)

            else:
                f = open('out.txt')
                context = f.read()
                result = context
                Obj1 = {}
                Obj1['运行结果'] = result
                List1.append(Obj1)


            return List1





            # @bainying: 不识别格式会报错：TypeError: Object of type DataFrame is not JSON serializable
            # 目前直接返回的是list
            # result = pd.DataFrame(result)
            # return result
