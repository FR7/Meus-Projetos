#Crie um algoritimo que leia um número e mostre seu dobro; seu triplo e raiz quadrada.

from math import sqrt

num = float(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raizq = sqrt(num)

print('Você digitou o número {}.'.format(num))
print('O dobro de {} é {}. O seu triplo é {}. E a raiz quadrada é {:.2f}.'.format(num, dobro, triplo, raizq))