import _sqlite3

conector = _sqlite3.connect("academia.db")
cursor = conector.cursor()
sql = """
    create table cadastro
    (codigo integer, nome texto, idade interger)

"""
cursor.execute(sql)
sql = """
    insert into cadastro
    (codigo, nome, idade) values (1284, "Pedro de Oliveira", 32)
"""

cursor.execute(sql)
sql = """
    insert into cadastro
    (codigo, nome, idade) values (1309, "Maria Lucia Machado", 37)
"""
cursor.execute(sql)
cursor.execute(sql)
conector.commit()
cursor.close()
conector.close()


