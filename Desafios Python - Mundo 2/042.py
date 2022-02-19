# Refaça o desafio 035 dos triângulos, acrescentando
# o recurso de mostrar que tipo de triângulo será formado:

# - Equilátero: Todos os lados iguais
# - Isóceles: dois lados iguais.
# - Escaleno: Todos os lados diferentes.

#Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que
#a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.

#| a < b + c
#| b < a + c
#| c < a + b

#10 < 14 + 10
#8 < 14 + 10
#14 < 10 + 8
cores = {'retira':'\033[m',
         'blue':'\033[1;34m',
         'red':'\033[1;31m'
         }
print('''X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
X    {}ANALISADOR DE TRIÂNGULOS{}   X
X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X'''.format(cores['blue'], cores['retira']))

r1 = int(input("Digite a primeira reta: "))
r2 = int(input("Digite a segunda reta: "))
r3 = int(input("Digite a terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os seguimentos acima PODEM FORMAR UM TRIÂNGULO ", end='')
    if r1 == r2 == r3:
        print("{}EQUILATERO!!{}".format(cores['blue'], cores['retira']))
    elif r1 != r2 != r3 != r1:
        print("{}ESCALENO{}".format(cores['blue'],cores['retira']))
    else:
        print("{}ISÓCELES!{}".format(cores['blue'] ,cores['retira']))

else:
    print("{}Não PODEM FORMAR UM TRIÂNGULO!{}".format(cores['red'], cores['retira']))