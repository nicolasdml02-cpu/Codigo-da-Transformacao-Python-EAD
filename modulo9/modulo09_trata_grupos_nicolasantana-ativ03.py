def cadastrar_idade():
    while True:
        try:
            idade_input = input("Por favor, digite a sua idade: ")
            idade = int(idade_input)

            if idade <= 0:
                print("Erro: A idade deve ser um número inteiro estritamente positivo (maior que zero). Try again!\n")
                continue

            print(f"Sucesso! Idade cadastrada com sucesso: {idade} anos.")
            return idade

        except ValueError:
            print("Erro: Digite um número inteiro válido para a idade.\n")

if __name__ == "__main__":
    cadastrar_idade()