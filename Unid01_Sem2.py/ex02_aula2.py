#Escreva um programa que calcule o rendimento em    Km/l de um automóvel.
#Sendo dados: a quantidade de litros de combustível gosto é de 43 litros e a
#distância percorrida é igual a 473Km.

litros_gasolina = int(input("Digite a quantidade de litros consumidos: "))
distancia = float(input("Digite a distância percorrida em kilomêtros: "))
km_porlitro = distancia / litros_gasolina

print('''Você colocou {} litros de gasolina e rodou um distância de {} kilômetros.
Você rodou {} kilômetros com um litro!!'''.format(litros_gasolina, distancia, km_porlitro))





