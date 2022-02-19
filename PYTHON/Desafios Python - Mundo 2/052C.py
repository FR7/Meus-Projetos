# Faça um programa que leia um número inteiro e diga se ele
# é ou não um número primo.
# Números primos são aqueles divisíveis por 1 e ele mesmo.

num = int(input("Digite um número: "))
count = 0
for c in range (1, num + 1):
    if num % c  == 0:
        print('\033[33m', end=' ')
        count = count + 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\33[mO número {} foi divisível {} vezes'.format(num, count))
if count == 2:
    print("E por isso ele é PRIMO!!")
else:
    print("E por isso ele NÃO é primo!!")
