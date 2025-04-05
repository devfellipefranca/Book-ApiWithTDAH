# Exemplos de código organizados por capítulo para fácil referência

# Capítulo 1: Introdução
HELLO_WORLD = '''print("Olá, Mundo!")'''

# Capítulo 2: Fundamentos Básicos
VARIABLES_EXAMPLE = '''# Declarando variáveis de diferentes tipos
nome = "Ana"  # String (texto)
idade = 25    # Integer (número inteiro)
altura = 1.65 # Float (número decimal)
is_programadora = True  # Boolean (verdadeiro/falso)

# Exibindo as variáveis
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}m")
print(f"É programadora? {is_programadora}")'''

CONDITIONAL_EXAMPLE = '''idade = 18

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade.")'''

LOOP_EXAMPLE = '''# Loop for para contar de 1 a 5
print("Contando com for:")
for numero in range(1, 6):
    print(numero)

# Loop while para contar de 1 a 5
print("\\nContando com while:")
contador = 1
while contador <= 5:
    print(contador)
    contador += 1'''

FUNCTION_EXAMPLE = '''# Definindo uma função simples
def saudacao(nome):
    """Esta função retorna uma saudação personalizada"""
    return f"Olá, {nome}! Bem-vindo(a) ao mundo das APIs!"

# Chamando a função
mensagem = saudacao("Ana")
print(mensagem)'''

# Capítulo 3: Estruturas de Dados Simples
LIST_EXAMPLE = '''# Criando uma lista de linguagens de programação
linguagens = ["Python", "JavaScript", "Java", "Go", "Ruby"]

# Acessando elementos da lista
print(f"Primeira linguagem: {linguagens[0]}")
print(f"Última linguagem: {linguagens[-1]}")

# Modificando um elemento
linguagens[1] = "TypeScript"

# Adicionando um elemento
linguagens.append("PHP")

# Removendo um elemento
linguagens.remove("Java")

print(f"Lista atualizada: {linguagens}")'''

DICTIONARY_EXAMPLE = '''# Criando um dicionário com informações de uma pessoa
pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "profissao": "Desenvolvedor",
    "linguagens": ["Python", "JavaScript", "SQL"]
}

# Acessando valores
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")

# Adicionando um novo par chave-valor
pessoa["cidade"] = "São Paulo"

# Modificando um valor existente
pessoa["idade"] = 31

# Removendo um par chave-valor
del pessoa["profissao"]

print(f"Dicionário atualizado: {pessoa}")'''

# Capítulo 4: Primeiros Passos com APIs
FLASK_HELLO_WORLD = '''from flask import Flask

# Criando uma instância da aplicação Flask
app = Flask(__name__)

# Definindo uma rota
@app.route("/")
def hello_world():
    return {"mensagem": "Olá, Mundo! Esta é minha primeira API!"}

# Executando a aplicação
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)'''

FASTAPI_HELLO_WORLD = '''from fastapi import FastAPI
import uvicorn

# Criando uma instância da aplicação FastAPI
app = FastAPI()

# Definindo uma rota
@app.get("/")
def hello_world():
    return {"mensagem": "Olá, Mundo! Esta é minha primeira API com FastAPI!"}

# Executando a aplicação
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)'''

# Capítulo 5: Métodos HTTP
HTTP_METHODS_FLASK = '''from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de dados simples (simulando um banco de dados)
tarefas = [
    {"id": 1, "titulo": "Estudar APIs", "concluida": False},
    {"id": 2, "titulo": "Fazer exercícios", "concluida": True}
]

# Rota GET para obter todas as tarefas
@app.route("/tarefas", methods=["GET"])
def obter_tarefas():
    return jsonify(tarefas)

# Rota GET para obter uma tarefa específica
@app.route("/tarefas/<int:tarefa_id>", methods=["GET"])
def obter_tarefa(tarefa_id):
    tarefa = next((t for t in tarefas if t["id"] == tarefa_id), None)
    if tarefa:
        return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

# Rota POST para criar uma nova tarefa
@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    nova_tarefa = request.json
    
    # Verificando se tem os campos necessários
    if not nova_tarefa or "titulo" not in nova_tarefa:
        return jsonify({"erro": "Dados inválidos"}), 400
    
    # Gerando um novo ID
    novo_id = max([t["id"] for t in tarefas], default=0) + 1
    
    # Criando a nova tarefa
    tarefa = {
        "id": novo_id,
        "titulo": nova_tarefa["titulo"],
        "concluida": nova_tarefa.get("concluida", False)
    }
    
    # Adicionando à lista
    tarefas.append(tarefa)
    
    return jsonify(tarefa), 201

# Rota PUT para atualizar uma tarefa existente
@app.route("/tarefas/<int:tarefa_id>", methods=["PUT"])
def atualizar_tarefa(tarefa_id):
    dados = request.json
    
    # Encontrando a tarefa
    tarefa = next((t for t in tarefas if t["id"] == tarefa_id), None)
    if not tarefa:
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    
    # Atualizando os campos
    if "titulo" in dados:
        tarefa["titulo"] = dados["titulo"]
    if "concluida" in dados:
        tarefa["concluida"] = dados["concluida"]
    
    return jsonify(tarefa)

# Rota DELETE para remover uma tarefa
@app.route("/tarefas/<int:tarefa_id>", methods=["DELETE"])
def remover_tarefa(tarefa_id):
    global tarefas
    tamanho_inicial = len(tarefas)
    tarefas = [t for t in tarefas if t["id"] != tarefa_id]
    
    if len(tarefas) < tamanho_inicial:
        return jsonify({"mensagem": "Tarefa removida com sucesso"}), 200
    
    return jsonify({"erro": "Tarefa não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)'''

