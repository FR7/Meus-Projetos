#Desenvolva um programa que pergunte a distânica de uma viagem
# em km. Calcule o preço da passagem, cobrando R$0.50 por Km
# para viagens de até 200Km e R$0.45 para viagens mais longes.

distancia = float(input('Qual será a distância percorrida em sua viagem? '))
preço1 = distancia * 0.50
preço2 = distancia * 0.45

if distancia <= 200:
    print('Sua passagem custará {} reais'.format(preço1))
else:
    print('Sua passagem custará {} reais'.format(preço2))