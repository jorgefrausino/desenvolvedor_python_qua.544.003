# importação da biblioteca
import os 

# laço da repetição
while True:
    # limpa tela do terminal
    os.system("cls" if os.name == "nt" else "clear")

    # entrada de dados
    nome = input("Informe o nome: ").strip().title()
    idade = int(input("Informe a idade: "))
    cpf = input("Informe ocpf: ").strip()
    email = input("Informe o e-mai: ").strip().lower()

    os.system("cls" if os.name == "nt" else "clear")

    #saída de dados
    print(f"Nome: {nome}.")
    print(f"idade: {idade}.")
    print(f"cpf: {cpf}.")
    print(f"E-mai: {email}.")

    # menu
    print("1 - Informar dados de outro usuário")
    print("2 - Sair do programa")

    opcao = input("Informe a opção desejada: ").strip()

    match opcao:
        case "1":
            continue
        case "2":
            break
        case _:
            print("opção invalida.")