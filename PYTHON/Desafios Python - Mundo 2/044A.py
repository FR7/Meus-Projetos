# Elabore um programa que calcule o valor a ser pago
# por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:

# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto.
# em até 2x no cartão: preço normal.
# 3x ou mais no cartão: 20% de juros.

print('''=====================
   {}URSOS & CIA{}  
====================='''.format('\033[1;34m', '\033[m'))

preço = float(input("Preço das compras:R$"))
print(''' FORMAS DE PAGAMENTO:
[1] 10 % DE DESCONTO À VISTA DINHEIRO/CHEQUE
[2]  5 % À VISTA NO CARTÃO
[3] 2X NO CARTÃO - PREÇO NORMAL
[4] 3X OU MAIS NO CARTÃO COM 20% DE JUROS''')

opção = int(input("Qual é a opção? "))
if opção == 1:
    total = preço - (preço * (10 / 100))
    print("Sua compra de R${:.2f} reias, vai custar R${:.2f} reais no pagamento à vista no dinheiro/cheque".format(preço,total))
elif opção == 2:
    total = preço - (preço * (5 / 100))
    print("Sua compra e R${:.2f} reais, vai custar R${:.2f} reias no pagamento à vista no cartão".format(preço, total))
elif opção == 3:
    cartao2 = preço / 2
    print("Sua compra de R${:.2f} reias, ficará 2x de {:.2f} reais e não terá desconto.".format(preço, cartao2))
elif opção == 4:
    parcelas = int(input("Digite o número de parcelas: "))
    if parcelas >= 3:
        total = preço + (preço * (20 / 100))
        novopreço = total / parcelas
        print("Sua compra no valor de R${} reais, ficará em {} parcelas de R${:.2f} reais com 20% de acréscimo.".format(preço, parcelas, novopreço))
        print("Totalizando R${:.2f} reais no término do pagamento".format(total))
else:
    print("Opção inválida! Refaça a operação")


