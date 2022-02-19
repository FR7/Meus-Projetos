# CRIE UM PROGRAMA QUE MOSTRE NA TELA TODOS OS NÚMEROS
# PARES QUE ESTÃO NO INTERVALO ENTRE 1 E 50

from time import  sleep
print("Apresentação dos números pares:")
for c in range (1, 51):
    if c % 2 == 0:
        print(c, end='')
        print(" |", end=' ')
        sleep(1)
print('FIM!!')