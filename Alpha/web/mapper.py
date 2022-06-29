# -*- codeing = utf-8 -*-
# @Time : 2022/6/28 9:14
# @Author : Biangbiang
# @File : mapper.py
# @Software : PyCharm

import subprocess
import os

def controlSQL(db,sql):
    command = 'sqlite-amalgamation-3380500 "'+db+'" '+sql
    resCode = subprocess.run(command).returncode
    res = os.popen(command).readlines()
    return res,resCode