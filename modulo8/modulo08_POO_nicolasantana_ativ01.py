# exercicio1_carro.py

# Define a estrutura e os comportamentos de um carro
class Carro:
    """
    Classe base para representar um carro comum.
    """
    # Método construtor: inicializa a marca e o modelo ao criar um novo objeto
    def __init__(self, marca: str, modelo: str):
        # Inicialização dos atributos básicos do carro
        self.marca = marca
        self.modelo = modelo

    # Exibe as informações formatadas do carro no terminal
    def exibir_info(self):
        """
        Método responsável por exibir no terminal os dados do carro.
        """
        print(f"Carro: {self.marca} {self.modelo}")

# Ponto de entrada do script: cria uma instância de Carro e executa o teste apenas se o arquivo for rodado diretamente
if __name__ == "__main__":
    meu_carro = Carro(marca="Toyota", modelo="Supra Mk4")
    meu_carro.exibir_info()