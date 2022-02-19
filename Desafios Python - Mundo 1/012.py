# FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO.

produto = float(input('Digite o preço do produto: R$ '))

descprod = produto - (produto * (5 / 100))

print('O valor original do produto é: {}. E com 5% de desconto fica: {}. '.format(produto, descprod))