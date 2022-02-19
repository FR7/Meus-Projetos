# DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE ALUNO, CALCULE E MOSTRE A SUA MÉDIA.

nome = input('Digite seu nome: ')
n1 = float(input('Nota da prova 1: '))
n2 = float(input('Nota da prova 2: '))

s = n1 + n2
med = s / 2

print("\n{0}, a nota da sua primeira prova é: {1}. A nota da sua segunda prova é: {2}."
      "\n\nTotal: {3} pontos.\n\nSua média é {4}.".format(nome, n1, n2, s, med))
