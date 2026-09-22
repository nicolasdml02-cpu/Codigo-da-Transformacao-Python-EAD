import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)
NOME_BANCO = 'database.db'

# Função auxiliar para inicializar a tabela no SQLite
def init_db():
    conn = sqlite3.connect(NOME_BANCO)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Inicializa o banco ao carregar o script
init_db()

@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    dados = request.get_json()

    if not dados or 'nome' not in dados or 'email' not in dados:
        return jsonify({"erro": "Informe 'nome' e 'email'."}), 400

    nome = dados['nome']
    email = dados['email']

    try:
        conn = sqlite3.connect(NOME_BANCO)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()
        id_criado = cursor.lastrowid
        conn.close()

        return jsonify({
            "mensagem": "Usuário salvo no banco de dados com sucesso!",
            "id": id_criado,
            "nome": nome,
            "email": email
        }), 201

    except sqlite3.IntegrityError:
        return jsonify({"erro": "Este e-mail já está cadastrado."}), 400
    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    conn = sqlite3.connect(NOME_BANCO)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM usuarios")
    linhas = cursor.fetchall()
    conn.close()

    usuarios = [{"id": row[0], "nome": row[1], "email": row[2]} for row in linhas]
    return jsonify(usuarios), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)