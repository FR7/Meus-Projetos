import _sqlite3

def ExibeDados(L):
    """Exibe uma saida formatada dos dados contidos em L"""
    print("\nConsulta ao Banco de Dados 'academia.db'\n")
    print("Dados da tabela 'cadastro'")
    print("-"* 35)
    print("{:7} {:20} {:>6}".format("Código", "Nome", "Idade"))
    print("- " * 18)
    for d in L:
        print("{:<7} {:20} {:>6}".format(d[0], d[1], d[2]))
    print("-" * 35)
    print("Encontrados {} registros".format(len(dados)))



conector = _sqlite3.connect("academia.db")
cursor = conector.cursor()
sql = """
    insert into cadastro
    (codigo, nome, idade) values (?, ?, ?)
"""
print("Digite os dados separados por virgula")
print("Codigo, Nome, Idade")
Ler = input()
while Ler != "":
    D = Ler.split(",")
    try:
        cursor.execute(sql, D)
        conector.commit()
    except:
        print("{} Dados inválidos".format(D))
    else:
        print(" "*30, "...dados inseridos com sucesso")
    finally:
        print("Codigo, Nome, Idade")
    Ler = input()

sql = "select * from cadastro"

cursor.execute(sql)
dados = cursor.fetchall()
cursor.close()
conector.close()
ExibeDados(dados)
print("\n\nFim do Programa")

