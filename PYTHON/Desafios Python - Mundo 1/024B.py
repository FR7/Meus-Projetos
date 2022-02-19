#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome: "Santo".

cidade = str(input("Informe o nome da sua cidade: ")).strip().upper()

print("A cidade {} começa com o nome Santo?: {}".format(cidade, 'SANTO'in cidade[:5]))