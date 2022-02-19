#Crie um algoritimo que leia um número e mostre seu dobro; seu triplo e raiz quadrada.

from math import sqrt

num = float(input("Digite um número: "))
dobro = num * 2
triplo = num * 3

print("O dobro de {} é {}.".format(num, dobro))
print("O triplo de {}, é {}".format(num, triplo))
print("A raiz quadrada de {}. é {:.2f}".format(num, pow(num,(1/2))))