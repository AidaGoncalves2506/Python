# -*- coding: utf-8 -*-
#isto serve para poder usar acentos, esqueci me do que o stor me deu.
#importar biblioteca
import csv
import os
from login import *
from novocadastro import *
from ficheirodelogs import *

#função para escolher entre fazer login ou cadastro
def bemvindo():
    logoucad= input("Seja bem vindo!\nDeseja fazer login ou fazer novo cadastro? ")
    
    
    if logoucad== "login":
        fazerlog()
        
        
    else:
        logoucad== "novo cadastro"
        
        novoemail()
     
    
bemvindo()
        
        
