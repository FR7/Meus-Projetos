#Ler três valores para os lados de um triângulo, considerando os lados como: A, B e C. Verificar se
#os lados fornecidos formam realmente um triângulo. Se afirmativo, deverá ser indicado qual tipo
#de triângulo foi formado: isósceles, escaleno ou equilátero.
#Orientações:
#Devemos saber primeiramente qual a definição de um triângulo.
#Triângulo é uma forma geométrica (polígono) composta de três lados, onde cada lado é menor que a soma dos outros
#dois lados.
#Perceba que isto é uma regra (uma condição) e deverá ser considerada. É um triângulo quando A < B + C, quando B <
#A + C e quando C < A + B.
#Tendo certeza que os valores informados para os três lados formam um triângulo, serão então, analisados os valores
#para se estabelecer qual tipo de triângulo será formado: isósceles, escaleno ou equilátero.

# isósceles quando possui dois lados iguais e um diferente, sendo A=B ou A=C ou B=C;
# escaleno quando possui todos os lados diferentes, sendo A <> B e B <> C; e
# equilátero quando possui todos os lados iguais, sendo A=B e B=C.

#Etapas principais do algoritmo:

# Ler três valores para os lados de um triângulo: A, B e C;
# Verificar se cada lado é menor que a soma dos outros dois lados
#Se sim, saber se A=B e se B=C, sendo verdade o triângulo é equilátero
#Se não, verificar se A=B ou se A=C ou se B=C, sendo verdade o triângulo é isósceles, caso
#contrário o triângulo é escaleno.
# Caso os lados fornecidos não caracterizem um triângulo, avisar a ocorrência.

a = int(input("Digite o lado A do triângulo!: "))
b = int(input("Digite o lado B do triângulo!: "))
c = int(input("Digite o lado C do triângulo!: "))

if a < b + c or b < a + c or c < b + a:
    if a == b and b == c:
        print("Forma um triângulo EQUILÁTERO!!!")
    else:
        if a != b != c != a:
            print("Forma um triângulo ESCALENO!!")
        else:
            print("Forma um triângulo ISÓSCELES!!")

else:
    print("Os seguimentos acima NÃO FORMAM UM TRIÂNGULO!!!")












