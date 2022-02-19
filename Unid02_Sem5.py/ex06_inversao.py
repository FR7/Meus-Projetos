#Escreva um programa ler um número inteiro n, que não contém dígito 0, e escrever um número
#inteiro m que corresponde ao número n invertido. Por exemplo, se n igual a 123, a saída será m
#igual a 321.

n = -1
while n<=0:
    n = int(input("Digite um número inteiro e positivo:"))

m = 0
while n != 0:
    resto = n % 10
    m = m*10 + resto
    n = n // 10
print("O número inertido = {}".format(m))

