import streamlit as st
from utils.helpers import display_chapter_navigation, display_note, display_tip, display_warning, display_code_with_explanation, display_encouragement, display_break_reminder, display_interactive_practice
from utils.code_examples import API_VALIDATION_SECURITY

# Configuração da página
st.set_page_config(
    page_title="Validação e Segurança | APIs do Zero ao Avançado",
    page_icon="📚",
    layout="wide"
)

def main():
    # Título principal
    st.title("8. Validação e Segurança")

    st.markdown("""
    A segurança é um aspecto crítico no desenvolvimento de APIs. Neste capítulo, 
    vamos aprender como proteger nossas APIs através de validação de
    dados e implementação de medidas de segurança básicas.
    """)

    # Seção 1: A importância da segurança em APIs
    st.markdown("## 8.1. A importância da segurança em APIs")

    st.markdown("""
    Quando criamos uma API, estamos essencialmente abrindo uma porta para o mundo exterior
    acessar nossos dados e funcionalidades. Sem as devidas proteções, essa porta pode ser
    usada de formas maliciosas:

    ### Riscos comuns em APIs:

    1. **Acesso não autorizado**: Pessoas acessando dados que não deveriam
    2. **Injeção de código**: Inserção de código malicioso através de inputs não validados
    3. **Sobrecarga de servidor**: Bombardeamento de requisições para derrubar o serviço
    4. **Exposição de dados sensíveis**: Vazamento de informações confidenciais
    5. **Manipulação de dados**: Alteração não autorizada de informações

    ### Exemplos de incidentes reais:

    - Em 2019, a **First American Financial Corp** expôs 885 milhões de registros sensíveis devido a uma falha em sua API
    - A **Equifax** sofreu um vazamento de dados que afetou 147 milhões de pessoas devido a falhas de segurança
    - A **Facebook** teve dados de 50 milhões de usuários expostos devido a vulnerabilidades em sua API Graph

    ### Por que a segurança é frequentemente negligenciada?

    1. Pressão por entregas rápidas
    2. Falta de conhecimento sobre riscos
    3. Percepção de que "ninguém vai atacar minha pequena API"

    A verdade é que até mesmo APIs pequenas são alvos, muitas vezes de forma automatizada por bots que varrem a internet em busca de vulnerabilidades.
    """)

    display_warning("Nunca pense 'minha API é pequena/simples demais para ser atacada'. Ataques automatizados não discriminam por tamanho - eles simplesmente procuram vulnerabilidades conhecidas.")

    # Seção 2: Validação de Dados
    st.markdown("## 8.2. Validação de Dados")

    st.markdown("""
    A validação de dados é a primeira linha de defesa. Nunca confie em dados enviados pelo cliente!

    ### Por que validar dados?

    1. **Segurança**: Previne injeção de código malicioso
    2. **Integridade**: Garante que os dados estão no formato esperado
    3. **Consistência**: Mantém a qualidade e uniformidade dos dados

    ### Tipos de validação
    #### 1. Validação de Tipo
    Verifica se o dado é do tipo esperado (string, número, booleano, etc.):

    ```python
    # Validando tipo de dados
    def validar_idade(idade):
        if not isinstance(idade, int):
            return False, "Idade deve ser um número inteiro"
        return True, ""
    ```

    #### 2. Validação de Formato
    Verifica se o dado segue um padrão específico (email, telefone, CEP):

    ```python
    import re

    # Validando formato de email
    def validar_email(email):
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(padrao, email):
            return False, "Formato de email inválido"
        return True, ""
    ```

    #### 3. Validação de Tamanho/Limite
    Verifica se o dado está dentro de limites aceitáveis:

    ```python
    # Validando tamanho de senha
    def validar_senha(senha):
        if len(senha) < 8:
            return False, "Senha deve ter no mínimo 8 caracteres"
        return True, ""
    ```

    #### 4. Validação de Conteúdo
    Verifica se o conteúdo é aceitável:

    ```python
    # Validando valor dentro de opções aceitas
    def validar_categoria(categoria):
        categorias_validas = ["tecnologia", "saúde", "educação", "finanças"]
        if categoria not in categorias_validas:
            return False, "Categoria inválida"
        return True, ""
    ```

    #### 5. Validação de Presença
    Verifica se campos obrigatórios estão presentes:

    ```python
    # Validando campos obrigatórios
    def validar_campos_obrigatorios(dados, campos):
        for campo in campos:
            if campo not in dados or not dados[campo]:
                return False, f"Campo obrigatório ausente: {campo}"
        return True, ""
    ```

    ### Sanitização de Dados
    Além de validar, é importante sanitizar dados para remover conteúdo potencialmente perigoso:

    ```python
    import html

    # Sanitizando HTML para prevenir XSS
    def sanitizar_texto(texto):
        return html.escape(texto)

    # Sanitizando entrada para prevenir injeção SQL
    def sanitizar_input_sql(input_texto):
        # Exemplo simples - em produção use bibliotecas especializadas ou ORM!
        return input_texto.replace("'", "''")
    ```
    """)

    display_tip("Uma boa abordagem é 'validar na entrada, sanitizar na saída'. Valide rigorosamente o que entra na sua API e sanitize tudo que sai dela. Isso cria duas camadas de proteção.")

    # Pausa para reflexão
    display_encouragement()

    # Seção 3: Autenticação e Autorização
    st.markdown("## 8.3. Autenticação e Autorização")

    st.markdown("""
    Autenticação e autorização são fundamentais para controlar o acesso à sua API.

    ### Autenticação vs Autorização

    - **Autenticação**: Verifica **quem** você é (identidade)
    - **Autorização**: Determina **o que** você pode fazer (permissões)

    ### Métodos de Autenticação em APIs

    #### 1. Autenticação por Token
    O cliente recebe um token após login bem-sucedido e o envia em cada requisição:

    ```
    POST /login
    {
        "email": "usuario@exemplo.com",
        "senha": "senha123"
    }

    Resposta:
    {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    }

    // Nas próximas requisições:
    GET /recursos
    Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
    ```

    #### 2. Autenticação por API Key
    O cliente recebe uma chave única que identifica a aplicação:

    ```
    GET /recursos?api_key=a1b2c3d4e5f6g7h8i9j0

    // ou

    GET /recursos
    X-API-Key: a1b2c3d4e5f6g7h8i9j0
    ```

    #### 3. Autenticação Básica HTTP
    O cliente envia nome de usuário e senha em cada requisição:

    ```
    GET /recursos
    Authorization: Basic dXN1YXJpbzpzZW5oYTEyMw==
    ```

    O valor é a codificação Base64 de "usuario:senha123".

    #### 4. OAuth 2.0
    Um protocolo mais complexo para autorização delegada:

    ```
    // Passo 1: Redirecionamento para autenticação
    GET /auth?client_id=app123&redirect_uri=https://app.com/callback&response_type=code

    // Passo 2: Após login, receber código de autorização
    GET https://app.com/callback?code=a1b2c3...

    // Passo 3: Trocar código por token
    POST /token
    {
        "code": "a1b2c3...",
        "client_id": "app123",
        "client_secret": "secret456",
        "grant_type": "authorization_code"
    }

    // Passo 4: Usar o token para acessar recursos
    GET /recursos
    Authorization: Bearer xyz789...
    ```

    ### Implementando Autenticação por Token em Flask

    ```python
    import secrets
    from functools import wraps
    from flask import request, jsonify

    # Simulação de banco de dados de tokens
    tokens_validos = {}  # token -> user_id

    # Função decoradora para proteger rotas
    def requer_autenticacao(f):
        @wraps(f)
        def decorada(*args, **kwargs):
            # Obter token do cabeçalho
            auth_header = request.headers.get('Authorization')
            if not auth_header or not auth_header.startswith('Bearer '):
                return jsonify({"erro": "Token não fornecido"}), 401

            token = auth_header.split(' ')[1]
            if token not in tokens_validos:
                return jsonify({"erro": "Token inválido"}), 401

            # Adicionar ID do usuário aos argumentos
            user_id = tokens_validos[token]
            return f(user_id, *args, **kwargs)

        return decorada

    # Rota de login
    @app.route("/login", methods=["POST"])
    def login():
        dados = request.json
        # Aqui você verificaria as credenciais no banco de dados
        # ...

        # Gerar e armazenar token
        token = secrets.token_hex(16)
        tokens_validos[token] = user_id

        return jsonify({"token": token})

    # Rota protegida
    @app.route("/perfil", methods=["GET"])
    @requer_autenticacao
    def perfil(user_id):
        # O user_id é injetado pelo decorador
        # Buscar dados do usuário no banco
        # ...
        return jsonify({"mensagem": f"Dados do usuário {user_id}"})
    ```
    """)

    display_note("Tokens JWT (JSON Web Tokens) são uma opção popular para autenticação em APIs. Eles são auto-contidos, ou seja, carregam informações do usuário dentro do próprio token, evitando consultas ao banco de dados a cada requisição.")

    # Lembrete para pausa
    display_break_reminder()

    # Seção 4: Proteção contra Ataques Comuns
    st.markdown("## 8.4. Proteção contra Ataques Comuns")

    st.markdown("""
    Vamos explorar alguns ataques comuns contra APIs e como se proteger:

    ### 1. Injeção SQL

    **O ataque**: O atacante insere código SQL malicioso nos parâmetros da requisição.

    **Exemplo vulnerável**:
    ```python
    @app.route("/usuarios/<nome>")
    def buscar_usuario(nome):
        query = f"SELECT * FROM usuarios WHERE nome = '{nome}'"
        # Se nome = "'; DROP TABLE usuarios; --", temos um problema!
    ```

    **Proteção**:
    ```python
    @app.route("/usuarios/<nome>")
    def buscar_usuario(nome):
        query = "SELECT * FROM usuarios WHERE nome = ?"
        cursor.execute(query, (nome,))  # Parâmetros são escapados automaticamente
    ```

    ### 2. Cross-Site Scripting (XSS)

    **O ataque**: O atacante insere código JavaScript que será executado no navegador do usuário.

    **Exemplo vulnerável**:
    ```python
    @app.route("/perfil/<nome>")
    def perfil(nome):
        return f"<h1>Perfil de {nome}</h1>"
        # Se nome = "<script>alert('Hackeado!')</script>", o script será executado

    ```
    """)

if __name__ == "__main__":
    main()