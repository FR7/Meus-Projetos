#Estrutura de seleção simples
idade = int(input("Digite sua idade: "))

if idade <= 3:
    #o que vou fazer se a condição for verdadeira?
    print("Voçê é um bebê!.")
elif idade >= 4 and idade <= 12:
    print("Você é uma criança!!")

elif idade >=13 and idade <= 18:
    print("Você é um adolescente!")
elif idade >= 19 and idade <= 25:
    print("Você é jovem!!")
else:
    print("Você é adulto!!")

