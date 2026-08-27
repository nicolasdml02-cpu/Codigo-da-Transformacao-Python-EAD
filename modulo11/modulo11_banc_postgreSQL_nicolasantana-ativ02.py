import sqlite3

def conectar():
    # Retorna uma conexão ativa com o banco de dados
    return sqlite3.connect('empresa.db')

def inserir_cliente(nome, email):
    # Insere um novo cliente na tabela
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Clientes (nome, email) VALUES (?, ?)', (nome, email))
    conn.commit()
    conn.close()
    print(f"Cliente '{nome}' inserido com sucesso!")

def listar_clientes():
    # Consulta e exibe todos os clientes cadastrados
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Clientes')
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def atualizar_email(id_cliente, novo_email):
    # Atualiza o e-mail de um cliente pelo ID
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('UPDATE Clientes SET email = ? WHERE id = ?', (novo_email, id_cliente))
    conn.commit()
    conn.close()
    print(f"E-mail do cliente ID {id_cliente} atualizado!")

def deletar_cliente(id_cliente):
    # Remove um cliente da tabela pelo ID
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Clientes WHERE id = ?', (id_cliente,))
    conn.commit()
    conn.close()
    print(f"Cliente ID {id_cliente} removido!")

if __name__ == '__main__':
    inserir_cliente('Nicolas Santana', 'nicolas@email.com')
    inserir_cliente('Ivan Paulino', 'ivan@email.com')
    
    print("\nLista de Clientes:", listar_clientes())
    
    atualizar_email(1, 'nicolas.santana@novoemail.com')
    deletar_cliente(2)
    
    print("\nLista Atualizada:", listar_clientes())