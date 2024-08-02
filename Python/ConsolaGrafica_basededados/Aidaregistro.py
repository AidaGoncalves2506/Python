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

def novoregistro():
    entuser=utilizador_entry.get()
    entpp=password_entry.get() ####

    em=[] 
    saveinfo=[]

    file = open("csv.csv", "r")
    reader = csv.reader(file) 
        
    for lines in reader:
        em.append(lines[0])
            
    if entuser in em:
        print("este user já existe")
        label4=tk.Label(janela,text="Este username já existe, crie outro!",fg='Purple')
        label4.grid(columnspan=2)
        label4.config(font=['Garamond',12])
        
    else:
        print("user autorizado")
        label4=tk.Label(janela,text="Username aceite!",fg='Purple')
        label4.grid(columnspan=2)
        label4.config(font=['Garamond',12])
        
        saveinfo=[entuser,entpp]
        
        with open("csv.csv", "a+", newline="") as file:

            write=csv.writer(file)
            write.writerow(saveinfo)
            
 
                        
#criar a janela   
janela = tk.Tk()
janela.title("<3 Registro <3")          
          
#criar labels
label1=tk.Label(janela,text="Registro em Purplefy!",fg='Purple')
label1.grid(columnspan=2)
label1.config(font=['Garamond',12])

label2=tk.Label(janela,text="Escolha o seu username e a sua palavra-passe!",fg='Purple')
label2.grid(columnspan=2)
label2.config(font=['Garamond',12])
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

#botao para registrar
registro_button =tk.Button(janela,text="Registrar-me", fg='Purple', bg='white',command=novoregistro)
registro_button.grid(column=1,row=5)
registro_button.config(font=['Garamond',10],width=10)

#botao para voltar para o menu inicial
registro_button =tk.Button(janela,text="Voltar para o menu principal", fg='Purple', bg='white',command=voltar)
registro_button.grid(column=1,row=6)
registro_button.config(font=['Garamond',10],width=22)

# botao para fechar janela
close_button = tk.Button(janela,text="Fechar",fg='Purple',bg='white', command= close_window)
close_button.grid(column=1,row=7)
close_button.config(font=['Garamond',10],width=10)

#botao para mostrar palavra-passe
mostrarpp_button =tk.Button(janela,text="Mostrar Palavra-passe", bg='white',fg='Purple',width=15,command=mostrarapp)
mostrarpp_button.grid(row=3,column=2,padx=5,pady=5)
mostrarpp_button.config(font=['Garamond',10])



tk.mainloop()