import tkinter as tk
from tkinter import *
import csv
import hashlib

def login():
    import LoginNoTkinterAida
    
def registro():
    import Aidaregistro
    
    
#funçao pra sair 
def close_window():
    janela.destroy()  
    close_button.configure(bg='white',fg='Purple') 
    
#criar a janela   
janela = tk.Tk()
janela.title("<3 Menu Principal <3")
    
#criar a label
label = tk.Label(janela, text="Bem vindo ao Purplefy! <3 ", width=100, fg='purple')
label.grid(columnspan=2) 
label.config(font=['Garamond',15])

label2=tk.Label(janela,text=" A melhor plataforma de streaming de música, subscreva-se já! ", fg='Purple')
label2.grid(columnspan=2)
label2.config(font=['Garamond',12])

label2=tk.Label(janela,text=" Deseja: ", fg='Purple')
label2.grid(columnspan=2)
label2.config(font=['Garamond',12])
#botao para continuar
login_button =tk.Button(janela,text="Iniciar sessão", fg='Purple', bg='white', command=login)
login_button.grid(columnspan=2)
login_button.config(font=['Garamond',10],width=10)

registro_button=tk.Button(janela,text="Registro",fg='Purple',bg='White',command=registro)
registro_button.grid(columnspan=2)
registro_button.config(font=['Garamond',10],width=10)

label3=tk.Label(janela,text="")
label3.grid(row=10,columnspan=2)


# botao para fechar janela
close_button = tk.Button(janela,text="Fechar",fg='Purple',bg='white', command= close_window)
close_button.grid(columnspan=2,row=6)
close_button.config(font=['Garamond',10],width=10)
tk.mainloop()
    