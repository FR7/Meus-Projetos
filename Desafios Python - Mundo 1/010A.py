#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR.

saldo = float(input("Quanto você tem de SALDO em sua conta?? R$"))
dolares = float(input("Informe qual o dolar do dia:$"))

saldoEmDolares = saldo / dolares

print("Seu SALDO é de R${:.2f} reais. Com esse saldo você conseguirá comprar ${:.2f} dólares.".format(saldo, saldoEmDolares))

