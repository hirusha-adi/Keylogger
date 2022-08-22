#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#    Aug 22, 2022 12:49:46 PM +0530  platform: Windows NT

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
        self.selectedButton = tk.IntVar()

        self.config_MenuBar()

        self.config_Frame()

        self.config_Email()
        

        self.config_MainInputs()
        

        self.config_RadioButtons()

        self.config_PostWebServer()

        self.Frame1_1_1 = tk.Frame(self.top)
        self.Frame1_1_1.place(relx=0.67, rely=0.375, relheight=0.381
                , relwidth=0.308)
        self.Frame1_1_1.configure(relief='groove')
        self.Frame1_1_1.configure(borderwidth="2")
        self.Frame1_1_1.configure(relief="groove")
        self.Frame1_1_1.configure(background="#1e1e1e")
        self.Frame1_1_1.configure(highlightbackground="#d9d9d9")
        self.Frame1_1_1.configure(highlightcolor="black")

        self.Label1_1_3_2 = tk.Label(self.Frame1_1_1)
        self.Label1_1_3_2.place(relx=0.048, rely=0.052, height=21, width=174)
        self.Label1_1_3_2.configure(activebackground="#f9f9f9")
        self.Label1_1_3_2.configure(anchor='w')
        self.Label1_1_3_2.configure(background="#1e1e1e")
        self.Label1_1_3_2.configure(compound='left')
        self.Label1_1_3_2.configure(disabledforeground="#a3a3a3")
        self.Label1_1_3_2.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label1_1_3_2.configure(foreground="#49b618")
        self.Label1_1_3_2.configure(highlightbackground="#d9d9d9")
        self.Label1_1_3_2.configure(highlightcolor="black")
        self.Label1_1_3_2.configure(text='''Base Filename:''')

        self.Entry1_1_2_1 = tk.Entry(self.Frame1_1_1)
        self.Entry1_1_2_1.place(relx=0.048, rely=0.176, height=30
                , relwidth=0.889)
        self.Entry1_1_2_1.configure(background="#191919")
        self.Entry1_1_2_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1_2_1.configure(font="TkFixedFont")
        self.Entry1_1_2_1.configure(foreground="#ffffff")
        self.Entry1_1_2_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1_2_1.configure(highlightcolor="black")
        self.Entry1_1_2_1.configure(insertbackground="black")
        self.Entry1_1_2_1.configure(selectbackground="#c4c4c4")
        self.Entry1_1_2_1.configure(selectforeground="black")

        self.Label1_1_3_2_1 = tk.Label(self.Frame1_1_1)
        self.Label1_1_3_2_1.place(relx=0.048, rely=0.358, height=20, width=174)
        self.Label1_1_3_2_1.configure(activebackground="#f9f9f9")
        self.Label1_1_3_2_1.configure(anchor='w')
        self.Label1_1_3_2_1.configure(background="#1e1e1e")
        self.Label1_1_3_2_1.configure(compound='left')
        self.Label1_1_3_2_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_3_2_1.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label1_1_3_2_1.configure(foreground="#49b618")
        self.Label1_1_3_2_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_3_2_1.configure(highlightcolor="black")
        self.Label1_1_3_2_1.configure(text='''File Extension:''')

        self.Entry1_1_2_1_1 = tk.Entry(self.Frame1_1_1)
        self.Entry1_1_2_1_1.place(relx=0.048, rely=0.487, height=30
                , relwidth=0.889)
        self.Entry1_1_2_1_1.configure(background="#191919")
        self.Entry1_1_2_1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1_2_1_1.configure(font="TkFixedFont")
        self.Entry1_1_2_1_1.configure(foreground="#ffffff")
        self.Entry1_1_2_1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1_2_1_1.configure(highlightcolor="black")
        self.Entry1_1_2_1_1.configure(insertbackground="black")
        self.Entry1_1_2_1_1.configure(selectbackground="#c4c4c4")
        self.Entry1_1_2_1_1.configure(selectforeground="black")

        self.Label1_1_3_2_1_1 = tk.Label(self.Frame1_1_1)
        self.Label1_1_3_2_1_1.place(relx=0.048, rely=0.668, height=20, width=174)

        self.Label1_1_3_2_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_3_2_1_1.configure(anchor='w')
        self.Label1_1_3_2_1_1.configure(background="#1e1e1e")
        self.Label1_1_3_2_1_1.configure(compound='left')
        self.Label1_1_3_2_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_3_2_1_1.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label1_1_3_2_1_1.configure(foreground="#49b618")
        self.Label1_1_3_2_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_3_2_1_1.configure(highlightcolor="black")
        self.Label1_1_3_2_1_1.configure(text='''Save Format:''')

        self.Radiobutton1_1_2 = tk.Radiobutton(self.Frame1_1_1)
        self.Radiobutton1_1_2.place(relx=0.193, rely=0.798, relheight=0.124
                , relwidth=0.309)
        self.Radiobutton1_1_2.configure(activebackground="beige")
        self.Radiobutton1_1_2.configure(activeforeground="black")
        self.Radiobutton1_1_2.configure(anchor='w')
        self.Radiobutton1_1_2.configure(background="#1e1e1e")
        self.Radiobutton1_1_2.configure(compound='left')
        self.Radiobutton1_1_2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1_1_2.configure(foreground="#49b618")
        self.Radiobutton1_1_2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1_1_2.configure(highlightcolor="black")
        self.Radiobutton1_1_2.configure(justify='left')
        self.Radiobutton1_1_2.configure(selectcolor="#d9d9d9")
        self.Radiobutton1_1_2.configure(text='''TXT''')
        self.Radiobutton1_1_2.configure(variable=self.selectedButton)

        self.Radiobutton1_1_2_1 = tk.Radiobutton(self.Frame1_1_1)
        self.Radiobutton1_1_2_1.place(relx=0.531, rely=0.798, relheight=0.124
                , relwidth=0.309)
        self.Radiobutton1_1_2_1.configure(activebackground="beige")
        self.Radiobutton1_1_2_1.configure(activeforeground="black")
        self.Radiobutton1_1_2_1.configure(anchor='w')
        self.Radiobutton1_1_2_1.configure(background="#1e1e1e")
        self.Radiobutton1_1_2_1.configure(compound='left')
        self.Radiobutton1_1_2_1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1_1_2_1.configure(foreground="#49b618")
        self.Radiobutton1_1_2_1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1_1_2_1.configure(highlightcolor="black")
        self.Radiobutton1_1_2_1.configure(justify='left')
        self.Radiobutton1_1_2_1.configure(selectcolor="#d9d9d9")
        self.Radiobutton1_1_2_1.configure(text='''JSON''')
        self.Radiobutton1_1_2_1.configure(variable=self.selectedButton)

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

        _style_code()
        self.Scrolledtext1 = ScrolledText(self.top)
        self.Scrolledtext1.place(relx=0.015, rely=0.789, relheight=0.193
                , relwidth=0.766)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(foreground="black")
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

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.074, rely=0.02, height=71, width=303)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#1e1e1e")
        self.Label2.configure(compound='left')
        self.Label2.configure(cursor="fleur")
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
        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.015, rely=0.371, relheight=0.381
                , relwidth=0.308)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#1e1e1e")
    
    def config_Email(self):
        self.Label1_1 = tk.Label(self.Frame1)
        self.Label1_1.place(relx=0.048, rely=0.041, height=21, width=174)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(anchor='w')
        self.Label1_1.configure(background="#1e1e1e")
        self.Label1_1.configure(compound='left')
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label1_1.configure(foreground="#49b618")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''from Email:''')
        
        self.Entry1_1 = tk.Entry(self.Frame1)
        self.Entry1_1.place(relx=0.048, rely=0.176, height=30, relwidth=0.889)
        self.Entry1_1.configure(background="#191919")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#ffffff")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="#c4c4c4")
        self.Entry1_1.configure(selectforeground="black")
        
        self.Label1_1_1 = tk.Label(self.Frame1)
        self.Label1_1_1.place(relx=0.048, rely=0.358, height=20, width=174)
        self.Label1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1.configure(anchor='w')
        self.Label1_1_1.configure(background="#1e1e1e")
        self.Label1_1_1.configure(compound='left')
        self.Label1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label1_1_1.configure(foreground="#49b618")
        self.Label1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1.configure(highlightcolor="black")
        self.Label1_1_1.configure(text='''from Password:''')
        
        self.Entry1_1_1 = tk.Entry(self.Frame1)
        self.Entry1_1_1.place(relx=0.048, rely=0.487, height=30, relwidth=0.889)
        self.Entry1_1_1.configure(background="#191919")
        self.Entry1_1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1_1.configure(font="TkFixedFont")
        self.Entry1_1_1.configure(foreground="#ffffff")
        self.Entry1_1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1_1.configure(highlightcolor="black")
        self.Entry1_1_1.configure(insertbackground="black")
        self.Entry1_1_1.configure(selectbackground="#c4c4c4")
        self.Entry1_1_1.configure(selectforeground="black")
        
        self.Label1_1_2 = tk.Label(self.Frame1)
        self.Label1_1_2.place(relx=0.048, rely=0.663, height=21, width=174)
        self.Label1_1_2.configure(activebackground="#f9f9f9")
        self.Label1_1_2.configure(anchor='w')
        self.Label1_1_2.configure(background="#1e1e1e")
        self.Label1_1_2.configure(compound='left')
        self.Label1_1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_1_2.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label1_1_2.configure(foreground="#49b618")
        self.Label1_1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_1_2.configure(highlightcolor="black")
        self.Label1_1_2.configure(text='''to Email:''')

        self.Entry1_1_1_1 = tk.Entry(self.Frame1)
        self.Entry1_1_1_1.place(relx=0.048, rely=0.798, height=30
                , relwidth=0.889)
        self.Entry1_1_1_1.configure(background="#191919")
        self.Entry1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1_1_1.configure(font="TkFixedFont")
        self.Entry1_1_1_1.configure(foreground="#ffffff")
        self.Entry1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1_1_1.configure(highlightcolor="black")
        self.Entry1_1_1_1.configure(insertbackground="black")
        self.Entry1_1_1_1.configure(selectbackground="#c4c4c4")
        self.Entry1_1_1_1.configure(selectforeground="black")
    
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
        self.Label1.configure(cursor="fleur")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label1.configure(foreground="#49b618")
        self.Label1.configure(text='''Executable Name:''')
    
    def config_RadioButtons(self):
        self.Radiobutton1 = tk.Radiobutton(self.top)
        self.Radiobutton1.place(relx=0.089, rely=0.302, relheight=0.059
                , relwidth=0.155)
        self.Radiobutton1.configure(activebackground="beige")
        self.Radiobutton1.configure(activeforeground="black")
        self.Radiobutton1.configure(anchor='w')
        self.Radiobutton1.configure(background="#1e1e1e")
        self.Radiobutton1.configure(compound='left')
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#49b618")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(selectcolor="#d9d9d9")
        self.Radiobutton1.configure(text='''Send via Email''')
        self.Radiobutton1.configure(variable=self.selectedButton)

        self.Radiobutton1_1 = tk.Radiobutton(self.top)
        self.Radiobutton1_1.place(relx=0.759, rely=0.302, relheight=0.059
                , relwidth=0.155)
        self.Radiobutton1_1.configure(activebackground="beige")
        self.Radiobutton1_1.configure(activeforeground="black")
        self.Radiobutton1_1.configure(anchor='w')
        self.Radiobutton1_1.configure(background="#1e1e1e")
        self.Radiobutton1_1.configure(compound='left')
        self.Radiobutton1_1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1_1.configure(foreground="#49b618")
        self.Radiobutton1_1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1_1.configure(highlightcolor="black")
        self.Radiobutton1_1.configure(justify='left')
        self.Radiobutton1_1.configure(selectcolor="#d9d9d9")
        self.Radiobutton1_1.configure(text='''Save to File''')
        self.Radiobutton1_1.configure(variable=self.selectedButton)

        self.Radiobutton1_1_1 = tk.Radiobutton(self.top)
        self.Radiobutton1_1_1.place(relx=0.387, rely=0.302, relheight=0.059
                , relwidth=0.217)
        self.Radiobutton1_1_1.configure(activebackground="beige")
        self.Radiobutton1_1_1.configure(activeforeground="black")
        self.Radiobutton1_1_1.configure(anchor='w')
        self.Radiobutton1_1_1.configure(background="#1e1e1e")
        self.Radiobutton1_1_1.configure(compound='left')
        self.Radiobutton1_1_1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1_1_1.configure(foreground="#49b618")
        self.Radiobutton1_1_1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1_1_1.configure(highlightcolor="black")
        self.Radiobutton1_1_1.configure(justify='left')
        self.Radiobutton1_1_1.configure(selectcolor="#d9d9d9")
        self.Radiobutton1_1_1.configure(text='''POST to Web Server''')
        self.Radiobutton1_1_1.configure(variable=self.selectedButton)
    
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
        self.Entry1_1_1_2.configure(cursor="fleur")
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




