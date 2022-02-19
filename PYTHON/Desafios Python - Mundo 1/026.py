#Faça um programa que leia uma frase pelo teclado e mostre:

# * Quantas vezes aparece a letra 'A'.
# * Em que posição ela aparece  a primeira vez.
# * Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase qualuqer: ')).strip().upper()

print('A letra a aparece: {} vez(es).'.format(frase.count('A')))
print('A letra a aparece nas posições: {}'.format(frase.find('A')))
print('A ultima lce na posição: {}'.format(frase.rfind('A')))