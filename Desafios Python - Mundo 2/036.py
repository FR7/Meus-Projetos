#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
# ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do salário ou então o empréstimo será negado.

vcasa = float(input("Informe o valor da casa:R$"))
salario = float(input("Qual o salário do comprador?R$"))
periodo_financiamento = float(input("Informe a quantidade de meses do financiamento:"))

prestacao = vcasa / periodo_financiamento
percentual = (prestacao / salario) * 100

if prestacao > 0.30 * salario:
    print("EMPRÉSTIMO NEGADO! O VALOR DA PRESTAÇÃO DE R${:.2f} REAIS, SUPERA OS 30% DE SEU SALÁRIO.".format(prestacao))
    print("A PRESTAÇÃO SUPERA OS  {:.4f}% DO SEU SALÁRIO PARA COMPRA DESTA CASA!!!".format(percentual))

else:
    print("PARABÉNS!!! EMPRÉSTIMO CONCEDIDO, NO VALOR DE R${:.2f} REAIS. COM PARCELAS DE {:.2f} REIAS MENSAIS".format(vcasa, prestacao))
    print("VOCÊ ESTÁ UTILIZANDO {:.4f}% DO SEU SALÁRIO PARA COMPRAR ESTA CASA!!!".format(percentual))
