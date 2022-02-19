###Funções###
def eh_palindromo(texto):
    for i in range(len(texto)):
        if texto[i] != texto [1 -i]:
            return False
    return True

###Código Principal###
entradas = ['arara', 'elefante', 'radar', 'banana']
palindromos = []

for palavra in entradas:
    if(eh_palindromo(palavra)):
        palindromos.append(palavra)
        
print(palindromos)