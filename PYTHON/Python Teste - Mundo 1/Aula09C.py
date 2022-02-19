#Fatiamento
#frase = 'Curso em Vídeo Python'

#print(frase[9::3])

# Análise

frase = "Curso em Video Python"
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2]) #vai até 14 pulando de 2 em 2
print(frase[::2]) #vai do começo ao fim de 2 em 2
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.replace("Python", "DoCaralho"))
print(frase.lower().find('video'))
print(frase.split())
dividido = frase.split()
print(dividido[2][3])

