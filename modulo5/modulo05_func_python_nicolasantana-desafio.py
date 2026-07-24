# Desafio Extra: Sistema de Login Simples
# Função para validar usuário e senha usando um dicionário para armazenar os dados de acesso.

# Dicionário simulando um banco de dados de usuários e senhas
usuarios_cadastrados = {
    "Nicolas": "12345",
    "Ivan": "python2026",
    "Vocação": "123"
}

def validar_login(usuario, senha, banco_dados):
    """
    Valida se o usuário existe e se a senha informada está correta.
    """
    if usuario in banco_dados:
        if banco_dados[usuario] == senha:
            return True, "Login realizado com sucesso! Bem-vindo(a)."
        else:
            return False, "Senha incorreta. Tente novamente."
    else:
        return False, "Usuário não encontrado."

# Exemplo de uso:
if __name__ == "__main__":
    print("--- SISTEMA DE LOGIN ---")
    user_input = input("Usuário: ")
    senha_input = input("Senha: ")
    
    sucesso, mensagem = validar_login(user_input, senha_input, usuarios_cadastrados)
    print(mensagem)