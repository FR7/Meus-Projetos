#Faça um programa que leia de um número de 0 a 9999, e mostre na tela um dos digitos separados.

#Ex. Digite um número: 1834
#//*unidade:
#dezena:
#centena:
#milhar:*//

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número: {}'.format(num))
print('A unidade é: {}'.format(u))
print('A dezena é: {}'.format(d))
print('A centena é: {}'.format(c))
print('E o milhar é: {}'.format(m))