# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo.Calcule e mostre o comprimento da hipotenusa.

import math
catoposto = float(input("Digite o cateto oposto: "))
catadjace = float(input("Digite o cateto adjacente:"))

hip = math.hypot(catoposto, catadjace)

print("A hipotenusa do cateto adjacente {} e do cateto oposto {}, é igual a {:.4f}".format(catadjace, catoposto,hip))
