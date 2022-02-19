# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:

#-A MÉDIA DE IDADE DO GRUPO
#qUAL É O NOME DO HOMEM MAIS VELHO
# QUANTAS MULHERES TEM MENOS DE 20 ANOS.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print('------- {}ª PESSOA ------'.format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade?: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    media = somaidade / p
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
print("A média de idade do grupo é de {} anos".format(media))
print("O homem mais velho tem {} ano(s) e se chama {}.".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))