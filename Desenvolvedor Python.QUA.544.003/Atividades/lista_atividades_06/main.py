from models import Conta

def main():
    # Instanciando uma nova conta bancária
    conta = Conta(
        titular="Jorge Pinheiro",
        cpf="123.456.789-00",
        agencia="0001",
        n_conta="12345-6",
        saldo=1000.00
    )

    print("--- CONSULTANDO DADOS DA CONTA ---")
    conta.consultar_conta()
    print()

    print("--- REALIZANDO DEPÓSITO ---")
    valor_deposito = 500.00
    conta.fazer_deposito(valor_deposito)
    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
    print(f"Novo saldo: R$ {conta.saldo:.2f}")
    print()

    print("--- REALIZANDO SAQUE ---")
    valor_saque = 200.00
    conta.fazer_saque(valor_saque)
    print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
    print(f"Novo saldo: R$ {conta.saldo:.2f}")
    print()

    print("--- GERANDO EXTRATO BANCÁRIO ---")
    nome_arquivo = "extrato_maria.txt"
    conta.gerar_extrato(nome_arquivo)
    print(f"Extrato gerado com sucesso no arquivo: '{nome_arquivo}'")

if __name__ == "__main__":
    main()