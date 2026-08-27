import sqlite3

def buscar_clientes_por_inicial(inicial):
    # Busca e exibe clientes cujo nome começa com a letra informada
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()
    
    # O operador LIKE com '%' busca registros que comecem com a inicial passada
    cursor.execute('SELECT * FROM Clientes WHERE nome LIKE ?', (f'{inicial}%',))
    resultados = cursor.fetchall()
    
    conn.close()
    return resultados

if __name__ == '__main__':
    letra = 'A'
    clientes_encontrados = buscar_clientes_por_inicial(letra)
    
    print(f"Clientes que começam com a letra '{letra}':")
    for cliente in clientes_encontrados:
        print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]}")