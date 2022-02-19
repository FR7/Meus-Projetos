#2) Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da
#compra for menor que R$ 20,00; caso contrário, o lucro será de 30%. Escreva um programa que
#receba o valor do produto e exiba o valor da venda.


produto = float(input("Informe o valor do produto em reais: R$"))
if produto < 20:
    prod_45 = produto + (produto * (45/100))
    print("O valor do produto com 45% de lucro é {:.2f}".format(prod_45))
else:
    prod_30 = produto + (produto * (30/100))
    print("O valor do produto com 30% de lucro é {:.2f}".format(prod_30))
