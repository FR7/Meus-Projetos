#FAÇA UM ALGOTITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO COM 15% DE AUMENTO.

salario = float(input("Informe o seu salário: R$"))

nsalario = salario + (salario * (15 / 100))

print("Seu salário é de R${:.2f} reias. Com o aumento de 15% seu novo salário será de:R${:.2f} reais.".format(salario, nsalario))
