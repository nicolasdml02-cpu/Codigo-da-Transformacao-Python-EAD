# Recebendo os dois números do usuário
numero_a = float(input("Digite o primeiro número: "))
numero_b = float(input("Digite o segundo número: "))

# Comparando os números utilizando a estrutura condicional if
if numero_a > numero_b:
    print(f"O maior número é o primeiro: {numero_a}")
elif numero_b > numero_a:
    print(f"O maior número é o segundo: {numero_b}")
else:
    print("Os dois números são iguais.")