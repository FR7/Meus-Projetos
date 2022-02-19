# Crie um script Python que leia dois números e tente mostrar a soma entre eles


import requests as Req

cep = input("Entre com o CEP: ")
url = f"http://viacep.com.br/ws/{cep}/json"
endereco = Req.get(url).json()

logradouro = endereco['logradouro']
cidade = endereco['localidade']
estado = endereco['uf']

print(f"{logradouro}, {cidade} - {estado}")
