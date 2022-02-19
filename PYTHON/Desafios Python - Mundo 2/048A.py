# FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS
# IMPARES QUE SÃO MULTIPLOS DE TRÊS E QUE SE
# ENCONTRAM NO INTERVALO DE 1 ATÉ 500

from time import sleep
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        count = count + c
        print(c, ' ', count)

print('Soma total é igual a: {} '.format(count))


