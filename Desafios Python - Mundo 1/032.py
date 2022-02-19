# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O Ano {} É UM ANO BISSEXTO!!!!'.format(ano))
else:
    print('{} NAÕ É UM ANO BISSEXTO'.format(ano))