#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR.


carteira = float(input('Quanto tem em sua carteira: R$'))
dolar = float(input('Informe o dólar do dia: $'))

dolares = carteira / dolar

print('Você possui R${} reais em sua carteira. Equivalente a ${:.2f} dólares.'.format(carteira, dolares))
