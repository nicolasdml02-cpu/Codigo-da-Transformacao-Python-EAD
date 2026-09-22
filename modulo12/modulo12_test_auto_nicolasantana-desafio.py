import pytest
from flask import Flask, jsonify, request

# Aplicação Flask para o teste
app = Flask(__name__)

@app.route('/somar', methods=['POST'])
def api_somar():
    data = request.get_json()
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({'error': 'Parâmetros inválidos'}), 400
    
    resultado = data['a'] + data['b']
    return jsonify({'resultado': resultado}), 200


# Fixture do Pytest para criar o cliente de teste
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Testes da API usando pytest
def test_api_somar_sucesso(client):
    resposta = client.post('/somar', json={'a': 4, 'b': 6})
    dados = resposta.get_json()
    
    assert resposta.status_code == 200
    assert dados['resultado'] == 10

def test_api_somar_payload_invalido(client):
    resposta = client.post('/somar', json={'a': 4})
    
    assert resposta.status_code == 400