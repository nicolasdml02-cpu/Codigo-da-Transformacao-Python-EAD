"""
Programa 4: Estruturação e Organização de Projetos
Demonstração independente do Desafio Extra simulando uma estrutura organizada.
"""

# Classe agrupando métodos de cálculos geométricos
class CalculadoraGeometria:
    """Classe responsável por cálculos geométricos."""
    
    # Calcula e retorna a área de um retângulo (largura * altura)
    @staticmethod
    def area_retangulo(largura, altura):
        return largura * altura

    # Calcula e retorna o perímetro de um retângulo (2 * (largura + altura))
    @staticmethod
    def perimetro_retangulo(largura, altura):
        return 2 * (largura + altura)


# Classe agrupando métodos para conversão de unidades de medida
class ConversorUnidades:
    """Classe responsável por conversões de medida."""
    
    # Converte uma temperatura de Celsius para Fahrenheit
    @staticmethod
    def celsius_para_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    # Converte uma distância de quilômetros para milhas
    @staticmethod
    def km_para_milhas(km):
        return km * 0.621371


# Função principal que executa a demonstração do sistema
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

# Ponto de entrada do script: executa o sistema apenas se o arquivo for rodado diretamente
if __name__ == "__main__":
    executar_sistema()