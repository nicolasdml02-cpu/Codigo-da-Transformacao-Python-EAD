"""
Programa 3: Jogo de Adivinhação de Números
Arquivo independente utilizando random e math para interagir com o usuário.
"""

import random
import math

# Executa a lógica principal do jogo de adivinhação e controla as tentativas do jogador
def iniciar_jogo():
    print("=" * 45)
    print("    BEM-VINDO AO JOGO DE ADIVINHAÇÃO    ")
    print("=" * 45)
    print("Tente adivinhar o número secreto entre 1 e 100!")
    
    # Sorteia o número secreto e define os parâmetros do jogo
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10
    acertou = False

    # Calcula e exibe a raiz quadrada do número secreto como dica inicial
    raiz = round(math.sqrt(numero_secreto), 2)
    print(f"💡 DICA INICIAL: A raiz quadrada aproximada do número é {raiz}")
    print("-" * 45)

    # Loop principal que roda até o jogador acertar ou atingir o limite de tentativas
    while not acertou and tentativas < max_tentativas:
        try:
            # Captura o palpite do usuário e incrementa o contador
            chute = int(input(f"Digite o seu palpite (Tentativa {tentativas + 1}/{max_tentativas}): "))
            tentativas += 1

            # Valida se o número está dentro do intervalo permitido (1 a 100)
            if chute < 1 or chute > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue

            # Calcula a distância absoluta entre o chute e o número secreto
            diferenca = abs(numero_secreto - chute)

            # Verifica o palpite e fornece dicas se o número é maior ou menor
            if chute == numero_secreto:
                acertou = True
                print(f"\n🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s)!")
            elif chute < numero_secreto:
                print(f"O número secreto é MAIOR que {chute}.")
            else:
                print(f"O número secreto é MENOR que {chute}.")

            # Dá um alerta extra se o jogador estiver muito perto do número secreto
            if not acertou and diferenca <= 5:
                print("🔥 Você está MUITO PERTO! (Diferença de 5 unidades ou menos)")

        # Trata erros caso o usuário digite texto em vez de número
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

    # Mensagem exibida caso as tentativas se esgotem sem acerto
    if not acertou:
        print(f"\n❌ Você atingiu o limite de {max_tentativas} tentativas! O número secreto era {numero_secreto}.")

# Ponto de entrada do script: executa o jogo apenas se o arquivo for rodado diretamente
if __name__ == "__main__":
    iniciar_jogo()