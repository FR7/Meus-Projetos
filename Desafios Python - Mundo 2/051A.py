# Desenvolva um programa que leia o primeiro termos e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.


from time import sleep

print("============================")
print("Os 10 primeiros termos são: ")
print("==============================")
t1 = int(input("Primeiro termo: "))
razao = int(input("Qual a razão da P.A?: "))
rf = int(input("Qual a range final: "))


for c in range(1, rf + 1):
    t = t1 + (c - 1) * razao
    sleep(1)
    print(t, end= ' -> ')
print("Acabou!!!")

