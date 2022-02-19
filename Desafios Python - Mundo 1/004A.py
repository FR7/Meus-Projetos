#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
#possíveis sobre ele

algo = input('Digite algo: ')

print('Qual o tipo? ',type(algo))
print('É um numero? ', algo.isnumeric())
print('É maiúsculo?? ', algo.isupper())
print('É minúsculo? ', algo.islower())
print('Está capitalizado? ', algo.istitle())
print('É alfanumérico?', algo.isalnum())
print('É alfabético?? ', algo.isalpha())
print('Só tem espaços??', algo.isspace())