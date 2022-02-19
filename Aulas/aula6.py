#%Aula 6 -  Tipos primitivos

#São tipos primitivos:

#int (7, -4, 0, 9875)
#float (4.5, 0.076,-15.223, 7.0)
#bool (True , False)
#str ('Olá')

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro número: "))

soma = n1 + n2
print('A soma vale', soma)
print('A soma vale {}'.format(soma))
print("A soma entre {} e {} vale {}.".format(n1, n2,soma))

