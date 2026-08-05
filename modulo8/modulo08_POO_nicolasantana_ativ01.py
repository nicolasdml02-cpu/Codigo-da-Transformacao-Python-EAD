# exercicio1_carro.py

class Carro:
    """
    Classe base para representar um carro comum.
    """
    def __init__(self, marca: str, modelo: str):
        # Inicialização dos atributos básicos do carro
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        """
        Método responsável por exibir no terminal os dados do carro.
        """
        print(f"Carro: {self.marca} {self.modelo}")

# Teste da classe (executado ao rodar o arquivo)
if __name__ == "__main__":
    meu_carro = Carro(marca="Toyota", modelo="Supra Mk4")
    meu_carro.exibir_info()