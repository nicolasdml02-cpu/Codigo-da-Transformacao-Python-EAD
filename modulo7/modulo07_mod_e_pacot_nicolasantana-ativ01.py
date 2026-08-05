"""
Programa 1: Funções Matemáticas
Arquivo totalmente independente contendo operações matemáticas e testes integrados.
"""

import math

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def calcular_area_circulo(raio):
    if raio < 0:
        raise ValueError("O raio não pode ser negativo.")
    return math.pi * (raio ** 2)

def eh_par(numero):
    return numero % 2 == 0

def executar_demonstracao():
    print("=== MÓDULO DE UTILIDADES MATEMÁTICAS ===")
    
    n1, n2 = 15, 4
    print(f"Soma ({n1} + {n2}): {somar(n1, n2)}")
    print(f"Subtração ({n1} - {n2}): {subtrair(n1, n2)}")
    print(f"Multiplicação ({n1} * {n2}): {multiplicar(n1, n2)}")
    print(f"Divisão ({n1} / {n2}): {dividir(n1, n2):.2f}")
    
    raio = 5
    area = calcular_area_circulo(raio)
    print(f"Área de um círculo com raio {raio}: {area:.2f}")

    numero_teste = 42
    print(f"O número {numero_teste} é par? {eh_par(numero_teste)}")
    print("=========================================")

if __name__ == "__main__":
    executar_demonstracao()