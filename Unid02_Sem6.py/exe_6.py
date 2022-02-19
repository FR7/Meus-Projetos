#Elabore um programa que, dados dois números naturais n1 e n2, representando um intervalo
#[n1,n2], exibe todos os números primos do intervalo.
n1 = int(input("Digite o primeiro num do intervalo: "))
n2 = int(input("Digite o segundo num do intervalo: "))

while n2<=n1:
    n2 = int(input("Digite o 2º numero do intervalo maior que n1: "))
print("Números primos no intervalo de {} e {}.".format(n1, n2))

for cont1 in range (n1, n2 + 1):
    ePrimo = True
    for cont2 in range (2, cont1):
        if cont1 % cont2 == 0:
            ePrimo = False
    if ePrimo == True:
        print(cont1)