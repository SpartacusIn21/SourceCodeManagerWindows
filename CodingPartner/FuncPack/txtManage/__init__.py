__author__ = 'JD'
from PathPack.Path import *
from tkinter import * #when use realted module, we need to import the realted package
from tkinter.messagebox import *
from datetime import *
import shutil #delete directory recursively related
import shutil, errno
import PathPack.Path.__init__
#Add, Delete, Modify and Query the txt file under FuncModule directory and Project directory
###################################### Manage Directory #########################################
    #Add
def ManageDirectory_Add(object,Type, Code_Type):
    if Type == "":
        object.wm_attributes("-topmost", 0)
        showwarning("Warning","\'Type\'"+" can't be null")#show a warning MessageBox
        object.wm_attributes("-topmost", 1)
        return
    Type_Dict = {"Function Module": PathPack.Path.__init__.Path_FuncModule,"Project": PathPack.Path.__init__.Path_Project} #Map Type to related directory
    Code_Type_Dict = {"C++": "CPlusPlus","Java": "Java","Python": "Python","C#": "CSharp","SQL": "SQL","Html/CSS": "HTML_CSS","C_Lang": "C_Lang","Matlab": "Matlab"} #Map Code Type to related directory
    Add_Code_Type_Pairs(Code_Type_Dict, Code_Type)
    Type_Dir = ''
    if Type in Type_Dict:
        Type_Dir = Type_Dict[Type]
    else:
        Type_Dir = PathPack.Path.__init__.AbsolutePath  +  Type
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
    Type_Dict = {"Function Module": PathPack.Path.__init__.Path_FuncModule,"Project": PathPack.Path.__init__.Path_Project} #Map Type to related directory
    Code_Type_Dict = {"C++": "CPlusPlus","Java": "Java","Python": "Python","C#": "CSharp","SQL": "SQL","Html/CSS": "HTML_CSS","C_Lang": "C_Lang","Matlab": "Matlab"} #Map Code Type to related directory
    Type_Dir = ''
    if Type in Type_Dict:
        Type_Dir = Type_Dict[Type]
    else:
        Type_Dir = PathPack.Path.__init__.AbsolutePath  +  Type
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
    # Dir_Name = src.split('/')
    # Dir_Name = Dir_Name[-1]
    # dst += "/" + Dir_Name
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):#目录
            copytree(s, d, symlinks, ignore)
        else:#文件
            if (not os.path.exists(d)) or (os.stat(s).st_mtime - os.stat(d).st_mtime > 1):
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
    Type_Dict = {"Function Module": PathPack.Path.__init__.Path_FuncModule,"Project": PathPack.Path.__init__.Path_Project} #Map Type to related directory
    Code_Type_Dict = {"C++": "CPlusPlus","Java": "Java","Python": "Python","C#": "CSharp","SQL": "SQL","Html/CSS": "HTML_CSS","C_Lang": "C_Lang","Matlab": "Matlab"} #Map Code Type to related directory
    Add_Code_Type_Pairs(Code_Type_Dict, Code_Type)
    Type_Dir = ''
    if Type in Type_Dict:
        Type_Dir = Type_Dict[Type]
    else:
        Type_Dir = PathPack.Path.__init__.AbsolutePath  +  Type
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
        #创建根目录
        temp_Dir_Name = DirPath.split('/')
        temp_Dir_Name = temp_Dir_Name[-1]
        temp_Code_Type_Dir = Code_Type_Dir + "/" + temp_Dir_Name
        if not os.path.exists(temp_Code_Type_Dir):
            os.makedirs(temp_Code_Type_Dir)
        copytree(DirPath, temp_Code_Type_Dir)#文件夹拷贝
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
    TypeDirList = []
    CodeTypeDirList = []
    TraveringTypeCodeTypeFiles(TypeDirList,CodeTypeDirList)
    rootpathlist = []
    for TypeDir in TypeDirList:
        rootpathlist.append(PathPack.Path.__init__.AbsolutePath + TypeDir + "/Record.txt")
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
            if RootPath == PathPack.Path.__init__.Path_FuncModule_txt:
                for TypeDir in TypeDirList:
                    for CodeTypeDir in CodeTypeDirList:
                        Path = PathPack.Path.__init__.AbsolutePath.replace('/', '\\')+ TypeDir + "\\" +CodeTypeDir+ "\\"+ DirectoryOrFileName[count]
                        if os.path.exists(Path):
                            ResultList.append(Str_index[count]+"\n  PATH:  " + Path+"\n")
                count = count + 1
            else:
                for TypeDir in TypeDirList:
                    for CodeTypeDir in CodeTypeDirList:
                        Path = PathPack.Path.__init__.AbsolutePath.replace('/', '\\')+ TypeDir + "\\" +CodeTypeDir+ "\\"+ DirectoryOrFileName[count]
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
    Dirs = [d for d in os.listdir(PathPack.Path.__init__.AbsolutePath) if os.path.isdir((os.path.join(PathPack.Path.__init__.AbsolutePath,d)))]#list only the directory under given directory
    if '.git' in Dirs:
        Dirs.remove('.git')
    if 'CodingPartner' in Dirs:
        Dirs.remove('CodingPartner')
    for dir in Dirs:
        TypeDirList.append(dir)
    # Manage_Dir_GUI.cmbEditComboList_Code_Type = self.Combobox_Code_Type.get()
    Type_Dict = {"Function Module": PathPack.Path.__init__.Path_FuncModule,"Project": PathPack.Path.__init__.Path_Project} #Map Type to related directory
    cmbEditComboList_Code_Type_Const = {"CPlusPlus": "C++","Java": "Java","Python": "Python","CSharp": "C#","SQL": "SQL","HTML_CSS": "Html/CSS","C_Lang": "C_Lang","Matlab": "Matlab"}
    TypeDirMap = {"Function Module":"FuncModule", "Project":"Project"}
    Dirs = []
    for dir in TypeDirList:
        TypeDir = os.path.join(PathPack.Path.__init__.AbsolutePath, TypeDirMap[dir] if dir in TypeDirMap else dir)
        Dirs = [d for d in os.listdir(TypeDir) if os.path.isdir(os.path.join(TypeDir,d))]#list only the directory under given directory
    for dir in Dirs:
        CodeTypeDirList.append(dir)

