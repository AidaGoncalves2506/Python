 # -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import csv
import hashlib

#funçao pra sair 
def close_window():
    janela.destroy()  
    close_button.configure(bg='white',fg='Purple') 
   
def mostrarapp():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        mostrarpp_button.config(text='Mostrar Palavra-Passe')
    else:
        password_entry.config(show='')
        mostrarpp_button.config(text='Esconder Palavra-Passe')  
        
def voltar():
    import menuprincipal 
    
def informacoes():
    entuser=utilizador_entry.get()
    entpp=password_entry.get()
    
    email = []
    pp = []
    
    with open('csv.csv', 'r') as file:
        reader = csv.reader(file)
        
        for lines in reader:
            email.append(lines[0])
            pp.append(lines[1])        
        
        if entuser == email[0] and entpp== pp[0]:
            label3.config(text="Iniciou sessão com sucesso",fg='purple')
            label3.config(font=['Garamond',12])
        else:
            label3.config(text="Erro ao iniciar sessão, por favor tente novamente.",fg='purple')
            label3.config(font=['Garamond',12])
            
#nao to a perceber nd disto 
        
    pass_encriptada = hashlib.sha1(entpp.encode())

    print("Password: " , entpp)
    print("Hash:", pass_encriptada.hexdigest())

    verificar_pass = input("Password: ")
    verificar_pass = hashlib.sha1(verificar_pass.encode())

    if pass_encriptada.hexdigest() == verificar_pass.hexdigest():
        print("Sucesso")
    else:
        print("Insucesso")

#criar a janela   
janela = tk.Tk()
janela.title("<3 Login <3")

#frase
label1=tk.Label(janela,text="Inicio de sessão em Purplefy",fg='Purple')
label1.grid(columnspan=2)
label1.config(font=['Garamond',12])

#criar o espaço para o utilizador
utilizador_label=tk.Label(janela,text="Utilizador: ",fg='purple')
utilizador_label.grid(row=2,column=0,padx=5,pady=5)
utilizador_label.config(font=['Garamond',12])
utilizador_entry=tk.Entry(janela)
utilizador_entry.grid(row=2,column=1,padx=5,pady=5)

#criar o espaço para inserir a password
password_label=tk.Label(janela,text="Palavra-passe: ",fg='Purple')
password_label.grid(row=3,column=0,padx=5,pady=5)
password_label.config(font=['Garamond',12])
password_entry=tk.Entry(janela)
password_entry.grid(row=3,column=1,padx=5,pady=5)
password_entry.config(show='*')

label3=tk.Label(janela,text="")
label3.grid(row=4,columnspan=2)

#botao para continuar
login_button =tk.Button(janela,text="Login", fg='Purple', bg='white',command=informacoes)
login_button.grid(columnspan=2,row=5)
login_button.config(font=['Garamond',10],width=10)
 
#botao para voltar para o menu inicial
registro_button =tk.Button(janela,text="Voltar para o menu principal", fg='Purple', bg='white',command=voltar)
registro_button.grid(columnspan=2,row=6)
registro_button.config(font=['Garamond',10],width=22)
   
# botao para fechar janela
close_button = tk.Button(janela,text="Fechar",fg='Purple',bg='white', command= close_window)
close_button.grid(columnspan=2,row=7)
close_button.config(font=['Garamond',10],width=10)

#botao para mostrar palavra-passe
mostrarpp_button =tk.Button(janela,text="Mostrar Palavra-passe", bg='white',fg='Purple',width=15,command=mostrarapp)
mostrarpp_button.grid(row=3,column=2,padx=5,pady=5)
mostrarpp_button.config(font=['Garamond',10])

    
#executar em loop
tk.mainloop()