 # -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import hashlib
import mysql.connector 
banana = mysql.connector.connect(host="localhost", user="root", password="", database="pauta_escola")
cursor=banana.cursor()

#função para mostrar a palavra-passe
def mostrarpp():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        mostrarpp_button.config(text='Mostrar Palavra-Passe')
    else:
        password_entry.config(show='')
        mostrarpp_button.config(text='Esconder Palavra-Passe')
        
#funçao registo
def registo():
    entuser=utilizador_entry.get()
    entpp=password_entry.get()
    entturma=turma_entry.get()
    entperm=profoualuno_entry.get()
    entppprof=ppprofessor_entry.get()
    
    checkuser=[]
    check_email=f"SELECT Nome_utilizador FROM users"
    cursor.execute(check_email)
    user= cursor.fetchall()
    for values in user:
        checkuser.append(str(values[0]))
    if entuser in checkuser:
        labelregisto.config(text="Nome de utilizador em uso, crie outro")
    else:
        if entperm == "professor" and entppprof == "professor123":
            print("acerto de palavra passe")
            labelppprof.config(text="Palavra-passe correta",fg="green")  
            labelregisto.config(text="Conta criada com sucesso!",fg="green")
            adduser=f"INSERT INTO users(Nome_utilizador,Palavra_passe,Perm,Turma) VALUES ('{entuser}','{entpp}','{entperm}','{entturma}')"
            cursor.execute(adduser)
            banana.commit()
        elif entperm =="aluno" and entppprof=="":
            labelregisto.config(text="Conta criada com sucesso!",fg="green")
            adduser=f"INSERT INTO users(Nome_utilizador,Palavra_passe,Perm,Turma) VALUES ('{entuser}','{entpp}','{entperm}','{entturma}')"
            cursor.execute(adduser)
            banana.commit()
            
        else:
            print("errou a palavra passe do professor ou as permissões")    
            labelppprof.config(text="Errou a palavra passe do professor ou as permissões, por favor tente novamente.",fg="red")
                          
#função login
def login():
    global perm, showturma,showperm,shownome
    
    entuser=utilizador_entry.get()
    entpp=password_entry.get()
    entturma=turma_entry.get()
    entperm=profoualuno_entry.get()

    checkuser=[]
    checkppasse=[]
    checkturma=[]
    checkperm=[]
    
    check_email=f"SELECT Nome_utilizador FROM users"
    cursor.execute(check_email)
    user = cursor.fetchall()
    
    check_pp=f"SELECT Palavra_Passe FROM users"
    cursor.execute(check_pp)
    pp= cursor.fetchall()
    
    check_turma=f"SELECT Turma FROM users"
    cursor.execute(check_turma)
    turma= cursor.fetchall()
    
    check_perm=f"SELECT Perm FROM users"
    cursor.execute(check_perm)
    perm = cursor.fetchall()
    
    for values in user:
            checkuser.append(str(values[0]))
            
    for valuespp in pp:
            checkppasse.append(str(valuespp[0])) 
            
    for valuesturma in turma:
            checkturma.append(str(valuesturma[0]))
            
    for valuesperm in perm:
            checkperm.append(str(valuesperm[0]))
            
    i=0
    
    while (i < len(check_email)-1): 
        
            if entuser == checkuser[i] and entpp == checkppasse[i] and entturma == checkturma[i] and entperm == checkperm[i]:
                labellogin.config(text="Iniciou sessão com sucesso",fg="green")
                print("sucesso")   
                entrada_button=tk.Button(janela,text="Ver info", bg='white',command=verinformacoes)
                entrada_button.grid(columnspan=2,row=7)
                entrada_button.config(font=['Garamond',8],width=10) 
                showturma=entturma
                showperm=entperm
                shownome=entuser
                
                break
            else:
                labellogin.config(text="Erro ao iniciar sessão, por favor tente novamente.",fg="red")
                print("insucesso")
                
            i+=1
