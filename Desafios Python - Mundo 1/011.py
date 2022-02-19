#FAÇA UM PROGRAMA QUE LEIA A LARGURA E ALTURA DE UMA PAREDE EM METROS.
#CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTA-LÁ,
# SABENDO QUE CADA LITRO DE TINTAS PINTA UMA ÁREA DE 2 M².


largura = float(input('Qual a largura da parede?: '))
altura = float(input('Qual a altura da parede?: '))
area = largura * altura
qtdtinta = area * (1/2)

print('A largura da parede é {} metros e sua altura é {} metros; totalizando uma área de {} m². A quantidade de tinta necessária é {} litos.'.format(largura, altura, area, qtdtinta ))



