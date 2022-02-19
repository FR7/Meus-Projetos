#Crie um script Python que leia o dia, mês e o ano de nascimento
#de uma pessoa e mostre uma mensagem com a data formatada.

nome = input("Qual o seu nome?")
dia = input("Em que dia do mês você nasceu?")
mes =  input("Em que mês você nasceu?")
ano = input("Em que ano você nasceu?")

print("{}, você nasceu no dia {} de {} de {}".format(nome,dia,mes,ano))