
'''
FileName: CodingPartner
Create Time:   2015/08
Modify Time:
Author: Chen Yangchun
Owner:  Chen Yangchun
Place:  Shanghai Jiao Tong University, Min Hang district.
Reference:
Description: (1)Can based on document ReadMe.txt record, according to the keywords to search the corresponding code path, convenient query and management of files
'''
__author__ = 'JD'
#Main Function
from tkinter import *
import subprocess
import os
import sys,os
from tkinter import * #when use realted module, we need to import the realted package
from tkinter.messagebox import *
from datetime import *
import shutil #delete directory recursively related
import shutil, errno
from tkinter import * #when use realted module, we need to import the realted package
from tkinter.ttk import * #Combobox
from tkinter import filedialog




AbsolutePath = ""
###################Text File Path in  FuncModule####################
#C
Path_FuncModule_C= ""
#CPlusPlus
Path_FuncModule_CPlusPlus= ""
#CSharp
Path_FuncModule_CSharp= ""
#HTML_CSS
Path_FuncModule_HTML_CSS= ""
#Matlab
Path_FuncModule_Matlab= ""
#Python
Path_FuncModule_Python= ""
#SQL
Path_FuncModule_SQL= ""

###################Text File Path in Project##########################
#C
Path_Project_C= ""
#CPlusPlus
Path_Project_CPlusPlus= ""
#CSharp
Path_Project_CSharp= ""
#HTML_CSS
Path_Project_HTML_CSS= ""
#Matlab
Path_Project_Matlab= ""
#Python
Path_Project_Python= ""
#SQL
Path_Project_SQL= ""
########################### Path List ###############################
Path_FuncModule= ""
Path_Project= ""

Path_FuncModule_txt= ""
Path_Project_txt= ""

#Three Path Lists
RootPathList= ""
FuncModulePathList= ""
ProjectPathList= ""
ProjectPathList = ""

def Path_Assig_Value():
    ###################Text File Path in  FuncModule####################
    #C
    global AbsolutePath
    temp_AbsolutePath = AbsolutePath
    global Path_FuncModule_C
    Path_FuncModule_C = temp_AbsolutePath + "FuncModule/C/Record.txt"
    #CPlusPlus
    global Path_FuncModule_CPlusPlus
    Path_FuncModule_CPlusPlus = temp_AbsolutePath+"FuncModule/CPlusPlus/Record.txt"
    #CSharp
    global Path_FuncModule_CSharp
    Path_FuncModule_CSharp = temp_AbsolutePath+"FuncModule/CSharp/Record.txt"
    #HTML_CSS
    global Path_FuncModule_HTML_CSS
    Path_FuncModule_HTML_CSS = temp_AbsolutePath+"FuncModule/HTML_CSS/Record.txt"
    #Matlab
    global Path_FuncModule_Matlab
    Path_FuncModule_Matlab = temp_AbsolutePath+"FuncModule/Matlab/Record.txt"
    #Python
    global Path_FuncModule_Python
    Path_FuncModule_Python = temp_AbsolutePath+"FuncModule/Python/Record.txt"
    #SQL
    global Path_FuncModule_SQL
    Path_FuncModule_SQL = temp_AbsolutePath+"FuncModule/SQL/Record.txt"

    ###################Text File Path in Project##########################
    #C
    global Path_Project_C
    Path_Project_C = temp_AbsolutePath+"Project/C/Record.txt"
    #CPlusPlus
    global Path_Project_CPlusPlus
    Path_Project_CPlusPlus = temp_AbsolutePath+"Project/CPlusPlus/Record.txt"
    #CSharp
    global Path_Project_CSharp
    Path_Project_CSharp = temp_AbsolutePath+"Project/CSharp/Record.txt"
    #HTML_CSS
    global Path_Project_HTML_CSS
    Path_Project_HTML_CSS = temp_AbsolutePath+"Project/HTML_CSS/Record.txt"
    #Matlab
    global Path_Project_Matlab
    Path_Project_Matlab = temp_AbsolutePath+"Project/Matlab/Record.txt"
    #Python
    global Path_Project_Python
    Path_Project_Python =temp_AbsolutePath+ "Project/Python/Record.txt"
    #SQL
    global Path_Project_SQL
    Path_Project_SQL = temp_AbsolutePath+"Project/SQL/Record.txt"
    ########################### Path List ###############################
    global Path_FuncModule
    Path_FuncModule =temp_AbsolutePath+ "FuncModule/"
    global Path_Project
    Path_Project = temp_AbsolutePath+"Project/"
    global Path_FuncModule_txt
    Path_FuncModule_txt = temp_AbsolutePath+"FuncModule/Record.txt"
    global Path_Project_txt
    Path_Project_txt = temp_AbsolutePath+"Project/Record.txt"
    #Three Path Lists
    global RootPathList
    RootPathList = [Path_FuncModule_txt,Path_Project_txt]
    global FuncModulePathList
    FuncModulePathList = [Path_FuncModule_C,Path_FuncModule_CPlusPlus, Path_FuncModule_CSharp, Path_FuncModule_HTML_CSS, Path_FuncModule_Matlab, Path_FuncModule_Python,Path_FuncModule_SQL]
    global ProjectPathList
    ProjectPathList = [Path_Project_C,Path_Project_CPlusPlus, Path_Project_CSharp, Path_Project_HTML_CSS, Path_Project_Matlab, Path_Project_Python,Path_Project_SQL]

#Add, Delete, Modify and Query the txt file under FuncModule directory and Project directory
###################################### Manage Directory #########################################
    #Add
def ManageDirectory_Add(object,Type, Code_Type):
    if Type == "":
        object.wm_attributes("-topmost", 0)
        showwarning("Warning","\'Type\'"+" can't be null")#show a warning MessageBox
        object.wm_attributes("-topmost", 1)
        return
    Type_Dict = {"Function Module": Path_FuncModule,"Project": Path_Project} #Map Type to related directory
    Code_Type_Dict = {"C++": "CPlusPlus","Java": "Java","Python": "Python","C#": "CSharp","SQL": "SQL","Html/CSS": "HTML_CSS","C_Lang": "C_Lang","Matlab": "Matlab"} #Map Code Type to related directory
    Add_Code_Type_Pairs(Code_Type_Dict, Code_Type)
    Type_Dir = ''
    if Type in Type_Dict:
        Type_Dir = Type_Dict[Type]
    else:
        Type_Dir = AbsolutePath  +  Type
    #Judge whether Type directory exists
    if os.path.exists(Type_Dir):#Type directory exists
        #Judge whether Code_Type directory exists further
        Code_Type_Dir = ''
        temp_Dir = Type_Dict[Type] if Type in Type_Dict else Type
        if Code_Type == "":
            Code_Type_Dir = temp_Dir
        elif Code_Type in Code_Type_Dict:
            Code_Type_Dir = temp_Dir  +  Code_Type_Dict[Code_Type]
        else:
            Code_Type_Dir = temp_Dir  +  Code_Type
        if os.path.exists(Code_Type_Dir):#Type directory exists
            if Code_Type == "":#Code Type directory does not exist
                object.wm_attributes("-topmost", 0)
                showwarning("Warning","\'"+Type+"\'"+" directory exists")#show a warning MessageBox
                object.wm_attributes("-topmost", 1)
            else:
                object.wm_attributes("-topmost", 0)
                showwarning("Warning","\'"+Code_Type_Dict[Code_Type]+"\'"+" directory exists")#show a warning MessageBox
                object.wm_attributes("-topmost", 1)
        else:#Code Type directory does not exist
            object.wm_attributes("-topmost", 0)
            Create_Code_Type_Direcotry(Type, Type_Dir, Code_Type_Dict[Code_Type] if (Code_Type in Code_Type_Dict) else Code_Type, Code_Type_Dir)#create Record.txt
            showinfo("Success","\'"+  Code_Type +"\'"+" directory was created")
            object.wm_attributes("-topmost", 1)
    else:#Type directory does not exist
        object.wm_attributes("-topmost", 0)
        Create_Type_Direcotry(Type, Type_Dir)#create Record.txt
        showinfo("Success","\'"+  Type +"\'"+" directory was created")
        object.wm_attributes("-topmost", 1)
