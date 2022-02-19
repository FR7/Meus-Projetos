# Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre
# e mostre a temperatura em graus Celsios,sabendo que:

f = float(input("Digite o grau em Fahrenheit: "))
c =  5 * (f -32)/9
print("{} graus Fahrenheit é igual a {:.4f} graus Celsius.".format(f, c))