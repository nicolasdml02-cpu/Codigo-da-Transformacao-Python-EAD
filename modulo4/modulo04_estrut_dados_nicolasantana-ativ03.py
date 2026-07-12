# Arquivo: pares_impares.py

# Conjunto de números inicial (pode ser alterado livremente)
numeros = [12, 7, 23, 44, 8, 15, 92, 31, 50]

# Listas auxiliares para armazenar a separação
pares = []
impares = []

# Loop para iterar e identificar cada número
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Exibindo os resultados
print(f"Conjunto original: {numeros}")
print(f"Números Pares: {pares}")
print(f"Números Ímpares: {impares}")