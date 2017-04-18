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
from Main_UI import *
from tkinter import *
from PathPack.Path import *
import PathPack.Path.__init__
import subprocess
import os
from tkinter import filedialog
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
        if Path != "":
            if os.path.exists(Path):
                if self.Combobox_Dir.get() == "Existed":
                    os.mkdir(self.DefaultDir)
                    DefaultPath = self.DefaultDir + "\\DefaultPath.txt"
                    fid = open(DefaultPath, "wt")
                    Path = Path+"/"
                    fid.write(Path)#This str should get from UI set
                    fid.close()
                    PathPack.Path.__init__.AbsolutePath = Path
                    PathPack.Path.__init__.Path_Assig_Value()
                elif self.Combobox_Dir.get() == "New":
                    os.mkdir(self.DefaultDir)
                    DefaultPath = self.DefaultDir + "\\DefaultPath.txt"
                    fid = open(DefaultPath, "wt")
                    if not os.path.exists(Path + "/Coding_Partner"):
                        os.mkdir(Path + "/Coding_Partner")
                    Path = Path + "/Coding_Partner/"
                    fid.write(Path)#This str should get from UI set
                    fid.close()
                    PathPack.Path.__init__.AbsolutePath = Path
                    PathPack.Path.__init__.Path_Assig_Value()
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
            self.entry_PATH = Entry(self.PathSetUI,width = 60, bd =5)
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
            PathPack.Path.__init__.AbsolutePath = line
            PathPack.Path.__init__.Path_Assig_Value()



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
    entry_query = Entry(frmMain,width = 95, bd =5, fg = 'blue')
    entry_query.grid(row=0, column=3, columnspan = 2)
    button_query = Button(frmMain, text = "query", command = lambda:KeywordQuery(entry_query.get(),Text_result))#tied the entry to the button, when the button is being clicked, function KeywordQuery will be called.
    button_query.grid(row=0, column=5)
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
    entry_query.bind('<KeyRelease>', callback)#<KeyRelease>
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
    KeywordQuery(entry_query.get(), Text_result)#Init
    frmMain.mainloop()






