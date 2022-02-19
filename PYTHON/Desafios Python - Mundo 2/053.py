#Crie um programa que leia uma frase qualquer
# e dia se ela é um palindromo; desconsiderando os espaços
# Ex. apos a sopa ;  a sacada da casa, a torre da derrota

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("Não temos um Palíndromo!!")
