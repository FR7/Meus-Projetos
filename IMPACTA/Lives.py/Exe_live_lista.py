#Criar lista entre 3 a 7 elementos


n = int(input("Digite a quantidade de elementos da lista: "))

lista_numeros =[]
#digitar somente valores entre 3 e 7
while n < 3 or n > 7:
    n = int(input("Digite a quantidade de elementos da lista entre 3 e 7: "))
#lista de n elementos, porém, no indice 0 tenha o valor 1000.
for x in range (1, n + 1 ):
    valor = int(input("Digite um número: "))
    lista_numeros.append(valor)
#inserir valor 1000 no indice 0
lista_numeros.insert(0, 1000)
#lista final depois de inserir o valor 1000
print("Números digitados pelo usuário: {}".format(lista_numeros))
#Excluir o índice 2
del lista_numeros[2]
print('Lista depois de excluir indice 2')
result = lista_numeros.count(67)
if result > 0:
    print("Existe o número 67 na lista")
else:
    print("Não existe  o numero 67 na lista")
print(result)
#ordernar lista
print(sorted(lista_numeros))