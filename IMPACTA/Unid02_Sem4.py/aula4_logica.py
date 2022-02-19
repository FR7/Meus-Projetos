media = float(input("Digite a nota final: "))
frequencia = float(input("Digite sua frequência em sala de aula: "))
if media >= 7.5 and frequencia >= 0.75:
    print("Aprovado Direto!!")
else:
    if media >= 6.0 and frequencia >= 0.75:
        print("Aprovado com Exame!")
    else:
        print("Reprovado!!!")