# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for impar, desconsidere-o
from time import sleep
soma  = 0
count = 0
for c in range(1, 10):
    num = int(input("Digite o {}º valor: ".format(c)))
    if num % 2 == 0:
        soma = soma + num
        count = count + 1
print("Você informou {} números PARES  e a soma foi {}".format(count, soma))




