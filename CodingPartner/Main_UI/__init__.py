__author__ = 'JD'
from PathPack.Path import *
from tkinter import * #when use realted module, we need to import the realted package
from PathPack.Path import *;from FuncPack.txtManage import *
from tkinter.ttk import * #Combobox
from tkinter import filedialog
import PathPack.Path.__init__
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
        Dirs = [d for d in os.listdir(PathPack.Path.__init__.AbsolutePath) if os.path.isdir((os.path.join(PathPack.Path.__init__.AbsolutePath,d)))]#list only the directory under given directory
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
        Type_Dict = {"Function Module": PathPack.Path.__init__.Path_FuncModule,"Project": PathPack.Path.__init__.Path_Project} #Map Type to related directory
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
        Type_Dict = {"Function Module": PathPack.Path.__init__.Path_FuncModule,"Project": PathPack.Path.__init__.Path_Project} #Map Type to related directory
        cmbEditComboList_Code_Type_Const = {"CPlusPlus": "C++","Java": "Java","Python": "Python","CSharp": "C#","SQL": "SQL","HTML_CSS": "Html/CSS","C_Lang": "C_Lang","Matlab": "Matlab"}
        if Type in Type_Dict:
            if Type != "" and os.path.exists(Type_Dict[Type]):
                Dirs = [d for d in os.listdir(Type_Dict[Type]) if os.path.isdir(os.path.join(Type_Dict[Type],d))]#list only the directory under given directory
            else:
                Dirs = [d for d in os.listdir(PathPack.Path.__init__.AbsolutePath + "\\" + Type) if os.path.isdir(os.path.join(PathPack.Path.__init__.AbsolutePath + "\\" + Type,d))]#list only the directory under given directory
            self.Combobox_Code_Type['value'] = (Dirs)
    def TraveringTypeFiles(self,event):
        self.Combobox_Type['value'] = ("")
        # Manage_Dir_GUI.cmbEditComboList_Code_Type = self.Combobox_Code_Type.get()
        Dirs = [d for d in os.listdir(PathPack.Path.__init__.AbsolutePath) if os.path.isdir((os.path.join(PathPack.Path.__init__.AbsolutePath,d)))]#list only the directory under given directory
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




