# Arquivo: dados_alunos.py

# Criando o dicionário com as informações do aluno
aluno = {
    "nome": "Gabriel Silva",
    "idade": 19,
    "notas": [8.5, 7.0, 9.0]
}

# Calculando a média das notas para deixar o programa mais completo
media = sum(aluno["notas"]) / len(aluno["notas"])

# Exibindo os dados de forma organizada no console
print("--- DADOS DO ALUNO ---")
print(f"Nome do Aluno: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")
print(f"Notas: {aluno['notas']}")
print(f"Média Final: {media:.2f}")