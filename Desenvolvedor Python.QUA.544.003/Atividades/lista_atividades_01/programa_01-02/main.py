# TODO: atividade 01
"""
Crie um programa que receba uma vez o nome e a idade do usuário, e em seguida mostre os filmes em cartaz em 5 salas de cinema:
- A Volta dos Que Não Foram (livre)
- A Roda Quadrada (12 anos)
- As Trnças do Rei Careca (14 anos)
- Poeira em Alto Mar (16 anos)
- A Vingança do frango Assado (18 anos)
O usuário íra escolher a sala onde o filme desejado está passando. Caso o usuário não tenha idade, o programa impede sua entrada e re-exibe a lista para que o mesmo possa escolher outro filme. Caso o usuário tenha idade mínima, o porgrama grava em arquivo o bilhete do filme e encerra o programa.

"""
import datetime

# Definir dados dos filmes
filmes = [
    {"nome": "A Volta dos Que Não Foram", "idade": 0},
    {"nome": "A Roda Quadrada", "idade": 12},
    {"nome": "As Trnças do Rei Careca", "idade": 14},
    {"nome": "Poeira em Alto Mar", "idade": 16},
    {"nome": "A Vingança do frango Assado", "idade": 18}
]

def obter_entrada_usuario():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    return nome, idade

def mostrar_filmes(idade):
    print("\nFilmes em cartaz:")
    for i, filme in enumerate(filmes):
        if idade >= filme["idade"]:
            print(f"{i+1}. {filme['nome']} ({filme['idade']} anos)")
        else:
            print(f"{i+1}. {filme['nome']} (idade mínima: {filme['idade']} anos)")

def escolher_filme():
    escolha = int(input("\nEscolha o número do filme desejado: ")) - 1
    return filmes[escolha] if 0 <= escolha < len(filmes) else None

def escrever_bilhete(filme, nome, idade):
    nome_arquivo = f"bilhete_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Idade: {idade}\n")
        arquivo.write(f"Filme: {filme['nome']}\n")
        arquivo.write(f"Data: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
    print(f"Bilhete gravado em {nome_arquivo}")

def main():
    nome, idade = obter_entrada_usuario()
    
    while True:
        mostrar_filmes(idade)
        filme = escolher_filme()
        
        if filme is None:
            print("Opção inválida!")
            continue
            
        if idade >= filme["idade"]:
            escrever_bilhete(filme, nome, idade)
            break
        else:
            print(f"Você não tem idade suficiente para assistir ao filme {filme['nome']}!")

if __name__ == "__main__":
    main()