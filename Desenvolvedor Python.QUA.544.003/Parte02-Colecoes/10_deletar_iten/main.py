nomes = [
"Fulano",
"Cicrano",
"Beltrano",
"João",
"Maria",
"José",
"Esmeralda"
]

nome = input("Informe o nome a ser deletado: ").strip().title()

if nome in nomes:
    indice = nomes.index(nome)

    #apaga item da lista
    del(nomes[indice])

    # exibe a nova linha sem o item deletado
    for nome in nomes:
        print(nome)
else:
    print("Nome não encontrado.")