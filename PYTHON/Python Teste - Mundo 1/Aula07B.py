n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {},\no produto é {}.\ne a divisão é {}'.format(s, m, d), end=' >>>')
print('\nA divisão inteira é {}, e a potência é {}'.format(di, e))
