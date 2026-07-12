# Arquivo: lista_compras.py

lista_compras = []

while True:
    print("\n--- LISTA DE COMPRAS ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Visualizar lista")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        item = input("Digite o nome do item para adicionar: ").strip()
        if item:
            lista_compras.append(item)
            print(f"'{item}' foi adicionado com sucesso!")
        else:
            print("Item inválido.")
            
    elif opcao == "2":
        if not lista_compras:
            print("A lista está vazia. Nada para remover.")
        else:
            print("\nItens atuais:", lista_compras)
            item = input("Digite o nome do item que deseja remover: ").strip()
            if item in lista_compras:
                lista_compras.remove(item)
                print(f"'{item}' foi removido da lista.")
            else:
                print("Item não encontrado na lista.")
                
    elif opcao == "3":
        if not lista_compras:
            print("\nSua lista de compras está vazia.")
        else:
            print("\n--- Itens na Lista ---")
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i}. {item}")
                
    elif opcao == "4":
        print("Saindo do programa de compras. Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")