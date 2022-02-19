# Desenvolva uma lógica que leia o peso e altura
# de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:

# - Abaixo de 18.5 Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - De 25 até 30: Sobrepeso
# - Acima de 40: Obesidade mórbida.


nome = str(input("Qual o seu nome? ")).capitalize()
peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é a sua altura? (m) "))


imc = peso / (altura ** 2)
print("{} o seu IMC é de  {:.2f}".format(nome, imc))
if imc < 18.5:
    print("{}, você está ABAIXO DO PESO!".format(nome))
elif imc >= 18.5 and imc < 25:
    print("{}, você está com o PESO IDEAL! PARABÉNS!".format(nome))
elif imc >= 25 and imc < 30:
    print("{}, você está com SOBRE-PESO".format(nome))
elif imc >= 30 and imc < 40:
    print("{}, você está OBESO.".format(nome))
elif imc >= 40:
    print("{}, você está com OBESIDADE MÓRBIDA!")

