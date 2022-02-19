#FAÇA UM PROGRAMA QUE LEIA200 A LARGURA E ALTURA DE UMA PAREDE EM METROS.
#CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTA-LÁ,
# SABENDO QUE CADA LITRO DE TINTAS PINTA UMA ÁREA DE 2 M².

largura = float(input("Informe a largura em metros: "))
altura = float(input("Infome a altura em centímetros: "))

area = largura * altura
tinta = area / 2

print("A parede tem {} metros quadrados. E a quantidade de tinta necessária para pintá-la é de {} litros.".format(area, tinta))