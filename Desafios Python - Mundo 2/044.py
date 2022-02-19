# Elabore um programa que calcule o valor a ser pago
# por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:

# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto.
# em até 2x no cartão: preço normal.
# 3x ou mais no cartão: 20% de juros.

cores = {'ret':'\033[m', 'red':'\033[1;31m', 'blue':'\033[1;34m'}
print('''********************
*    {}URSOS & CIA {}  *
********************'''.format(cores['blue'], cores['ret']))

produto = float(input("Informe o valor do produto:R$"))
print('''FORMAS DE PAGAMENTO:
[1] À vista dinheiro/cheque: com 10% de desconto.
[2] À vista no cartão: 5% de desconto.
[3] Em até 2x no cartão: preço normal
[4] Em 3x ou mais no cartão, com 20% de juros.''')
f_pagamento = int(input("Digite a opção desejada: "))
if f_pagamento == 1:
    des1 = 10
    pf1 = (produto * (100 - des1)/100 )
    print("Você terá {}% de desconto e estará pagando R${:.2f} reais. ".format(des1,pf1 ))
elif f_pagamento == 2:
    des2 = 5
    pf2 = (produto * (100 - des2)/100)
    print("Você terá {}% no cartão à vista e estará pagando R${:.2f} reais".format(des2, pf2))
elif f_pagamento == 3:
    duas_vezes = 50
    pf3 = (produto * (100 - duas_vezes) / 100)
    print("Pagará em 2x sem juros: R${:.2f} agora e mais R${:.2f} daqui 60 dias".format(pf3, pf3))
elif f_pagamento == 4:
    parcelas = int(input("Qual a quantidade de parcelas? "))
    juros = 20
    pf4 = (produto * (100 + juros) / 100) / parcelas
    if parcelas < 3 or parcelas > 12:
        print("Só poderá parcelar de 3 a 12 vezes! Refaça a compra!")
    else:
        print("Pagará em {}x com {}% de juros. ".format(parcelas, juros), end='')
        print("Ficará {} parcelas de R${:.2f} reais por mês. Totalizando R${:.2f}".format(parcelas, pf4, pf4 * parcelas))
else:
    print("Opção inválida de PAGAMENTO!!!")