# Capítulo 6: Manipulação de Dados
DATA_VALIDATION = '''from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.json
    
    # Validando os campos obrigatórios
    campos_obrigatorios = ["nome", "email", "senha"]
    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({
                "erro": f"Campo obrigatório ausente: {campo}"
            }), 400
    
    # Validando o formato do email (verificação simples)
    if "@" not in dados["email"] or "." not in dados["email"]:
        return jsonify({
            "erro": "Formato de email inválido"
        }), 400
    
    # Verificando se o email já existe
    if any(u["email"] == dados["email"] for u in usuarios):
        return jsonify({
            "erro": "Email já cadastrado"
        }), 400
    
    # Verificando o tamanho da senha
    if len(dados["senha"]) < 6:
        return jsonify({
            "erro": "A senha deve ter pelo menos 6 caracteres"
        }), 400
    
    # Criando o novo usuário
    novo_id = len(usuarios) + 1
    novo_usuario = {
        "id": novo_id,
        "nome": dados["nome"],
        "email": dados["email"],
        "senha": dados["senha"]  # Em uma API real, nunca armazene senhas em texto plano!
    }
    
    usuarios.append(novo_usuario)
    
    # Não retorne a senha na resposta
    resposta = {k: v for k, v in novo_usuario.items() if k != "senha"}
    return jsonify(resposta), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)'''

# Capítulo 7: Armazenamento Básico
JSON_STORAGE = '''import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Caminho para o arquivo JSON que servirá como nosso "banco de dados"
ARQUIVO_DB = "tarefas.json"

# Função para carregar os dados do arquivo
def carregar_tarefas():
    if not os.path.exists(ARQUIVO_DB):
        return []
    
    with open(ARQUIVO_DB, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            # Se o arquivo estiver vazio ou corrompido, retorna uma lista vazia
            return []

# Função para salvar os dados no arquivo
def salvar_tarefas(tarefas):
    with open(ARQUIVO_DB, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

# Rota para obter todas as tarefas
@app.route("/tarefas", methods=["GET"])
def obter_tarefas():
    tarefas = carregar_tarefas()
    return jsonify(tarefas)

# Rota para criar uma nova tarefa
@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.json
    
    if not dados or "titulo" not in dados:
        return jsonify({"erro": "O título da tarefa é obrigatório"}), 400
    
    tarefas = carregar_tarefas()
    
    # Gerando um novo ID
    novo_id = max([t.get("id", 0) for t in tarefas], default=0) + 1
    
    nova_tarefa = {
        "id": novo_id,
        "titulo": dados["titulo"],
        "concluida": dados.get("concluida", False)
    }
    
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    
    return jsonify(nova_tarefa), 201

# Rota para atualizar uma tarefa existente
@app.route("/tarefas/<int:tarefa_id>", methods=["PUT"])
def atualizar_tarefa(tarefa_id):
    dados = request.json
    tarefas = carregar_tarefas()
    
    # Encontrando a tarefa
    for tarefa in tarefas:
        if tarefa.get("id") == tarefa_id:
            # Atualizando os campos
            if "titulo" in dados:
                tarefa["titulo"] = dados["titulo"]
            if "concluida" in dados:
                tarefa["concluida"] = dados["concluida"]
                
            salvar_tarefas(tarefas)
            return jsonify(tarefa)
    
    return jsonify({"erro": "Tarefa não encontrada"}), 404

# Rota para remover uma tarefa
@app.route("/tarefas/<int:tarefa_id>", methods=["DELETE"])
def remover_tarefa(tarefa_id):
    tarefas = carregar_tarefas()
    
    # Filtrando a lista para remover a tarefa
    tarefas_atualizadas = [t for t in tarefas if t.get("id") != tarefa_id]
    
    if len(tarefas_atualizadas) < len(tarefas):
        salvar_tarefas(tarefas_atualizadas)
        return jsonify({"mensagem": "Tarefa removida com sucesso"})
    
    return jsonify({"erro": "Tarefa não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)'''

