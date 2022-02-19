#Validação de dados de entrada:

# Consiste em verificar se o valor
#usamos a estrutura condicional para checar informações de entrada e, em caso de erro,
#encerrávamos o programa.

# Usando uma estrutura de repetição podemos permitir que o usuário digite o dado enquant
#esteja informando de forma incorreta.

# Exemplo: Se o usuário precisa digitar um número no intervalo 1
#estrutura de repetição que recebe o número e, enquanto este número estiver fora do intervalo
#permitido, pede novamente a digitação e você conseguirá interromper a execução do programa permitido, pede novamente a digitação.

num = int(input("Digite um número de 1 a 50: "))
while num < 1 or num > 50:
    num = int(input("Número fora do intervalo. Digite novamente: "))
print("Número aceito!!")