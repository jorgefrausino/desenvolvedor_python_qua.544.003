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

# Define movie data
movies = [
    {"name": "A Volta dos Que Não Foram", "age": 0},
    {"name": "A Roda Quadrada", "age": 12},
    {"name": "As Trnças do Rei Careca", "age": 14},
    {"name": "Poeira em Alto Mar", "age": 16},
    {"name": "A Vingança do frango Assado", "age": 18}
]

def get_user_input():
    name = input("Digite seu nome: ")
    age = int(input("Digite sua idade: "))
    return name, age

def show_movies(age):
    print("\nFilmes em cartaz:")
    for i, movie in enumerate(movies):
        if age >= movie["age"]:
            print(f"{i+1}. {movie['name']} ({movie['age']} anos)")
        else:
            print(f"{i+1}. {movie['name']} (idade mínima: {movie['age']} anos)")

def choose_movie():
    choice = int(input("\nEscolha o número do filme desejado: ")) - 1
    return movies[choice] if 0 <= choice < len(movies) else None

def write_ticket(movie, name, age):
    filename = f"bilhete_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    with open(filename, 'w') as file:
        file.write(f"Nome: {name}\n")
        file.write(f"Idade: {age}\n")
        file.write(f"Filme: {movie['name']}\n")
        file.write(f"Data: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
    print(f"Bilhete gravado em {filename}")

def main():
    name, age = get_user_input()
    
    while True:
        show_movies(age)
        movie = choose_movie()
        
        if movie is None:
            print("Opção inválida!")
            continue
            
        if age >= movie["age"]:
            write_ticket(movie, name, age)
            break
        else:
            print(f"Você não tem idade suficiente para assistir ao filme {movie['name']}!")

if __name__ == "__main__":
    main()