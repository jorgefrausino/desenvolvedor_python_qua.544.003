# TODO: atividade 01
"""
Crie um programa que receba o nome, peso e altura do usuário e informe na tela o seu IMC o seu diagnóstico com base no valor do IMC.
"""

def calculate_bmi(name, weight, height):
    """Calculate BMI and provide diagnostic information."""
    # Convert height from cm to meters
    height_m = height / 100
    
    # Calculate BMI
    bmi = weight / (height_m ** 2)
    
    # Determine diagnosis based on BMI ranges
    if bmi < 18.5:
        diagnosis = "Abaixo do peso"
    elif 18.5 <= bmi < 25:
        diagnosis = "Peso normal"
    elif 25 <= bmi < 30:
        diagnosis = "Sobrepeso"
    elif 30 <= bmi < 35:
        diagnosis = "Obesidade grau I"
    elif 35 <= bmi < 40:
        diagnosis = "Obesidade grau II"
    else:
        diagnosis = "Obesidade grau III"
    
    return {
        "name": name,
        "weight": weight,
        "height": height,
        "bmi": round(bmi, 2),
        "diagnosis": diagnosis
    }

def get_user_input():
    """Get user input for name, weight, and height."""
    name = input("Digite seu nome: ")
    weight = float(input("Digite seu peso (kg): "))
    height = float(input("Digite sua altura (cm): "))
    return name, weight, height

def display_result(result):
    """Display the BMI calculation and diagnosis."""
    print("\n--- Resultado ---")
    print(f"Nome: {result['name']}")
    print(f"Peso: {result['weight']} kg")
    print(f"Altura: {result['height']} cm")
    print(f"IMC: {result['bmi']}")
    print(f"Diagnóstico: {result['diagnosis']}")

def main():
    """Main function to run the BMI calculator."""
    try:
        name, weight, height = get_user_input()
        result = calculate_bmi(name, weight, height)
        display_result(result)
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()