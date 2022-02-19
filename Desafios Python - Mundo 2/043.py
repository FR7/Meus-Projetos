# Desenvolva uma lógica que leia o peso e altura
# de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:

# - Abaixo de 18.5 Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - De 25 até 30: Sobrepeso
# - Acima de 40: Obesidade mórbida.
nome = input("Informe seu nome: ").title()
peso = float(input("{}, informe o seu peso: ".format(nome)))
altura = float(input("{}, informe sua altura: ".format(nome)))

imc = peso / (altura * altura)
base = 18.5
if imc < base:
    print("{}, seu IMC está em {:.2f} ".format(nome, imc), end='')
    print("Você está abaixo do peso")
elif imc >= base and imc <= 25:
    print("{}, seu IMC está em {:.2f}. ".format(nome, imc), end='')
    print("Você está com o peso ideal!")
elif imc > 25 and imc <= 30:
    print("{}, seu IMC  está em {:.2f}. ".format(nome, imc), end='')
    print("ATENÇÃO!! Você está acima do peso!")
elif imc > 30 and imc <=40:
    print("{}, seu IMC está em {:.2f} ".format(nome, imc), end='')
    print("Você está OBESO!! CUIDADO!!")
else:
    print("{}, seu IMC está em {:.2f}".format(nome, imc))
    print("OBESIDADE MÓRBIDA! NECESSÁRIO CIRURGIA!!")