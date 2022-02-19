# A série de Fibonacci é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, ... Escreva um programa
# que apresente a série de Fibonacci até o n-ésimo termo (n > 0).
    n = int(input("Digite o num n-ésimo termo para mostrar a serie de fibonacci: "))
    a = 0
    b = 1
    print(a)

    for x in range (b, n):
        c = a
        a = b
        b = a + c
        print(a)
