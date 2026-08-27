"""
Programa 2: Manipulação de Datas
Arquivo independente que realiza cálculos e formatação de datas usando datetime.
"""

from datetime import datetime, timedelta

# Obtém a data e hora atual e exibe um relatório com cálculos de prazos e dias decorridos
def exibir_relatorio_datas():
    # Captura o momento exato do sistema (data e hora atuais)
    agora = datetime.now()
    
    print("=== RELATÓRIO DE DATAS E HORÁRIOS ===")
    # Formata e exibe a data e hora no padrão brasileiro (DD/MM/AAAA HH:MM:SS)
    print(f"Data e Hora atual: {agora.strftime('%d/%m/%Y %H:%M:%S')}")
    # Exibe o nome do dia da semana correspondente
    print(f"Dia da semana: {agora.strftime('%A')}")
    
    # Calcula uma data futura somando 15 dias à data atual
    prazo_entrega = agora + timedelta(days=15)
    print(f"Prazo de entrega (+15 dias): {prazo_entrega.strftime('%d/%m/%Y')}")
    
    # Define uma data fixa e calcula quantos dias se passaram até a data atual
    data_inicio_curso = datetime(2026, 1, 15)
    dias_decorridos = (agora - data_inicio_curso).days
    print(f"Dias decorridos desde o início das aulas (15/01/2026): {dias_decorridos} dias")
    print("======================================")

# Ponto de entrada do script: executa o relatório apenas se o arquivo for rodado diretamente
if __name__ == "__main__":
    exibir_relatorio_datas()