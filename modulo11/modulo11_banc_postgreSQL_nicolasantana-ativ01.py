import sqlite3

def criar_banco_e_tabela():
    # Conecta ao banco de dados (cria o arquivo se não existir) e cria a tabela Clientes
    conexao = sqlite3.connect('empresa.db')
    cursor = conexao.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    
    conexao.commit()
    conexao.close()
    print("Banco de dados e tabela 'Clientes' criados com sucesso!")

if __name__ == '__main__':
    criar_banco_e_tabela()