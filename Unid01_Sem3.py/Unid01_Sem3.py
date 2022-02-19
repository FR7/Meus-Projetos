#1) Escreva um programa que leia um número inteiro e exiba se ele é um
# número par ou ímpar.

numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("{} é um número par!!".format(numero))
else:
    print("{} é um número impar.".format(numero))

#math.acos(x) retorna o arco cosseno de x
#math.asin(x) retorna o arco seno de x
#math.atan(x) retorna o arco tangente de x
#math.ceil(x) retorna o menor inteiro maior ou igual a x como int
#math.cos(x) retorna o cosseno de x
#math.degrees(r) converte radianos para graus  Sintaxe Descrição
#math.e constante e (aproximadamente 2.7182818284590451)
#math.exp(x) retorna o exponencial de x (ex)
#math.fabs(x) retorne o valor absoluto de x
#math.factorial(x) retorna x!
#math.floor(x) retorna o maior inteiro menor ou igual a x como um int
#math.log(x,b) retorna logb x (se b for omitido, retorna log x na base e)
#math.log10(x) retorna log10 x
#math.modf(x) retorna a parte fracionária e a parte inteira como dois floats
#math.pi constante  (aproximadamente 3.1415926535897931)
#math.pow(x,y) retorna xy

#math.radians(g) converte graus para radianos
#math.sin(x) retorna o seno de x
#math.sqrt(x) retorna a raiz quadrada de x
#math.tan(x) retorna a tangente de x
#math.trunc(x) retorna a parte inteira de x como um int; igual a int(x)