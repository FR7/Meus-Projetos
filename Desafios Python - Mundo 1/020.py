#O mesmo professor do desafide anterior quer sortear a ordem da apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada.

import random

n1 = input ('Primeiro aluno: ')
n2 = input ('Segundo aluno: ')
n3 = input ('Terceiro aluno: ')
n4 = input ('quarto aluno: ')

lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))






