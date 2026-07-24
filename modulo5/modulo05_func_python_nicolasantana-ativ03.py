# Exercício 3: Encontre o maior e o menor
# Função maior_menor() que recebe uma lista de números e retorna o maior e o menor valor.

def maior_menor(lista_numeros):
    """
    Recebe uma lista de números e retorna uma tupla (maior, menor).
    """
    if not lista_numeros:
        return None, None
    
    maior = max(lista_numeros)
    menor = min(lista_numeros)
    
    return maior, menor

# Exemplo de uso:
if __name__ == "__main__":
    numeros = [15, 42, 3, 89, 23, 7, 99, 1]
    maior, menor = maior_menor(numeros)
    
    print(f"Lista de números: {numeros}")
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")