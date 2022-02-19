# Um Fabricante vendeu 120 unidades de um produto que custa R$40,00 cada.
# Sobre o valor vendido, o fabricante paga 40% de imposto. Escreva um pro-
# grama que calcule o valor de imposto a ser pago.

quantidade = int(input("Digite a quantidade de produtos vendidos: "))
v_prod = float(input("Digite o valor do produto vendido: "))
percentual_imposto = 40
imposto = (quantidade * v_prod) * (percentual_imposto /100)
print("Total de venda é de {:.2f} reais e o valor de imposto a ser pago é {:.2f}".format((v_prod * quantidade),imposto))





