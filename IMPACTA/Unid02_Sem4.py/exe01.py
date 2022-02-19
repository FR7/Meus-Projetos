#EXERCÍCIO 1
#Faça um programa que leia três números inteiros e encontra o menor deles.
#Sugestão: Sejam 3 números A, B e C. A ideia principal é:
# verificar se A é menor valor que B e C e se não for,
#verificar entre B e C

#a = int(input("digite um numero para a: "))
#b = int(input("digite um numero para b: "))
#c = int(input("digite um numero para c: "))


#if a < b and a < c:
#    print("a é menor")
#elif b < a and b < c:
#    print("b é menor")
#else:
#    print(("c é menor"))

a = int(input("Digite um número para a: "))
b = int(input("Digite um número para b: "))
c = int(input("Digite um número para c: "))

if  a < b and a < c:
    print("{} é o menor número".format(a))
elif b < a and b < c:
    print("{} é o menor número".format(b))
elif c < a and c < b:
    print("{} é o menor número:".format(c))
else:
    print("Os números digitados são iguais")


