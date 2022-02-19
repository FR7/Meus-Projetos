#Crie um programa que leia um numero Real  qualquer pelo teclado mostre na tela a sua porção inteira.
# Exemplo: Digite um número: 6.127. O número 6.126 tem  parte inteira 6.

from math import trunc

num = float(input('Digite um número qualquer: '))

print("O número {} tem a parte inteira {}".format(num,trunc(num)))

num = float(input('Digite um valor: '))
print("O número {} tem a parte inteira {}".format(num,int(num)))