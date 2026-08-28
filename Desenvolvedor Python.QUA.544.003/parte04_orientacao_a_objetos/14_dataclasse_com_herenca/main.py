import os

from models import PessoaFisica, PessoaJuridica


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = PessoaFisica(
            nome="",cpf="",profissao="",idade=0,salario=0.0,telefone="",email=""
    )
    empresa = PessoaJuridica(
            razao_social="",nome_fantasia="",cnpj="",valor_mercado=0.0,telefone="",email=""
    )

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.profissao = input("Informe a profissão do usuário: ")
    usuario.idade = int(input("Informe a idade: "))
    usuario.telefone = input("Informe o telefone do usuário: ").strip().lower()
    usuario.email = input("Informe o e-mail do ")
   
    

if __name__ == "__main__":
    main()
