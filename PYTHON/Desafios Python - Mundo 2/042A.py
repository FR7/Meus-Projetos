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

print('''*********************************
*    {}ANALISADOR DE TRIÂNGULOS{}   *
*********************************
'''.format('\033[1;34m', '\033[m'))

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os seguimentos acima PODEM FORMAR UM TRIÂNGULO ", end='')
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO!")
    else:
        print("ISÓCELES")
else:
    print("Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!")