#Faça um programa que leia de um número de 0 a 9999, e mostre na tela um dos digitos separados.

#Ex. Digite um número: 1834
#//
# unidade:
#dezena:
#centena:
#milhar:*//

num = int( input("Digite um número número qualquer: "))


uni =    num // 1 % 10
dez = num // 10      % 10
cen = num // 100     % 10
mil = num // 1000    % 10

print('Você digitou o número {} e sua unidade é: {}'.format(num, uni))
print('Sua dezena é: {}.' .format(dez))
print('Sua centena é: {}'.format(cen))
print('E seu milhar é {}: '.format(mil))
