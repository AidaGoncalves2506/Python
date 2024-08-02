 # -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import random
import this

#funçao pra sair
def close_window():
    janelinha.destroy()   

#Função frases escolhidas por mim

def mudarTexto():
    frases=["' They all say it gets better but what if I dont? '",
             "'When pretty isnt pretty enough, what do you do? '",
             "' And ain't it funny how you ran to her / The second that we called it quits? '",
             "' Maybe I'm too emotional. '",
             "' Well, good for you, I guess you moved on really easily. '",
             "' So find someone great, but don't find no one better '",
             "' I hope you're happy, but don't be happier. '",
             "' I wanna be you so bad, and I don't even know you. '",
             "' One heart broke, four hands bloody. '",
             "' Don't know if I'll see you again someday / But if you're out there, I hope that you're okay. '",
             "' And we both drew blood, but, man, those cuts were never equal. '"]

    frase=random.choice(frases)
    label3.config(text=frase) 
 
   #função frases ZEN 
def mudarsegundotexto():
    zen=[''.join(this.d.get(el, el) for el in this.s)]   
    pythonzen=random.choice(zen)
    linhasseparadas=pythonzen.splitlines()
    linhas=random.choice(linhasseparadas)
    label5.config(text=linhas)   
      
#criar uma janela    
janelinha = tk.Tk()
janelinha.title("<3 Frases de Músicas <3")

label1 = tk.Label(janelinha,text="Olá, aqui vão as frases!", width=70,fg='Purple')
label1.grid(columnspan=2)
label1.config(font=['Garamond',15])

label2 = tk.Label(janelinha,text="",fg='Purple')
label2.grid(row=1,column=0,padx=5,pady=5)
label2.config(font=['Garamond',14])

label6 = tk.Label(janelinha,text="(As frases da direita são de Zen Python!)", width=70,fg='Purple')
label6.grid(row=1,column=1,padx=5,pady=5)
label6.config(font=['Garamond',14])

label3=tk.Label(janelinha,text="Começa!",fg='Purple',bg='MediumPurple',width=70)
label3.grid(row=2,column=0,padx=10,pady=10)
label3.config(font=['Garamond',12])

label4 = tk.Label(janelinha,text="(As frases da esquerda são de músicas da Olivia Rodrigo!)", width=50,fg='Purple')
label4.grid(row=1,column=0,padx=5,pady=5)
label4.config(font=['Garamond',14])

label5=tk.Label(janelinha,text="Começa de novo!",fg='Purple',bg='MediumPurple',width=70)
label5.grid(row=2,column=1,padx=5,pady=5)
label5.config(font=['Garamond',12])

botaozinho=tk.Button(janelinha,text="Mudar",command=mudarTexto,fg='DarkMagenta',bg='white',width=50)
botaozinho.grid(row=3,column=0,padx=5,pady=5)

botaozinho=tk.Button(janelinha,text="Mudar",command=mudarsegundotexto,fg='DarkMagenta',bg='white',width=50)
botaozinho.grid(row=3,column=1,padx=5,pady=5)





#criar o botao de fechar janela
close_button = tk.Button(janelinha,text="Fechar",fg='DarkMagenta',bg='white', command= close_window,width=50)
close_button.grid(columnspan=2)
close_button.config(font=['Garamond',12])
tk.mainloop()
