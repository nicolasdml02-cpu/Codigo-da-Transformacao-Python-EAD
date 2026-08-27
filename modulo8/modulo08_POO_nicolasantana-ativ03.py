# exercicio3_metodos_especiais.py

# Define uma classe para demonstrar o uso de métodos especiais do Python
class CarroEspecial:
    """
    Demonstração do uso dos métodos especiais __init__ e __str__.
    """
    # Método construtor: inicializa marca, modelo e opcionalmente a autonomia da bateria
    def __init__(self, marca: str, modelo: str, autonomia_bateria: int = None):
        self.marca = marca
        self.modelo = modelo
        self.autonomia_bateria = autonomia_bateria

    # Método especial que define a representação em texto do objeto ao ser impresso
    def __str__(self) -> str:
        """
        O método __str__ é invocado quando usamos print(objeto) ou str(objeto).
        Retorna uma representação amigável do objeto.
        """
        # Retorna o formato para carro elétrico caso a autonomia seja informada
        if self.autonomia_bateria:
            return f"[Elétrico] {self.marca} {self.modelo} - Autonomia: {self.autonomia_bateria}km"
        # Retorna o formato padrão para carro a combustão
        return f"[Combustão] {self.marca} {self.modelo}"

# Ponto de entrada do script: cria e exibe dois carros para testar o método __str__
if __name__ == "__main__":
    carro_combustao = CarroEspecial("Ford", "Mustang")
    carro_eletrico = CarroEspecial("BYD", "Seal", 520)

    # Ao utilizar print(), o Python invoca automaticamente o método __str__
    print(carro_combustao)
    print(carro_eletrico)