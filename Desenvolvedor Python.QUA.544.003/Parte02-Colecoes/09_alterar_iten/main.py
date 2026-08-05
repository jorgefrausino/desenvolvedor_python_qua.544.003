nomes = [
"Fulano",
"Cicrano",
"Beltrano",
"João",
"Maria",
"José",
"Esmeralda"
]

# usuários informa o nome que deseja alterar
nome_antigo = input("Informe o nome que deseja alterar: ").strip().title()

# armazena a posição do nome na lista caso exista
if nome_antigo in nomes:
    indice = nomes.index(nome_antigo)
else:
    print("Nome não encontrado.")
    for nome in nomes:
        print(nomes)
    else:
        print("Nome não encontrado.")