#Faça um programa que apresente se o número que o usuário digitou é
# divisível por 3 e por 5 ao mesmo tempo

numero = int(input("Digite um número: "))
if numero % 3 == 0:
    print("{} é divisível por 3!".format(numero))
elif numero % 5  == 0:
    print("{} é divisível por 5!!".format(numero))
else:
    print("{} não é divisíve por 3 e nem por 5!!".format(numero))