# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.

import math

def calcular_area_base(raio):
    """Calcula a área da base de um círculo dado o raio."""
    return math.pi * raio ** 2

def calcular_volume_cilindro(raio, altura):
    """Calcula o volume de um cilindro utilizando a área da base."""
    return calcular_area_base(raio) * altura

def main():
    # Entrada do usuário
    raio = float(input("Digite o raio do cilindro: "))
    altura = float(input("Digite a altura do cilindro: "))

    # Cálculos
    area_base = calcular_area_base(raio)
    volume = calcular_volume_cilindro(raio, altura)

    # Resultados
    print(f"A área da base do cilindro é: {area_base:.2f}")
    print(f"O volume do cilindro é: {volume:.2f}")

if __name__ == "__main__":
    main()