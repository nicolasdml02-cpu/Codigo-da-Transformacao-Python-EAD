# Atividade 2: Manipulação de Arquivo JSON com Dicionário de Clientes
import json

def salvar_clientes(nome_arquivo, dicionario_clientes):
    # Função para salvar um dicionário contendo dados de clientes em um arquivo .json
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dicionario_clientes, arquivo, indent=4, ensure_ascii=False)
    print(f"Dados dos clientes salvos em '{nome_arquivo}'.")

def carregar_clientes(nome_arquivo):
    # Função para carregar e retornar o dicionário de clientes salvo no arquivo .json
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            print("\n--- Clientes Carregados do JSON ---")
            for id_cliente, info in dados.items():
                print(f"ID: {id_cliente} | Nome: {info['nome']} | E-mail: {info['email']}")
            print("-----------------------------------\n")
            return dados
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None

# Execução do programa
if __name__ == "__main__":
    arquivo_json = "clientes.json"
    
    clientes_dados = {
        "CLI001": {"nome": "Nicolas Santana", "email": "nicolas@email.com"},
        "CLI002": {"nome": "Ivan Paulino", "email": "Ivan@email.com"},
        "CLI003": {"nome": "Vocação", "email": "vocacao@email.com"}
    }
    
    salvar_clientes(arquivo_json, clientes_dados)
    carregar_clientes(arquivo_json)