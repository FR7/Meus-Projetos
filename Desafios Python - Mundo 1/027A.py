# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome, separadamente.

# Ex. Ana Maria de Souza

# Primeiro = Ana
# Último = Souza

nome = str(input(" Digite o seu nome completo: ")).strip()

l= nome.split()

print('Seu nome completo é: {}'.format(nome))
print('Seu primeiro nome é: {}'.format(l[0]))
print('Seu último nome é: {}'.format(l[len(l)-1]))
