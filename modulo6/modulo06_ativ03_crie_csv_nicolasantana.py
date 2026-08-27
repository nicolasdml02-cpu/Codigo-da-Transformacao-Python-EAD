# Atividade 3: Sistema de Notas de Alunos em CSV
import csv

def adicionar_nota(nome_arquivo, aluno, disciplina, nota):
    # Função para adicionar o registro de nota de um aluno no final do arquivo .csv
    with open(nome_arquivo, 'a', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([aluno, disciplina, nota])
    print(f"Nota de {aluno} gravada no CSV com sucesso.")

def carregar_notas(nome_arquivo):
    # Função para ler todas as notas registradas no arquivo .csv e exibi-las na tela
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            print("\n--- Sistema de Notas (CSV) ---")
            for linha in leitor:
                if linha:  # Evita linhas em branco
                    print(f"Aluno: {linha[0]} | Disciplina: {linha[1]} | Nota: {linha[2]}")
            print("------------------------------\n")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")

# Execução do programa
if __name__ == "__main__":
    arquivo_csv = "notas.csv"
    
    # Criando o arquivo e adicionando algumas notas de exemplo
    adicionar_nota(arquivo_csv, "Nicolas Santana", "Programação Python", "9.5")
    adicionar_nota(arquivo_csv, "Ivan Paulino", "Programação Python", "8.0")
    adicionar_nota(arquivo_csv, "Vocação", "Banco de Dados", "10.0")
    
    # Lendo o arquivo CSV gerado
    carregar_notas(arquivo_csv)