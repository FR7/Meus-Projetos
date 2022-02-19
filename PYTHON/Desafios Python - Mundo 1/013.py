#FAÇA UM ALGOTITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO COM 15% DE AUMENTO.

salario = float(input('Digite o seu salário : R$'))

novosalario = salario + (salario * 15/100)

print('Seu salário atual é de R${} reais e passou a ser de R${:.2f} reais com o aumento de 15%.'.format(salario, novosalario))