def Create_Code_Type_Direcotry(Type, Type_Dir, Code_Type, Dir):#create related directory in directory Dir(decided by TypeorCode_Type variable) and Record.txt
    os.mkdir(Dir)#create directory
    Init_buffer = Type+"-"+Code_Type+"总纲领每添加一个功能模块代码，更新该文档。切记，要维护好本源码功能快速定位功能，需要每次更新完代码后都要实时更新该文本。\n****************************************"+Code_Type+"****************************************************\n标准记录格式：序号-日期：中英文关键字；\n"+"1-"+("%s"%date.today()).replace('-', '')+":Init\n"
    with open(os.path.join(Dir, "Record.txt"), 'wt') as Record_file:
        Record_file.write(Init_buffer)
    Type_Init_Buffer = "\n****************************************"+Code_Type+"****************************************************\n"+"1-"+("%s"%date.today()).replace('-', '')+":Init\n"
    with open(os.path.join(Type_Dir, "Record.txt"), 'at+') as Record_file:
        Record_file.write(Type_Init_Buffer)
def Create_Type_Direcotry(Type, Dir):#create related directory in directory Dir(decided by TypeorCode_Type variable) and Record.txt
    os.mkdir(Dir)#create directory
    Init_buffer = Type+"总纲领\n总纲领每次当更新一次源代码的时候除了在其所属文件夹更新ReadMe记录信息外，还需要更新本文档的记录信息，\n这样的话每次查询需要的代码模块的时候就可以按照以下方式快速定位需要寻找的代码模块或者功能：\n=====================1.在本文档用Ctrl+F寻找关键字(单词，中文关键字)，定位该功能在哪个语言版本中存在=================================================\n=====================2.根据1的结果到相应的文件夹中的ReadMe文件中用Ctrl+F寻找代码功能模块源码所属文件夹=================================================\n切记，要维护好本源码功能快速定位功能，需要每次更新完代码后都要实时更新该文本。\n"
    with open(os.path.join(Dir, "Record.txt"), 'wt') as Record_file:
        Record_file.write(Init_buffer)
def Add_Code_Type_Pairs(Dict, Code_Type):
    if Code_Type not in Dict:
        Dict[Code_Type] = Code_Type

    #Delete
def ManageDirectory_Delete(object,Type, Code_Type):
    if Type == "":
        object.wm_attributes("-topmost", 0)
        showwarning("Warning","\'Type\'"+" can't be null")#show a warning MessageBox
        object.wm_attributes("-topmost", 1)
        return
    Type_Dict = {"Function Module": Path_FuncModule,"Project": Path_Project} #Map Type to related directory
    Code_Type_Dict = {"C++": "CPlusPlus","Java": "Java","Python": "Python","C#": "CSharp","SQL": "SQL","Html/CSS": "HTML_CSS","C_Lang": "C_Lang","Matlab": "Matlab"} #Map Code Type to related directory
    Type_Dir = ''
    if Type in Type_Dict:
        Type_Dir = Type_Dict[Type]
    else:
        global AbsolutePath
        Type_Dir = AbsolutePath  +  Type
    Add_Code_Type_Pairs(Code_Type_Dict, Code_Type)
    #Judge whether Type directory exists
    if os.path.exists(Type_Dir):#Type directory exists
        #Judge whether Code_Type directory exists further
        Code_Type_Dir = ''
        Code_Type_Dir = Type_Dir + Code_Type_Dict[Code_Type] if Code_Type in Code_Type_Dict else Type_Dir + Code_Type
        if os.path.exists(Code_Type_Dir) and Code_Type != "":#Code Type directory exists
            object.wm_attributes("-topmost", 0)
            result = askyesno("Caution","Do you really want to delete %s?"%Code_Type)
            if result == True:
                shutil.rmtree(Code_Type_Dir)#delete directory
                Delete_Dir_RenewRecordtxt(Type_Dir, Code_Type)#delete related record in file Record.txt
                showinfo("Success","\'"+  Code_Type_Dir +"\'"+" directory was deleted")
                object.wm_attributes("-topmost", 1)
            else:
                object.wm_attributes("-topmost", 1)
        elif Code_Type == "":#Code Type directory does not exist
            object.wm_attributes("-topmost", 0)
            result = askyesno("Caution","Do you really want to delete %s?"%Type)
            if result == True:
                shutil.rmtree(Type_Dir)
                showinfo("Success","\'"+  Type_Dir +"\'"+" directory was deleted")
                object.wm_attributes("-topmost", 1)
            else:
                object.wm_attributes("-topmost", 1)
        else:
            object.wm_attributes("-topmost", 0)
            showwarning("Warning","\'"+Code_Type_Dir+"\'"+" directory does not exist")#show a warning MessageBox
            object.wm_attributes("-topmost", 1)
    else:#Type directory does not exist
        object.wm_attributes("-topmost", 0)
        showwarning("Warning","\'"+Type+"\'"+" directory does not exist")#show a warning MessageBox
        object.wm_attributes("-topmost", 1)
def Delete_Dir_RenewRecordtxt(Type_Dir, Code_Type):#create related directory in directory Dir(decided by TypeorCode_Type variable) and Record.txt
    Code_Type_Dict = {"C++": "CPlusPlus","Java": "Java","Python": "Python","C#": "CSharp","SQL": "SQL","Html/CSS": "HTML_CSS","C_Lang": "C_Lang","Matlab": "Matlab"} #Map Code Type to related directory
    Record_txt = Type_Dir + "Record.txt"
    fid = open(Record_txt,"r")
    lines = fid.readlines()
    fid.close()
    fid = open(Record_txt,"wt")
    #locate if the postion of keyword is between two "*" realted line
    endflag = 0#0 means the keyword related record is last record
    KeywordPos = float("inf")#represent infinity, no numbers in python larger than this number
    CurPos = 0
    for line in lines:
        Keywordindex = line.find(Code_Type_Dict[Code_Type] if Code_Type in Code_Type_Dict else Code_Type)
        CurPos = CurPos + len(line)
        Otherindex = line.find('*')
        count = 0
        count = CntStarCharinLine(line)
        if  Keywordindex != -1:#keyword line
            KeywordPos = Keywordindex + CurPos
        elif CurPos + Otherindex > KeywordPos and count >= 20:
            endflag = 1
    #write the text back to file except content to be deleted
    writeflag = 1
    CurPos = 0
    KeywordPos = float("inf")
    for line in lines:
        count = 0
        CurPos = CurPos + len(line)
        count = CntStarCharinLine(line)#decide the deletion end position
        if line.find(Code_Type_Dict[Code_Type] if Code_Type in Code_Type_Dict else Code_Type) == -1 and writeflag == 1:#ahead keyword record
            fid.write(line)
        elif count >= 20 and CurPos + line.find('*') > KeywordPos:#after keyword line
            fid.write(line)
            writeflag = 1
        elif line.find(Code_Type_Dict[Code_Type] if Code_Type in Code_Type_Dict else Code_Type) != -1:#keyword line
            if endflag == 1:
                writeflag = 0
                KeywordPos = CurPos + line.find(Code_Type_Dict[Code_Type] if Code_Type in Code_Type_Dict else Code_Type)
                continue
            else:
                break
    fid.close()
def CntStarCharinLine(line):
    count = 0
    for char in line:
        if char == '*':
            count += 1
    return count
