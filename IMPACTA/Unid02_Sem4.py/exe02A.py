#Faça um programa que leia três números inteiros e colocá-los em ordem crescente.
#Sugestão: Sejam 3 números A, B e C. A ideia principal é:
# – armazenar em A o menor valor
# – armazenar em B o valor intermediário
# – armazenar em C o maior valor

a = int(input("Digite um número para a: "))
b = int(input("Digite um número para b: "))
c = int(input("Digite um número para c: "))
#a é o menor:
if a < b and a < c:
    if b < c:
        print("{}, {}, {}".format(a, b, c))
    else:
        print("{},{},{}".format(a, c, b))
#b é menor:
elif b < a and b < c:
    if a < c:
        print("{}, {}, {}".format(b, a, c))
    else:
        print("{}, {}, {}".format(b, c, a))
else:
    if a > b:
        print("{}, {}, {}".format(c, b, a))
    else:
        print("{}, {}, {}".format(c, a, b))






