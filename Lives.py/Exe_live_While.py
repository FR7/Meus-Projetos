count = 20
while count >= 1:
    print(count)
    count = count - 1
print("""****************************\n""")

soma = 0 #inicialização da variável acumuladora
cont = 1 #inicialização da variável contadora

while cont <= 5:
    num = int(input("Digite um número: "))
    soma = soma + num #atualização da variável acumudara
    cont = cont + 1 #atualização da variável contador
print("A soma dos números é = {}".format(soma))


