#Interrupção do Laço – Flag booleano

# O controle do laço while pode ser feito por meio do loop infinito de uma única variável
#booleana, chamada flag booleano. Quando uma ocorrência acontecer, podemos alterar o valor
#dessa variável.

# Exemplo:

valido = False
while not valido:
    num = int(input("Digite um número inteiro e positivo: "))
    if num >= 0:
        valido = True
print(num)
print("Número aceito!")