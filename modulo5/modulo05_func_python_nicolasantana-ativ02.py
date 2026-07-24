# Exercício 2: Calcule a média de alunos (Versão Atualizada)
# O usuário digita as notas, o programa calcula a média e verifica se a média é >= 6.0 para aprovação.

def calcular_media(notas, media_corte=6.0):
    """
    Recebe uma lista de notas, calcula a média e exibe o resultado final.
    """
    if not notas:
        print("Nenhuma nota foi informada.")
        return
    
    media = sum(notas) / len(notas)
    
    print("--- RESULTADO FINAL ---")
    print(f"Média apurada: {media:.2f}")
    
    if media >= media_corte:
        print("Status: APROVADO!")
    else:
        print("Status: REPROVADO.")

# Exemplo de uso interativo:
if __name__ == "__main__":
    print("--- SISTEMA DE NOTAS DO ALUNO ---")
    
    notas = []
    
    # Pergunta quantas notas o usuário deseja inserir
    qtd_notas = int(input("Quantas notas você deseja cadastrar? "))
    
    for i in range(1, qtd_notas + 1):
        nota = float(input(f"Digite a nota {i}: "))
        notas.append(nota)
    
    # Chama a função para calcular e exibir o status
    calcular_media(notas)