# Capítulo 8: Validação e Segurança
API_VALIDATION_SECURITY = '''from flask import Flask, request, jsonify
import re
import hashlib
import secrets
import time

app = Flask(__name__)

# Simulação de um banco de dados de usuários
usuarios_db = []

# Simulação de um banco de dados de tokens
tokens_db = {}

# Função para criar um hash seguro da senha
def hash_senha(senha, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)
    
    # Combinando senha e salt
    senha_salgada = (senha + salt).encode('utf-8')
    
    # Criando o hash
    hash_senha = hashlib.sha256(senha_salgada).hexdigest()
    
    return hash_senha, salt

# Função para validar email
def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None

# Função para validar senha
def validar_senha(senha):
    # Pelo menos 8 caracteres, uma letra maiúscula, uma minúscula e um número
    if len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres"
    
    if not re.search(r'[A-Z]', senha):
        return False, "A senha deve conter pelo menos uma letra maiúscula"
    
    if not re.search(r'[a-z]', senha):
        return False, "A senha deve conter pelo menos uma letra minúscula"
    
    if not re.search(r'[0-9]', senha):
        return False, "A senha deve conter pelo menos um número"
    
    return True, ""

# Função para verificar se o token é válido
def verificar_token(token):
    if token not in tokens_db:
        return False
    
    # Verificando se o token expirou (1 hora de validade)
    tempo_atual = time.time()
    if tempo_atual - tokens_db[token]["criado_em"] > 3600:
        # Token expirado, removendo
        del tokens_db[token]
        return False
    
    return True

# Middleware para verificar autenticação
def requer_autenticacao(fn):
    def wrapper(*args, **kwargs):
        # Obtendo o token do cabeçalho Authorization
        auth_header = request.headers.get('Authorization')
        
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"erro": "Token de autenticação não fornecido"}), 401
        
        token = auth_header.split(' ')[1]
        
        if not verificar_token(token):
            return jsonify({"erro": "Token de autenticação inválido ou expirado"}), 401
        
        # Passando o ID do usuário para a função original
        return fn(tokens_db[token]["usuario_id"], *args, **kwargs)
    
    # Preservando nome e docstring da função original
    wrapper.__name__ = fn.__name__
    wrapper.__doc__ = fn.__doc__
    
    return wrapper

# Rota para registro de usuário
@app.route("/registro", methods=["POST"])
def registrar_usuario():
    dados = request.json
    
    # Validando campos obrigatórios
    if not dados or "nome" not in dados or "email" not in dados or "senha" not in dados:
        return jsonify({"erro": "Campos obrigatórios ausentes"}), 400
    
    nome = dados["nome"]
    email = dados["email"]
    senha = dados["senha"]
    
    # Validando email
    if not validar_email(email):
        return jsonify({"erro": "Formato de email inválido"}), 400
    
    # Verificando se email já existe
    if any(u["email"] == email for u in usuarios_db):
        return jsonify({"erro": "Email já cadastrado"}), 400
    
    # Validando senha
    senha_valida, erro_senha = validar_senha(senha)
    if not senha_valida:
        return jsonify({"erro": erro_senha}), 400
    
    # Criando hash da senha
    hash_senha_valor, salt = hash_senha(senha)
    
    # Criando novo usuário
    novo_id = len(usuarios_db) + 1
    novo_usuario = {
        "id": novo_id,
        "nome": nome,
        "email": email,
        "senha_hash": hash_senha_valor,
        "salt": salt
    }
    
    usuarios_db.append(novo_usuario)
    
    # Retornando usuário criado (sem dados sensíveis)
    return jsonify({
        "id": novo_usuario["id"],
        "nome": novo_usuario["nome"],
        "email": novo_usuario["email"]
    }), 201

# Rota para login
@app.route("/login", methods=["POST"])
def login():
    dados = request.json
    
    if not dados or "email" not in dados or "senha" not in dados:
        return jsonify({"erro": "Email e senha são obrigatórios"}), 400
    
    email = dados["email"]
    senha = dados["senha"]
    
    # Procurando usuário pelo email
    usuario = next((u for u in usuarios_db if u["email"] == email), None)
    
    if not usuario:
        return jsonify({"erro": "Credenciais inválidas"}), 401
    
    # Verificando senha
    hash_senha_valor, _ = hash_senha(senha, usuario["salt"])
    
    if hash_senha_valor != usuario["senha_hash"]:
        return jsonify({"erro": "Credenciais inválidas"}), 401
    
    # Gerando token de autenticação
    token = secrets.token_hex(32)
    
    # Armazenando token
    tokens_db[token] = {
        "usuario_id": usuario["id"],
        "criado_em": time.time()
    }
    
    return jsonify({
        "token": token,
        "tipo": "Bearer",
        "expira_em": 3600  # 1 hora em segundos
    })

# Rota protegida por autenticação
@app.route("/perfil", methods=["GET"])
@requer_autenticacao
def obter_perfil(usuario_id):
    # Procurando usuário pelo ID
    usuario = next((u for u in usuarios_db if u["id"] == usuario_id), None)
    
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404
    
    # Retornando dados do usuário (sem dados sensíveis)
    return jsonify({
        "id": usuario["id"],
        "nome": usuario["nome"],
        "email": usuario["email"]
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)'''

