#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
#   GUI module generated by PAGE version 7.5
#   in conjunction with Tcl version 8.6
# 

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import keylogger_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='TkDefaultFont')
    style.map('.',background = [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground = [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground = [('selected', 'black'), ('active','black')])
    style.configure('Vertical.TScrollbar',  background=_bgcolor, arrowcolor= _fgcolor)
    style.configure('Horizontal.TScrollbar',  background=_bgcolor, arrowcolor= _fgcolor)
    _style_code_ran = 1

class Toplevel1:
    def __init__(self, top=None):

        top.geometry("672x507+583+374")
        top.minsize(120, 1)
        top.maxsize(4644, 1161)
        top.resizable(1,  1)
        top.title("Keylogger v2 - by @hirushaadi")
        top.configure(background="#1e1e1e")

        self.top = top
        self.selected_ReportMode = tk.IntVar()
        self.selected_SaveFileFormat = tk.IntVar()
        
        self.selected_ReportMode.set(1)
        self.selected_SaveFileFormat.set(1)

        self.config_MenuBar() # menu bar
        self.config_Topic() # topic
        self.config_Frame() # main frame, has everything
        self.config_MainInputs() # required inputs
        self.config_RadioButtons() # radio buttons (select 1 option)
        self.config_Email() # email config
        self.config_PostWebServer() # post to web server config
        self.config_File() # save to file config
        self.config_Bottom() # log, build and clear log buttons

        _style_code()
        
    def config_MenuBar(self):
        self.menubar = tk.Menu(self.top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        self.top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(self.top, activebackground='beige', activeborderwidth=1
                ,activeforeground='black', background='#d9d9d9', borderwidth=1
                ,disabledforeground='#a3a3a3', foreground='#000000', tearoff=0)
        self.menubar.add_cascade(compound='left', label='Menu', menu=self.sub_menu
                ,)
        self.sub_menu.add_command(compound='left',label='Save')
        self.sub_menu.add_command(compound='left',label='Build')
        self.sub_menu1 = tk.Menu(self.top, activebackground='beige'
                ,activeborderwidth=1, activeforeground='black'
                ,background='#d9d9d9', borderwidth=1, disabledforeground='#a3a3a3'
                ,foreground='#000000', tearoff=0)
        self.menubar.add_cascade(compound='left', label='Actions'
                ,menu=self.sub_menu1, )
        self.sub_menu1.add_command(compound='left',label='Build')
        self.sub_menu1.add_separator()
        self.sub_menu1.add_command(compound='left',label='Reset')
        self.sub_menu12 = tk.Menu(self.top, activebackground='beige'
                ,activeborderwidth=1, activeforeground='black'
                ,background='#d9d9d9', borderwidth=1, disabledforeground='#a3a3a3'
                ,foreground='#000000', tearoff=0)
        self.menubar.add_cascade(compound='left', label='Other'
                ,menu=self.sub_menu12, )
        self.sub_menu12.add_command(compound='left',label='Source Code')
        self.sub_menu12.add_command(compound='left',label='About')
        self.sub_menu12.add_command(compound='left',label='Help') 
    
    def config_Frame(self):
        self.f_Main = tk.Frame(self.top)
        self.f_Main.place(relx=0.015, rely=0.371, relheight=0.381
                , relwidth=0.308)
        self.f_Main.configure(relief='groove')
        self.f_Main.configure(borderwidth="2")
        self.f_Main.configure(relief="groove")
        self.f_Main.configure(background="#1e1e1e")
    
    def config_Email(self):
        self.l_FromEmail = tk.Label(self.f_Main)
        self.l_FromEmail.place(relx=0.048, rely=0.041, height=21, width=174)
        self.l_FromEmail.configure(activebackground="#f9f9f9")
        self.l_FromEmail.configure(anchor='w')
        self.l_FromEmail.configure(background="#1e1e1e")
        self.l_FromEmail.configure(compound='left')
        self.l_FromEmail.configure(disabledforeground="#a3a3a3")
        self.l_FromEmail.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.l_FromEmail.configure(foreground="#49b618")
        self.l_FromEmail.configure(highlightbackground="#d9d9d9")
        self.l_FromEmail.configure(highlightcolor="black")
        self.l_FromEmail.configure(text='''from Email:''')
        
        self.e_FromEmail = tk.Entry(self.f_Main)
        self.e_FromEmail.place(relx=0.048, rely=0.176, height=30, relwidth=0.889)
        self.e_FromEmail.configure(background="#191919")
        self.e_FromEmail.configure(disabledforeground="#a3a3a3")
        self.e_FromEmail.configure(font="TkFixedFont")
        self.e_FromEmail.configure(foreground="#ffffff")
        self.e_FromEmail.configure(highlightbackground="#d9d9d9")
        self.e_FromEmail.configure(highlightcolor="black")
        self.e_FromEmail.configure(insertbackground="black")
        self.e_FromEmail.configure(selectbackground="#c4c4c4")
        self.e_FromEmail.configure(selectforeground="black")
        
        self.l_FromPassword = tk.Label(self.f_Main)
        self.l_FromPassword.place(relx=0.048, rely=0.358, height=20, width=174)
        self.l_FromPassword.configure(activebackground="#f9f9f9")
        self.l_FromPassword.configure(anchor='w')
        self.l_FromPassword.configure(background="#1e1e1e")
        self.l_FromPassword.configure(compound='left')
        self.l_FromPassword.configure(disabledforeground="#a3a3a3")
        self.l_FromPassword.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.l_FromPassword.configure(foreground="#49b618")
        self.l_FromPassword.configure(highlightbackground="#d9d9d9")
        self.l_FromPassword.configure(highlightcolor="black")
        self.l_FromPassword.configure(text='''from Password:''')
        
        self.e_FromPassword = tk.Entry(self.f_Main)
        self.e_FromPassword.place(relx=0.048, rely=0.487, height=30, relwidth=0.889)
        self.e_FromPassword.configure(background="#191919")
        self.e_FromPassword.configure(disabledforeground="#a3a3a3")
        self.e_FromPassword.configure(font="TkFixedFont")
        self.e_FromPassword.configure(foreground="#ffffff")
        self.e_FromPassword.configure(highlightbackground="#d9d9d9")
        self.e_FromPassword.configure(highlightcolor="black")
        self.e_FromPassword.configure(insertbackground="black")
        self.e_FromPassword.configure(selectbackground="#c4c4c4")
        self.e_FromPassword.configure(selectforeground="black")
        
        self.l_ToEmail = tk.Label(self.f_Main)
        self.l_ToEmail.place(relx=0.048, rely=0.663, height=21, width=174)
        self.l_ToEmail.configure(activebackground="#f9f9f9")
        self.l_ToEmail.configure(anchor='w')
        self.l_ToEmail.configure(background="#1e1e1e")
        self.l_ToEmail.configure(compound='left')
        self.l_ToEmail.configure(disabledforeground="#a3a3a3")
        self.l_ToEmail.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.l_ToEmail.configure(foreground="#49b618")
        self.l_ToEmail.configure(highlightbackground="#d9d9d9")
        self.l_ToEmail.configure(highlightcolor="black")
        self.l_ToEmail.configure(text='''to Email:''')

        self.e_ToEmail = tk.Entry(self.f_Main)
        self.e_ToEmail.place(relx=0.048, rely=0.798, height=30
                , relwidth=0.889)
        self.e_ToEmail.configure(background="#191919")
        self.e_ToEmail.configure(disabledforeground="#a3a3a3")
        self.e_ToEmail.configure(font="TkFixedFont")
        self.e_ToEmail.configure(foreground="#ffffff")
        self.e_ToEmail.configure(highlightbackground="#d9d9d9")
        self.e_ToEmail.configure(highlightcolor="black")
        self.e_ToEmail.configure(insertbackground="black")
        self.e_ToEmail.configure(selectbackground="#c4c4c4")
        self.e_ToEmail.configure(selectforeground="black")
    
    def config_MainInputs(self):
        self.Entry1 = tk.Entry(self.top)
        self.Entry1.place(relx=0.58, rely=0.061, height=30, relwidth=0.348)
        self.Entry1.configure(background="#191919")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#ffffff")
        self.Entry1.configure(insertbackground="black")

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.58, rely=0.02, height=25, width=174)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#1e1e1e")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label1.configure(foreground="#49b618")
        self.Label1.configure(text='''Executable Name:''')
        
        self.Label1_2 = tk.Label(self.top)
        self.Label1_2.place(relx=0.58, rely=0.164, height=24, width=174)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(anchor='w')
        self.Label1_2.configure(background="#1e1e1e")
        self.Label1_2.configure(compound='left')
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label1_2.configure(foreground="#49b618")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''Send Interval (seconds):''')

        self.Entry1_2 = tk.Entry(self.top)
        self.Entry1_2.place(relx=0.58, rely=0.203, height=30, relwidth=0.348)
        self.Entry1_2.configure(background="#191919")
        self.Entry1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2.configure(font="TkFixedFont")
        self.Entry1_2.configure(foreground="#ffffff")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="#c4c4c4")
        self.Entry1_2.configure(selectforeground="black")
    
    def config_RadioButtons(self):
        self.rb_SendEmail = tk.Radiobutton(self.top)
        self.rb_SendEmail.place(relx=0.089, rely=0.302, relheight=0.059
                , relwidth=0.155)
        self.rb_SendEmail.configure(activebackground="beige")
        self.rb_SendEmail.configure(activeforeground="black")
        self.rb_SendEmail.configure(anchor='w')
        self.rb_SendEmail.configure(background="#1e1e1e")
        self.rb_SendEmail.configure(compound='left')
        self.rb_SendEmail.configure(disabledforeground="#a3a3a3")
        self.rb_SendEmail.configure(foreground="#49b618")
        self.rb_SendEmail.configure(highlightbackground="#d9d9d9")
        self.rb_SendEmail.configure(highlightcolor="black")
        self.rb_SendEmail.configure(justify='left')
        self.rb_SendEmail.configure(selectcolor="#d9d9d9")
        self.rb_SendEmail.configure(text='''Send via Email''')
        self.rb_SendEmail.configure(variable=self.selected_ReportMode)
        self.rb_SendEmail.configure(value=1)

        self.rb_SaveFile = tk.Radiobutton(self.top)
        self.rb_SaveFile.place(relx=0.759, rely=0.302, relheight=0.059
                , relwidth=0.155)
        self.rb_SaveFile.configure(activebackground="beige")
        self.rb_SaveFile.configure(activeforeground="black")
        self.rb_SaveFile.configure(anchor='w')
        self.rb_SaveFile.configure(background="#1e1e1e")
        self.rb_SaveFile.configure(compound='left')
        self.rb_SaveFile.configure(disabledforeground="#a3a3a3")
        self.rb_SaveFile.configure(foreground="#49b618")
        self.rb_SaveFile.configure(highlightbackground="#d9d9d9")
        self.rb_SaveFile.configure(highlightcolor="black")
        self.rb_SaveFile.configure(justify='left')
        self.rb_SaveFile.configure(selectcolor="#d9d9d9")
        self.rb_SaveFile.configure(text='''Save to File''')
        self.rb_SaveFile.configure(variable=self.selected_ReportMode)
        self.rb_SaveFile.configure(value=2)

        self.rb_PostWeb = tk.Radiobutton(self.top)
        self.rb_PostWeb.place(relx=0.387, rely=0.302, relheight=0.059
                , relwidth=0.217)
        self.rb_PostWeb.configure(activebackground="beige")
        self.rb_PostWeb.configure(activeforeground="black")
        self.rb_PostWeb.configure(anchor='w')
        self.rb_PostWeb.configure(background="#1e1e1e")
        self.rb_PostWeb.configure(compound='left')
        self.rb_PostWeb.configure(disabledforeground="#a3a3a3")
        self.rb_PostWeb.configure(foreground="#49b618")
        self.rb_PostWeb.configure(highlightbackground="#d9d9d9")
        self.rb_PostWeb.configure(highlightcolor="black")
        self.rb_PostWeb.configure(justify='left')
        self.rb_PostWeb.configure(selectcolor="#d9d9d9")
        self.rb_PostWeb.configure(text='''POST to Web Server''')
        self.rb_PostWeb.configure(variable=self.selected_ReportMode)
        self.rb_PostWeb.configure(value=3)
    
    def config_PostWebServer(self):
        self.Frame1_1 = tk.Frame(self.top)
        self.Frame1_1.place(relx=0.342, rely=0.371, relheight=0.381
                , relwidth=0.308)
        self.Frame1_1.configure(relief='groove')
        self.Frame1_1.configure(borderwidth="2")
        self.Frame1_1.configure(relief="groove")
        self.Frame1_1.configure(background="#1e1e1e")
        self.Frame1_1.configure(highlightbackground="#d9d9d9")
        self.Frame1_1.configure(highlightcolor="black")

        self.Label1_1_3 = tk.Label(self.Frame1_1)
        self.Label1_1_3.place(relx=0.048, rely=0.041, height=21, width=174)
        self.Label1_1_3.configure(activebackground="#f9f9f9")
        self.Label1_1_3.configure(anchor='w')
        self.Label1_1_3.configure(background="#1e1e1e")
        self.Label1_1_3.configure(compound='left')
        self.Label1_1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_1_3.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label1_1_3.configure(foreground="#49b618")
        self.Label1_1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_1_3.configure(highlightcolor="black")
        self.Label1_1_3.configure(text='''Endpoint URL:''')

        self.Entry1_1_2 = tk.Entry(self.Frame1_1)
        self.Entry1_1_2.place(relx=0.048, rely=0.176, height=30, relwidth=0.889)
        self.Entry1_1_2.configure(background="#191919")
        self.Entry1_1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_1_2.configure(font="TkFixedFont")
        self.Entry1_1_2.configure(foreground="#ffffff")
        self.Entry1_1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_1_2.configure(highlightcolor="black")
        self.Entry1_1_2.configure(insertbackground="black")
        self.Entry1_1_2.configure(selectbackground="#c4c4c4")
        self.Entry1_1_2.configure(selectforeground="black")

        self.Label1_1_3_1 = tk.Label(self.Frame1_1)
        self.Label1_1_3_1.place(relx=0.048, rely=0.358, height=20, width=174)
        self.Label1_1_3_1.configure(activebackground="#f9f9f9")
        self.Label1_1_3_1.configure(anchor='w')
        self.Label1_1_3_1.configure(background="#1e1e1e")
        self.Label1_1_3_1.configure(compound='left')
        self.Label1_1_3_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_3_1.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label1_1_3_1.configure(foreground="#49b618")
        self.Label1_1_3_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_3_1.configure(highlightcolor="black")
        self.Label1_1_3_1.configure(text='''Parameter Name:''')

        self.Entry1_1_1_2 = tk.Entry(self.Frame1_1)
        self.Entry1_1_1_2.place(relx=0.048, rely=0.487, height=30
                , relwidth=0.889)
        self.Entry1_1_1_2.configure(background="#191919")
        self.Entry1_1_1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_1_1_2.configure(font="TkFixedFont")
        self.Entry1_1_1_2.configure(foreground="#ffffff")
        self.Entry1_1_1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_1_1_2.configure(highlightcolor="black")
        self.Entry1_1_1_2.configure(insertbackground="black")
        self.Entry1_1_1_2.configure(selectbackground="#c4c4c4")
        self.Entry1_1_1_2.configure(selectforeground="black")

        self.Label1_1_3_1_1 = tk.Label(self.Frame1_1)
        self.Label1_1_3_1_1.place(relx=0.048, rely=0.668, height=20, width=174)
        self.Label1_1_3_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_3_1_1.configure(anchor='w')
        self.Label1_1_3_1_1.configure(background="#1e1e1e")
        self.Label1_1_3_1_1.configure(compound='left')
        self.Label1_1_3_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_3_1_1.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label1_1_3_1_1.configure(foreground="#49b618")
        self.Label1_1_3_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_3_1_1.configure(highlightcolor="black")
        self.Label1_1_3_1_1.configure(text='''Expected Result:''')

        self.Entry1_1_1_2_1 = tk.Entry(self.Frame1_1)
        self.Entry1_1_1_2_1.place(relx=0.048, rely=0.798, height=30
                , relwidth=0.889)
        self.Entry1_1_1_2_1.configure(background="#191919")
        self.Entry1_1_1_2_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1_1_2_1.configure(font="TkFixedFont")
        self.Entry1_1_1_2_1.configure(foreground="#ffffff")
        self.Entry1_1_1_2_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1_1_2_1.configure(highlightcolor="black")
        self.Entry1_1_1_2_1.configure(insertbackground="black")
        self.Entry1_1_1_2_1.configure(selectbackground="#c4c4c4")
        self.Entry1_1_1_2_1.configure(selectforeground="black")
    
    def config_File(self):
        self.f_SaveFile = tk.Frame(self.top)
        self.f_SaveFile.place(relx=0.67, rely=0.375, relheight=0.381
                , relwidth=0.308)
        self.f_SaveFile.configure(relief='groove')
        self.f_SaveFile.configure(borderwidth="2")
        self.f_SaveFile.configure(relief="groove")
        self.f_SaveFile.configure(background="#1e1e1e")
        self.f_SaveFile.configure(highlightbackground="#d9d9d9")
        self.f_SaveFile.configure(highlightcolor="black")

        self.l_BaseFilename = tk.Label(self.f_SaveFile)
        self.l_BaseFilename.place(relx=0.048, rely=0.052, height=21, width=174)
        self.l_BaseFilename.configure(activebackground="#f9f9f9")
        self.l_BaseFilename.configure(anchor='w')
        self.l_BaseFilename.configure(background="#1e1e1e")
        self.l_BaseFilename.configure(compound='left')
        self.l_BaseFilename.configure(disabledforeground="#a3a3a3")
        self.l_BaseFilename.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.l_BaseFilename.configure(foreground="#49b618")
        self.l_BaseFilename.configure(highlightbackground="#d9d9d9")
        self.l_BaseFilename.configure(highlightcolor="black")
        self.l_BaseFilename.configure(text='''Base Filename:''')

        self.e_BaseFilename = tk.Entry(self.f_SaveFile)
        self.e_BaseFilename.place(relx=0.048, rely=0.176, height=30
                , relwidth=0.889)
        self.e_BaseFilename.configure(background="#191919")
        self.e_BaseFilename.configure(disabledforeground="#a3a3a3")
        self.e_BaseFilename.configure(font="TkFixedFont")
        self.e_BaseFilename.configure(foreground="#ffffff")
        self.e_BaseFilename.configure(highlightbackground="#d9d9d9")
        self.e_BaseFilename.configure(highlightcolor="black")
        self.e_BaseFilename.configure(insertbackground="black")
        self.e_BaseFilename.configure(selectbackground="#c4c4c4")
        self.e_BaseFilename.configure(selectforeground="black")

        self.l_FileExtension = tk.Label(self.f_SaveFile)
        self.l_FileExtension.place(relx=0.048, rely=0.358, height=20, width=174)
        self.l_FileExtension.configure(activebackground="#f9f9f9")
        self.l_FileExtension.configure(anchor='w')
        self.l_FileExtension.configure(background="#1e1e1e")
        self.l_FileExtension.configure(compound='left')
        self.l_FileExtension.configure(disabledforeground="#a3a3a3")
        self.l_FileExtension.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.l_FileExtension.configure(foreground="#49b618")
        self.l_FileExtension.configure(highlightbackground="#d9d9d9")
        self.l_FileExtension.configure(highlightcolor="black")
        self.l_FileExtension.configure(text='''File Extension:''')

        self.e_FileExtension = tk.Entry(self.f_SaveFile)
        self.e_FileExtension.place(relx=0.048, rely=0.487, height=30
                , relwidth=0.889)
        self.e_FileExtension.configure(background="#191919")
        self.e_FileExtension.configure(disabledforeground="#a3a3a3")
        self.e_FileExtension.configure(font="TkFixedFont")
        self.e_FileExtension.configure(foreground="#ffffff")
        self.e_FileExtension.configure(highlightbackground="#d9d9d9")
        self.e_FileExtension.configure(highlightcolor="black")
        self.e_FileExtension.configure(insertbackground="black")
        self.e_FileExtension.configure(selectbackground="#c4c4c4")
        self.e_FileExtension.configure(selectforeground="black")

        self.l_SaveFormat = tk.Label(self.f_SaveFile)
        self.l_SaveFormat.place(relx=0.048, rely=0.668, height=20, width=174)

        self.l_SaveFormat.configure(activebackground="#f9f9f9")
        self.l_SaveFormat.configure(anchor='w')
        self.l_SaveFormat.configure(background="#1e1e1e")
        self.l_SaveFormat.configure(compound='left')
        self.l_SaveFormat.configure(disabledforeground="#a3a3a3")
        self.l_SaveFormat.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.l_SaveFormat.configure(foreground="#49b618")
        self.l_SaveFormat.configure(highlightbackground="#d9d9d9")
        self.l_SaveFormat.configure(highlightcolor="black")
        self.l_SaveFormat.configure(text='''Save Format:''')

        self.rb_SaveFileTXT = tk.Radiobutton(self.f_SaveFile)
        self.rb_SaveFileTXT.place(relx=0.193, rely=0.798, relheight=0.124
                , relwidth=0.309)
        self.rb_SaveFileTXT.configure(activebackground="beige")
        self.rb_SaveFileTXT.configure(activeforeground="black")
        self.rb_SaveFileTXT.configure(anchor='w')
        self.rb_SaveFileTXT.configure(background="#1e1e1e")
        self.rb_SaveFileTXT.configure(compound='left')
        self.rb_SaveFileTXT.configure(disabledforeground="#a3a3a3")
        self.rb_SaveFileTXT.configure(foreground="#49b618")
        self.rb_SaveFileTXT.configure(highlightbackground="#d9d9d9")
        self.rb_SaveFileTXT.configure(highlightcolor="black")
        self.rb_SaveFileTXT.configure(justify='left')
        self.rb_SaveFileTXT.configure(selectcolor="#d9d9d9")
        self.rb_SaveFileTXT.configure(text='''TXT''')
        self.rb_SaveFileTXT.configure(variable=self.selected_SaveFileFormat)
        self.rb_SaveFileTXT.configure(value=1)

        self.rb_SaveFileJSON = tk.Radiobutton(self.f_SaveFile)
        self.rb_SaveFileJSON.place(relx=0.531, rely=0.798, relheight=0.124
                , relwidth=0.309)
        self.rb_SaveFileJSON.configure(activebackground="beige")
        self.rb_SaveFileJSON.configure(activeforeground="black")
        self.rb_SaveFileJSON.configure(anchor='w')
        self.rb_SaveFileJSON.configure(background="#1e1e1e")
        self.rb_SaveFileJSON.configure(compound='left')
        self.rb_SaveFileJSON.configure(disabledforeground="#a3a3a3")
        self.rb_SaveFileJSON.configure(foreground="#49b618")
        self.rb_SaveFileJSON.configure(highlightbackground="#d9d9d9")
        self.rb_SaveFileJSON.configure(highlightcolor="black")
        self.rb_SaveFileJSON.configure(justify='left')
        self.rb_SaveFileJSON.configure(selectcolor="#d9d9d9")
        self.rb_SaveFileJSON.configure(text='''JSON''')
        self.rb_SaveFileJSON.configure(variable=self.selected_SaveFileFormat)
        self.rb_SaveFileJSON.configure(value=2)

    def config_Topic(self):
        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.074, rely=0.02, height=71, width=303)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#1e1e1e")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 36 -weight bold -slant italic")
        self.Label2.configure(foreground="#00ff00")
        self.Label2.configure(text='''Keylogger v2''')

        self.Label2_1 = tk.Label(self.top)
        self.Label2_1.place(relx=0.179, rely=0.158, height=41, width=164)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(anchor='w')
        self.Label2_1.configure(background="#1e1e1e")
        self.Label2_1.configure(compound='left')
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font="-family {Segoe UI} -size 16 -weight bold -slant italic")
        self.Label2_1.configure(foreground="#00ff00")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''by @hirushaadi''')
    
    def config_Bottom(self):
        self.Scrolledtext1 = ScrolledText(self.top)
        self.Scrolledtext1.place(relx=0.015, rely=0.789, relheight=0.193
                , relwidth=0.766)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(foreground="#00ff00")
        self.Scrolledtext1.configure(background="#191919")
        self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext1.configure(highlightcolor="black")
        self.Scrolledtext1.configure(insertbackground="black")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(selectforeground="black")
        self.Scrolledtext1.configure(wrap="none")

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.804, rely=0.789, height=54, width=117)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#191919")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#00ff00")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Build''')

        self.Button2 = tk.Button(self.top)
        self.Button2.place(relx=0.804, rely=0.907, height=34, width=117)
        self.Button2.configure(activebackground="beige")
        self.Button2.configure(activeforeground="black")
        self.Button2.configure(background="#191919")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#00ff00")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Clear Log''')
        self.Button2.configure(command=self.a_ClearLog)

    def a_ClearLog(self):
        self.Scrolledtext1.delete('1.0', END)
    
    def get_Email(self):
        FromEmail = self.e_FromEmail.get()
        FromPassword = self.e_FromPassword.get()
        ToEmail = self.e_ToEmail.get()
    
# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

def start_up():
    keylogger_support.main()

if __name__ == '__main__':
    keylogger_support.main()

