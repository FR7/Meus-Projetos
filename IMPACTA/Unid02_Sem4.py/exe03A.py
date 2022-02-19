#Faça um programa que faz a leitura de três valores reais (A, B e C), representando os coeficientes
#de uma equação do 2o. grau, calcula o valor do delta e os valores das raízes reais, caso existam.
#Considere que:

#– se A for igual a zero, exiba a mensagem “Não é equação de 2o grau!” e encerre;
#– se o delta for negativo, exiba a mensagem “Não existem raízes reais” e encerre.
#– Se o delta for zero ou positivo, exibe a raiz ou as raízes e encerre.
import math
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if a == 0:
    print("Não é uma equação do segundo grau. A é == 0.")
else:
    delta = b**2 - (4*a*c)
    #verificar se delta é negativo
    if delta < 0:
        print("Não existem raízes reais para delta negativo")
    else:
        #calcule as raízes x1 e xe
        x1 = (-b + (math.sqrt(delta))) / 2*a
        x2 = (-b - (math.sqrt(delta))) / 2*a
        print("x1 = {:.4f} e X2 = {:.4f}".format(x1, x2))









