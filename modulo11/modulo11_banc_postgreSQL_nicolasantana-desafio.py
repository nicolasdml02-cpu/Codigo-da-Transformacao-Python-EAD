import sqlite3

def inicializar_banco_tarefas():
    # Cria a tabela de tarefas caso ainda não exista
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_tarefa(descricao):
    # Cadastra uma nova tarefa no banco de dados
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Tarefas (descricao) VALUES (?)', (descricao,))
    conn.commit()
    conn.close()
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

def visualizar_tarefas():
    # Exibe todas as tarefas pendentes
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Tarefas')
    tarefas = cursor.fetchall()
    conn.close()
    
    print("\n--- LISTA DE TAREFAS ---")
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    for t in tarefas:
        print(f"[{t[0]}] {t[1]}")

def excluir_tarefa(id_tarefa):
    # Exclui uma tarefa do banco pelo seu ID
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Tarefas WHERE id = ?', (id_tarefa,))
    conn.commit()
    conn.close()
    print(f"Tarefa ID {id_tarefa} excluída com sucesso!")

if __name__ == '__main__':
    inicializar_banco_tarefas()
    
    # Exemplo de uso do sistema de tarefas
    adicionar_tarefa("Estudar Python e SQLite")
    adicionar_tarefa("Enviar atividade para o professor")
    
    visualizar_tarefas()
    
    excluir_tarefa(1)
    
    visualizar_tarefas()