##################################### Manage Record ##########################################
#Add Button
def copytree(src, dst, symlinks=False, ignore=None):
    Dir_Name = src.split('/')
    Dir_Name = Dir_Name[-1]
    dst += "/" + Dir_Name
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)
def ManageRecord_Add_RenewRecordtxt(Code_Type, Type_Dir,Code_Type_Dir, Description, Keywords,DirPath, FilePath):
    CodeType_RecordPath = Code_Type_Dir + "/Record.txt"
    # RecordFileName = ""#used to store as file name in Record.txt
    # if os.path.exists(DirPath) and DirPath != "":
    #     RecordFileName = Code_Type_Dir + "/" + DirPath.split('/')[-1] + "/" + FilePath.split('/')[-1]
    fid = open(CodeType_RecordPath,"r")
    lines = fid.readlines()
    fid.close()
    #Renew Record.txt under Code Type directory
        #Get last record's index and date
    index_data_record = ""
    for line in reversed(lines):
        if line != '\n':
            index_data_record = line
            break
    index_data_record = index_data_record.split('-')
    index = str(int(index_data_record[0]) + 1)
    #Renew Record.txt under Type directory
    fid = open(CodeType_RecordPath,"at")
    record = ""
    if os.path.exists(DirPath) and DirPath != "":
        record =  index + "-" + ("%s"%date.today()).replace('-', '') + ":" + "增加了Directory>" + DirPath.split('/')[-1] + ">" + FilePath.split('/')[-1] +">" + Description + "关键字:" + Keywords
    else:
        record = index + "-" + ("%s"%date.today()).replace('-', '') + ":" + "增加了File>" +FilePath.split('/')[-1] +">" + Description + "关键字:" + Keywords
    record = record+"\n"
    fid.write(record)
    fid.close()
    #Renew Record.txt under Type directory
    Code_Type_Dict = {"C++": "CPlusPlus","Java": "Java","Python": "Python","C#": "CSharp","SQL": "SQL","Html/CSS": "HTML_CSS","C_Lang": "C_Lang","Matlab": "Matlab"} #Map Code Type to related directory
    Type_Record_txt = Type_Dir + "Record.txt"
    #locate if the postion of keyword is between two "*" realted line
    fid = open(Type_Record_txt,"r")
    lines = fid.readlines()
    fid.close()
    endflag = 0#0 means the keyword related record is last record
    KeywordPos = float("inf")#represent infinity, no numbers in python larger than this number
    CurPos = 0
    for line in lines:
        Keywordindex = line.find(Code_Type_Dict[Code_Type] if Code_Type in Code_Type_Dict else Code_Type)
        CurPos = CurPos + len(line)
        Otherindex = line.find('*')
        count = 0
        count = CntStarCharinLine(line)
        if  Keywordindex != -1:#keyword line
            KeywordPos = Keywordindex + CurPos
        elif CurPos + Otherindex > KeywordPos and count >= 20:
            endflag = 1
    fid = open(Type_Record_txt,"at")
    if endflag == 0:
        fid.write(record+"\n")
        fid.close()
        return
    fid = open(Type_Record_txt,"wt")
    #write the text back to file except content to be deleted
    writeflag = 0
    CurPos = 0
    KeywordPos = float("inf")
    for line in lines:
        count = 0
        CurPos = CurPos + len(line)
        count = CntStarCharinLine(line)#decide the deletion end position
        if line.find(Code_Type_Dict[Code_Type] if Code_Type in Code_Type_Dict else Code_Type) == -1:#except keyword record line
            if count >= 20 and CurPos + line.find('*') > KeywordPos and writeflag == 1:#after keyword line
                fid.write(record)
                fid.write("\n" + line)
                writeflag = 0
            else:
                fid.write(line)
        elif line.find(Code_Type_Dict[Code_Type] if Code_Type in Code_Type_Dict else Code_Type) != -1:#keyword line
            if endflag == 1:
                writeflag = 1
                KeywordPos = CurPos + line.find(Code_Type_Dict[Code_Type] if Code_Type in Code_Type_Dict else Code_Type)
                fid.write(line)
    fid.close()


def ManageRecord_Add(object,Type, Code_Type, Description, Keywords, DirPath, FilePath):
    if Type == "" or Code_Type == "" or Description == "" or Keywords == "" or FilePath == "" or not os.path.exists(FilePath):
        object.wm_attributes("-topmost", 0)
        showerror("Parameter Error", "Please configure parameters correctly!")
        object.wm_attributes("-topmost", 1)
        return
    if ":" in Description:
        object.wm_attributes("-topmost", 0)
        showwarning("Warning","\'"+"Description" +"\'" + " can't contain colon(:), please write it like" + " \'" + "description1;description2; " +"\'")#show a warning MessageBox
        object.wm_attributes("-topmost", 1)
        return
    if ":" in Keywords:
        object.wm_attributes("-topmost", 0)
        showwarning("Warning","\'"+"Keywords" +"\'" + " can't contain colon(:), please write it like" + " \'" + "keyword1;keyword2; " +"\'")#show a warning MessageBox
        object.wm_attributes("-topmost", 1)
        return
    #Functions of this function:
    #(1)Refer to Type and Code_Type, find the Code Type directory,copy related directory or file and..
    #(2) add record to Record.txt under found directory;
    #(3)Refer to Type, find the Type directory, add record to Record.txt under the directory.
    Type_Dict = {"Function Module": Path_FuncModule,"Project": Path_Project} #Map Type to related directory
    Code_Type_Dict = {"C++": "CPlusPlus","Java": "Java","Python": "Python","C#": "CSharp","SQL": "SQL","Html/CSS": "HTML_CSS","C_Lang": "C_Lang","Matlab": "Matlab"} #Map Code Type to related directory
    Add_Code_Type_Pairs(Code_Type_Dict, Code_Type)
    Type_Dir = ''
    if Type in Type_Dict:
        Type_Dir = Type_Dict[Type]
    else:
        global AbsolutePath
        Type_Dir = AbsolutePath  +  Type
    Code_Type_Dir = ''
    temp_Dir = Type_Dict[Type] if Type in Type_Dict else Type
    if Code_Type == "":
        Code_Type_Dir = temp_Dir+ "/"
    elif Code_Type in Code_Type_Dict:
        Code_Type_Dir = temp_Dir  +  Code_Type_Dict[Code_Type]+ "/"
    else:
        Code_Type_Dir = temp_Dir  +  Code_Type+ "/"
    #As (1) listed before
    if os.path.exists(DirPath) and os.path.exists(FilePath):
        copytree(DirPath, Code_Type_Dir)
        object.wm_attributes("-topmost", 0)
        showinfo("Success","\'"+  DirPath +"\'"+" directory was copied")
        object.wm_attributes("-topmost", 1)
    elif ~os.path.exists(DirPath) and os.path.exists(FilePath):
        shutil.copy2(FilePath, Code_Type_Dir)
        object.wm_attributes("-topmost", 0)
        showinfo("Success","\'"+  FilePath +"\'"+" file was copied")
        object.wm_attributes("-topmost", 1)
    else:
        showwarning("Warning","Directory or File path illegal")#show a warning MessageBox
    #As (2),(3) listed before
    ManageRecord_Add_RenewRecordtxt(Code_Type, Type_Dir, Code_Type_Dir, Description,Keywords, DirPath, FilePath)
#Delete Button
def ManageRecord_Delete(object_frm_Manage_Record,Keyword_Query, object_Combobox_Index, object_entry_Description_Delete, object_entry_Keywords_Delete, object_entry_Dir_Path_Delete, object_entry_File_Path_Delete, index_list, description_list, keywords_list, DirPath_list, FilePath_list, MatchedRecordStr):
    #the code here can refer to KeywordQuery, query result can store in parameters and return to calling function
        #query the result refer to keyword and store results into index_list to FilePath_list below.
    index_list.clear()
    description_list.clear()
    keywords_list.clear()
    DirPath_list.clear()
    FilePath_list.clear()
    MatchedRecordStr.clear()
    KeywordQuery_DeleteRecord(Keyword_Query,index_list, description_list, keywords_list, DirPath_list, FilePath_list, MatchedRecordStr)
        #as default, we display the first index on UI
    if index_list:
        object_Combobox_Index['value'] = ""
        object_Combobox_Index['value'] = (index_list)
        object_Combobox_Index.set(index_list[0])
    if description_list:
        object_entry_Description_Delete.delete(0, END)
        object_entry_Description_Delete.insert(0, description_list[index_list[0]])
    if keywords_list:
        object_entry_Keywords_Delete.delete(0, END)
        object_entry_Keywords_Delete.insert(0, keywords_list[index_list[0]])
    if DirPath_list:
        object_entry_Dir_Path_Delete.delete(0, END)
        object_entry_Dir_Path_Delete.insert(0, DirPath_list[index_list[0]])
    if FilePath_list:
        object_entry_File_Path_Delete.delete(0, END)
        object_entry_File_Path_Delete.delete(0, END)
        object_entry_File_Path_Delete.insert(0, FilePath_list[index_list[0]])
