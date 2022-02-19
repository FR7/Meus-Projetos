#Crie um script Python que leia o dia, mês e o ano de nascimento
#de uma pessoa e mostre uma mensagem com a data formatada.

nome = str(input("Digite o se nome: "))
dia_nasc = int(input("Digite o seu dia de nascimento: "))
mes_nasc = str(input("Digite o mês de nascimento: "))
ano_nasc = int (input("Informe o seu ano de nascimento: "))
ano_atual = int(input("Infome o ano atual: "))
idade = ano_atual - ano_nasc

print("{}, vocẽ nasceu no dia {} de {} de {}. Portanto, você tem {} anos.".format(nome, dia_nasc, mes_nasc, ano_nasc, idade))