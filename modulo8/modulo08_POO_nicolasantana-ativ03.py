# exercicio3_metodos_especiais.py

class CarroEspecial:
    """
    Demonstração do uso dos métodos especiais __init__ e __str__.
    """
    def __init__(self, marca: str, modelo: str, autonomia_bateria: int = None):
        self.marca = marca
        self.modelo = modelo
        self.autonomia_bateria = autonomia_bateria

    def __str__(self) -> str:
        """
        O método __str__ é invocado quando usamos print(objeto) ou str(objeto).
        Retorna uma representação amigável do objeto.
        """
        if self.autonomia_bateria:
            return f"[Elétrico] {self.marca} {self.modelo} - Autonomia: {self.autonomia_bateria}km"
        return f"[Combustão] {self.marca} {self.modelo}"

# Teste da representação do objeto
if __name__ == "__main__":
    carro_combustao = CarroEspecial("Ford", "Mustang")
    carro_eletrico = CarroEspecial("BYD", "Seal", 520)

    # Ao utilizar print(), o Python invoca automaticamente o método __str__
    print(carro_combustao)
    print(carro_eletrico)