def alterarnotasdosalunos():
    global nomealuno_entry,nota_entry
    #criar a janela   
    janelapauta = tk.Toplevel()
    janelapauta.title("Alterar notas dos alunos")
    janelapauta.geometry("600x250")
    #criar a label
    label = tk.Label(janelapauta, text="",width=50)
    label.grid(columnspan=2) 
    label.config(font=['Garamond',15])
    
    labelnomealuno=tk.Label(janelapauta,text="Nome do aluno: ")
    labelnomealuno.grid(column=0,row=15)
    labelnomealuno.config(font=['Garamond',12])
    nomealuno_entry=tk.Entry(janelapauta)
    nomealuno_entry.grid(column=1,row=15,padx=5,pady=5)
    
    labelaltnota=tk.Label(janelapauta,text="Nota que deseja colocar: ")
    labelaltnota.grid(column=0,row=17)
    labelaltnota.config(font=['Garamond',12])
    nota_entry=tk.Entry(janelapauta)
    nota_entry.grid(column=1,row=17,padx=5,pady=5)
  
    #mensagem das notas
    labelmsgnota=tk.Label(janelapauta,text="",fg="green")
    labelmsgnota.grid(column=2,row=19)
    labelmsgnota.config(font=['Garamond',15],width=50)
    #botao para fechar janela
    close_button = tk.Button(janelapauta,text="Fechar",bg='white', command= exit)
    close_button.grid(column=1,row=19)
    close_button.config(font=['Garamond',10],width=20)
    
    #botao para alterar as notas
    notas_button = tk.Button(janelapauta,text="Alterar notas",command=botaoalterarnotas,bg='white')
    notas_button.grid(column=1,row=18)
    notas_button.config(font=['Garamond',10],width=20)
    
def botaoalterarnotas():
    
    entnota=nota_entry.get()
    entnomealuno=nomealuno_entry.get()
    notaaluno=f"UPDATE users SET Nota_Final= '{entnota}' WHERE Nome_Utilizador = '{entnomealuno}'"
    cursor.execute(notaaluno)
    banana.commit()   
    print(notaaluno)
    
