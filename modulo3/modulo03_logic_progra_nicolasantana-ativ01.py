# Solicitando os números ao usuário e convertendo para float (permite números com vírgula)
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realizando os cálculos aritméticos
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Tratamento para evitar erro de divisão por zero
if num2 != 0:
    divisao = num1 / num2
    resto = num1 % num2
else:
    divisao = "Não é possível dividir por zero"
    resto = "Não é possível calcular o resto por zero"

# Exibindo os resultados na tela
print("\n--- Resultados ---")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Resto da divisão: {resto}")