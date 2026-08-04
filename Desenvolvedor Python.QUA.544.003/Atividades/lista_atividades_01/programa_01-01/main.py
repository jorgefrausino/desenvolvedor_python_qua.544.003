# TODO: atividade 01
"""
Crie um programa que receba o nome, peso e altura do usuário e informe na tela o seu IMC o seu diagnóstico com base no valor do IMC.
"""

def calcular_imc(nome, peso, altura):
    """Calcula o IMC e fornece informações de diagnóstico."""
    # Converter altura de cm para metros
    altura_m = altura / 100
    
    # Calcular IMC
    imc = peso / (altura_m ** 2)
    
    # Determinar diagnóstico baseado nos intervalos de IMC
    if imc < 18.5:
        diagnostico = "Abaixo do peso"
    elif 18.5 <= imc < 25:
        diagnostico = "Peso normal"
    elif 25 <= imc < 30:
        diagnostico = "Sobrepeso"
    elif 30 <= imc < 35:
        diagnostico = "Obesidade grau I"
    elif 35 <= imc < 40:
        diagnostico = "Obesidade grau II"
    else:
        diagnostico = "Obesidade grau III"
    
    return {
        "nome": nome,
        "peso": peso,
        "altura": altura,
        "imc": round(imc, 2),
        "diagnostico": diagnostico
    }

def obter_entrada_usuario():
    """Obtém entrada do usuário para nome, peso e altura."""
    nome = input("Digite seu nome: ")
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (cm): "))
    return nome, peso, altura

def exibir_resultado(resultado):
    """Exibe o cálculo do IMC e o diagnóstico."""
    print("\n--- Resultado ---")
    print(f"Nome: {resultado['nome']}")
    print(f"Peso: {resultado['peso']} kg")
    print(f"Altura: {resultado['altura']} cm")
    print(f"IMC: {resultado['imc']}")
    print(f"Diagnóstico: {resultado['diagnostico']}")

def main():
    """Função principal para executar o calculador de IMC."""
    try:
        nome, peso, altura = obter_entrada_usuario()
        resultado = calcular_imc(nome, peso, altura)
        exibir_resultado(resultado)
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()