# Capítulo 9: APIs Avançadas
API_WITH_DATABASE = '''from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Caminho para o banco de dados
DB_PATH = "tarefas.db"

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Para obter resultados como dicionários
    return conn

# Função para inicializar o banco de dados
def inicializar_db():
    # Verificando se o banco de dados já existe
    db_exists = os.path.exists(DB_PATH)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Criando a tabela de tarefas se não existir
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descricao TEXT,
        concluida INTEGER DEFAULT 0,
        data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Criando a tabela de categorias se não existir
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE
    )
    """)
    
    # Criando a tabela de relacionamento entre tarefas e categorias
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefa_categoria (
        tarefa_id INTEGER,
        categoria_id INTEGER,
        PRIMARY KEY (tarefa_id, categoria_id),
        FOREIGN KEY (tarefa_id) REFERENCES tarefas (id) ON DELETE CASCADE,
        FOREIGN KEY (categoria_id) REFERENCES categorias (id) ON DELETE CASCADE
    )
    """)
    
    # Inserindo algumas categorias padrão se o banco acabou de ser criado
    if not db_exists:
        categorias_padrao = ["Trabalho", "Estudos", "Pessoal", "Saúde", "Finanças"]
        for categoria in categorias_padrao:
            cursor.execute("INSERT INTO categorias (nome) VALUES (?)", (categoria,))
    
    conn.commit()
    conn.close()

# Inicializando o banco de dados na inicialização da aplicação
inicializar_db()

# Função auxiliar para converter os resultados do SQLite para dicionários
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#
# Rotas para Tarefas
#

# Rota para listar todas as tarefas
@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Parâmetros de consulta para filtragem
    concluida = request.args.get("concluida")
    categoria_id = request.args.get("categoria_id")
    
    query = "SELECT * FROM tarefas"
    params = []
    
    # Adicionando filtros se fornecidos
    where_clauses = []
    
    if concluida is not None:
        where_clauses.append("concluida = ?")
        params.append(1 if concluida.lower() == "true" else 0)
    
    if categoria_id is not None:
        query = """
        SELECT t.* FROM tarefas t
        JOIN tarefa_categoria tc ON t.id = tc.tarefa_id
        WHERE tc.categoria_id = ?
        """
        params.append(categoria_id)
        
        # Se também tiver o filtro de concluída
        if concluida is not None:
            query += " AND t.concluida = ?"
    elif where_clauses:
        # Se não tem categoria mas tem outros filtros
        query += " WHERE " + " AND ".join(where_clauses)
    
    cursor.execute(query, params)
    tarefas = [dict(row) for row in cursor.fetchall()]
    
    # Para cada tarefa, buscando suas categorias
    for tarefa in tarefas:
        cursor.execute("""
        SELECT c.id, c.nome FROM categorias c
        JOIN tarefa_categoria tc ON c.id = tc.categoria_id
        WHERE tc.tarefa_id = ?
        """, (tarefa["id"],))
        
        tarefa["categorias"] = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    return jsonify(tarefas)

# Rota para obter uma tarefa específica
@app.route("/tarefas/<int:tarefa_id>", methods=["GET"])
def obter_tarefa(tarefa_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tarefas WHERE id = ?", (tarefa_id,))
    tarefa = cursor.fetchone()
    
    if not tarefa:
        conn.close()
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    
    # Convertendo para dicionário
    tarefa_dict = dict(tarefa)
    
    # Buscando as categorias da tarefa
    cursor.execute("""
    SELECT c.id, c.nome FROM categorias c
    JOIN tarefa_categoria tc ON c.id = tc.categoria_id
    WHERE tc.tarefa_id = ?
    """, (tarefa_id,))
    
    tarefa_dict["categorias"] = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    return jsonify(tarefa_dict)

# Rota para criar uma nova tarefa
@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.json
    
    if not dados or "titulo" not in dados:
        return jsonify({"erro": "O título da tarefa é obrigatório"}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Inserindo a tarefa
    cursor.execute("""
    INSERT INTO tarefas (titulo, descricao, concluida)
    VALUES (?, ?, ?)
    """, (
        dados["titulo"],
        dados.get("descricao", ""),
        1 if dados.get("concluida", False) else 0
    ))
    
    # Obtendo o ID da tarefa inserida
    tarefa_id = cursor.lastrowid
    
    # Associando as categorias, se fornecidas
    categorias_ids = dados.get("categorias_ids", [])
    for categoria_id in categorias_ids:
        try:
            cursor.execute("""
            INSERT INTO tarefa_categoria (tarefa_id, categoria_id)
            VALUES (?, ?)
            """, (tarefa_id, categoria_id))
        except sqlite3.IntegrityError:
            # Se a categoria não existir, ignoramos
            pass
    
    conn.commit()
    
    # Buscando a tarefa recém-criada para retornar
    cursor.execute("SELECT * FROM tarefas WHERE id = ?", (tarefa_id,))
    tarefa = dict(cursor.fetchone())
    
    # Buscando as categorias associadas
    cursor.execute("""
    SELECT c.id, c.nome FROM categorias c
    JOIN tarefa_categoria tc ON c.id = tc.categoria_id
    WHERE tc.tarefa_id = ?
    """, (tarefa_id,))
    
    tarefa["categorias"] = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    return jsonify(tarefa), 201

# Rota para atualizar uma tarefa
@app.route("/tarefas/<int:tarefa_id>", methods=["PUT"])
def atualizar_tarefa(tarefa_id):
    dados = request.json
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Verificando se a tarefa existe
    cursor.execute("SELECT * FROM tarefas WHERE id = ?", (tarefa_id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    
    # Campos que podem ser atualizados
    campos_atualizaveis = ["titulo", "descricao", "concluida"]
    campos_a_atualizar = {}
    
    for campo in campos_atualizaveis:
        if campo in dados:
            # Convertendo booleano para inteiro no caso do campo 'concluida'
            if campo == "concluida":
                campos_a_atualizar[campo] = 1 if dados[campo] else 0
            else:
                campos_a_atualizar[campo] = dados[campo]
    
    # Se não há campos para atualizar
    if not campos_a_atualizar:
        conn.close()
        return jsonify({"erro": "Nenhum campo válido para atualização"}), 400
    
    # Construindo a query de atualização
    campos_set = ", ".join([f"{campo} = ?" for campo in campos_a_atualizar])
    valores = list(campos_a_atualizar.values())
    valores.append(tarefa_id)
    
    cursor.execute(f"UPDATE tarefas SET {campos_set} WHERE id = ?", valores)
    
    # Atualizando as categorias, se fornecidas
    if "categorias_ids" in dados:
        # Removendo todas as associações existentes
        cursor.execute("DELETE FROM tarefa_categoria WHERE tarefa_id = ?", (tarefa_id,))
        
        # Adicionando as novas associações
        for categoria_id in dados["categorias_ids"]:
            try:
                cursor.execute("""
                INSERT INTO tarefa_categoria (tarefa_id, categoria_id)
                VALUES (?, ?)
                """, (tarefa_id, categoria_id))
            except sqlite3.IntegrityError:
                # Se a categoria não existir, ignoramos
                pass
    
    conn.commit()
    
    # Buscando a tarefa atualizada para retornar
    cursor.execute("SELECT * FROM tarefas WHERE id = ?", (tarefa_id,))
    tarefa = dict(cursor.fetchone())
    
    # Buscando as categorias associadas
    cursor.execute("""
    SELECT c.id, c.nome FROM categorias c
    JOIN tarefa_categoria tc ON c.id = tc.categoria_id
    WHERE tc.tarefa_id = ?
    """, (tarefa_id,))
    
    tarefa["categorias"] = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    return jsonify(tarefa)

# Rota para excluir uma tarefa
@app.route("/tarefas/<int:tarefa_id>", methods=["DELETE"])
def excluir_tarefa(tarefa_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Verificando se a tarefa existe
    cursor.execute("SELECT * FROM tarefas WHERE id = ?", (tarefa_id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    
    # Excluindo a tarefa (as associações com categorias serão excluídas automaticamente pelo ON DELETE CASCADE)
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
    
    conn.commit()
    conn.close()
    
    return jsonify({"mensagem": "Tarefa excluída com sucesso"})

#
# Rotas para Categorias
#

# Rota para listar todas as categorias
@app.route("/categorias", methods=["GET"])
def listar_categorias():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM categorias")
    categorias = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    return jsonify(categorias)

# Rota para criar uma nova categoria
@app.route("/categorias", methods=["POST"])
def criar_categoria():
    dados = request.json
    
    if not dados or "nome" not in dados:
        return jsonify({"erro": "O nome da categoria é obrigatório"}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO categorias (nome) VALUES (?)", (dados["nome"],))
        conn.commit()
        
        # Obtendo a categoria recém-criada
        categoria_id = cursor.lastrowid
        cursor.execute("SELECT * FROM categorias WHERE id = ?", (categoria_id,))
        categoria = dict(cursor.fetchone())
        
        conn.close()
        return jsonify(categoria), 201
    
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"erro": "Já existe uma categoria com esse nome"}), 400

# Rota para excluir uma categoria
@app.route("/categorias/<int:categoria_id>", methods=["DELETE"])
def excluir_categoria(categoria_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Verificando se a categoria existe
    cursor.execute("SELECT * FROM categorias WHERE id = ?", (categoria_id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"erro": "Categoria não encontrada"}), 404
    
    # Excluindo a categoria (as associações com tarefas serão excluídas automaticamente pelo ON DELETE CASCADE)
    cursor.execute("DELETE FROM categorias WHERE id = ?", (categoria_id,))
    
    conn.commit()
    conn.close()
    
    return jsonify({"mensagem": "Categoria excluída com sucesso"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)'''