def KeywordQuery_DeleteRecord(keyword, index_list, description_list, keywords_list, DirPath_list, FilePath_list,MatchedRecordStr):
    global AbsolutePath
    TypeDirList = []
    CodeTypeDirList = []
    TraveringTypeCodeTypeFiles(TypeDirList,CodeTypeDirList)
    rootpathlist = []
    for TypeDir in TypeDirList:     
        rootpathlist.append(AbsolutePath + TypeDir + "/Record.txt")
    #Traverse rootpathlist with KeyWord
    MatchedRecordStr_temp = []
    if len(keyword) == 0:#if keyword is space, program will return
        return
    #Split Keyword by space
    keyword = ' '.join(keyword.split())
    keyword = keyword.split(' ')
    ResultList = []
    QueriedResultCounts = 0
    for RootPath in rootpathlist:#Used to read the two root text file
        handle = open(RootPath, 'r')#Open File and Read text
        #The next three variables is very important!
        index = [] #used to store the file position of the "keyword" and paried string        Str_Language = []
        Str_index = []#the string of where keyword belongs to.
        index_Language = {"index_C_Lang": 0,"index_CplusPlus": 0, "index_Csharp": 0, "index_Python": 0, "index_SQL": 0, "index_HTML_CSS": 0, "index_Matlab": 0, "index_Java": 0} #Used to store the current file position of each language index, like "CPlusPlus" and so on.
        DirectoryOrFileName = [] #used to store the directory discribed in keyword

        Curr_Pos = 0#Current file postion in the text file
        for eachLine in handle:#Traverse the text in file and calculate the value of variable "index" and "index_Language"
            tempindex = -1
            for keyword_item in keyword:
                tempindex = eachLine.find(keyword_item)
                if tempindex != -1:
                    continue
                else:
                    break
            tempindex1 = tempindex + Curr_Pos
            if tempindex != -1:
                index.append(tempindex1)#Add the keyword's position in index list
                MatchedRecordStr_temp.append(eachLine)
                Str_index.append(eachLine)
                tempstr = eachLine.split('>')
                if len(tempstr) >= 4:
                    DirectoryOrFileName.append(tempstr[1] + "\\" + tempstr[2]) #The code directory related to keyword
                elif len(tempstr) >= 2:
                    DirectoryOrFileName.append(tempstr[1]) #The code directory related to keyword
                else:
                    DirectoryOrFileName.append("")
        count = 0        
        for i in index:            
            if RootPath == Path_FuncModule_txt:
                for TypeDir in TypeDirList:
                    for CodeTypeDir in CodeTypeDirList:                        
                        Path = AbsolutePath.replace('/', '\\')+ TypeDir + "\\" +CodeTypeDir+ "\\"+ DirectoryOrFileName[count]
                        if os.path.exists(Path):
                            ResultList.append(Str_index[count]+"\n  PATH:  " + Path+"\n")
                count = count + 1
            else:
                for TypeDir in TypeDirList:
                    for CodeTypeDir in CodeTypeDirList:                        
                        Path = AbsolutePath.replace('/', '\\')+ TypeDir + "\\" +CodeTypeDir+ "\\"+ DirectoryOrFileName[count]
                        if os.path.exists(Path):
                            ResultList.append(Str_index[count]+"\n  PATH:  " + Path+ "\n")
                count = count + 1
        QueriedResultCounts = QueriedResultCounts + count
    temp_Count = 0
    for querieditems in ResultList: #display the queried result in entry control of GUI
        FileName = ""
        Description = ""
        Splitof_colon = querieditems.split(':')
        index_list.append(Splitof_colon[0])
        Description = str.replace(Splitof_colon[1],"关键字","",1).split('>')
        FileType = str.replace(Description[0],"增加了","",1)
        if FileType == "Directory" and len(Description) >= 4:
            FileName = Description[2]
            Description = Description[3]
        elif len(Description) >= 3:
            FileName = Description[1]
            Description = Description[2]
        description_list[Splitof_colon[0]] = Description
        Keyword = str.replace(Splitof_colon[2],"PATH","",1)
        keywords_list[Splitof_colon[0]] = Keyword
        Path = ""
        if len(Splitof_colon) >= 5:
            Path = Splitof_colon[3] + ":" + Splitof_colon[4]
        Path = str.replace(Path, "\n", "",1)
        Path = str.replace(Path, " ", "")
        FilePath_list[Splitof_colon[0]] = Path
        if FileType == "Directory":
            if '.'  in Path:
                Path = str.replace(Path, FileName, "",1)
            Path = str.replace(Path, "\n", "",1)
            Path = str.replace(Path, " ", "")
            Path = Path[::-1].replace("\\","",1)[::-1]
            DirPath_list[Splitof_colon[0]] = Path
        else:
            DirPath_list[Splitof_colon[0]] = "\n"
        MatchedRecordStr[Splitof_colon[0]] = MatchedRecordStr_temp[temp_Count]
        temp_Count += 1
##################################### Query ##########################################
#First, Query text file just under FuncModule directory and Project directory, and query next layer directory based on result queried in FuncModule and Project directory
def TraveringTypeCodeTypeFiles(TypeDirList, CodeTypeDirList):
    # Manage_Dir_GUI.cmbEditComboList_Code_Type = self.Combobox_Code_Type.get()
    global AbsolutePath
    Dirs = [d for d in os.listdir(AbsolutePath) if os.path.isdir((os.path.join(AbsolutePath,d)))]#list only the directory under given directory
    if '.git' in Dirs:
        Dirs.remove('.git')
    if 'CodingPartner' in Dirs:
        Dirs.remove('CodingPartner')
    for dir in Dirs:
        TypeDirList.append(dir)
    # Manage_Dir_GUI.cmbEditComboList_Code_Type = self.Combobox_Code_Type.get()
    Type_Dict = {"Function Module": Path_FuncModule,"Project": Path_Project} #Map Type to related directory
    cmbEditComboList_Code_Type_Const = {"CPlusPlus": "C++","Java": "Java","Python": "Python","CSharp": "C#","SQL": "SQL","HTML_CSS": "Html/CSS","C_Lang": "C_Lang","Matlab": "Matlab"}
    TypeDirMap = {"Function Module":"FuncModule", "Project":"Project"}
    Dirs = []
    for dir in TypeDirList:
        TypeDir = os.path.join(AbsolutePath, TypeDirMap[dir] if dir in TypeDirMap else dir)
        Dirs = [d for d in os.listdir(TypeDir) if os.path.isdir(os.path.join(TypeDir,d))]#list only the directory under given directory
    for dir in Dirs:
        CodeTypeDirList.append(dir)

