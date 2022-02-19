# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo.Calcule e mostre o comprimento da hipotenusa.

from math import hypot

catop = float(input('Digite o Cateto Oposto: '))
catadj = float(input('Digite o Cateto Adjacente: '))

'''hip = (catadj ** 2 + catop ** 2)  ** (1/2)'''
hip = hypot(catop, catadj)

print("Dados os valores do cateto oposto e do cateto adjacente, o comprimento da hipotenusa é: {:.2f}".format(hip))