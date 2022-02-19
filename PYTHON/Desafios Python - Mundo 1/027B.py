# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome, separadamente.

#Ex. Ana Maria de Souza

# Primeiro = Ana
# Último = Souza

nome = str(input("Escreva seu nome completo: ")).strip().lower()

lista = nome.split()

print("Muito prazer em te conhecer. Seu primeiro nome é {} e seu último nome é {}".format(lista[0], lista[len(lista)-1]))
