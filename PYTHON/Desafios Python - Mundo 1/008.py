# escreva um programa que leia um valor em metros e a exiba convertida em centímetros e milímetros.

metros = float(input('Informe a metragem: '))

decimetros = metros  *    10
centimetros = metros *   100
milimetros = metros  *  1000
kilometros = metros / 1000


print('{} metros equivale a {} decímetros'.format(metros, decimetros))
print('{} centimetros.'.format(centimetros))
print('{} milímetros'.format(milimetros))
print('{} kilometros'.format(kilometros))

