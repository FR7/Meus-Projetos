#EXERCÍCIO 2

#Escreva um programa para escrever na tela a contagem regressiva do lançamento de um foguete.
#O programa deve exibir 10, 9, 8, ..., 1,0 e Fogo!
cont = 0
num = int(input("Digite um número: "))
while num >= cont:

    print(num)
    num = num - 1
print("Fire!!!")


