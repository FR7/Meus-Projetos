aula9 = """ Aula 09

'Curso em Vídeo Python'
 
 * Fatiamento:     frase[9]     = Pegará a Letra V
                   frase[9:13]  = Pegará  as letras Vide
                   frase[9:21]  = Pegará  as letras Video Python - existe uma função melhor 
                   frase[9:21:2] = Do 9 a0 21 pulando de 2 em 2  = V d 0 P t o
                   frase[:5]  = Começa do caracter 0 até 5 - Curso
                   frase [15:] = Começa do 15 até o último caractere.
                   frase [9::3] = Começa no 9 até o final de 3 em 3.
    
 *Análise:         len(frase)  =  Faz a contagem dos caracteres.
                   frase.count('0") = Quantas vezes aparece a letra o
                   frase.count('0',0,13) =  Contagem com fatiamento - do 0 ao 13 conta apenas 1 letra O.
                   frase.find('deo') = Encontrar DEO na posição 11.
                   frase.find('androide') = Se coloca uma frase que não existe, a função retorna -1 (não encontrado)
                   "Curso'in frase = existe curso em frase? = retorna True.
                
 *Transformação     frase.replace('Python'.'Androide').
                    frase.upper()  = O que é maisculo mantém e o que for minúscula ele troca por maíscula.
                    frase.lower()  = Mantém o que é minusculo, e o que é maiúsculo muda para minúsculo.
                    frase.capitalize() =  Joga todos os caracteres para minusculo e a primeira maiúsculo: Curso em video python
                    frase.title() = As primeiras letras de cada frase ficam em maiúsculo - Curso Em Video Python.
                    frase.strip() =  Remove todos os espaços inúteis.
                    frase.rstrip() = Remove os espaços  na direita
                    frase.lstrip() = Remove os espaços na esquerda.
                    
  * Divisão         frase.split()  = Ocorre uma divisão onde tem espaços e cria novas indexações.
                    '-'.join(frase)
 
  
  

"""
print(aula9)