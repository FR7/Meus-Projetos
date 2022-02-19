# FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS
# IMPARES QUE SÃO MULTIPLOS DE TRÊS E QUE SE
# ENCONTRAM NO INTERVALO DE 1 ATÉ 500
from time import sleep
soma = 0
cont = 0
for c in range (1, 500, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
        print('{}====={}'.format(c, soma))
        sleep(0.2)
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))


