import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)
NOME_BANCO = 'blog.db'

def init_db():
    conn = sqlite3.connect(NOME_BANCO)
    cursor = conn.cursor()
    # Tabela de usuários para autenticação
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    # Tabela de postagens do blog
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL,
            autor_id INTEGER NOT NULL,
            FOREIGN KEY (autor_id) REFERENCES usuarios (id)
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# --- Rota de Cadastro de Usuário ---
@app.route('/api/registrar', methods=['POST'])
def registrar():
    dados = request.get_json()
    if not dados or 'username' not in dados or 'senha' not in dados:
        return jsonify({"erro": "Envie 'username' e 'senha'."}), 400

    try:
        conn = sqlite3.connect(NOME_BANCO)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (username, senha) VALUES (?, ?)", 
                       (dados['username'], dados['senha']))
        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Usuário registrado com sucesso!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"erro": "Nome de usuário já existe."}), 400

# --- Rota de Autenticação (Login) ---
@app.route('/api/login', methods=['POST'])
def login():
    dados = request.get_json()
    if not dados or 'username' not in dados or 'senha' not in dados:
        return jsonify({"erro": "Envie 'username' e 'senha'."}), 400

    conn = sqlite3.connect(NOME_BANCO)
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM usuarios WHERE username = ? AND senha = ?", 
                   (dados['username'], dados['senha']))
    usuario = cursor.fetchone()
    conn.close()

    if usuario:
        return jsonify({
            "mensagem": "Login realizado com sucesso!",
            "usuario_id": usuario[0],
            "username": usuario[1]
        }), 200
    else:
        return jsonify({"erro": "Credenciais inválidas."}), 401

# --- Criar Postagem (Requer enviar o autor_id) ---
@app.route('/api/posts', methods=['POST'])
def criar_post():
    dados = request.get_json()
    if not dados or 'titulo' not in dados or 'conteudo' not in dados or 'autor_id' not in dados:
        return jsonify({"erro": "Campos 'titulo', 'conteudo' e 'autor_id' são obrigatórios."}), 400

    conn = sqlite3.connect(NOME_BANCO)
    cursor = conn.cursor()
    
    # Verifica se o autor existe
    cursor.execute("SELECT id FROM usuarios WHERE id = ?", (dados['autor_id'],))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"erro": "Autor não encontrado."}), 404

    cursor.execute("INSERT INTO posts (titulo, conteudo, autor_id) VALUES (?, ?, ?)",
                   (dados['titulo'], dados['conteudo'], dados['autor_id']))
    conn.commit()
    post_id = cursor.lastrowid
    conn.close()

    return jsonify({"mensagem": "Post criado com sucesso!", "post_id": post_id}), 201

# --- Listar Todos os Posts ---
@app.route('/api/posts', methods=['GET'])
def listar_posts():
    conn = sqlite3.connect(NOME_BANCO)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT p.id, p.titulo, p.conteudo, u.username 
        FROM posts p
        JOIN usuarios u ON p.autor_id = u.id
    ''')
    linhas = cursor.fetchall()
    conn.close()

    posts = [
        {"id": r[0], "titulo": r[1], "conteudo": r[2], "autor": r[3]} 
        for r in linhas
    ]
    return jsonify(posts), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)