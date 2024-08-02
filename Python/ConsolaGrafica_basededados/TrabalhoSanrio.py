 # -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import datetime
from datetime import datetime

def atualizar_horas():
    data_hora = datetime.now()
    dh = data_hora.strftime("Data: " + '%d/%m/%Y' + " " + "Horas: " + '%H:%M:%S')
    label3.config(text=dh)
    
    janela.after(1000, atualizar_horas)  # Chama a função a cada 1000ms (1 segundo)


#funçao pra sair

def close_window():
    janela.destroy()   
    
#criar uma janela    
janela = tk.Tk()
janela.title("Sanrio")

label1 = tk.Label(janela,text="Bem vindo ao Mundo de Sanrio!", width=50,bg='MistyRose')
label2 = tk.Label(janela,text="Escolhe o teu favorito:",width=50,bg='Khaki')
label3 = tk.Label(janela,text="",bg='grey',relief=RIDGE)
label4=tk.Button(janela,text="Hello Kitty",bg='DarkSalmon',fg='white')
label5 =tk.Button(janela,text="Kuromi",bg='DarkOrchid',fg='purple')
label6= tk.Button(janela,text="My Melody",bg='pink',fg='white')
label7=tk.Button(janela,text="Cinnamoroll",bg='light blue',fg='white')
label8=tk.Button(janela,text="Keroppi",bg='light green',fg='white')
label9=tk.Button(janela,text="Kiki & Lala", bg='pink', fg='CadetBlue')
label10=tk.Button(janela,text="Batzs-Maru",bg='yellow',fg='black')
label11=tk.Button(janela,text="Pochacco")
label12=tk.Button(janela,text="Pompompurin",bg='SaddleBrown',fg='yellow')
label13=tk.Button(janela,text="Chococat",bg='black',fg='white')

label1.grid(row=0,column=0,padx=5,pady=5)
label2.grid(row=1,column=0,padx=5,pady=5)
label3.grid(row=0,column=4,padx=5,pady=5)
label4.grid(row=2,column=0,padx=5,pady=5)
label5.grid(row=3,column=0,padx=5,pady=5)
label6.grid(row=4,column=0,padx=5,pady=5)
label7.grid(row=5,column=0,padx=5,pady=5)
label8.grid(row=6,column=0,padx=5,pady=5)
label9.grid(row=7,column=0,padx=5,pady=5)
label10.grid(row=8,column=0,padx=5,pady=5)
label11.grid(row=9,column=0,padx=5,pady=5)
label12.grid(row=10,column=0,padx=5,pady=5)
label13.grid(row=11,column=0,padx=5,pady=5)

atualizar_horas()  # Inicia a função para atualizar as horas

#criar o botao de fechar janela
close_button = tk.Button(janela,text="Fechar", command= close_window)
close_button.grid(row=20,column=0,padx=5,pady=5)

janela.mainloop() 