def KeywordQuery(keyword, Text_result_control):
    TypeDirList = []
    CodeTypeDirList = []
    TraveringTypeCodeTypeFiles(TypeDirList,CodeTypeDirList)
    rootpathlist = []
    for TypeDir in TypeDirList:
        rootpathlist.append(PathPack.Path.__init__.AbsolutePath + TypeDir + "/Record.txt")
    #clear the Text
    Text_result_control.delete(0.0, END) #based on the package imported at the topmost of this page, namely tkinter
    #Traverse rootpathlist with KeyWord
    # if len(keyword) == 0:#if keyword is space, program will return
    #     return
    ResultList = []
    QueriedResultCounts = 0
    #Split Keyword by space
    keyword = ' '.join(keyword.split())
    keyword = keyword.split(' ')
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
            if len(keyword) == 0:
                tempindex = 0;
                index.append(tempindex)
                continue
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
            if RootPath == PathPack.Path.__init__.Path_FuncModule_txt:
                for TypeDir in TypeDirList:
                    for CodeTypeDir in CodeTypeDirList:
                        Path = PathPack.Path.__init__.AbsolutePath.replace('/', '\\')+ TypeDir + "\\" +CodeTypeDir+ "\\"+ DirectoryOrFileName[count]
                        if os.path.exists(Path):
                            ResultList.append("\n-******************************************%s**************************************- \nTYPE:  "% (QueriedResultCounts+count) + TypeDir +" \nDESCRIPTION: \n"+Str_index[count]+"PATH:\n " + Path+"\n\n")
                count = count + 1

            else:
                for TypeDir in TypeDirList:
                    for CodeTypeDir in CodeTypeDirList:
                        Path = PathPack.Path.__init__.AbsolutePath.replace('/', '\\')+ TypeDir + "\\" +CodeTypeDir+ "\\"+ DirectoryOrFileName[count]
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



