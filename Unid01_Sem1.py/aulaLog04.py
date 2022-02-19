num = int(input("Digite um número: "))
if num % 3 and num % 5 == 0:
    print("O numero {}, é divisel por 3 e por 5".format(num))
elif num % 3 == 0:
    print("Divisível por 3")
elif num % 5 == 0:
    print("Divisivel por 5")
else:
    print("Não é divisível nem por 3 e nem por 5")
