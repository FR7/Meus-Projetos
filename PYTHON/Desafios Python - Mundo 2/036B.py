#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
# ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do salário ou então o empréstimo será negado.

print("Bem vindo ao nosso simulador de empréstimo bancário:")
print('')

nome = str(input("Qual o seu nome? "))
salario = float(input("{}, qual o seu salário?".format(nome)))
casa = float(input("Qual o valor da casa, {}".format(nome)))
anos = int(input("Em quantos anos pretende financiar?"))

prestacao = (casa / anos) / 12
if prestacao > salario * 30/100:
    print("A prestação ficou em R${} reais e esse valor ultrapassa os 30%".format(prestacao))
if prestacao <= salario * 30/100:
    print("A prestação ficará {} parcelas de R${}".format(anos*12, prestacao))
