#EXERCÍCIO 3

#Escreva um programa para exibir todos os números pares de 0 até o número informado pelo
#usuário.

num = int(input("Digite um número: "))
print("Todos os números pares de 0 até {}.".format(num))

c = 0
while c <= num:
    if c % 2 == 0:
        print(c)
    c = c + 1

