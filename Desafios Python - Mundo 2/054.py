# Crie um programa que leia o ano de nascimento
# de sete pessoas. No final, mostre quantas pessoas
# ainda não aingiram a maioridade e quantas já são maiores.

from datetime import date
from time import sleep
atual = date.today().year
totalmaior = 0
totalmenor = 0

for c in range(1, 8):

    ano_nasc = int(input("Em que ano nasceu a {}° pessoa?: ".format(c)))
    idade = atual - ano_nasc
    sleep(0.5)
    if idade >= 21:
        totalmaior +=  1

    else:
        totalmenor += 1


print("\nTivemos {} pessoa(s) que atingiu(ram) a maioridade".format(totalmaior))
print("Tivemos {} pessoa(s) menor(es) de idade!!".format(totalmenor))
