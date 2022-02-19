#Elabore um programa que verifica se um número natural é primo.

n = int(input("Digite o num: "))
ePrimo = True

for x in range(2, n ):
    if n % x == 0:
        ePrimo = False

if ePrimo == True:
    print(n, " e Prímo")
else:
    print(n, " não é Primo!!")