# Capítulo 10: Projeto Final
FINAL_PROJECT = '''from flask import Flask, request, jsonify
import sqlite3
import os
import hashlib
import secrets
import datetime
import re

app = Flask(__name__)

# Caminho para o banco de dados
DB_PATH = "gerenciador_tarefas.db"

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Para obter resultados como dicionários
    return conn

# Função para inicializar o banco de dados
def inicializar_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Criando a tabela de usuários
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha_hash TEXT NOT NULL,
        salt TEXT NOT NULL,
        data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Criando a tabela de tarefas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        titulo TEXT NOT NULL,
        descricao TEXT,
        prioridade TEXT CHECK(prioridade IN ('baixa', 'media', 'alta')) DEFAULT 'media',
        concluida INTEGER DEFAULT 0,
        data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        data_conclusao TIMESTAMP,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id) ON DELETE CASCADE
    )
    """)
    
    # Criando a tabela de categorias
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cor TEXT DEFAULT '#4285F4',
        usuario_id INTEGER,
        UNIQUE(nome, usuario_id),
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id) ON DELETE CASCADE
    )
    """)
    
    # Criando a tabela de relação entre tarefas e categorias
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefa_categoria (
        tarefa_id INTEGER,
        categoria_id INTEGER,
        PRIMARY KEY (tarefa_id, categoria_id),
        FOREIGN KEY (tarefa_id) REFERENCES tarefas (id) ON DELETE CASCADE,
        FOREIGN KEY (categoria_id) REFERENCES categorias (id) ON DELETE CASCADE
    )
    """)
    
    # Criando a tabela de tokens de autenticação
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tokens (
        token TEXT PRIMARY KEY,
        usuario_id INTEGER NOT NULL,
        criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        expira_em TIMESTAMP NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id) ON DELETE CASCADE
    )
    """)
    
    conn.commit()
    conn.close()

# Inicializando o banco de dados
inicializar_db()

# Função para criar um hash seguro da senha
def hash_senha(senha, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)
    
    # Combinando senha e salt
    senha_salgada = (senha + salt).encode('utf-8')
    
    # Criando o hash
    hash_senha = hashlib.sha256(senha_salgada).hexdigest()
    
    return hash_senha, salt

# Função para validar email
def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None

# Função para validar senha
def validar_senha(senha):
    # Pelo menos 8 caracteres, uma letra maiúscula, uma minúscula e um número
    if len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres"
    
    if not re.search(r'[A-Z]', senha):
        return False, "A senha deve conter pelo menos uma letra maiúscula"
    
    if not re.search(r'[a-z]', senha):
        return False, "A senha deve conter pelo menos uma letra minúscula"
    
    if not re.search(r'[0-9]', senha):
        return False, "A senha deve conter pelo menos um número"
    
    return True, ""

# Função para verificar se o token é válido
def verificar_token(token):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Buscando o token
    cursor.execute("""
    SELECT usuario_id, expira_em FROM tokens 
    WHERE token = ?
    """, (token,))
    
    resultado = cursor.fetchone()
    
    if not resultado:
        conn.close()
        return None
    
    usuario_id = resultado["usuario_id"]
    expira_em = resultado["expira_em"]
    
    # Verificando se o token expirou
    agora = datetime.datetime.now().isoformat()
    
    if agora > expira_em:
        # Token expirado, removendo
        cursor.execute("DELETE FROM tokens WHERE token = ?", (token,))
        conn.commit()
        conn.close()
        return None
    
    conn.close()
    return usuario_id

# Middleware para verificar autenticação
def requer_autenticacao(fn):
    def wrapper(*args, **kwargs):
        # Obtendo o token do cabeçalho Authorization
        auth_header = request.headers.get('Authorization')
        
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"erro": "Token de autenticação não fornecido"}), 401
        
        token = auth_header.split(' ')[1]
        
        usuario_id = verificar_token(token)
        if not usuario_id:
            return jsonify({"erro": "Token de autenticação inválido ou expirado"}), 401
        
        # Passando o ID do usuário para a função original
        return fn(usuario_id, *args, **kwargs)
    
    # Preservando nome e docstring da função original
    wrapper.__name__ = fn.__name__
    wrapper.__doc__ = fn.__doc__
    
    return wrapper

#
# Rotas de Autenticação
#

@app.route("/registro", methods=["POST"])
def registrar():
    dados = request.json
    
    # Validando campos obrigatórios
    if not dados or "nome" not in dados or "email" not in dados or "senha" not in dados:
        return jsonify({"erro": "Dados incompletos. Nome, email e senha são obrigatórios"}), 400
    
    nome = dados["nome"]
    email = dados["email"]
    senha = dados["senha"]
    
    # Validando email
    if not validar_email(email):
        return jsonify({"erro": "Formato de email inválido"}), 400
    
    # Validando senha
    senha_valida, erro_senha = validar_senha(senha)
    if not senha_valida:
        return jsonify({"erro": erro_senha}), 400
    
    # Verificando se o email já está registrado
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
    if cursor.fetchone():
        conn.close()
        return jsonify({"erro": "Email já registrado"}), 400
    
    # Criando hash da senha
    senha_hash, salt = hash_senha(senha)
    
    # Inserindo o novo usuário
    cursor.execute("""
    INSERT INTO usuarios (nome, email, senha_hash, salt)
    VALUES (?, ?, ?, ?)
    """, (nome, email, senha_hash, salt))
    
    conn.commit()
    
    # Obtendo o ID do usuário inserido
    usuario_id = cursor.lastrowid
    
    # Inserindo categorias padrão para o usuário
    categorias_padrao = [
        ("Trabalho", "#4285F4"),  # Azul
        ("Estudos", "#0F9D58"),   # Verde
        ("Pessoal", "#F4B400"),   # Amarelo
        ("Saúde", "#DB4437"),     # Vermelho
        ("Finanças", "#9C27B0")   # Roxo
    ]
    
    for nome_categoria, cor in categorias_padrao:
        cursor.execute("""
        INSERT INTO categorias (nome, cor, usuario_id)
        VALUES (?, ?, ?)
        """, (nome_categoria, cor, usuario_id))
    
    conn.commit()
    conn.close()
    
    return jsonify({
        "mensagem": "Usuário registrado com sucesso",
        "usuario": {
            "id": usuario_id,
            "nome": nome,
            "email": email
        }
    }), 201

@app.route("/login", methods=["POST"])
def login():
    dados = request.json
    
    if not dados or "email" not in dados or "senha" not in dados:
        return jsonify({"erro": "Email e senha são obrigatórios"}), 400
    
    email = dados["email"]
    senha = dados["senha"]
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Buscando o usuário pelo email
    cursor.execute("""
    SELECT id, nome, email, senha_hash, salt
    FROM usuarios
    WHERE email = ?
    """, (email,))
    
    usuario = cursor.fetchone()
    
    if not usuario:
        conn.close()
        return jsonify({"erro": "Credenciais inválidas"}), 401
    
    # Verificando a senha
    senha_hash, _ = hash_senha(senha, usuario["salt"])
    
    if senha_hash != usuario["senha_hash"]:
        conn.close()
        return jsonify({"erro": "Credenciais inválidas"}), 401
    
    # Gerando token de autenticação
    token = secrets.token_hex(32)
    
    # Calculando data de expiração (1 hora)
    agora = datetime.datetime.now()
    expira_em = (agora + datetime.timedelta(hours=1)).isoformat()
    
    # Armazenando o token
    cursor.execute("""
    INSERT INTO tokens (token, usuario_id, expira_em)
    VALUES (?, ?, ?)
    """, (token, usuario["id"], expira_em))
    
    conn.commit()
    conn.close()
    
    return jsonify({
        "token": token,
        "tipo": "Bearer",
        "expira_em": 3600,  # 1 hora em segundos
        "usuario": {
            "id": usuario["id"],
            "nome": usuario["nome"],
            "email": usuario["email"]
        }
    })

@app.route("/logout", methods=["POST"])
@requer_autenticacao
def logout(usuario_id):
    auth_header = request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Removendo o token
    cursor.execute("DELETE FROM tokens WHERE token = ?", (token,))
    
    conn.commit()
    conn.close()
    
    return jsonify({"mensagem": "Logout realizado com sucesso"})

#
# Rotas de Tarefas
#

@app.route("/tarefas", methods=["GET"])
@requer_autenticacao
def listar_tarefas(usuario_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Parâmetros para filtragem
    concluida = request.args.get("concluida")
    categoria_id = request.args.get("categoria_id")
    prioridade = request.args.get("prioridade")
    
    query = """
    SELECT t.id, t.titulo, t.descricao, t.prioridade, 
           t.concluida, t.data_criacao, t.data_conclusao
    FROM tarefas t
    WHERE t.usuario_id = ?
    """
    params = [usuario_id]
    
    # Adicionando filtros
    if concluida is not None:
        query += " AND t.concluida = ?"
        params.append(1 if concluida.lower() == "true" else 0)
    
    if prioridade:
        query += " AND t.prioridade = ?"
        params.append(prioridade.lower())
    
    # Filtro por categoria
    if categoria_id:
        query = """
        SELECT t.id, t.titulo, t.descricao, t.prioridade, 
               t.concluida, t.data_criacao, t.data_conclusao
        FROM tarefas t
        JOIN tarefa_categoria tc ON t.id = tc.tarefa_id
        WHERE t.usuario_id = ? AND tc.categoria_id = ?
        """
        params = [usuario_id, categoria_id]
        
        # Adicionando outros filtros
        if concluida is not None:
            query += " AND t.concluida = ?"
            params.append(1 if concluida.lower() == "true" else 0)
        
        if prioridade:
            query += " AND t.prioridade = ?"
            params.append(prioridade.lower())
    
    cursor.execute(query, params)
    tarefas = [dict(row) for row in cursor.fetchall()]
    
    # Para cada tarefa, buscando suas categorias
    for tarefa in tarefas:
        cursor.execute("""
        SELECT c.id, c.nome, c.cor
        FROM categorias c
        JOIN tarefa_categoria tc ON c.id = tc.categoria_id
        WHERE tc.tarefa_id = ?
        """, (tarefa["id"],))
        
        tarefa["categorias"] = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    return jsonify(tarefas)

@app.route("/tarefas", methods=["POST"])
@requer_autenticacao
def criar_tarefa(usuario_id):
    dados = request.json
    
    if not dados or "titulo" not in dados:
        return jsonify({"erro": "O título da tarefa é obrigatório"}), 400
    
    # Extraindo dados
    titulo = dados["titulo"]
    descricao = dados.get("descricao", "")
    prioridade = dados.get("prioridade", "media").lower()
    concluida = 1 if dados.get("concluida", False) else 0
    categorias_ids = dados.get("categorias_ids", [])
    
    # Validando prioridade
    if prioridade not in ["baixa", "media", "alta"]:
        return jsonify({"erro": "Prioridade inválida. Use 'baixa', 'media' ou 'alta'"}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Inserindo a tarefa
    cursor.execute("""
    INSERT INTO tarefas (usuario_id, titulo, descricao, prioridade, concluida)
    VALUES (?, ?, ?, ?, ?)
    """, (usuario_id, titulo, descricao, prioridade, concluida))
    
    tarefa_id = cursor.lastrowid
    
    # Associando às categorias
    for categoria_id in categorias_ids:
        # Verificando se a categoria pertence ao usuário
        cursor.execute("""
        SELECT id FROM categorias
        WHERE id = ? AND (usuario_id = ? OR usuario_id IS NULL)
        """, (categoria_id, usuario_id))
        
        if cursor.fetchone():
            cursor.execute("""
            INSERT INTO tarefa_categoria (tarefa_id, categoria_id)
            VALUES (?, ?)
            """, (tarefa_id, categoria_id))
    
    conn.commit()
    
    # Buscando a tarefa completa para retornar
    cursor.execute("""
    SELECT id, titulo, descricao, prioridade, concluida, data_criacao, data_conclusao
    FROM tarefas
    WHERE id = ?
    """, (tarefa_id,))
    
    tarefa = dict(cursor.fetchone())
    
    # Buscando as categorias da tarefa
    cursor.execute("""
    SELECT c.id, c.nome, c.cor
    FROM categorias c
    JOIN tarefa_categoria tc ON c.id = tc.categoria_id
    WHERE tc.tarefa_id = ?
    """, (tarefa_id,))
    
    tarefa["categorias"] = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    return jsonify(tarefa), 201

@app.route("/tarefas/<int:tarefa_id>", methods=["GET"])
@requer_autenticacao
def obter_tarefa(usuario_id, tarefa_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Buscando a tarefa
    cursor.execute("""
    SELECT id, titulo, descricao, prioridade, concluida, data_criacao, data_conclusao
    FROM tarefas
    WHERE id = ? AND usuario_id = ?
    """, (tarefa_id, usuario_id))
    
    tarefa = cursor.fetchone()
    
    if not tarefa:
        conn.close()
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    
    tarefa = dict(tarefa)
    
    # Buscando as categorias da tarefa
    cursor.execute("""
    SELECT c.id, c.nome, c.cor
    FROM categorias c
    JOIN tarefa_categoria tc ON c.id = tc.categoria_id
    WHERE tc.tarefa_id = ?
    """, (tarefa_id,))
    
    tarefa["categorias"] = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    return jsonify(tarefa)

@app.route("/tarefas/<int:tarefa_id>", methods=["PUT"])
@requer_autenticacao
def atualizar_tarefa(usuario_id, tarefa_id):
    dados = request.json
    
    if not dados:
        return jsonify({"erro": "Nenhum dado fornecido para atualização"}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Verificando se a tarefa existe e pertence ao usuário
    cursor.execute("""
    SELECT id FROM tarefas
    WHERE id = ? AND usuario_id = ?
    """, (tarefa_id, usuario_id))
    
    if not cursor.fetchone():
        conn.close()
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    
    # Campos que podem ser atualizados
    campos_atualizaveis = {
        "titulo": str,
        "descricao": str,
        "prioridade": str,
        "concluida": bool
    }
    
    # Construindo a query de atualização
    atualizacoes = []
    valores = []
    
    for campo, tipo in campos_atualizaveis.items():
        if campo in dados:
            valor = dados[campo]
            
            # Validações específicas
            if campo == "prioridade" and valor not in ["baixa", "media", "alta"]:
                conn.close()
                return jsonify({"erro": "Prioridade inválida. Use 'baixa', 'media' ou 'alta'"}), 400
            
            # Convertendo para o tipo esperado
            if campo == "concluida":
                valor = 1 if valor else 0
                
                # Se estiver marcando como concluída, registra a data de conclusão
                if valor == 1:
                    atualizacoes.append("data_conclusao = ?")
                    valores.append(datetime.datetime.now().isoformat())
                else:
                    # Se estiver desmarcando, remove a data de conclusão
                    atualizacoes.append("data_conclusao = NULL")
            
            atualizacoes.append(f"{campo} = ?")
            valores.append(valor)
    
    if not atualizacoes:
        conn.close()
        return jsonify({"erro": "Nenhum campo válido para atualização"}), 400
    
    # Executando a atualização
    query = f"UPDATE tarefas SET {', '.join(atualizacoes)} WHERE id = ? AND usuario_id = ?"
    valores.extend([tarefa_id, usuario_id])
    
    cursor.execute(query, valores)
    
    # Atualizando categorias, se fornecidas
    if "categorias_ids" in dados:
        # Removendo associações existentes
        cursor.execute("DELETE FROM tarefa_categoria WHERE tarefa_id = ?", (tarefa_id,))
        
        # Adicionando novas associações
        for categoria_id in dados["categorias_ids"]:
            # Verificando se a categoria pertence ao usuário
            cursor.execute("""
            SELECT id FROM categorias
            WHERE id = ? AND (usuario_id = ? OR usuario_id IS NULL)
            """, (categoria_id, usuario_id))
            
            if cursor.fetchone():
                cursor.execute("""
                INSERT INTO tarefa_categoria (tarefa_id, categoria_id)
                VALUES (?, ?)
                """, (tarefa_id, categoria_id))
    
    conn.commit()
    
    # Buscando a tarefa atualizada
    cursor.execute("""
    SELECT id, titulo, descricao, prioridade, concluida, data_criacao, data_conclusao
    FROM tarefas
    WHERE id = ?
    """, (tarefa_id,))
    
    tarefa = dict(cursor.fetchone())
    
    # Buscando as categorias
    cursor.execute("""
    SELECT c.id, c.nome, c.cor
    FROM categorias c
    JOIN tarefa_categoria tc ON c.id = tc.categoria_id
    WHERE tc.tarefa_id = ?
    """, (tarefa_id,))
    
    tarefa["categorias"] = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    return jsonify(tarefa)

@app.route("/tarefas/<int:tarefa_id>", methods=["DELETE"])
@requer_autenticacao
def excluir_tarefa(usuario_id, tarefa_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Verificando se a tarefa existe e pertence ao usuário
    cursor.execute("""
    SELECT id FROM tarefas
    WHERE id = ? AND usuario_id = ?
    """, (tarefa_id, usuario_id))
    
    if not cursor.fetchone():
        conn.close()
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    
    # Excluindo a tarefa (as associações serão excluídas pelo ON DELETE CASCADE)
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
    
    conn.commit()
    conn.close()
    
    return jsonify({"mensagem": "Tarefa excluída com sucesso"})

#
# Rotas de Categorias
#

@app.route("/categorias", methods=["GET"])
@requer_autenticacao
def listar_categorias(usuario_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Buscando categorias do sistema (sem usuário) e do usuário
    cursor.execute("""
    SELECT id, nome, cor, usuario_id
    FROM categorias
    WHERE usuario_id = ? OR usuario_id IS NULL
    ORDER BY nome
    """, (usuario_id,))
    
    categorias = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    return jsonify(categorias)

@app.route("/categorias", methods=["POST"])
@requer_autenticacao
def criar_categoria(usuario_id):
    dados = request.json
    
    if not dados or "nome" not in dados:
        return jsonify({"erro": "O nome da categoria é obrigatório"}), 400
    
    nome = dados["nome"]
    cor = dados.get("cor", "#4285F4")  # Cor padrão azul
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Inserindo a categoria
        cursor.execute("""
        INSERT INTO categorias (nome, cor, usuario_id)
        VALUES (?, ?, ?)
        """, (nome, cor, usuario_id))
        
        categoria_id = cursor.lastrowid
        
        conn.commit()
        
        # Buscando a categoria criada
        cursor.execute("""
        SELECT id, nome, cor, usuario_id
        FROM categorias
        WHERE id = ?
        """, (categoria_id,))
        
        categoria = dict(cursor.fetchone())
        
        conn.close()
        return jsonify(categoria), 201
    
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"erro": "Já existe uma categoria com esse nome"}), 400

@app.route("/categorias/<int:categoria_id>", methods=["PUT"])
@requer_autenticacao
def atualizar_categoria(usuario_id, categoria_id):
    dados = request.json
    
    if not dados:
        return jsonify({"erro": "Nenhum dado fornecido para atualização"}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Verificando se a categoria existe e pertence ao usuário
    cursor.execute("""
    SELECT id FROM categorias
    WHERE id = ? AND usuario_id = ?
    """, (categoria_id, usuario_id))
    
    if not cursor.fetchone():
        conn.close()
        return jsonify({"erro": "Categoria não encontrada ou você não tem permissão para editá-la"}), 404
    
    # Campos que podem ser atualizados
    atualizacoes = []
    valores = []
    
    if "nome" in dados:
        atualizacoes.append("nome = ?")
        valores.append(dados["nome"])
    
    if "cor" in dados:
        atualizacoes.append("cor = ?")
        valores.append(dados["cor"])
    
    if not atualizacoes:
        conn.close()
        return jsonify({"erro": "Nenhum campo válido para atualização"}), 400
    
    # Executando a atualização
    query = f"UPDATE categorias SET {', '.join(atualizacoes)} WHERE id = ? AND usuario_id = ?"
    valores.extend([categoria_id, usuario_id])
    
    try:
        cursor.execute(query, valores)
        conn.commit()
        
        # Buscando a categoria atualizada
        cursor.execute("""
        SELECT id, nome, cor, usuario_id
        FROM categorias
        WHERE id = ?
        """, (categoria_id,))
        
        categoria = dict(cursor.fetchone())
        
        conn.close()
        return jsonify(categoria)
    
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"erro": "Já existe uma categoria com esse nome"}), 400

@app.route("/categorias/<int:categoria_id>", methods=["DELETE"])
@requer_autenticacao
def excluir_categoria(usuario_id, categoria_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Verificando se a categoria existe e pertence ao usuário
    cursor.execute("""
    SELECT id FROM categorias
    WHERE id = ? AND usuario_id = ?
    """, (categoria_id, usuario_id))
    
    if not cursor.fetchone():
        conn.close()
        return jsonify({"erro": "Categoria não encontrada ou você não tem permissão para excluí-la"}), 404
    
    # Excluindo a categoria
    cursor.execute("DELETE FROM categorias WHERE id = ?", (categoria_id,))
    
    conn.commit()
    conn.close()
    
    return jsonify({"mensagem": "Categoria excluída com sucesso"})

#
# Rota para estatísticas
#

@app.route("/estatisticas", methods=["GET"])
@requer_autenticacao
def obter_estatisticas(usuario_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Total de tarefas
    cursor.execute("""
    SELECT COUNT(*) as total FROM tarefas
    WHERE usuario_id = ?
    """, (usuario_id,))
    total_tarefas = cursor.fetchone()["total"]
    
    # Tarefas concluídas
    cursor.execute("""
    SELECT COUNT(*) as concluidas FROM tarefas
    WHERE usuario_id = ? AND concluida = 1
    """, (usuario_id,))
    tarefas_concluidas = cursor.fetchone()["concluidas"]
    
    # Tarefas pendentes
    cursor.execute("""
    SELECT COUNT(*) as pendentes FROM tarefas
    WHERE usuario_id = ? AND concluida = 0
    """, (usuario_id,))
    tarefas_pendentes = cursor.fetchone()["pendentes"]
    
    # Tarefas por prioridade
    cursor.execute("""
    SELECT prioridade, COUNT(*) as quantidade FROM tarefas
    WHERE usuario_id = ?
    GROUP BY prioridade
    """, (usuario_id,))
    
    tarefas_por_prioridade = {}
    for prioridade in ["baixa", "media", "alta"]:
        tarefas_por_prioridade[prioridade] = 0
    
    for row in cursor.fetchall():
        tarefas_por_prioridade[row["prioridade"]] = row["quantidade"]
    
    # Tarefas por categoria
    cursor.execute("""
    SELECT c.nome, COUNT(tc.tarefa_id) as quantidade 
    FROM categorias c
    LEFT JOIN tarefa_categoria tc ON c.id = tc.categoria_id
    LEFT JOIN tarefas t ON tc.tarefa_id = t.id AND t.usuario_id = ?
    WHERE c.usuario_id = ? OR c.usuario_id IS NULL
    GROUP BY c.id
    """, (usuario_id, usuario_id))
    
    tarefas_por_categoria = {}
    for row in cursor.fetchall():
        tarefas_por_categoria[row["nome"]] = row["quantidade"]
    
    conn.close()
    
    return jsonify({
        "total_tarefas": total_tarefas,
        "tarefas_concluidas": tarefas_concluidas,
        "tarefas_pendentes": tarefas_pendentes,
        "progresso": round(tarefas_concluidas / total_tarefas * 100, 1) if total_tarefas > 0 else 0,
        "tarefas_por_prioridade": tarefas_por_prioridade,
        "tarefas_por_categoria": tarefas_por_categoria
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)'''
