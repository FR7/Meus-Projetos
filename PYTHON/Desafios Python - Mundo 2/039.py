# Faça um programa que leia o ano de nascimento
# de um jovem e informe, de acondo com sua idade:

# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta
# ou que passou do prazo.

from datetime import date

print('''Digite o sexo:
[M] para masculino
[F] para feminino
''')

sexo = str(input("Digitar: ")).lower()


if sexo == 'f':
    print("Sexo não elegível para alistamento!!")
elif sexo == 'm':
    atual = date.today().year

    ano_nascimento = int(input("Digite em que ano você nasceu: "))
    idade = atual - ano_nascimento
    if idade == 18:
        print("Você tem {} anos!! Já está na hora de se alistar!!".format(idade))
    elif idade < 18:
        print("Você tem {} anos.".format(idade))
        print('Falta(m) {} ano(s) para completar 18 anos'.format(18 - idade))
        print('E você deverá se alistar em {}.'.format(atual + (18 - idade)))

    elif idade > 18:
        print("Você está com {} anos de idade!!!".format(idade))
        print("Já passou(aram) {} ano (s) do seu alistamento!!".format(idade - 18))
        print("O Ano do seu alistamento foi em {}.".format(atual - (idade - 18)))
else:
    print("Opção inválida!!!!")

