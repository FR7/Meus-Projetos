# Elabore um algoritimo que calcule o que  deve ser pago  por um produto,
#considerando o preço normal e a condição da forma de pagamento.
#códigos:
#1 - `a vista em dinheiro ou chegue , recebe 10% de desconto.
#2 - À vista no cartão de crédito, recebe 5% de desconto.
#3 - Em 2 vezes, preço normal de etiqueta sem juros.
#4 - Em 3 vezes, preço normal de etiqueta mais juros de 10%

produto = float(input("Digite o valor do produto adquirido:R$"))
forma_pagamento = int(input('''
FORMA DE PAGAMENTO:

1) À vista em dinheiro ou chegue , recebe 10% de desconto
2) À vista no cartão de crédito, recebe 5% de desconto.
3) Em 2 vezes, preço normal de etiqueta sem juros.
4) Em 3 vezes, preço normal de etiqueta mais juros de 10%

Digite a opção de pagamento: '''))

if forma_pagamento == 1:
    desc_dinheiro = produto - (produto * (10/100))
    print("Total da compra é de {:.2f} real(s). Com 10% de desconto no dinheiro, ficará R${} reais.".format(produto, desc_dinheiro))
elif forma_pagamento == 2:
    desc_cartao = produto - (produto * (5/100))
    print("Total de compra é de {:.2f} real(s). Com 5% de desconto à vista no cartão, ficará R${:.2f} reais".format(produto, desc_cartao))
elif forma_pagamento == 3:
    duas_veze_sjuros = produto / 2
    print("Total de compra é de {:.2f} real(ais). Em duas vezes sem juros ficará 2x de R${:.2f} reais".format(produto, duas_veze_sjuros))
elif forma_pagamento == 4:
    tres_vezes_cj = (produto + (produto * (10/100))) / 3
    print("Total de compra é de {:.2f} real(ais). Em três vezes com juros com 10% ficará, 3x de R${:.2f} reais".format(produto, tres_vezes_cj))
else:
    print("FORMA DE PAGAMENTO NÃO RECONHECIDA!!!")

