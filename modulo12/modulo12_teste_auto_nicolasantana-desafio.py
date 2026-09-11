import pytest
from flask import Flask, jsonify, request

# Instância da aplicação Flask
app = Flask(__name__)

@app.route('/soma', methods=['POST'])
def rota_soma():
    dados = request.get_json()
    if not dados or 'a' not in dados or 'b' not in dados:
        return jsonify({'erro': 'Parâmetros a e b são obrigatórios'}), 400
    
    a = dados['a']
    b = dados['b']
    return jsonify({'resultado': a + b}), 200

# Fixture do pytest para criar o cliente de teste do Flask
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Testes da API Flask usando pytest
def test_rota_soma_sucesso(client):
    resposta = client.post('/soma', json={'a': 4, 'b': 6})
    assert resposta.status_code == 200
    assert resposta.get_json() == {'resultado': 10}

def test_rota_soma_dados_invalidos(client):
    resposta = client.post('/soma', json={'a': 4})
    assert resposta.status_code == 400
    assert 'erro' in resposta.get_json()