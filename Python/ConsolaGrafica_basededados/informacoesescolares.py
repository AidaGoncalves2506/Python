 # -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import hashlib
import mysql.connector 
banana = mysql.connector.connect(host="localhost", user="root", password="", database="pauta_escola")
cursor=banana.cursor()


#funçao pra sair 
def close_window():
    janela.destroy()  
    close_button.configure() 
    
    




#para poder inicializar o prog
tk.mainloop()
