# Desafio Extra: Saudação com Hora Atual
# Complemente o programa anterior exibindo também a hora atual ao lado da mensagem.
from datetime import datetime

# Obtém a hora atual do sistema
hora_atual = datetime.now().strftime("%H:%M:%S")

nome = input("Digite o seu nome: ")
print(f"Olá, {nome}! Seja bem-vindo(a)! Agora são {hora_atual}.")