# Exercício 1: Crie sua primeira função
# Função chamada saudacao() que recebe um nome e imprime uma mensagem personalizada.

def saudacao(nome):
    """
    Função que recebe o nome de uma pessoa e exibe uma saudação personalizada.
    """
    print(f"Olá, {nome}! Seja muito bem-vindo(a) aos estudos de Python!")

# Exemplo de uso:
if __name__ == "__main__":
    nome_usuario = input("Digite o seu nome: ")
    saudacao(nome_usuario)