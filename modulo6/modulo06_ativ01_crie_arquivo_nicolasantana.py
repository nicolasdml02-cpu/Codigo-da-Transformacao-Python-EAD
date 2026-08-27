# Atividade 1: Manipulação de Arquivo TXT

def escrever_arquivo(nome_arquivo, conteudo):
    # Função para escrever uma mensagem/conteúdo dentro de um arquivo de texto (.txt)
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)
    print(f"Conteúdo salvo com sucesso em '{nome_arquivo}'.")

def ler_arquivo(nome_arquivo):
    # Função para ler e exibir na tela o conteúdo de um arquivo de texto (.txt)
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print("\n--- Conteúdo do Arquivo TXT ---")
            print(conteudo)
            print("--------------------------------\n")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")

# Execução do programa
if __name__ == "__main__":
    arquivo_txt = "exemplo.txt"
    texto_exemplo = "Olá! Este é um arquivo de texto criado para demonstrar a leitura e escrita em Python."
    
    escrever_arquivo(arquivo_txt, texto_exemplo)
    ler_arquivo(arquivo_txt)