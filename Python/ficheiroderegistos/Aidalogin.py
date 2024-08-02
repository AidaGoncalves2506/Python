# -*- coding: utf-8 -*-
#isto serve para poder usar acentos, esqueci me do que o stor me deu.
#importar biblioteca

import csv
import os
from ficheirodelogs import *
#funcao para o email e password
def fazerlog():
    iniciosessao=True
    while iniciosessao:
        email = input("Email: ")
        password = input("Palavra-Passe: ")
        
        with open('csv.csv', 'r') as file:
            reader = csv.reader(file)
            for lines in reader:
            
                if email == lines[0] and password== lines[1]: 
                    print(email,password)
                    print("Iniciou sessão com sucesso. Está autenticado.")
                    iniciosessao=False
                    break
                else:
                    print(email, password)
                    print("Ocorreu um erro ao iniciar a sua sessão, por favor tente novamente.")
                