def KeywordQuery(keyword, Text_result_control):
    global AbsolutePath
    TypeDirList = []
    CodeTypeDirList = []
    TraveringTypeCodeTypeFiles(TypeDirList,CodeTypeDirList)
    rootpathlist = []
    for TypeDir in TypeDirList:      
        rootpathlist.append(AbsolutePath + TypeDir + "/Record.txt")
    #clear the Text
    Text_result_control.delete(0.0, END) #based on the package imported at the topmost of this page, namely tkinter
    #Traverse rootpathlist with KeyWord
    if len(keyword) == 0:#if keyword is space, program will return
        return
    #Split Keyword by space
    keyword = ' '.join(keyword.split())
    keyword = keyword.split(' ')
    ResultList = []
    QueriedResultCounts = 0
    for RootPath in rootpathlist:#Used to read the two root text file
        handle = open(RootPath, 'r')#Open File and Read text
        #The next three variables is very important!
        index = [] #used to store the file position of the "keyword" and paried string        Str_Language = []
        Str_index = []#the string of where keyword belongs to.
        index_Language = {"index_C_Lang": 0,"index_CplusPlus": 0, "index_Csharp": 0, "index_Python": 0, "index_SQL": 0, "index_HTML_CSS": 0, "index_Matlab": 0, "index_Java": 0} #Used to store the current file position of each language index, like "CPlusPlus" and so on.
        DirectoryOrFileName = [] #used to store the directory discribed in keyword

        Curr_Pos = 0#Current file postion in the text file
        for eachLine in handle:#Traverse the text in file and calculate the value of variable "index" and "index_Language"
            tempindex = -1
            for keyword_item in keyword:
                tempindex = eachLine.find(keyword_item)
                if tempindex != -1:
                    continue
                else:
                    break
            tempindex1 = tempindex + Curr_Pos
            if tempindex != -1:
                index.append(tempindex1)#Add the keyword's position in index list
                Str_index.append(eachLine)
                tempstr = eachLine.split('>')
                if len(tempstr) >= 4:
                    DirectoryOrFileName.append(tempstr[1] + "\\" + tempstr[2]) #The code directory related to keyword
                elif len(tempstr) >= 2:
                    DirectoryOrFileName.append(tempstr[1]) #The code directory related to keyword
                else:
                    DirectoryOrFileName.append("")
        count = 0        
        for i in index:
            if RootPath == Path_FuncModule_txt:
                for TypeDir in TypeDirList:
                    for CodeTypeDir in CodeTypeDirList:
                        Path = AbsolutePath.replace('/', '\\')+ TypeDir + "\\" +CodeTypeDir+ "\\"+ DirectoryOrFileName[count]
                        if os.path.exists(Path):
                            ResultList.append("\n-******************************************%s**************************************- \nTYPE:  "% (QueriedResultCounts+count) + TypeDir +" \nDESCRIPTION: \n"+Str_index[count]+"PATH:\n " + Path+"\n\n")
                count = count + 1
            else:
                for TypeDir in TypeDirList:
                    for CodeTypeDir in CodeTypeDirList:
                        Path = AbsolutePath.replace('/', '\\')+ TypeDir + "\\" +CodeTypeDir+ "\\"+ DirectoryOrFileName[count]
                        if os.path.exists(Path):
                            ResultList.append("\n-******************************************%s**************************************- \nTYPE:  "% (QueriedResultCounts+count) + TypeDir +" \nDESCRIPTION: \n"+Str_index[count]+"PATH:\n " + Path+ "\n\n")
                count = count + 1
        QueriedResultCounts = QueriedResultCounts + count
    # return ResultList#return the queried result.
    # print(ResultList)#print the queried result.
    count1 = 1.0
    for querieditems in ResultList: #display the queried result in entry control of GUI
        Text_result_control.insert(count1, querieditems)
        count1 = count1 + 7.0

def AddValueInDict(index_list, str, value, CurrPos):
    if value != -1:
        index_list[str] = value + CurrPos





#Main Frame Form
    #Manage Record GUI
def Call_Manage_Record_GUI(object):
    Manage_Record_GUI_1 = Manage_Record_GUI(object)
