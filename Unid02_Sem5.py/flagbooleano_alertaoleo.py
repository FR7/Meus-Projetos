# Exemplo: Sabendo que um carro precisa trocar o óleo a cada 10.000 km e que há um alerta
#quando completa 8.000, escreva um programa que determina se um carro precisa trocar o
#óleo imediatamente, brevemente ou não precisa trocar.

troca_oleo = 10000
alerta_oleo = 8000
entradaValida = False

while not entradaValida:
    ultima_km = int(input("Digite a quilometragem da última troca: "))
    atual_km = int(input("Digite a kilometragem atual: "))

    if atual_km < ultima_km:
        print("Entrada inválida!!")
    else:
        estrada_km = atual_km - ultima_km
        entradaValida = True
if estrada_km >= troca_oleo:
    print("Você precisa fazer a troca de óleo!")
elif atual_km - ultima_km >= 8000:
    print("Brevemente você precisará fazer a troca de óleo!")
else:
    print("Você não precisa fazer a troca de óleo imediatamente!")