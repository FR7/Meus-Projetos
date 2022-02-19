#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome: "Santo".

cidade = str(input("Digite o nome de uma cidade: ")).strip().upper()

print('A cidade {} começa com - Santo - em seu nome?:{}'.format(cidade, 'SANTO'in cidade[:5]))
