from flask import Flask, jsonify, request

app = Flask(__name__)

# Rota POST para receber dados JSON e validar a entrada
@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    dados = request.get_json()

    # Validação básica dos dados recebidos
    if not dados or 'nome' not in dados or 'email' not in dados:
        return jsonify({
            "erro": "Dados inválidos. É necessário fornecer 'nome' e 'email'."
        }), 400

    nome = dados['nome']
    email = dados['email']

    # Simulação do processamento de cadastro
    return jsonify({
        "mensagem": "Usuário cadastrado com sucesso!",
        "usuario": {
            "nome": nome,
            "email": email
        }
    }), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)