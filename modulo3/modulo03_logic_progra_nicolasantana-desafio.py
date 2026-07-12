# Inicializando o loop como Verdadeiro para o menu rodar continuamente
opcao = ""

while opcao != "3":
    # Exibindo o menu interativo no console
    print("\n======== MENU DA CALCULADORA ========")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Sair")
    opcao = input("Escolha uma opção (1, 2 ou 3): ")

    # Processando a escolha do usuário
    if opcao == "1":
        print("\n--- Operação de Soma ---")
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print(f"Resultado da Soma: {n1 + n2}")
        
    elif opcao == "2":
        print("\n--- Operação de Subtração ---")
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print(f"Resultado da Subtração: {n1 - n2}")
        
    elif opcao == "3":
        print("\nSaindo do programa... Até logo!")
        
    else:
        print("\nOpção inválida! Por favor, escolha 1, 2 ou 3.")