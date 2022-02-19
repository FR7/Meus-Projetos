# Desenvolva um programa que leia seis números inteiros e mostre  a soma apenas
# daqueles que forem pares. Se o valor digitado for impar, desconsidere-o


soma = 0

for c in range(1, 7):
    n = int(input("Digite o {}º valor: ".format(c)))
    if n % 2 == 0:
        soma = soma + n


print(soma)




