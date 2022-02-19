# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7.00 por cada km acima do limite.

carSpeed = float(input('\nInforme qual a velocidade do carro: '))
multa = (carSpeed - 80) * 7
if carSpeed > 80:
    print('Você excedeu o limite permitido que é de 80 km/h Km, e sua multa será de R${:.2f} reais.'.format(multa))
else:
    print('Você está dentro dos limites de velocidade')
