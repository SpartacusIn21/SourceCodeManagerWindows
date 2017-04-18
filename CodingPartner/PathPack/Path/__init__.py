__author__ = 'JD'
import sys,os

global AbsolutePath
###################Text File Path in  FuncModule####################
#C
global Path_FuncModule_C
#CPlusPlus
global Path_FuncModule_CPlusPlus
#CSharp
global Path_FuncModule_CSharp
#HTML_CSS
global Path_FuncModule_HTML_CSS
#Matlab
global Path_FuncModule_Matlab
#Python
global Path_FuncModule_Python
#SQL
global Path_FuncModule_SQL

###################Text File Path in Project##########################
#C
global Path_Project_C
#CPlusPlus
global Path_Project_CPlusPlus
#CSharp
global Path_Project_CSharp
#HTML_CSS
global Path_Project_HTML_CSS
#Matlab
global Path_Project_Matlab
#Python
global Path_Project_Python
#SQL
global Path_Project_SQL
########################### Path List ###############################
global Path_FuncModule
global Path_Project

global Path_FuncModule_txt
global Path_Project_txt

#Three Path Lists
global RootPathList
global FuncModulePathList
global ProjectPathList

def Path_Assig_Value():
    ###################Text File Path in  FuncModule####################
    #C
    global Path_FuncModule_C
    Path_FuncModule_C = AbsolutePath + "FuncModule/C/Record.txt"
    #CPlusPlus
    global Path_FuncModule_CPlusPlus
    Path_FuncModule_CPlusPlus = AbsolutePath+"FuncModule/CPlusPlus/Record.txt"
    #CSharp
    global Path_FuncModule_CSharp
    Path_FuncModule_CSharp = AbsolutePath+"FuncModule/CSharp/Record.txt"
    #HTML_CSS
    global Path_FuncModule_HTML_CSS
    Path_FuncModule_HTML_CSS = AbsolutePath+"FuncModule/HTML_CSS/Record.txt"
    #Matlab
    global Path_FuncModule_Matlab
    Path_FuncModule_Matlab = AbsolutePath+"FuncModule/Matlab/Record.txt"
    #Python
    global Path_FuncModule_Python
    Path_FuncModule_Python = AbsolutePath+"FuncModule/Python/Record.txt"
    #SQL
    global Path_FuncModule_SQL
    Path_FuncModule_SQL = AbsolutePath+"FuncModule/SQL/Record.txt"

    ###################Text File Path in Project##########################
    #C
    global Path_Project_C
    Path_Project_C = AbsolutePath+"Project/C/Record.txt"
    #CPlusPlus
    global Path_Project_CPlusPlus
    Path_Project_CPlusPlus = AbsolutePath+"Project/CPlusPlus/Record.txt"
    #CSharp
    global Path_Project_CSharp
    Path_Project_CSharp = AbsolutePath+"Project/CSharp/Record.txt"
    #HTML_CSS
    global Path_Project_HTML_CSS
    Path_Project_HTML_CSS = AbsolutePath+"Project/HTML_CSS/Record.txt"
    #Matlab
    global Path_Project_Matlab
    Path_Project_Matlab = AbsolutePath+"Project/Matlab/Record.txt"
    #Python
    global Path_Project_Python
    Path_Project_Python =AbsolutePath+ "Project/Python/Record.txt"
    #SQL
    global Path_Project_SQL
    Path_Project_SQL = AbsolutePath+"Project/SQL/Record.txt"
    ########################### Path List ###############################
    global Path_FuncModule
    Path_FuncModule =AbsolutePath+ "FuncModule/"
    global Path_Project
    Path_Project = AbsolutePath+"Project/"

    global Path_FuncModule_txt
    Path_FuncModule_txt = AbsolutePath+"FuncModule/Record.txt"
    global Path_Project_txt
    Path_Project_txt = AbsolutePath+"Project/Record.txt"
    #Three Path Lists
    global RootPathList
    RootPathList = [Path_FuncModule_txt,Path_Project_txt]
    global FuncModulePathList
    FuncModulePathList = [Path_FuncModule_C,Path_FuncModule_CPlusPlus, Path_FuncModule_CSharp, Path_FuncModule_HTML_CSS, Path_FuncModule_Matlab, Path_FuncModule_Python,Path_FuncModule_SQL]
    global ProjectPathList
    ProjectPathList = [Path_Project_C,Path_Project_CPlusPlus, Path_Project_CSharp, Path_Project_HTML_CSS, Path_Project_Matlab, Path_Project_Python,Path_Project_SQL]