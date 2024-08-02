# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import datetime
from datetime import datetime

tk =Tk()

btn_1=Button(tk,text="Linha 0, Coluna 0 ")
btn_1.grid(row=0,column=0,padx=5,pady=5)

btn_2=Button(tk,text="Linha 0, Coluna 1 ")
btn_2.grid(row=0,column=1,padx=5,pady=5)

btn_3=Button(tk,text="Linha 1, Coluna 0")
btn_3.grid(row=1,column=0,padx=5,pady=5)

btn_4=Button(tk,text="Linha 1, Coluna 1")
btn_4.grid(row=1,column=1,padx=5,pady=5)

btn_5=Button(tk,text="Linha 2, Coluna 0")
btn_5.grid(row=2,column=0,padx=5,pady=5)
btn_6=Button(tk,text="Linha 2, Coluna 1")
btn_6.grid(row=2,column=1,padx=5,pady=5)

btn_7=Button(tk,text="dkwgf",padx=5,pady=5,bg='yellow')
btn_7.grid(columnspan=2)
#sem variavel
Button(tk,text="Botãozinho").grid(row=2,column=4,padx=5,pady=5)


label_1= Label(text="VIOLETA",relief=RIDGE,width=10,bg='violet').grid(row=5,column=5)
tk.mainloop()