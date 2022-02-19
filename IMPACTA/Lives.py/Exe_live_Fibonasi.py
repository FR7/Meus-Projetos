n = int(input("Digite o n-ésimo termo para mostra a série de Fibonaci: "))
a = 0
b = 1
print(a)

for x in range(b, n):
    c = a
    a = b
    b = a + c
    print(a)


