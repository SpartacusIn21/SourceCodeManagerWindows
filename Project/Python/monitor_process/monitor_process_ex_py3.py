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
import msvcrt
#将qixiu.ini日志等级修改为2
def ChangeLogLev(Path,sec,key,val='0'):
    if not os.path.exists(Path):
        print(Path+"does not exist!")
        return
    cf = configparser.ConfigParser()
    cf.read(Path)
    #print(Path)
    #cf.readfp(codecs.open(Path,"r","gb2312"))
    log_level = cf.get(sec,key)
    print(key+":"+log_level)
    
    if key=='on_line':        
        if log_level=='0':
            val='1'
        elif log_level=='1':
            val='0'
    if int(log_level) > 1:
        return
    else:
        print(key+" changed to:"+val)
        cf.set(sec,key,val)
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
            print("QXClient ProcessId:"+pid)
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
    print("qixiu.ini path:"+qixiu_ini_path)
    return qixiu_ini_path
	
def readInput(default="No order inputed,qixiu.ini will be changed inmediately!", timeout=30):
    start_time = time.time()
    sys.stdout.write(('(%d秒自动跳过,q:退出,o:修改on_line字段,l:用默认编辑器打开player.log文件,enter:立即改变log_level字段值):' % (timeout)))
    sys.stdout.flush()    
    input = ''
    while True:
        ini=msvcrt.kbhit()
        try:
            if ini:
                chr = msvcrt.getche()
                if ord(chr) == 13:  # enter_key                    
                    break
                elif ord(chr) >= 32:                    
                    input += chr.decode()
        except Exception as e:            
            pass
        if len(input) == 13 or time.time() - start_time > timeout:            
            break     
    if len(input) > 0:        
        return input+''
    else:        
        return default

if __name__ == '__main__':
    while True:
        bQXClientIsRunning,qixiu_ini_path = monitor_QXClient()
        if not bQXClientIsRunning:#如果QXClient.exe未在运行，就修改QyClient目录下的qixiu.ini文件
            qixiu_ini_path = getQiXiuPath()
            print("QXlient.exe is not running!")
        else:
            print("QXClient.exe is running!")
        ChangeLogLev(qixiu_ini_path,'common','log_level','2')
        print ("Input 'Enter' to change qixiu.ini inmediately!")
        s = readInput()
        print("\nInput Order:"+s)
        if s.strip()=='q':
            print ("Quit!")
            break
        elif s.strip()=='o':
            ChangeLogLev(qixiu_ini_path,'common','on_line')
        elif s.strip()=='l':
            ini_name="qixiu.ini"
            os.startfile(qixiu_ini_path[:-len(ini_name)]+"player.log")
            print("Open player.log with default IDE!")        
        else:
            pass
        print("\n")
