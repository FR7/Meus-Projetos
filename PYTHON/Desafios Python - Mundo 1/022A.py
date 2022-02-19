# Crie um progrma que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas
#O nome com todas as minúsculas
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = str(input("Digite o seu nome completo: ")).strip()

print('Analisando o seu nome: \n')
print('Com todas as letras maiúsculas é: {} '.format(nome.upper()))
print('Com todas as letras minúsculas é: {} '.format(nome.lower()))
print("Seu nome tem ao todo: {} letras.".format(len(nome) - nome.count(' ')))
#print("Seu primeiro nome tem ao todo {} letras".format(nome.find(" ")))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

