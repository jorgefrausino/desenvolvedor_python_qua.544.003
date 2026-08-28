from dataclasses import dataclass

@dataclass
class pessoa:
    telefone: str
    email: str

    def __str__(self):
        return f"Telefone: {self.telefone}\nE-mail: {self.email}"

    def __del__(self):
        print(f"Objeto (self) foi morto com sucesso!")

@dataclass
class PessoaFisica(pessoa):
    nome: str
    cpf: str
    profissao: str
    idade: int
    salario: float







    
















