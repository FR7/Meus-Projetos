#Crie um programa que leia um numero Real  qualquer pelo teclado mostre na tela a sua porção inteira.
# Exemplo: Digite um número: 6.127. O número 6.126 tem  parte inteira 6.
import math
num = float(input("Digite um numero qualquer: "))

print("O numero {} tem como parte inteira: {}".format(num, math.trunc(num)))
