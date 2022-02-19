#Escreva as seguintes expressões matemáticas utilizando operadores e funções da linguagem Python.
# y = a² + v 3b
#           -----
#             5x³
import math
a = int(input('Digite um valor para a: '))
b = int(input('Digite um valor para b: '))
x = int(input('Digite um valor para x: '))

y = (math.pow(a,2) + math.sqrt(3*b)) / (5 * math.pow(x,3))
print(y)

