"""
Programa 4: Estruturação e Organização de Projetos
Demonstração independente do Desafio Extra simulando uma estrutura organizada.
"""

class CalculadoraGeometria:
    """Classe responsável por cálculos geométricos."""
    @staticmethod
    def area_retangulo(largura, altura):
        return largura * altura

    @staticmethod
    def perimetro_retangulo(largura, altura):
        return 2 * (largura + altura)


class ConversorUnidades:
    """Classe responsável por conversões de medida."""
    @staticmethod
    def celsius_para_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def km_para_milhas(km):
        return km * 0.621371


def executar_sistema():
    print("=== SISTEMA INDEPENDENTE DE MÓDULOS E PACOTES ===")
    
    # Testando geometria
    largura, altura = 10, 5
    area = CalculadoraGeometria.area_retangulo(largura, altura)
    perimetro = CalculadoraGeometria.perimetro_retangulo(largura, altura)
    print(f"Retângulo {largura}x{altura} -> Área: {area} | Perímetro: {perimetro}")

    # Testando conversões
    temp_c = 25
    distancia_km = 100
    print(f"Temperatura: {temp_c}°C = {ConversorUnidades.celsius_para_fahrenheit(temp_c)}°F")
    print(f"Distância: {distancia_km} km = {ConversorUnidades.km_para_milhas(distancia_km):.2f} milhas")
    print("=================================================")

if __name__ == "__main__":
    executar_sistema()