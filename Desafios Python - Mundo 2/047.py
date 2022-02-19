# CRIE UM PROGRAMA QUE MOSTRE NA TELA TODOS OS NÚMEROS
# PARES QUE ESTÃO NO INTERVALO ENTRE 1 E 50
from time import sleep
print("Apresentação dos números pares:")
sleep(3)
for c in range (1, 51):
    if c % 2 == 0:
        sleep(0.3)
        print("|", end='')
        print(c, end="")


print("|FIM")