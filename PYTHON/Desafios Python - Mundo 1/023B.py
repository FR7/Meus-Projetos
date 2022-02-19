#Faça um programa que leia de um número de 0 a 9999, e mostre na tela um dos digitos separados.

#Ex. Digite um número: 1834
#//*unidade:
#dezena:
#centena:
#milhar:*//

num = float(input("Digite um número qualquer: "))

uni = num // 1     % 10
dez = num // 10    % 10
cen = num // 100   % 10
mil = num // 1000  % 10

print(" A unidade do número {} é: {}".format(num, uni))
print(" A dezena do número {} é: {}".format(num, dez))
print("A centena do número {} é: {}".format(num, cen))
print("O milhar do número {} é: {}".format(num, mil))