# exercicio4_desafio_biblioteca.py

# Define a estrutura de um livro individual
class Livro:
    """
    Representa um livro individual com título, autor e estado de disponibilidade.
    """
    # Método construtor: inicializa título, autor e marca a disponibilidade como True
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  # Todo livro começa como disponível

    # Retorna o título, autor e estado atual do livro formatados em texto
    def __str__(self) -> str:
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} [{status}]"


# Gerencia o conjunto de livros e as operações de empréstimo e devolução
class Biblioteca:
    """
    Gerencia um acervo de livros e o fluxo de empréstimos/devoluções.
    """
    # Método construtor: inicializa o nome da biblioteca e a lista do acervo vazia
    def __init__(self, nome: str):
        self.nome = nome
        self.acervo = []

    # Insere um objeto Livro na lista do acervo
    def adicionar_livro(self, livro: Livro):
        """Adiciona um objeto da classe Livro ao acervo."""
        self.acervo.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca '{self.nome}'.")

    # Localiza o livro pelo título e altera sua disponibilidade para False, se possível
    def emprestar_livro(self, titulo: str):
        """Busca o livro pelo título e realiza o empréstimo se disponível."""
        for livro in self.acervo:
            if livro.titulo.lower() == titulo.lower():
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"Sucesso: O livro '{livro.titulo}' foi emprestado.")
                    return
                else:
                    print(f"Aviso: O livro '{livro.titulo}' já está emprestado no momento.")
                    return
        print(f"Erro: O livro '{titulo}' não foi encontrado no acervo.")

    # Localiza o livro pelo título e altera sua disponibilidade para True, se estiver emprestado
    def devolver_livro(self, titulo: str):
        """Devolve um livro emprestado de volta ao acervo."""
        for livro in self.acervo:
            if livro.titulo.lower() == titulo.lower():
                if not livro.disponivel:
                    livro.disponivel = True
                    print(f"Sucesso: O livro '{livro.titulo}' foi devolvido.")
                    return
                else:
                    print(f"Aviso: O livro '{livro.titulo}' já estava na biblioteca.")
                    return
        print(f"Erro: O livro '{titulo}' não foi encontrado no acervo.")

    # Percorre e imprime no terminal a informação de todos os livros cadastrados
    def listar_acervo(self):
        """Exibe o estado de todos os livros no acervo."""
        print(f"\n--- Acervo da {self.nome} ---")
        if not self.acervo:
            print("Nenhum livro cadastrado.")
        for livro in self.acervo:
            print(f"- {livro}")
        print("-----------------------------\n")


# Ponto de entrada do script: simula o fluxo completo de cadastro, empréstimo e devolução de livros
if __name__ == "__main__":
    # Instanciando a biblioteca
    minha_biblioteca = Biblioteca("Biblioteca Central")

    # Criando alguns livros
    livro1 = Livro("Dom Casmurro", "Machado de Assis")
    livro2 = Livro("1984", "George Orwell")

    # Adicionando ao acervo
    minha_biblioteca.adicionar_livro(livro1)
    minha_biblioteca.adicionar_livro(livro2)

    # Exibindo status inicial
    minha_biblioteca.listar_acervo()

    # Realizando operações
    minha_biblioteca.emprestar_livro("1984")
    minha_biblioteca.listar_acervo()

    # Tentativa de emprestar novamente o mesmo livro
    minha_biblioteca.emprestar_livro("1984")

    # Devolvendo o livro
    minha_biblioteca.devolver_livro("1984")
    minha_biblioteca.listar_acervo()