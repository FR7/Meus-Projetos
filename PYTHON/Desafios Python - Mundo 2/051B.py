# Desenvolva um programa que leia o primeiro termos e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

# an = a1 + (n - 1) . r
# Onde,

# an : termo que queremos calcular
# a1: primeiro termo da P.A.
# n: posição do termo que queremos descobrir
# r: razão*/

print("===============================")
print("  Os dez primeiros termos são")
print("===============================")
a1 = int(input("Digite o primeiro termo: "))
an = int(input("Digite a quantidade de termos: "))
p = int(input("Digite a posição do termo que queremos descobri: "))
r =  int(input("Digite a razão da P.A.: "))

for c in range(1 , an + 1):
    termos = a1 + (c - 1) * r
    find = a1 + (p - 1) * r
    print('{}'.format(termos), end= ' ')
print("\nO {}º termo da P.A. é {}".format(p, find))