def verinformacoes():

    #criar a janela   
    janelapauta = tk.Toplevel()
    janelapauta.title("Informações aluno/professor")
    janelapauta.geometry("900x500")
    #criar a label
    label = tk.Label(janelapauta, text="",width=50)
    label.grid(columnspan=2) 
    label.config(font=['Garamond',15])
    
    if showperm=="professor":

        infonomeal=f"SELECT Turma2 FROM turmas WHERE Professores= '{shownome}' "
        cursor.execute(infonomeal)
        varinfonomeal= cursor.fetchall() 
        varnomeal1= []
        
        for values in varinfonomeal:
            varnomeal1.append(str(values[0]))
            
        i=0
        while (i<len(varnomeal1)):
            
            i+=1
        if i==1:
            
            #TURMA
            infoturmaal=f"SELECT Nome_utilizador,Turma,Nota_Final FROM users WHERE Turma IN ( '{varnomeal1[0]}')"
            cursor.execute(infoturmaal)
            varinfoturmaal=cursor.fetchall()
            varnomeal=""
            varnotaal=""
            varturmaal=""
            
            for values in varinfoturmaal:
                varnomeal+=str(values[0]) + '\n'
                varturmaal+=str(values[1]) + '\n'
                varnotaal+=str(values[2]) + '\n'

        elif i==2:   
            #TURMA
            infoturmaal=f"SELECT Nome_utilizador,Turma,Nota_Final FROM users WHERE Turma IN ( '{varnomeal1[0]}' , '{varnomeal1[1]}' )"
            cursor.execute(infoturmaal)
            varinfoturmaal=cursor.fetchall()
            varnomeal=""
            varnotaal=""
            varturmaal=""
            
            for values in varinfoturmaal:
                varnomeal+=str(values[0]) + '\n'
                varturmaal+=str(values[1]) + '\n'
                varnotaal+=str(values[2]) + '\n'
                
        elif i==3:
            #TURMA
            infoturmaal=f"SELECT Nome_utilizador,Turma,Nota_Final FROM users WHERE Turma IN ( '{varnomeal1[0]}' , '{varnomeal1[1]}', '{varnomeal1[2]}' )"
            cursor.execute(infoturmaal)
            varinfoturmaal=cursor.fetchall()
            varnomeal=""
            varnotaal=""
            varturmaal=""
            
            for values in varinfoturmaal:
                varnomeal+=str(values[0]) + '\n'
                varturmaal+=str(values[1]) + '\n'
                varnotaal+=str(values[2]) + '\n'
        else:
            pass
                                            
        # informações pessoais
        labelinfo =tk.Label(janelapauta,text="Suas informações:")
        labelinfo.grid(column=1,row=2)
        labelinfo.config(font=['Garamond',15])

        labelnome=tk.Label(janelapauta,text="Nome de Utilizador:")
        labelnome.grid(column=0,row=3)
        labelnome.config(font=['Garamond',12])

        labelinfonome=tk.Label(janelapauta,text=varnomeal)
        labelinfonome.grid(column=0,row=4)
        labelinfonome.config(font=['Garamond',12])

        labelturma=tk.Label(janelapauta,text="Turma:",width=50)
        labelturma.grid(column=1,row=3)
        labelturma.config(font=['Garamond',12])

        labelinfoturma=tk.Label(janelapauta,text=varturmaal)
        labelinfoturma.grid(column=1,row=4)
        labelinfoturma.config(font=['Garamond',12])

        labelnota=tk.Label(janelapauta,text="Nota final: ",width=10)
        labelnota.grid(column=2,row=3)
        labelnota.config(font=['Garamond',12])

        labelinfonota=tk.Label(janelapauta,text=varnotaal)
        labelinfonota.grid(column=2,row=4)
        labelinfonota.config(font=['Garamond',12])

        alterarnotas=tk.Button(janelapauta,text="Alterar notas", bg='white',command=alterarnotasdosalunos)
        alterarnotas.grid(column=1,row=10)
        alterarnotas.config(font=['Garamond',10],width=20)

        #botao para fechar janela
        close_button = tk.Button(janelapauta,text="Fechar",bg='white', command= exit)
        close_button.grid(column=1,row=12)
        close_button.config(font=['Garamond',10],width=20)

    else:
    #vou incrementar para quando adicionar um valor, automaticamente ele dá \n
    #querys para selecionar os nomes, turmas e notas finais   
    #NOME UTILIZADOR
    
        infonome=f"SELECT Nome_utilizador FROM users WHERE Turma = '{showturma}' ORDER BY Nome_utilizador ASC "
        cursor.execute(infonome)
        varinfonome= cursor.fetchall() 
        varnome= ""
    
        for values in varinfonome:
            varnome+=str(values[0]) + '\n'

        #TURMA
        infoturma=f"SELECT Turma FROM users WHERE Turma = '{showturma}' "
        cursor.execute(infoturma)
        varinfoturma=cursor.fetchall()
        varturma=""

        for values in varinfoturma:
            varturma+=str(values[0]) + '\n'

        #NOTA FINAL
        infonotafinal=f"SELECT Nota_final FROM users WHERE Turma= '{showturma}' "
        cursor.execute(infonotafinal)
        varinfonota=cursor.fetchall()
        varnota=""

        for values in varinfonota:
            varnota+=str(values[0])+ '\n'

        # informações pessoais
        labelinfo =tk.Label(janelapauta,text="Suas informações:")
        labelinfo.grid(column=1,row=2)
        labelinfo.config(font=['Garamond',15])

        labelnome=tk.Label(janelapauta,text="Nome de Utilizador:")
        labelnome.grid(column=0,row=3)
        labelnome.config(font=['Garamond',12])

        labelinfonome=tk.Label(janelapauta,text=varnome)
        labelinfonome.grid(column=0,row=4)
        labelinfonome.config(font=['Garamond',12])

        labelturma=tk.Label(janelapauta,text="Turma:",width=50)
        labelturma.grid(column=1,row=3)
        labelturma.config(font=['Garamond',12])

        labelinfoturma=tk.Label(janelapauta,text=varturma)
        labelinfoturma.grid(column=1,row=4)
        labelinfoturma.config(font=['Garamond',12])

        labelnota=tk.Label(janelapauta,text="Nota final: ",width=10)
        labelnota.grid(column=2,row=3)
        labelnota.config(font=['Garamond',12])

        labelinfonota=tk.Label(janelapauta,text=varnota)
        labelinfonota.grid(column=2,row=4)
        labelinfonota.config(font=['Garamond',12])

        #botao para fechar janela
        close_button = tk.Button(janelapauta,text="Fechar",bg='white', command= exit)
        close_button.grid(column=1,row=12)
        close_button.config(font=['Garamond',10],width=20)
    
