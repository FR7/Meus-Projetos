#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

nome = str(input("Digite um nome qualquer: "))

print('\nOlá {}. Seu nome tem SILVA?: {}'.format(nome, 'SILVA'in nome.upper()))

