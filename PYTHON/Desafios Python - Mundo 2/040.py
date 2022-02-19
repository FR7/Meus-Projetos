# Crie um programa que  leia duas notas de um aluno
# e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:

# Média abaixo de 5.0: REPROVADO.
# Média entre 5.0 e 6.9: RECUPERAÇÃO.
# Média 7.0 ou superior: APROVADO.

cores = {'apaga':'\033[m', 'red':'\033[1;31m', 'green':'\033[7;36m'}
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

soma = nota1 + nota2
media = soma / 2
if media < 5.0:
    print("Você obteve média: {}".format(media))
    print("Você está {}REPROVADO!!{}".format(cores['red'], cores['apaga']))
elif media >= 5 and media <= 6.9:
    print("Você obteve média {}".format(media))
    print("Você está em {}RECUPERAÇÃO!!!{}".format(cores['red'], cores['apaga']))
else:
    print("Você obteve média {}.".format(media))
    print("{}PARABÉNS!! APROVADO!!!{}".format(cores['green'], cores['apaga']))