"""
Programa 2: Manipulação de Datas
Arquivo independente que realiza cálculos e formatação de datas usando datetime.
"""

from datetime import datetime, timedelta

def exibir_relatorio_datas():
    agora = datetime.now()
    
    print("=== RELATÓRIO DE DATAS E HORÁRIOS ===")
    print(f"Data e Hora atual: {agora.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Dia da semana: {agora.strftime('%A')}")
    
    # Adicionando dias para simular prazo
    prazo_entrega = agora + timedelta(days=15)
    print(f"Prazo de entrega (+15 dias): {prazo_entrega.strftime('%d/%m/%Y')}")
    
    # Cálculo de dias decorridos a partir de uma data específica
    data_inicio_curso = datetime(2026, 1, 15)
    dias_decorridos = (agora - data_inicio_curso).days
    print(f"Dias decorridos desde o início das aulas (15/01/2026): {dias_decorridos} dias")
    print("======================================")

if __name__ == "__main__":
    exibir_relatorio_datas()