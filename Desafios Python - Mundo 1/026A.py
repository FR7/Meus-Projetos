#Faça um programa que leia uma frase pelo teclado e mostre:

# * Quantas vezes aparece a letra 'A'.
# * Em que posição ela aparece  a primeira vez.
# * Em que posição ela aparece a última vez.

frase = str(input("Digite uma frase qualquer: ")).upper()

print("A letra A aparece {} vez(es).".format(frase.count('A')))
print('Ela aparece a primeira vez na posição {}'.format(frase.find('A')))
print('Ela aparece a última vez na posição {}'.format(frase.rfind('A')))