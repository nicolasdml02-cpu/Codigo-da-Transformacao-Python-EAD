# Solicitando a idade da pessoa (número inteiro)
idade = int(input("Digite a idade da pessoa: "))

# Classificando a idade com base nas faixas etárias usuais
if idade < 0:
    print("Idade inválida! Digite um valor maior ou igual a zero.")
elif idade <= 12:
    print("Classificação: Criança")
elif idade <= 17:
    print("Classificação: Adolescente")
elif idade <= 59:
    print("Classificação: Adulto")
else:
    print("Classificação: Idoso")