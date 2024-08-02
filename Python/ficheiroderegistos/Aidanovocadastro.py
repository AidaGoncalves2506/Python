# -*- coding: utf-8 -*-
#isto serve para poder usar acentos, esqueci me do que o stor me deu.
#importar biblioteca

import csv
import os
import random
import secrets
from ficheirodelogs import *
os.system('cls' if os.name=='nt'else'clear')

#arrays para a password e gerar letras e numeros
letenum = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","0","1","2","3","4","5","6","7","8","9"]

#funcao para o novo cadastro
def novoemail():
    em=[] 
    password=[]
    verificarem=False
    while verificarem== False:
        
            email= input("Email: ")
            file = open('csv.csv','r')
            
            with open("csv.csv", "r+", newline="") as file:
                reader=csv.reader(file) 
                for lines in reader:
                    em.append(lines[0])
                    password.append(lines[1])
                    
            if email in em:
                print("este email ja existe. Crie outro email.")  
            else:
                print("Email autorizado, irá para o passo seguinte")
                verificarem=True
                
                with open("csv.csv", "a+", newline="") as file:

                    write=csv.writer(file)
                    #write.writerow([email])            

         
            #funcao para a nova palavra passe (criar ou gerar uma) 
   
   
    criarougerar=input("Deseja criar a sua palavra passe ou gerar uma?/n(Gerando uma palavra-passe sera uma opcao mais segura./n opcoes: criar/gerar)")
    
    if criarougerar=="criar":
            
        print("Tenha em mente que a sua palavra-passe deve ter entre 8-12 caracteres\nsem espacos, com letras e numeros!")
        
        password= input("Palavra-passe :")
        
        file = open('csv.csv','a+', newline='')
        #escrever dados no ficheiro
        
        with file:
                write = csv.writer(file)
                write.writerow([email,password])
                reader=csv.reader(file) 
                for lines in reader:
                    em.append(lines[0])
                    password.append(lines[1])  
                    
        print("A sua palavra-passe é: ", password)
        
    else:
        pp=random.choices(letenum, k = 12)
        password=[pp]
        password_len = 12
        ps = ''
        for i in range(password_len):  
            ps+= ''.join(secrets.choice(letenum))
        password=[ps]
           
        with open("csv.csv", "a+", newline="") as file:
        #escrever dados no ficheiro

            write = csv.writer(file)
            write.writerow([email,password])
            reader=csv.reader(file) 
            for lines in reader:
                em.append(lines[0])
                password.append(lines[1])  
                      
                print("A sua palavra-passe gerada é:" , password)      
       

