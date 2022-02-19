#Escreva um programa que calcule o valor de H, sendo que ele é determinado pela série
#H = 1/1 + 3/2 + 7/4 + 11/6 + 15/8 + 19/10 + ... + 99/50.

a = 3
b = 2
h = '1/1 + 3/2'

for x in range(3, 99, 4):
    a = a + 4
    b = b + 2
    h = h + ' + ' + str(a)+'/'+str(b)
print(h)