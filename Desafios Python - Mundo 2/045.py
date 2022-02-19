# Crie um programa que faça o computador jogar JOKENPÔ  com você!!

import random
from time import sleep

list = ['pedra', 'tesoura', 'papel']
computador = random.choice(list)

print('''VAMOS JOGAR JOKENPÔ???
Escolhar UMA DAS OPÇÇÕES ABAIXO:
*PEDRA
*TESOURA OU 
*PAPEL''')

escolha = str(input("Faça sua escolha: ")).lower()
print("JÔ")
sleep(1)
print("KEN")
sleep(1)
print("PO!")
sleep(1)

if escolha == 'pedra' and computador == 'tesoura':
    print("Você venceu!")
    print("Você escolheu {} e o computador escolheu {}".format(escolha, computador))
elif escolha == 'pedra' and computador == 'papel':
    print("Você perdeu!")
    print("Você escolheu {} e o computador escolheu {}".format(escolha, computador))
elif escolha == 'pedra' and computador == 'pedra':
    print("DEU EMPATE!!")
    print("Você escolheu {} e o computador escolheu {}".format(escolha, computador))
elif escolha == 'tesoura' and computador == 'tesoura':
    print("DEU EMPATE!")
    print("Você escolheu {} e o computador escolheu {}".format(escolha, computador))
elif escolha == 'tesoura' and computador == 'papel':
    print("Você ganhou!!")
    print("Você escolheu {} e o computador escolheu {}".format(escolha, computador))
elif escolha == 'tesoura' and computador == 'pedra':
    print("Você perdeu!!")
    print("Você escolheu {} e o computador escolheu {}".format(escolha, computador))
elif escolha == 'papel' and computador == 'tesoura':
    print("Você Perdeu!!")
    print("Você escolheu {} e o computador escolheu {}".format(escolha, computador))
elif escolha == 'papel' and computador == 'papel':
    print("DEU EMPATE!!")
    print("Você escolheu {} e o computador escolheu {}".format(escolha, computador))
elif escolha == 'papel' and computador == 'pedra':
    print("Você gannhou!!!")
    print("Você escolheu {} e o computador escolheu {}".format(escolha, computador))
else:
    print("Escolha novamente")


















