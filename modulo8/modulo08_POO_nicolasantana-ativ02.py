# exercicio2_carro_eletrico.py
from modulo08_POO_nicolasantana_ativ01 import Carro

class CarroEletrico(Carro):
    """
    Classe que representa um Carro Elétrico, herdando os atributos e métodos da classe Carro.
    """
    def __init__(self, marca: str, modelo: str, autonomia_bateria: int):
        # O método super() chama o construtor da classe pai (Carro)
        super().__init__(marca, modelo)
        # Atributo específico da classe filha (em km)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        """
        Sobrescreve o método da classe pai para incluir a autonomia da bateria.
        """
        print(f"Carro Elétrico: {self.marca} {self.modelo} | Autonomia: {self.autonomia_bateria} km")

# Teste da herança
if __name__ == "__main__":
    carro_ev = CarroEletrico(marca="Tesla", modelo="Model 3", autonomia_bateria=500)
    carro_ev.exibir_info()