# REFAÇA O DESAFIO 00, MOSTRANDO A TABUADA DE UM NÚMERO QUE
# O USUÁRIO ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR
from time import sleep
print('''***** TABOADA ******''')
sleep(3)

tab = int(input("Qual  a tabuada: "))
for c in range(-1, 10):
    c = c + 1
    r = c * tab
    sleep(1.5)
    print("{} x {} = {}".format(tab, c,r ))
print('FIM.')