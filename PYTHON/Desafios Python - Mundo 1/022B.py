# Crie um progrma que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas
#O nome com todas as minúsculas
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = str(input("Qual o seu nome completo? "))

print("Seu nome completo com letras maísculas, ficará: {} ".format(nome.upper()))
print("Seu nome completo com todas as letras minúsculas, ficará: {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))

lista = nome.split()
print("Seu  primeiro nome é {}, e ele tem: {} letras".format(lista[0], len(lista[0])))