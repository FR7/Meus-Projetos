# Exemplo: Escreva o trecho de um programa que lê e valida a entrada de um número inteiro e
#positivo. Usando uma estrutura de repetição podemos permitir que o usuário digite o dado
#enquanto esteja informando de forma incorreta.

num = -1
while num < 0:
    num = int(input("Digite um número inteiro e positivo: "))
print(num)
print("Número aceito!!")