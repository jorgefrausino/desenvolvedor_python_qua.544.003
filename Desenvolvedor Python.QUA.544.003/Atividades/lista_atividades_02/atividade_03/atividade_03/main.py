# TODO: atividade 03
# Crie um programa que receba o nome de um aluno e 3 notas.
# O programa deve calcular a média do aluno e informar se
# o aluno está aprovado (média mínima = 7) ou reprovado.
# O programa deve gravar esses dados em um JSON.
# Ao final, o usuário deverá escolher se deseja inserir as
# notas de outro aluno, que deverão ser gravadas no mesmo
# arquivo JSON.

import json
import os

alunos = []
abrir = ""

os.system("cls" if os.name == "nt" else "clear")

while True:

    print(f"{'-'*20} CADASTRO DE ALUNOS {'-'*20}")
    print("1 - Cadastrar aluno")
    print("2 - Cadastrar outro aluno")
    print("3 - Consultar alunos")
    print("4 - Sair")

    opcao = input("Informe a opção desejada: ").strip()

    os.system("cls" if os.name == "nt" else "clear")

    if opcao == "1" or opcao == "2":

        aluno = {}

        aluno['nome'] = input("Informe o nome do aluno: ").strip().title()
        aluno['nota1'] = float(input("Informe a primeira nota: "))
        aluno['nota2'] = float(input("Informe a segunda nota: "))
        aluno['nota3'] = float(input("Informe a terceira nota: "))

