# escreva um programa que leia um valor em metros e a exiba convertida em centímetros e milímetros.

metros = float(input("Digite a metragem do objeto: "))

cent = metros * 100
mili = metros * 1000

print('{} metros é equivalente a {} centímetros ou {} milimetros. '.format(metros, cent, mili))
