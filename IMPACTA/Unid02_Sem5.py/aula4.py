nota = float(input("Digite sua nota final: "))
frequencia = float(input("Digite a sua frequência: "))
if nota >= 7.5 and frequencia >=0.75:
    print('Aprovado Direto!!!')
elif nota >= 6.0 and frequencia >=0.75:
    print('Aprovado com Exame!!!')
else:
    print('REPROVADO!!!')