#Faça a um programa que mostre um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente.

import math
angulo = float(input("Digite um ângulo qualquer: "))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print("O seno do angulo {} é: {:.2f}".format(angulo, sen))
print("O Cosseno do ângulo {} é {:.2f}".format(angulo, cos))
print("A tangente do ângulo {} é: {:.2f}".format(angulo, tan))
