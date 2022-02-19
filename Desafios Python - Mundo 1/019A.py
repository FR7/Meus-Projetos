# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajuda ele
# lendo o nome deles e escrevendo o nome dele e escrevendo o nome do escolhidoe

import random
aluno1 = str(input("Digite o nome do primeiro aluno: "))
aluno2 = str(input("Digite o nome do segundo aluno: "))
aluno3 = str(input("Digite o nome do terceiro aluno: "))
aluno4 = str(input("Digite o nome do quarto aluno: "))

lista = [aluno1, aluno2, aluno3, aluno4]

escolhido = random.choice(lista)
print("Dos 4 alunos, o escolhido para apagar o quadro foi {}".format(escolhido))