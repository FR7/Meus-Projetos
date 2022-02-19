# Faça a um programa que mostre um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente.

from math import sin, cos, tan, radians

ang = float(input("Digite um ângulo qualquer: "))

sen = sin(radians(ang))
coss = cos(radians(ang))
tang= tan(radians(ang))

print("O Seno de {} graus é {:.2f}".format(ang, sen))
print("O Cosseno de {} Graus é {:.2f}".format(ang, coss))
print("E a Tangente de {} Graus é {:.2f}".format(ang, tang))