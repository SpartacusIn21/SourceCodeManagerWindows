from distutils.core import setup
import py2exe
#from glob import glob
#import sys
#sys.argv.append('py2exe')
#data_files = [("Microsoft.VC100.CRT", glob(r'C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\redist\x86\Microsoft.VC100.CRT\*.*')),
#("Microsoft.VC90.CRT", glob(r'C:\Program Files (x86)\Common Files\Microsoft Shared\VSTO\10.0\*.*'))]
#sys.path.append("C:\\Program Files (x86)\\Microsoft Visual Studio 10.0\\VC\\redist\\x86\\Microsoft.VC100.CRT")
#sys.path.append("C:\\Program Files (x86)\\Common Files\\Microsoft Shared\\VSTO\\10.0")
#setup(data_files=data_files,
setup(console=["monitor_process_ex_py3.py"],
options = { "py2exe": { "dll_excludes": ["msvcr71.dll","IPHLPAPI.DLL","NSI.dll","WINNSI.DLL","WTSAPI32.dll"] } })

