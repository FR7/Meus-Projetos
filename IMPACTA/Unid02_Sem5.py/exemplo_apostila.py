# Calcular a soma de 5 números digitados pelo usuário.

soma = 0 #inicialização da variaável acumuladora.
cont = 1 #inicialização da variaável contadora.

while cont <=5: #condição
    num = int(input("Digite um número: "))
    soma = soma + num #atualização da variável acumuladora.
    cont = cont + 1 # atualização da variável contador
print("A soma dos números digitados é: {}".format(soma))