class Manage_Record_GUI:
#using Type, Code_Type to find the Record.txt file and locate the position to add record
    cmbEditComboList_Code_Type = []
    index_list = []
    description_list = {}
    keywords_list = {}
    DirPath_list = {}
    FilePath_list = {}
    MatchedRecordStr = {}
    def __init__(self, object):
        self.object = object
        self.frm_Manage_Record = Toplevel(self.object)
        self.frm_Manage_Record.attributes("-toolwindow", 1)
        self.frm_Manage_Record.wm_attributes("-topmost", 1)
        self.object.wm_attributes("-disabled", 1)#Disable parent window
        self.frm_Manage_Record.title("Manage Record")
        self.frm_Manage_Record.resizable(False,False)
        self.Init()
    #Add Related UI
        #Type
    def TraveringTypeFiles(self,event):
        self.Combobox_Type.delete(0,END)
        # Manage_Dir_GUI.cmbEditComboList_Code_Type = self.Combobox_Code_Type.get()
        global AbsolutePath
        Dirs = [d for d in os.listdir(AbsolutePath) if os.path.isdir((os.path.join(AbsolutePath,d)))]#list only the directory under given directory
        if '.git' in Dirs:
            Dirs.remove('.git')
        if 'CodingPartner' in Dirs:
            Dirs.remove('CodingPartner')
        if 'FuncModule' in Dirs:
            Dirs.remove('FuncModule')
            Dirs.append('Function Module')
        self.Combobox_Type['value'] = (Dirs)
    def TraveringCodeTypeFiles(self,event):
        self.Combobox_Code_Type.delete(0,END)
        Type = self.Combobox_Type.get()
        # Manage_Dir_GUI.cmbEditComboList_Code_Type = self.Combobox_Code_Type.get()
        Type_Dict = {"Function Module": Path_FuncModule,"Project": Path_Project} #Map Type to related directory
        cmbEditComboList_Code_Type_Const = {"CPlusPlus": "C++","Java": "Java","Python": "Python","CSharp": "C#","SQL": "SQL","HTML_CSS": "Html/CSS","C_Lang": "C_Lang","Matlab": "Matlab"}
        Dirs = []
        if Type != '':
            if os.path.exists(Type_Dict[Type]):
                Dirs = [d for d in os.listdir(Type_Dict[Type]) if os.path.isdir(os.path.join(Type_Dict[Type],d))]#list only the directory under given directory
        self.Combobox_Code_Type['value'] = (Dirs)
    def EnableButton(self):
        self.object.wm_attributes("-disabled", 0)#Enable parent window
        self.frm_Manage_Record.destroy()

    def Init(self):
        self.label_Type = Label(self.frm_Manage_Record,anchor = "nw",text="Type")  #anchor:must be n, ne, e, se, s, sw, w, nw, or center
        self.label_Type.grid(row=0, column = 0, columnspan = 2)
        cmbEditComboList_Type = ['Function Module','Project',]
        self.Combobox_Type = Combobox(self.frm_Manage_Record, values = cmbEditComboList_Type, state = 'readonly')  #anchor:must be n, ne, e, se, s, sw, w, nw, or center
        self.Combobox_Type.grid(row=0, column = 2, columnspan = 2)
        self.Combobox_Type.bind('<Button-1>', self.TraveringTypeFiles)#<ComboboxSelected>
            #Code Type
        self.label_Code_Type = Label(self.frm_Manage_Record,anchor = "nw",text="Code Type")  #anchor:must be n, ne, e, se, s, sw, w, nw, or center
        self.label_Code_Type.grid(row=0, column = 6, columnspan = 2)
        #cmbEditComboList_Code_Type = ['C++','Java','Python','C#','SQL', 'Html/CSS','C', 'Matlab']
        self.Combobox_Code_Type = Combobox(self.frm_Manage_Record, state = 'readonly')
        self.Combobox_Code_Type.grid(row=0, column = 10, columnspan = 4)
        self.Combobox_Code_Type.bind('<Button-1>', self.TraveringCodeTypeFiles)#<ComboboxSelected>
            #Description
        self.label_Description = Label(self.frm_Manage_Record,anchor = "nw",text="Description")  #anchor:must be n, ne, e, se, s, sw, w, nw, or center
        self.label_Description.grid(row=0, column = 14, columnspan = 2)
        self.entry_Description = Entry(self.frm_Manage_Record)
        self.entry_Description.grid(row=0, column=16, columnspan = 4)
            #Keywords
        self.label_Keywords = Label(self.frm_Manage_Record,anchor = "nw",text="Keywords")  #anchor:must be n, ne, e, se, s, sw, w, nw, or center
        self.label_Keywords.grid(row=0, column = 20, columnspan = 2)
        self.entry_Keywords = Entry(self.frm_Manage_Record)
        self.entry_Keywords.grid(row=0, column=22, columnspan = 4)
            #Directory Path
        DirecotryPath = ''
        self.button_Dir_Path = Button(self.frm_Manage_Record, text = "Directory", command = lambda:OpenDir(DirecotryPath,self.entry_Dir_Path, self.Combobox_Type.get(), self.frm_Manage_Record))#Button used to add record in Record.txt
        self.button_Dir_Path.grid(row=0, column=26, columnspan = 2)
        self.entry_Dir_Path = Entry(self.frm_Manage_Record)
        self.entry_Dir_Path.grid(row=0, column=28, columnspan = 4)
            #File Path
        FilePath = ''
        self.button_File_Path = Button(self.frm_Manage_Record, text = "File", command = lambda:OpenFile(FilePath,self.entry_File_Path, self.Combobox_Type.get(), self.frm_Manage_Record))#Button used to add record in Record.txt
        self.button_File_Path.grid(row=0, column=32, columnspan = 2)
        self.entry_File_Path = Entry(self.frm_Manage_Record)
        self.entry_File_Path.grid(row=0, column=34, columnspan = 4)
            #Add
        self.button_Add = Button(self.frm_Manage_Record, text = "Add", command = lambda:ManageRecord_Add(self.frm_Manage_Record,self.Combobox_Type.get(), self.Combobox_Code_Type.get(), self.entry_Description.get(), self.entry_Keywords.get(), self.entry_Dir_Path.get(), self.entry_File_Path.get()))#Button used to add record in Record.txt      , command = lambda:OpenFile(FilePath,entry_Path, Combobox_Type.get())
        self.button_Add.grid(row=0, column=38, columnspan = 2)

        #Delete Related UI
            #Keyword_Query
        self.label_Keyword_Query = Label(self.frm_Manage_Record,anchor = "nw",text="Keyword")  #anchor:must be n, ne, e, se, s, sw, w, nw, or center
        self.label_Keyword_Query.grid(row=1, column = 0, columnspan = 2)
        self.entry_Keyword_Query = Entry(self.frm_Manage_Record)
        self.entry_Keyword_Query.grid(row=1, column = 2, columnspan = 4)

            #Index
        self.label_Index = Label(self.frm_Manage_Record,anchor = "nw",text="Index")  #anchor:must be n, ne, e, se, s, sw, w, nw, or center
        self.label_Index.grid(row=1, column = 6, columnspan = 2)
        self.Combobox_Index = Combobox(self.frm_Manage_Record, state = 'readonly')
        self.Combobox_Index.grid(row=1, column = 10, columnspan = 4)
        self.Combobox_Index.bind("<<ComboboxSelected>>", self.RenewManageRecord_Delete_UI)#<ComboboxSelected>
            #Description
        self.label_Description_Delete = Label(self.frm_Manage_Record,anchor = "nw",text="Description")  #anchor:must be n, ne, e, se, s, sw, w, nw, or center
        self.label_Description_Delete.grid(row=1, column = 14, columnspan = 2)
        self.entry_Description_Delete = Entry(self.frm_Manage_Record)
        self.entry_Description_Delete.grid(row=1, column=16, columnspan = 4)
            #Keywords
        self.label_Keywords_Delete = Label(self.frm_Manage_Record,anchor = "nw",text="Keywords")  #anchor:must be n, ne, e, se, s, sw, w, nw, or center
        self.label_Keywords_Delete.grid(row=1, column = 20, columnspan = 2)
        self.entry_Keywords_Delete = Entry(self.frm_Manage_Record)
        self.entry_Keywords_Delete.grid(row=1, column=22, columnspan = 4)
            #Directory Path
        self.label_Dir_Path = Label(self.frm_Manage_Record,anchor = "nw",text="Directory")  #anchor:must be n, ne, e, se, s, sw, w, nw, or center
        self.label_Dir_Path.grid(row=1, column = 26, columnspan = 2)
        self.entry_Dir_Path_Delete = Entry(self.frm_Manage_Record)
        self.entry_Dir_Path_Delete.grid(row=1, column=28, columnspan = 4)
            #File Path
        self.label_File_Path = Label(self.frm_Manage_Record,anchor = "nw",text="File")  #anchor:must be n, ne, e, se, s, sw, w, nw, or center
        self.label_File_Path.grid(row=1, column = 32, columnspan = 2)
        self.entry_File_Path_Delete = Entry(self.frm_Manage_Record)
        self.entry_File_Path_Delete.grid(row=1, column=34, columnspan = 4)
            #Delete
        self.button_Delete = Button(self.frm_Manage_Record, text = "Delete", command = lambda:ManageRecord_Delete_Button(self.frm_Manage_Record, self.Combobox_Index.get(), Manage_Record_GUI.MatchedRecordStr, self.entry_Dir_Path_Delete.get(), self.entry_File_Path_Delete.get()))#Button used to delete record in Record.txt
        self.button_Delete.grid(row=1, column=38, columnspan = 2)
        self.entry_Keyword_Query.bind('<KeyRelease>', self.ManageRecord_Delete_callback)
        #make the current main window lay in the middle of screen
        self.frm_Manage_Record.update_idletasks()
        w = self.frm_Manage_Record.winfo_screenwidth()
        h = self.frm_Manage_Record.winfo_screenheight()
        size = tuple(int(_) for _ in self.frm_Manage_Record.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        self.frm_Manage_Record.geometry("%dx%d+%d+%d" % (size + (x, y)))
        self.frm_Manage_Record.protocol ("WM_DELETE_WINDOW", self.EnableButton)

    def RenewManageRecord_Delete_UI(self, event):
        selected_index = self.Combobox_Index.get()
        self.entry_Description_Delete.delete(0, END)
        self.entry_Description_Delete.insert(0, Manage_Record_GUI.description_list[selected_index])
        self.entry_Keywords_Delete.delete(0, END)
        self.entry_Keywords_Delete.insert(0, Manage_Record_GUI.keywords_list[selected_index])
        self.entry_Dir_Path_Delete.delete(0, END)
        self.entry_Dir_Path_Delete.insert(0, Manage_Record_GUI.DirPath_list[selected_index])
        self.entry_File_Path_Delete.delete(0, END)
        self.entry_File_Path_Delete.insert(0, Manage_Record_GUI.FilePath_list[selected_index])

    def ManageRecord_Delete_callback(self,event):
        ManageRecord_Delete(self.frm_Manage_Record,self.entry_Keyword_Query.get(), self.Combobox_Index, self.entry_Description_Delete, self.entry_Keywords_Delete, self.entry_Dir_Path_Delete, self.entry_File_Path_Delete, Manage_Record_GUI.index_list, Manage_Record_GUI.description_list, Manage_Record_GUI.keywords_list,Manage_Record_GUI.DirPath_list, Manage_Record_GUI.FilePath_list,Manage_Record_GUI.MatchedRecordStr)

def ManageRecord_Delete_Button(object, index,RecordStrMap,Dir_Path, File_Path):
    if index == "" or RecordStrMap == "" or File_Path == "":
        object.wm_attributes("-topmost", 0)
        showerror("Parameter Error", "Please configure the parameter correctly!")
        object.wm_attributes("-topmost", 1)
        return
    RecordStr = RecordStrMap[index]
    #delete file or directory and renew record in Record.txt
    if os.path.isdir(Dir_Path) and Dir_Path != "":
        object.wm_attributes("-topmost", 0)
        result = askyesno("Caution","Do you really want to delete %s?"%Dir_Path)
        if result == True:
            shutil.rmtree(Dir_Path)#delete directory
            Delete_Record_RenewRecordtxt(Dir_Path,RecordStr)#delete related record in file Record.txt
            showinfo("Success","\'"+  Dir_Path +"\'"+" directory was deleted")
        object.wm_attributes("-topmost", 1)
    else:
        object.wm_attributes("-topmost", 0)
        result = askyesno("Caution","Do you really want to delete %s?"%File_Path)
        if result == True:
            os.remove(File_Path)#delete file
            Delete_Record_RenewRecordtxt(File_Path,RecordStr)#delete related record in file Record.txt
            showinfo("Success","\'"+  File_Path +"\'"+" file was deleted")
        object.wm_attributes("-topmost", 1)
def Delete_Record_RenewRecordtxt(Path,RecordStr):
    Path_CodeTypeRecordPath = str.replace(Path, Path.split('\\')[-2] if Path.split('\\')[-1] == '' else Path.split('\\')[-1], "",1)
    Path_TypeRecordPath = str.replace(Path_CodeTypeRecordPath, Path_CodeTypeRecordPath.split('\\')[-2] if Path_CodeTypeRecordPath.split('\\')[-1] == '' else Path_CodeTypeRecordPath.split('\\')[-1], "",1)
    CodeType_Recordtxt = Path_CodeTypeRecordPath + "\\Record.txt"
    Type_Recordtxt = Path_TypeRecordPath + "\\Record.txt"
    fid = open(CodeType_Recordtxt,"r")
    lines = fid.readlines()
    fid.close()
    fid = open(CodeType_Recordtxt,"wt")
    for line in lines:
        if line == RecordStr:
            continue
        else:
            fid.write(line)
    fid.close()
    fid = open(Type_Recordtxt,"r")
    lines = fid.readlines()
    fid.close()
    fid = open(Type_Recordtxt,"wt")
    for line in lines:
        if line == RecordStr:
            continue
        else:
            fid.write(line)
    fid.close()




    #Manage Directory GUI
def Call_Manage_Dir_GUI(object):
    Manage_Dir_GUI_1 = Manage_Dir_GUI(object)
class Manage_Dir_GUI:
#using Type, Code_Type to find the Record.txt file and locate the position to add record
    cmbEditComboList_Code_Type = []
    def __init__(self, object):
        self.object = object
        self.frm_Manage_Dir = Toplevel(self.object)
        self.frm_Manage_Dir.attributes("-toolwindow", 1)
        self.frm_Manage_Dir.wm_attributes("-topmost", 1)
        self.object.wm_attributes("-disabled", 1)#Disable parent window
        self.frm_Manage_Dir.title("Manage Directory")
        self.frm_Manage_Dir.resizable(False,False)
        self.Init()
    def TraveringCodeTypeFiles(self,event):
        self.Combobox_Code_Type['value'] = ("")
        Type = self.Combobox_Type.get()
        # Manage_Dir_GUI.cmbEditComboList_Code_Type = self.Combobox_Code_Type.get()
        Type_Dict = {"Function Module": Path_FuncModule,"Project": Path_Project} #Map Type to related directory
        cmbEditComboList_Code_Type_Const = {"CPlusPlus": "C++","Java": "Java","Python": "Python","CSharp": "C#","SQL": "SQL","HTML_CSS": "Html/CSS","C_Lang": "C_Lang","Matlab": "Matlab"}
        if Type in Type_Dict:
            if Type != "" and os.path.exists(Type_Dict[Type]):
                Dirs = [d for d in os.listdir(Type_Dict[Type]) if os.path.isdir(os.path.join(Type_Dict[Type],d))]#list only the directory under given directory
            else:
                global AbsolutePath
                Dirs = [d for d in os.listdir(AbsolutePath + "\\" + Type) if os.path.isdir(os.path.join(AbsolutePath + "\\" + Type,d))]#list only the directory under given directory
            self.Combobox_Code_Type['value'] = (Dirs)
    def TraveringTypeFiles(self,event):
        self.Combobox_Type['value'] = ("")
        # Manage_Dir_GUI.cmbEditComboList_Code_Type = self.Combobox_Code_Type.get()
        global AbsolutePath
        Dirs = [d for d in os.listdir(AbsolutePath) if os.path.isdir((os.path.join(AbsolutePath,d)))]#list only the directory under given directory
        if '.git' in Dirs:
            Dirs.remove('.git')
        if 'CodingPartner' in Dirs:
            Dirs.remove('CodingPartner')
        if 'FuncModule' in Dirs:
            Dirs.remove('FuncModule')
            Dirs.append('Function Module')
        self.Combobox_Type['value'] = (Dirs)
    def EnableButton(self):#when current windows closes, the parent window will be enable.
        self.object.wm_attributes("-disabled", 0)#Enable parent window
        self.frm_Manage_Dir.destroy()#Destory current window
    def Init(self):
        #GUI Related
            #Type
        self.label_Type = Label(self.frm_Manage_Dir,anchor = "nw",text="Type")  #anchor:must be n, ne, e, se, s, sw, w, nw, or center
        self.label_Type.grid(row=0, column = 0, columnspan = 2, rowspan = 3)
        cmbEditComboList_Type = ['Function Module','Project',]
        self.Combobox_Type = Combobox(self.frm_Manage_Dir, values = cmbEditComboList_Type)  #anchor:must be n, ne, e, se, s, sw, w, nw, or center  , state = 'readonly'
        self.Combobox_Type.grid(row=0, column = 2, columnspan = 10, rowspan = 3)
        self.Combobox_Type.bind('<Button-1>', self.TraveringTypeFiles)#<ComboboxSelected>
            #Code Type
        self.label_Code_Type = Label(self.frm_Manage_Dir,anchor = "nw",text="Code Type")  #anchor:must be n, ne, e, se, s, sw, w, nw, or center
        self.label_Code_Type.grid(row=0, column = 12, columnspan = 2, rowspan = 3)
        self.Combobox_Code_Type = Combobox(self.frm_Manage_Dir, values = Manage_Dir_GUI.cmbEditComboList_Code_Type)
        self.Combobox_Code_Type.grid(row=0, column = 14, columnspan = 4, rowspan = 3)
        self.Combobox_Code_Type.bind('<Button-1>', self.TraveringCodeTypeFiles)#<ComboboxSelected>
            #Add
        self.button_Add = Button(self.frm_Manage_Dir, text = "Add" , command = lambda:ManageDirectory_Add(self.frm_Manage_Dir,self.Combobox_Type.get(), self.Combobox_Code_Type.get()))#Button used to add Direcotory
        self.button_Add.grid(row=4, column=9, columnspan = 2)
        self.button_Delete = Button(self.frm_Manage_Dir, text = "Delete" , command = lambda:ManageDirectory_Delete(self.frm_Manage_Dir,self.Combobox_Type.get(), self.Combobox_Code_Type.get()))#Button used to add record in Record.txt      , command = lambda:OpenFile(FilePath,entry_Path, Combobox_Type.get())
        self.button_Delete.grid(row=4, column=14, columnspan = 2)
            #Delete
        #make the current main window lay in the middle of screen
        self.frm_Manage_Dir.update_idletasks()
        w = self.frm_Manage_Dir.winfo_screenwidth()
        h = self.frm_Manage_Dir.winfo_screenheight()
        size = tuple(int(_) for _ in self.frm_Manage_Dir.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        self.frm_Manage_Dir.geometry("%dx%d+%d+%d" % (size + (x, y)))
        self.frm_Manage_Dir.protocol ("WM_DELETE_WINDOW", self.EnableButton)
def OpenDir(Path,object, Type, Window_Name):#Get Directory
    Window_Name.wm_attributes("-topmost", 0)
    Path = ''#askopenfilename
    Path = filedialog.askdirectory()
    object.delete(0, END)
    object.insert(1, Path)
    Window_Name.wm_attributes("-topmost", 1)
def OpenFile(Path,object, Type, Window_Name):#Get File Directory
    Window_Name.wm_attributes("-topmost", 0)
    Path = ''#askopenfilename
    Path = filedialog.askopenfilename()
    object.delete(0, END)
    object.insert(1, Path)
    Window_Name.wm_attributes("-topmost", 1)




def SetDefaultWorkingFile(entry_query):#Get File Directory
    Path = filedialog.askdirectory()
    if os.path.exists(Path) and Path != "":
        entry_query.insert(0, Path)

class SetDefaultPath:
	#Flow:
	#(1)First: Judge whether there under the
    def __init__(self):
        self.DefaultPath = "C:\\Users\\Public\\Coding Partner\\DefaultPath.txt"
        self.DefaultDir = "C:\\Users\\Public\\Coding Partner"

        self.Init()
    def SetDefaultWorkingFile_OK(self):
        Path = self.entry_PATH.get()
        global AbsolutePath
        if Path != "":
            if os.path.exists(Path):
                if self.Combobox_Dir.get() == "Existed":
                    os.mkdir(self.DefaultDir)
                    DefaultPath = self.DefaultDir + "\\DefaultPath.txt"
                    fid = open(DefaultPath, "wt")
                    Path = Path+"/"
                    fid.write(Path)#This str should get from UI set
                    fid.close()            
                    AbsolutePath = Path
                    Path_Assig_Value()
                    self.PathSetUI.destroy()
                elif self.Combobox_Dir.get() == "New":
                    os.mkdir(self.DefaultDir)
                    DefaultPath = self.DefaultDir + "\\DefaultPath.txt"
                    fid = open(DefaultPath, "wt")
                    if not os.path.exists(Path + "/Coding_Partner"):
                        os.mkdir(Path + "/Coding_Partner")
                    Path = Path + "/Coding_Partner/"
                    fid.write(Path)#This str should get from UI set
                    fid.close()                    
                    AbsolutePath = Path
                    Path_Assig_Value()
                    self.PathSetUI.destroy()
    def CancelButtonFunc(self):
        self.PathSetUI.destroy()
        sys.exit()
    def Init(self):
        if not os.path.exists(self.DefaultPath):
            #result = askyesno("Attention","Do You Want Create A New Working Directory?")
            #if result == YES:
            self.PathSetUI = Tk()
            self.PathSetUI.title("Select Working Directory")
            self.PathSetUI.resizable(False,False)
            self.PathSetUI.protocol ("WM_DELETE_WINDOW", self.CancelButtonFunc)
            self.label_DirSelect = Label(self.PathSetUI,anchor = "nw",text="Directory Type")
            self.label_DirSelect.grid(row=0, column=0,sticky=W, columnspan = 2)
            cmbEditComboList_Dir = ["New", "Existed"]
            self.Combobox_Dir = Combobox(self.PathSetUI, values = cmbEditComboList_Dir, state = 'readonly')  #anchor:must be n, ne, e, se, s, sw, w, nw, or center
            self.Combobox_Dir.set("Existed");
            self.Combobox_Dir.grid(row=0, column = 2, columnspan = 2)
            self.label_PATH = Label(self.PathSetUI,anchor = "nw",text="PATH")  #anchor:must be n, ne, e, se, s, sw, w, nw, or center
            self.label_PATH.grid(row=0, column=4,sticky=W, columnspan = 3)
            self.entry_PATH = Entry(self.PathSetUI,width = 60)
            self.entry_PATH.grid(row=0, column=7, columnspan = 6)
            self.button_SetPath = Button(self.PathSetUI, text = "Open", command = lambda:SetDefaultWorkingFile( self.entry_PATH))#tied the entry to the button, when the button is being clicked, function KeywordQuery will be called.
            self.button_SetPath.grid(row=0, column=13)
            self.button_ok = Button(self.PathSetUI, text = "   OK   ", command = self.SetDefaultWorkingFile_OK)#tied the entry to the button, when the button is being clicked, function KeywordQuery will be called.
            self.button_ok.grid(row=1, column=4, columnspan = 4)
            self.button_cacel = Button(self.PathSetUI, text = "CACEL", command = self.CancelButtonFunc)#tied the entry to the button, when the button is being clicked, function KeywordQuery will be called.
            self.button_cacel.grid(row=1, column=8, columnspan = 4)
            #make the current main window lay in the middle of screen
            self.PathSetUI.update_idletasks()
            w = self.PathSetUI.winfo_screenwidth()
            h = self.PathSetUI.winfo_screenheight()
            size = tuple(int(_) for _ in self.PathSetUI.geometry().split('+')[0].split('x'))
            x = w/2 - size[0]/2
            y = h/2 - size[1]/2
            self.PathSetUI.geometry("%dx%d+%d+%d" % (size + (x, y)))
            self.PathSetUI.mainloop()
        else:
            fid = open(self.DefaultPath, "r")
            line = fid.readline()
            fid.close()
            global AbsolutePath
            AbsolutePath = line
            Path_Assig_Value()



class MainWindow:
    #Set a new default Directory or select existed directory
    QuriedResultList = []  #Queried result will be in this list variable
    #Later the GUI related code will be packaging and be putted in Main_UI directory
    #GUI Related
    ############################################Query GUI Related###############################################################
    #input gui entry contorl
if __name__ == "__main__":
    WindowsCodingPartnerPath = SetDefaultPath()
    frmMain = Tk()
    frmMain.title("Coding Partner")
    frmMain.resizable(False,False)
    label_query = Label(frmMain,anchor = "nw",text="Enter Keyword")  #anchor:must be n, ne, e, se, s, sw, w, nw, or center
    label_query.grid(row=0, sticky=W, columnspan = 3)
    entry_query = Entry(frmMain,  width = 95)
    entry_query.grid(row=0, column=3, columnspan = 2)
    button_query = Button(frmMain, text = "Query", width = 6, command = lambda:KeywordQuery(entry_query.get(),Text_result))#tied the entry to the button, when the button is being clicked, function KeywordQuery will be called.
    button_query.grid(row=0, column=5, columnspan = 2)
        #output gui entry contol
    label_result = Label(frmMain,anchor = "s",text="Queried Results")  #anchor:must be n, ne, e, se, s, sw, w, nw, or center
    label_result.grid(row=2, column=0, sticky=W)
    Text_result = Text(frmMain, width = 95, height = 15)
    Text_result.grid(row=2, column=3, columnspan = 2)
    #Bind the ENTER key to Entry to execute KeywordQuery function
    # create a popup menu
    def ShowInExplorer():
        selectedPath = Text_result.get('sel.first', 'sel.last')
        #judge whether the path exists
        if os.path.exists(selectedPath):
            if os.path.isdir(selectedPath):
                subprocess.Popen(r'explorer /select,"{0}"'.format(selectedPath))
        else:
            showwarning("Warning","\'"+selectedPath+"\'"+" do not exist")#show a warning MessageBox
    def OpenwithIDE():
        selectedPath = Text_result.get('sel.first', 'sel.last')
        #judge whether the path exists
        if os.path.exists(selectedPath):
            if os.path.isfile(selectedPath):
                os.startfile(selectedPath)
        else:
            showwarning("Warning","\'"+selectedPath+"\'"+" do not exist")#show a warning MessageBox

    menu = Menu(frmMain, tearoff=0)
    menu.add_command(label="show in windows explorer", command=ShowInExplorer)
    menu.add_command(label="open with related IDE", command=OpenwithIDE)
    def Text_result_callback(event):
        menu.post(event.x_root, event.y_root)
    Text_result.bind('<Button-3>', Text_result_callback)
    #Bind the ENTER key to Entry to execute KeywordQuery function
    def callback(event):
        KeywordQuery(entry_query.get(), Text_result)
    entry_query.bind('<KeyRelease>', callback)
    ############################################Add Record GUI Related######################################################
    button_Manage_Record = Button(frmMain, text="Manage Record", command= lambda:Call_Manage_Record_GUI(frmMain))
    button_Manage_Record.grid(row=4, column=3, rowspan = 2)
    button_Manage_Dir = Button(frmMain, text = "Manage Directory", command = lambda:Call_Manage_Dir_GUI(frmMain))#Button used to add record in Record.txt
    button_Manage_Dir.grid(row=4, column=4, rowspan = 2)
    ######################################################End###############################################################
    #make the current main window lay in the middle of screen
    frmMain.update_idletasks()
    w = frmMain.winfo_screenwidth()
    h = frmMain.winfo_screenheight()
    size = tuple(int(_) for _ in frmMain.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    frmMain.geometry("%dx%d+%d+%d" % (size + (x, y)))

    #ScrollBary in Text
    scrollbary = Scrollbar(frmMain, orient = 'vertical')
    scrollbary.grid(row = 2, column = 3,sticky = 'NES', columnspan = 2) #sticky is used to contorl the Control's direction in the contained Control
    # attach Text Control to scrollbar
    Text_result.config(yscrollcommand=scrollbary.set)
    scrollbary.config(command=Text_result.yview)
    #ScrollBarx in Text
    scrollbarx = Scrollbar(frmMain, orient = 'horizontal')
    scrollbarx.grid(row = 2, column =3,sticky = 'WSE', columnspan = 2) #sticky is used to contorl the Control's direction in the contained Control
    # attach Text Control to scrollbar
    Text_result.config(xscrollcommand=scrollbarx.set)
    scrollbarx.config(command=Text_result.xview)
    frmMain.mainloop()






