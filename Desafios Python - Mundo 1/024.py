#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome: "Santo".

cidade = str(input('Em que cidade você nasceu?: ')).strip()

print('O nome da cidade é: {} '.format(cidade))
print(cidade[0:5].upper() == 'SANTO')