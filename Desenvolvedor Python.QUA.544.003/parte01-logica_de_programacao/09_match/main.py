# entrada de dados
x = float(input("Informe o valor de x: ").replace(",","."))
y = float(input("Informe o valor de y: ").replace(",","."))

# menu
print("1 - somar")
print("2 - subtrair")
print("3 - multiplicar")
print("4 - dividir")

opcao = input("Informe a opção desejada: ").strip()

match opcao:
    case "1":
        print(f"A soma é {x+y}.")
    case "2":
        print(f"A subtração é {x-y}.")
    case "3":
        print(f"A multiplicação é {x*y}.")
    case "4":
        print(f"A divisão é {x/y}.")
    case _:
        print("Opção invalida.")
