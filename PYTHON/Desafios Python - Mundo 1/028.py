# Escreva um programa que faça o computador 'pensar' em
# um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi  numero escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador  = randint(0, 5)

print('=' * 50)
print('Agora é sua vez: Escolha um numero de 0 a 5: ')
print('=' * 50)

jogador = int(input('\nQual número eu escolhi? Faça sua aposta: '))
print('PROCESSANDO...')
sleep(3)


if computador == jogador:
    print('PARABÉNS!! Você escolheu o número {}. Você VENCEU!!!!'.format(jogador))
else:

    print('Você perdeu!!! O numero que eu escolhi foi {}'.format(computador))
