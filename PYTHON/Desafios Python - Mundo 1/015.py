#ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS
#PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0.15 POR KM RODADO.


dias = float(input('Quantos dias você vai ficar com o carro?: '))
km= float(input('Qual a kilometragem rodada?: '))

palug = (60 * dias) + (0.15 * km)

print('Você alugou o carro por {} dias e rodou {} kilômetros. Total a pagar é R${} reais'.format(dias, km, palug))
