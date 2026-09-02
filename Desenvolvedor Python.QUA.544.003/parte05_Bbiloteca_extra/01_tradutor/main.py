from deep_translator import GoogleTranslator

import os


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

    def traduzir(texto):
        tradutor = GoogleTranslator(source="auto",target="pt")
        return tradutor.translate(texto)

    def main():
        limpar()
        while True:
            print("0 - Sair do programa")
            print("1 - Traduzir texto para o português")
            opcao = input("Informe a opção desejada: ").strip()
            limpar()
            if opcao == "0":
                break
            elif opcao == "1":
                texto = input("Informe o texto a ser traduzido: ")
                limpar()
                texto_traduzido = traduzir(texto)
                print(traduzir(texto))
                continue
            else:
                print("Opção inválida.")


    if __name__ == "__main__":
        main()