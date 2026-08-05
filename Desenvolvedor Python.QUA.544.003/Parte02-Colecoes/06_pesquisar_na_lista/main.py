cidades = [
"Brasília",
"Rio de Janeiro",
"São Paulo",
"Belo Horizonte",
"Goiânia",
"Manaus",
"Fortaleza",
"Florianópolis"
]

# informa o nome da cidade a ser pesquisada
cidade_pesquisada = input("Informe o nome da cidade a ser pesquisada: ").trip().title()

# retorna resultado
print(f"{cidade_pesquisada} encontrada." if cidade_pesquisada in cidades else "cidade não encontrada.")