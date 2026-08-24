"""
Programa 3: Jogo de Adivinhação de Números
Arquivo independente utilizando random e math para interagir com o usuário.
"""

import random
import math

def iniciar_jogo():
    print("=" * 45)
    print("    BEM-VINDO AO JOGO DE ADIVINHAÇÃO    ")
    print("=" * 45)
    print("Tente adivinhar o número secreto entre 1 e 100!")
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10
    acertou = False

    # Dica calculada usando a biblioteca math
    raiz = round(math.sqrt(numero_secreto), 2)
    print(f"💡 DICA INICIAL: A raiz quadrada aproximada do número é {raiz}")
    print("-" * 45)

    while not acertou and tentativas < max_tentativas:
        try:
            chute = int(input(f"Digite o seu palpite (Tentativa {tentativas + 1}/{max_tentativas}): "))
            tentativas += 1

            if chute < 1 or chute > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue

            diferenca = abs(numero_secreto - chute)

            if chute == numero_secreto:
                acertou = True
                print(f"\n🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s)!")
            elif chute < numero_secreto:
                print(f"O número secreto é MAIOR que {chute}.")
            else:
                print(f"O número secreto é MENOR que {chute}.")

            if not acertou and diferenca <= 5:
                print("🔥 Você está MUITO PERTO! (Diferença de 5 unidades ou menos)")

        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

    if not acertou:
        print(f"\n❌ Você atingiu o limite de {max_tentativas} tentativas! O número secreto era {numero_secreto}.")

if __name__ == "__main__":
    iniciar_jogo()