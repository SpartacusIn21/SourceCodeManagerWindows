#date: 2017/12/15
__author__ = 'chenyangchun'
import os
import time
import subprocess
import configparser
import psutil
import sys
import codecs
from winreg import *
#将qixiu.ini日志等级修改为2
def ChangeLogLev(Path,logLevel='2'):
    if not os.path.exists(Path):
        print(Path+"does not exist!")
        return
    cf = configparser.ConfigParser()
    cf.read(Path)
    #print(Path)
    #cf.readfp(codecs.open(Path,"r","gb2312"))
    log_level = cf.get('common','log_level')
    print("log_level:"+log_level)
    if int(log_level) > 1:
        return
    else:
        print("log_level changed to:"+logLevel)
        cf.set('common','log_level',logLevel)
        cf.write(open(Path,"w"))
        #cf.write(codecs.open(Path,"w+","gb2312"))
        


process_name = 'QXClient.exe'
sleep_time = 60

#检测QXClient并返回进程是否运行以及进程路径
def monitor_QXClient():
    #Listing Processes which are not responding
    process_list = os.popen('tasklist"').read().strip().split('\n')
    bQXClientIsRunning = False
    qixiu_ini_path = ""
    for process in process_list:
        if process.startswith(process_name):
            bQXClientIsRunning = True
            pn = process.split(' ')            
            for i in pn:
                if i.isdigit():
                    pid = i
                    break
            print(pid)
            p = psutil.Process(int(pid))
            #QXClient.exe进程路径
            path = p.exe()
            #print(path)
            qixiu_ini_path = path[:-len(process_name)]+'qixiu.ini'
            print(qixiu_ini_path)
    return bQXClientIsRunning,qixiu_ini_path

#获取爱奇艺PC客户端QyClient目录qixiu下的qixiu.ini文件路径
def getQiXiuPath():
    regpath = "SOFTWARE\\Wow6432Node\\QiYi\\QiSu"
    installkey = "HDir"
    reg = OpenKey(HKEY_LOCAL_MACHINE, regpath)
    QyClientPath,type = QueryValueEx(reg, installkey)
    print("QyCient Path:"+QyClientPath)
    qixiu_ini_path = QyClientPath+"\\QYAppPlugin\\qixiu\\qixiu.ini"
    print(qixiu_ini_path)
    return qixiu_ini_path

if __name__ == '__main__':
    while True:
        bQXClientIsRunning,qixiu_ini_path = monitor_QXClient()
        if not bQXClientIsRunning:#如果QXClient.exe未在运行，就修改QyClient目录下的qixiu.ini文件
            qixiu_ini_path = getQiXiuPath()
            print("QXlient.exe is not running!")
        else:
            print("QXClient.exe is running!")
        ChangeLogLev(qixiu_ini_path)
        time.sleep(sleep_time)
