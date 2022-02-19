# A Confedereção Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre
# sua categria, de acordo com a idade:

# - Até 9 anos:  MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER

from datetime import date

nome = input("Qual  seu nome? ")
nascimento = int(input("{}, informe seu ano de nascimento e descubra sua categoria::".format(nome)))

atual = date.today().year
idade = atual - nascimento

if idade <= 9:
    print("{}, você é categoria MIRIM!".format(nome))
elif idade <= 14:
    print("{}, você é categoria INFANTIL".format(nome))
elif idade <= 19:
    print("{}, você é categoria JUNIOR".format(nome))
elif idade<=25:
    print("{}, sua categoria é SÊNIOR".format(nome))
else:
    print("{}, sua categoria é MASTER!".format(nome))