#3) As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
#compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas,
#calcule e escreva o custo total da compra.

qtdade_maca = int(input("Digite a quantidade de maçãs compradas: "))
if qtdade_maca < 12:
    valor = qtdade_maca * 1.30
    print("VocÊ comprou {} maçãs à R$1.30. Total a pagar: {:.2f} reais".format(qtdade_maca, valor))
if qtdade_maca >= 12:
    valor = qtdade_maca * 1.00
    print("Você comprou {} maçãs à R$1.00. Total a pagar: {:.2f} reais.".format(qtdade_maca, valor))
