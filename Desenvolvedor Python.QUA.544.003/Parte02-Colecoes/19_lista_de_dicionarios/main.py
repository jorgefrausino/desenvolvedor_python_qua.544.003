# lista de dicionarios
usuarios = [
{
    'nome':"Fulano de Tal",
    'idade': 35,
    'email': "fulano@gmail.com"
},
{
    'nome': "Cicrano",
    'idade': 21,
    'email': "cicrano@gmail.com"
},
{
    'nome': "Beltrano",
    'idade': 35,
    'email': "beltrano@gmail.com"
}
]

# percorre a lsita de dicionários

for usuario in usuarios:
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
        print(f"{'-'*40}")