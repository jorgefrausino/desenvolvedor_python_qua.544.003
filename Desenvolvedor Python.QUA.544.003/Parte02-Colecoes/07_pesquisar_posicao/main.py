cidades = [
"Brasília",
"Rio de Janeiro",
"São Paulo",
"Goiânia",
"Fortaleza",
"manaus"
]

cidade = input("Informe a cidade a ser pesquisa: ").strip().title()

# mostra a posição do iten na lista
if cidade in cidades:
    indice = cidades.index(cidade)
    print(f"indice de {cidade} na lista é {indice}.")
else:
    print("cidade não encontrada.")