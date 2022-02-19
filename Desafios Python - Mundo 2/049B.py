# REFAÇA O DESAFIO 00, MOSTRANDO A TABUADA DE UM NÚMERO QUE
# O USUÁRIO ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR

from time import sleep
print('''*************
*  {}TABUADA{}  *
*************'''.format('\033[1;34m', '\033[m'))
count = 0
tabuada = int(input("Escolha a tabuada: "))
for c in range(1, 11):
    count = count + 1
    sleep(1)
    print("{} X {} = {} ".format(tabuada, c, c * tabuada))
print("{}FIM{}".format('\033[1;34m', '\033[m'))

