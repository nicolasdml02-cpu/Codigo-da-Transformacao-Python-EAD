# Arquivo: agenda_contatos.py

agenda = {}

while True:
    print("\n--- AGENDA DE CONTATOS ---")
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Buscar contato")
    print("4. Gerenciar/Listar todos")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Digite o nome do contato: ").strip()
        if nome:
            telefone = input("Digite o telefone: ").strip()
            email = input("Digite o e-mail: ").strip()
            
            # Armazenando os dados em um dicionário interno
            agenda[nome] = {"telefone": telefone, "email": email}
            print(f"Contato '{nome}' adicionado com sucesso!")
        else:
            print("Nome não pode ser vazio.")
            
    elif opcao == "2":
        nome = input("Digite o nome do contato que deseja remover: ").strip()
        if nome in agenda:
            del agenda[nome]
            print(f"Contato '{nome}' removido com sucesso.")
        else:
            print("Contato não encontrado.")
            
    elif opcao == "3":
        nome = input("Digite o nome para buscar: ").strip()
        if nome in agenda:
            print(f"\n--- Dados de {nome} ---")
            print(f"Telefone: {agenda[nome]['telefone']}")
            print(f"E-mail: {agenda[nome]['email']}")
        else:
            print("Contato não encontrado.")
            
    elif opcao == "4":
        if not agenda:
            print("\nA agenda está vazia.")
        else:
            print("\n--- LISTA DE CONTATOS ---")
            for nome, info in agenda.items():
                print(f"Nome: {nome} | Tel: {info['telefone']} | E-mail: {info['email']}")
                
    elif opcao == "5":
        print("Fechando a agenda. Até mais!")
        break
    else:
        print("Opção inválida! Tente novamente.")