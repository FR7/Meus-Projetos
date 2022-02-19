#Crie um script Python que leia o dia, mês e o ano de nascimento
#de uma pessoa e mostre uma mensagem com a data formatada.

nome = str(input('Digite o seu nome: '))
dia = int(input('Em qual dia você nasceu, {}: '.format(nome)))
mes = str(input('{}, em que mês você nasceu? '.format(nome)))
ano = int(input('Digite o ano em que nasceu: '))

print('{}, você nasceu no dia {} de {} de {}'.format(nome,dia, mes, ano))