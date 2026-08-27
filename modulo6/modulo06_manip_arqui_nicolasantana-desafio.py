# Atividade 4 (Desafio Extra): Sistema de Backup Automático com shutil
import shutil
import os

def criar_backup(pasta_origem, pasta_destino):
    # Função para copiar todos os arquivos de uma pasta de origem para uma pasta de destino
    if not os.path.exists(pasta_origem):
        print(f"A pasta de origem '{pasta_origem}' não existe. Criando pasta de demonstração...")
        os.makedirs(pasta_origem)
        # Cria um arquivo de teste dentro da origem se estiver vazia
        with open(os.path.join(pasta_origem, "documento.txt"), "w") as f:
            f.write("Arquivo de teste para o backup.")

    # Copia toda a pasta de origem para a pasta de destino
    shutil.copytree(pasta_origem, pasta_destino, dirs_exist_ok=True)
    print(f"Backup realizado com sucesso! Conteúdo copiado de '{pasta_origem}' para '{pasta_destino}'.")

# Execução do programa
if __name__ == "__main__":
    origem = "pasta_origem"
    destino = "pasta_backup"
    
    criar_backup(origem, destino)