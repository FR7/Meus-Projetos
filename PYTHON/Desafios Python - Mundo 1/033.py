# FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL
# É O MAIOR E QUAL É O MENOR.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número:  '))
c = int(input('Digite o terceiro número: '))


menor = a

if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c


maior = a

if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

print('O menor número é: {}'.format(menor))
print('O maior número é: {}'.format(maior))

