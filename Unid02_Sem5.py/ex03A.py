#EXERCÍCIO 3

#Escreva um programa para exibir todos os números pares de 0 até o número informado pelo
#usuário.

cont = 0
num = int(input("Digite um número: "))
while cont <= num:
    if cont % 2 == 0:
        print(cont)
    cont = cont + 1


print("Fim!")

