# Faça um programa que leia um número inteiro e diga se ele
# é ou não um número primo.

num = int(input("Digite um número qualquer: "))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\33[33m', end=' ')
        total = total + 1
    else:
        print('\33[31m', end=' ')
    print("{}".format(c), end=' ')
print("\n\033[mO número {} foi divisível {} vezes".format(num, total ))
if total == 2:
    print("Por isso ele é PRIMO!!!")
else:
    print("Por isso ele {}NÃO É PRIMO!!{}".format('\33[31m', '\33[m'))