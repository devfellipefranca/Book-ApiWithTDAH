
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Documentação da API | APIs do Zero ao Avançado",
    page_icon="📚",
    layout="wide"
)

def main():
    st.title("Documentação da API")

    st.markdown("""
    ## Endpoints Disponíveis

    ### 1. Autenticação

    #### Registro de Usuário
    ```http
    POST /registro
    Content-Type: application/json

    {
        "nome": "string",
        "email": "string",
        "senha": "string"
    }
    ```

    #### Login
    ```http
    POST /login
    Content-Type: application/json

    {
        "email": "string",
        "senha": "string"
    }
    ```

    #### Logout
    ```http
    POST /logout
    Authorization: Bearer <token>
    ```

    ### 2. Tarefas

    #### Listar Tarefas
    ```http
    GET /tarefas
    Authorization: Bearer <token>
    ```

    Parâmetros de query:
    - `concluida`: boolean
    - `categoria_id`: number
    - `prioridade`: "baixa" | "media" | "alta"

    #### Criar Tarefa
    ```http
    POST /tarefas
    Authorization: Bearer <token>
    Content-Type: application/json

    {
        "titulo": "string",
        "descricao": "string",
        "prioridade": "baixa" | "media" | "alta",
        "concluida": boolean,
        "categorias_ids": number[]
    }
    ```

    #### Obter Tarefa
    ```http
    GET /tarefas/{tarefa_id}
    Authorization: Bearer <token>
    ```

    #### Atualizar Tarefa
    ```http
    PUT /tarefas/{tarefa_id}
    Authorization: Bearer <token>
    Content-Type: application/json

    {
        "titulo": "string",
        "descricao": "string",
        "prioridade": "baixa" | "media" | "alta",
        "concluida": boolean,
        "categorias_ids": number[]
    }
    ```

    #### Excluir Tarefa
    ```http
    DELETE /tarefas/{tarefa_id}
    Authorization: Bearer <token>
    ```

    ### 3. Categorias

    #### Listar Categorias
    ```http
    GET /categorias
    Authorization: Bearer <token>
    ```

    #### Criar Categoria
    ```http
    POST /categorias
    Authorization: Bearer <token>
    Content-Type: application/json

    {
        "nome": "string",
        "cor": "string" // Código hexadecimal, ex: "#4285F4"
    }
    ```

    #### Atualizar Categoria
    ```http
    PUT /categorias/{categoria_id}
    Authorization: Bearer <token>
    Content-Type: application/json

    {
        "nome": "string",
        "cor": "string"
    }
    ```

    #### Excluir Categoria
    ```http
    DELETE /categorias/{categoria_id}
    Authorization: Bearer <token>
    ```

    ### 4. Estatísticas

    #### Obter Estatísticas
    ```http
    GET /estatisticas
    Authorization: Bearer <token>
    ```

    ## Códigos de Status

    - 200: Sucesso
    - 201: Criado com sucesso
    - 400: Dados inválidos
    - 401: Não autorizado
    - 404: Não encontrado

    ## Autenticação

    Todas as rotas (exceto /registro e /login) requerem autenticação usando o token JWT no header:

    ```http
    Authorization: Bearer <seu_token_aqui>
    ```

    ## Exemplos de Uso

    ### Registro de usuário:
    ```bash
    curl -X POST http://localhost:5000/registro \\
        -H "Content-Type: application/json" \\
        -d '{"nome":"João","email":"joao@email.com","senha":"Senha123"}'
    ```

    ### Login:
    ```bash
    curl -X POST http://localhost:5000/login \\
        -H "Content-Type: application/json" \\
        -d '{"email":"joao@email.com","senha":"Senha123"}'
    ```

    ### Criar uma tarefa:
    ```bash
    curl -X POST http://localhost:5000/tarefas \\
        -H "Authorization: Bearer <seu_token>" \\
        -H "Content-Type: application/json" \\
        -d '{"titulo":"Estudar APIs","descricao":"Aprender sobre REST","prioridade":"alta"}'
    ```
    """)

if __name__ == "__main__":
    main()
