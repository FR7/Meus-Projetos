#Faça um programa que leia três números inteiros e colocá-los em ordem crescente.
#Sugestão: Sejam 3 números A, B e C. A ideia principal é:
# – armazenar em A o menor valor
# – armazenar em B o valor intermediário
# – armazenar em C o maior valor


a = int(input("digite um número em n1: "))
b = int(input("Digite um número em n2: "))
c = int(input("Digite um número em n3: "))
#menor a
if a < b  and a < c:
    if b > c:
        print("{}, {}, {}".format(a, c, b))
    else:
        print("{}, {}, {}".format(a, b, c))
#menor b
else:
    if b < a and b < c:
        if a > c:
            print("{}, {}, {}".format(b, c, a))
        else:
            print("{}, {}, {}".format(b, a , c))
    else:
        if a > b:
            print("{}, {}. {}".format(c, b, a))
        else:
            print("{}, {}, {}".format(c, a, b))






