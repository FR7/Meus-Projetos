#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

nome = str(input("Digite o seu nome completo ")).strip().lower()

print("Seu nome completo é: {}".format(nome))
print("Seu nome tem - SILVA - ?: {}".format("silva"in nome))