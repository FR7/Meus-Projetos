#Fatiamento
#frase = 'Curso em Vídeo Python'

#print(frase[9::3])

# Análise

frase = "Fabio Rodrigues Dias"

print(len(frase))
print(frase.count("o"))
print(frase.count("o", 0, 20))
print(frase.lower().find("Dias"))
print(frase.count("abio"))
print("Dias"in frase)
print('\n')

#Transformação

print(frase.replace("Python", "Fabio"))
print(frase.upper())
print(frase.lower())
print(frase.split())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
novafrase = frase.split()

print('-'.join(novafrase))





