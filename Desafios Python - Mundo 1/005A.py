# Crie um exercício que leia um número inteiro e mostre o seu sucessor e seu antecessor.

n1 = int(input('Digite um número: '))
ant = n1 - 1
suc = n1 + 1

print('Você digitou o número {}. Seu sucessor é {}. E seu antecessor é {}.'.format(n1, suc, ant))