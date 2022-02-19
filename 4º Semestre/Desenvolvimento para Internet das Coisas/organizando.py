import os

# 1 pegar o nome dos arquivos
# 2 Pegar a extensão do arquivo para determinar o tipo
# 3 Criar pastas: imagens, audios, documentos, outros
# 4 mover arquivos para as pastas correspondentes

"meu.bom_arquivo.py".rfind('.')
def pegar_extensao(nome):
    index = nome.rfind('.')
    return nome[index:]

def organizar(diretorio):


    nomes_arquivos = os.listdir(diretorio)

    for arquivo in nomes_arquivos:
        extensao = pegar_extensao()

