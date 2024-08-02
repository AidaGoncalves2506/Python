#!/usr/bin/env python
#-*- coding: latin-1 -*-
#from asyncore import loop
import random
from random import sample
#(random.randrange(1,51)


listanumerosEuromilhoes = sample(range(1, 51), 5)
estrelita = sample(range(1, 13), 2)




print ("Escolha o 1 numero para o Euromilhoes")
Euron1=int(input())

print ("Escolha o 2 numero para o Euromilhoes")
Euron2=int(input())

print ("Escolha o 3 numero para o Euromilhoes")
Euron3=int(input())

print ("Escolha o 4 numero para o Euromilhoes")
Euron4=int(input())

print ("Escolha o 5 numero para o Euromilhoes")
Euron5=int(input())




print ("Escolha o 1 numero para a estrela")
estrelita1=int(input())

print ("Escolha o 2 numero para a estrela")
estrelita2=int(input())





print ("Os numeros selecionados foram", listanumerosEuromilhoes, "e as estrelas selecionadas foram", estrelita , "!")


print ("Por ordem crescente")

listanumerosEuromilhoes.sort()
estrelita.sort()
print("Numeros:", listanumerosEuromilhoes)
print("Estrelas:", estrelita)


print("Os seus numeros foram", Euron1,  Euron2 , Euron3 , Euron4 , Euron5 , "e as suas estrelas foram", estrelita1 , estrelita2 , "!")



if Euron1 in listanumerosEuromilhoes or Euron2 in listanumerosEuromilhoes or Euron3 in listanumerosEuromilhoes or Euron4 in listanumerosEuromilhoes or Euron5 in listanumerosEuromilhoes or estrelita1 in estrelita or estrelita2 in estrelita:


    print("Parabens!! Voce ganhou o Euromilhoes!")

elif estrelita1 in estrelita or estrelita2 in estrelita:

    print("Parabens!! Voce ganhou o Euromilhoes!")
    

#----------------------------------------------------------------------------------------------------------#
#este trabalho está muito chato#
#usarei o chatgpt para auxilio porque nao estou a conseguir fazer sozinha.#

# Função que verifica se pelo menos um número ou estrela foi acertado

def verificar_acertos(aposta_numeros, aposta_estrelas, numeros_sorteados, estrelas_sorteadas):
    for numero in aposta_numeros:
        if numero in numeros_sorteados:
            return True
    for estrela in aposta_estrelas:
        if estrela in estrelas_sorteadas:
            return True
    return False


# Variáveis para contar o número de semanas com pelo menos um acerto
semanas_com_acertos = 0


print("Faça sua aposta para o Euromilhões:")
aposta_numeros = []
aposta_estrelas = []

# Pedir ao usuário para fazer a aposta
for i in range(5):
    numero = int(input(f"Escolha o {i+1}º número para o Euromilhões: "))
    aposta_numeros.append(numero)

for i in range(2):
    estrela = int(input(f"Escolha o {i+1}ª estrela para o Euromilhões: "))
    aposta_estrelas.append(estrela)
    
# Contador de acertos
acertos = 0

# Realizar o jogo por 100 semanas
for semana in range(1, 101):
    print(f"\nSemana {semana}:")
    # Sortear os números e estrelas da semana atual
    numeros_sorteados = sample(range(1, 51), 5)
    estrelas_sorteadas = sample(range(1, 13), 2)
    
    print("Números sorteados:", numeros_sorteados)
    print("Estrelas sorteadas:", estrelas_sorteadas)
    
    # Verificar se pelo menos um número ou estrela foi acertado
    
    if verificar_acertos(aposta_numeros, aposta_estrelas, numeros_sorteados, estrelas_sorteadas):
        print("Parabéns!! Você ganhou o Euromilhões!")
        acertos += 1
    else:
        print("Você perdeu, tente novamente no próximo Euromilhões")


# Exibir o número de semanas em que o usuário acertou
print(f"\nVocê acertou em {acertos} semanas.")












