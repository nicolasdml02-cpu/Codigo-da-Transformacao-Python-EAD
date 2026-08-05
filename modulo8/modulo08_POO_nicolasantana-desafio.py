# exercicio4_desafio_biblioteca.py

class Livro:
    """
    Representa um livro individual com título, autor e estado de disponibilidade.
    """
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  # Todo livro começa como disponível

    def __str__(self) -> str:
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} [{status}]"


class Biblioteca:
    """
    Gerencia um acervo de livros e o fluxo de empréstimos/devoluções.
    """
    def __init__(self, nome: str):
        self.nome = nome
        self.acervo = []

    def adicionar_livro(self, livro: Livro):
        """Adiciona um objeto da classe Livro ao acervo."""
        self.acervo.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca '{self.nome}'.")

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

    def listar_acervo(self):
        """Exibe o estado de todos os livros no acervo."""
        print(f"\n--- Acervo da {self.nome} ---")
        if not self.acervo:
            print("Nenhum livro cadastrado.")
        for livro in self.acervo:
            print(f"- {livro}")
        print("-----------------------------\n")


# Exemplo de uso do sistema de biblioteca
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