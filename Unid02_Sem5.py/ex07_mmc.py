#Escreva um programa que calcule o MMC (mínimo múltiplo comum) entre dois números naturais.

n1 = -1
n2 = -1
#while n1 <= 0 or n2 <= 0:
while not (n1>0 and  n2>0):
    n1 = int(input("Digite n1: "))
    n2 = int((input("Digite n2:" ))

resto = auxi % n2
while resto != 0:
    aux = auxi + n1
    resto = aux % n2
print("O MMC é {}".format(auxi))