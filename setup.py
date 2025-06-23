import cx_Freeze
import sys
import os
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\hp\AppData\Local\Programs\Python\Python311\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\hp\AppData\Local\Programs\Python\Python311\tcl\tk8.6"

executables = [cx_Freeze.Executable("main.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name = "Facial Recognition Attendence Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'image','data','database','attendence report']}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace System | Developed By Coderkk",
    executables = executables
    )
