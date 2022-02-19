# Crie um programa que leia o ano de nascimento
# de sete pessoas. No final, mostre quantas pessoas
# ainda não aingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range (1, 7 + 1):
    nasc = int(input("Digite o ano de nascimento da {}ª pessoa: ".format(c)))
    idade = atual -nasc

    if idade > 21:
        totmaior = totmaior + 1
    elif idade < 21:
        totmenor = totmenor + 1

print("\nA ao todo tivemos {} pessoas maiores de idade".format(totmaior))
print("E, também, tivemos  {} pessoas menores de idade".format(totmenor))
