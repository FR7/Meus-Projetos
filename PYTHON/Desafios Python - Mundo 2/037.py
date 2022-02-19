# Escreva um programa que ele leia um numero inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:

# 1 para binário
# 2 para octal
# 3 para hexadecimal

cores = {'limpa':'\033[m',
         'red':'\033[1;31m'}

numero = int(input("Digite um número inteiro qualquer: "))
print('''Escolha uma das bases para conversão:
[1] Converter para base BINÁRIO.
[2] Converter para base OCTAL.
[3] Converter para base HEXADECIMAL: ''')
opcoes = int(input('Escolha um das opções: '))

if opcoes == 1:
    print("{} convertido na base binária é: {}".format(numero, bin(numero)[2:]))
elif opcoes == 2:
    print("{} convertido na base octal é: {}".format(numero, oct(numero)[2:]))
elif opcoes == 3:
    print("{} convertido na base hexadecimal é: {}".format(numero ,hex(numero)[2:].upper()))
else:
    print("{}OPÇÃO INVÁLIDA!!{}".format(cores['red'], cores['limpa']))
