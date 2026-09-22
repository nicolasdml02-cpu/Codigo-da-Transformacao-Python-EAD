from flask import Flask, jsonify

app = Flask(__name__)

# Rota GET para retornar uma mensagem de saudação em JSON
@app.route('/saudacao', methods=['GET'])
def saudacao():
    return jsonify({
        "mensagem": "Olá! Seja bem-vindo à API Flask.",
        "status": "sucesso"
    }), 200

if __name__ == '__main__':
    # Executa o servidor em modo de depuração na porta 5000
    app.run(debug=True, port=5000)