#criar a janela
janela= tk.Tk()
janela.title("Site Escolar")

#frases
labelinicio=tk.Label(janela,text="Bem vindo ao site Escolar")
labelinicio.grid(columnspan=3)
labelinicio.config(font=['Garamond',15])

#utilizador
utilizador_label=tk.Label(janela,text="Utilizador: ")
utilizador_label.grid(row=2,column=0,padx=5,pady=5)
utilizador_label.config(font=['Garamond',12])
utilizador_entry=tk.Entry(janela)
utilizador_entry.grid(row=2,column=1,padx=5,pady=5)

#espaço para inserir a password
password_label=tk.Label(janela,text="Palavra-passe: ")
password_label.grid(row=3,column=0,padx=5,pady=5)
password_label.config(font=['Garamond',12])
password_entry=tk.Entry(janela)
password_entry.grid(row=3,column=1,padx=5,pady=5)
password_entry.config(show='*')

#turma
turma_label=tk.Label(janela,text="Turma: ")
turma_label.grid(row=4,column=0,padx=5,pady=5)
turma_label.config(font=['Garamond',12])
turma_entry=tk.Entry(janela)
turma_entry.grid(row=4,column=1,padx=5,pady=5)

labelvazia=tk.Label(janela,text="")
labelvazia.grid(row=6,columnspan=2)

#aluno/professor
profoualuno= tk.Label(janela,text="professor ou aluno?")
profoualuno.grid(row=5,column=0,padx=5,pady=5)
profoualuno.config(font=['Garamond',12])
profoualuno_entry=tk.Entry(janela)
profoualuno_entry.grid(row=5,column=1,padx=5,pady=5)

#ppprofessor
ppprofessor= tk.Label(janela,text="Palavra-passe professor: ")
ppprofessor.grid(row=6,column=0,padx=5,pady=5)
ppprofessor.config(font=['Garamond',12])
ppprofessor_entry=tk.Entry(janela)
ppprofessor_entry.grid(row=6,column=1,padx=5,pady=5)
ppprofessor_entry.config(show='*')

#login
login_button=tk.Button(janela,text="Login", bg='white')
login_button.grid(columnspan=2,row=7)
login_button.config(font=['Garamond',8],width=10,command=login)

#mensagem de login
labellogin=tk.Label(janela,text="")
labellogin.grid(column=2,row=14)
labellogin.config(font=['Garamond',15],width=50)

#registo
continuar_button=tk.Button(janela,text="Regisro", bg='white')
continuar_button.grid(columnspan=2,row=9)
continuar_button.config(font=['Garamond',8],width=10,command=registo)

#mensagem de registo
labelregisto=tk.Label(janela,text="")
labelregisto.grid(column=2,row=14)
labelregisto.config(font=['Garamond',15],width=50)

labelppprof=tk.Label(janela,text="")
labelppprof.grid(column=2,row=13)
labelppprof.config(font=['Garamond',15],width=10)

#botao para mostrar palavra-passe
mostrarpp_button =tk.Button(janela,text="Mostrar palavra-passe",bg='white',width=15,command=mostrarpp)
mostrarpp_button.grid(row=3,columnspan=3,padx=5,pady=5)
mostrarpp_button.config(font=['Garamond',10])  

#botao para fechar janela
close_button =tk.Button(janela,text="Fechar",bg='white', command=exit)
close_button.grid(columnspan=2,row=10)
close_button.config(font=['Garamond',8],width=10)

#executar em loop
tk.mainloop()
                