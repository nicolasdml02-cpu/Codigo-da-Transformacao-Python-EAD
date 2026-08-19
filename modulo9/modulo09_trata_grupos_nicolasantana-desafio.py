def sistema_login():
    # Credenciais cadastradas no sistema
    USUARIO_CORRETO = "admin"
    SENHA_CORRETA = "python123"
    MAX_TENTATIVAS = 3

    tentativas_restantes = MAX_TENTATIVAS

    print("=== Sistema de Login Seguros ===")

    while tentativas_restantes > 0:
        usuario = input("Usuário: ").strip()
        senha = input("Senha: ").strip()

        try:
            if usuario != USUARIO_CORRETO or senha != SENHA_CORRETA:
                tentativas_restantes -= 1
                raise ValueError("Credenciais inválidas! Usuário ou senha incorretos.")
            
            print("\n Login efetuado com sucesso! Bem-vindo ao sistema.")
            break

        except ValueError as erro:
            print(f"Erro: {erro}")
            if tentativas_restantes > 0:
                print(f"Você ainda tem {tentativas_restantes} tentativa(s).\n")
            else:
                print(" Acesso bloqueado! Número máximo de tentativas atingido.")

if __name__ == "__main__":
    sistema_login()