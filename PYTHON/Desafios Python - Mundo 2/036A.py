#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
# ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input("Quantos anos de financiamento? "))
minimo = salario * 30 / 100

prestacao = casa / (anos * 12)
print("Para pagar um casa de R${:.2f} em {} anos.".format(casa, anos), end="")
print(" a prestação será de R${:.2f}".format(prestacao))
print("COMPARANDO tem que pagar {} e o mínimo é de {}".format(prestacao, minimo))
