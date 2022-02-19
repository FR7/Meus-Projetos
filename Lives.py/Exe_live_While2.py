cont = 1  # variável contadora
soma = 0 # variável acumuladora
n = float(input("Digite um valor de números que serão digitados: "))

#validação da entrada dos dados
while n <= 0:
    n = float(input("Digite um valor válido maior que zero: "))
while cont <= n:
    n1 = float(input("Digite o {}º valor: ".format(cont)))
    soma = soma + n1
    cont = cont + 1

print("A soma é: {}".format(soma))

