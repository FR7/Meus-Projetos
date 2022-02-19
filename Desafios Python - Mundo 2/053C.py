#Crie um programa que leia uma frase qualquer
# e dia se ela é um palindromo; desconsiderando os espaços
# Ex. apos a sopa ;  a sacada da casa, a torre da derrota

frase = str(input("Digite uma frase: ")).strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1 ):
    inverso = inverso + junto[letra]
print(junto, inverso)
if junto == inverso:
    print("É um palíndromo")
else:
    print("Não é um palindromo!!")

