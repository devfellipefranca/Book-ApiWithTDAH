import streamlit as st
from utils.helpers import display_chapter_navigation, display_note, display_tip, display_warning, display_code_with_explanation, display_encouragement, display_break_reminder, display_interactive_practice
from utils.code_examples import HTTP_METHODS_FLASK

# Configuração da página
st.set_page_config(
    page_title="Métodos HTTP | APIs do Zero ao Avançado",
    page_icon="📚",
    layout="wide"
)

def main():
    # Título principal
    st.title("5. Métodos HTTP")

    st.markdown("""
    Até agora, criamos APIs simples que apenas retornam informações. No entanto, uma API completa
    precisa permitir várias operações: criar, ler, atualizar e excluir dados (conhecido como CRUD).
    

    Para fazer isso, utilizamos diferentes **métodos HTTP** (também chamados de verbos HTTP).
    Neste capítulo, vamos entender o que são esses métodos e como implementá-los em nossas APIs.
    """)

    # Seção 1: O que são Métodos HTTP
    st.markdown("## 5.1. O que são Métodos HTTP?")

    st.markdown("""
    Os **métodos HTTP** são verbos que indicam a ação que uma requisição deseja realizar 
    em um recurso. Pense neles como os verbos da "linguagem da web".

    ### Analogia com uma biblioteca física

    Para entender melhor, imagine uma biblioteca:

    - **GET** é como consultar um livro sem retirá-lo
    - **POST** é como adicionar um novo livro à biblioteca
    - **PUT** é como substituir um livro por uma nova edição
    - **PATCH** é como corrigir algumas páginas de um livro
    - **DELETE** é como remover um livro do acervo

    ### Os principais métodos HTTP

    1. **GET**: Solicita a leitura de um recurso
       - Não deve alterar nada no servidor
       - Pode ser cacheado (armazenado temporariamente)
       - As informações são enviadas na URL

    2. **POST**: Solicita a criação de um novo recurso
       - Causa uma mudança no servidor
       - Não é idempotente (chamar várias vezes causa múltiplas criações)
       - Os dados são enviados no corpo da requisição

    3. **PUT**: Solicita a substituição completa de um recurso
       - Causa uma mudança no servidor
       - É idempotente (chamar várias vezes tem o mesmo efeito que chamar uma vez)
       - Os dados são enviados no corpo da requisição

    4. **PATCH**: Solicita a atualização parcial de um recurso
       - Causa uma mudança no servidor
       - Atualiza apenas os campos informados, mantendo o resto
       - Os dados são enviados no corpo da requisição

    5. **DELETE**: Solicita a remoção de um recurso
       - Causa uma mudança no servidor
       - É idempotente (chamar várias vezes tem o mesmo efeito)
       - Geralmente não contém corpo na requisição
    """)

    display_note("Em APIs REST, combinamos os métodos HTTP com URLs para criar um sistema intuitivo. Por exemplo, uma API de biblioteca poderia ter: GET /livros (listar livros), POST /livros (adicionar livro), PUT /livros/123 (atualizar livro 123), DELETE /livros/123 (remover livro 123).")

    # Seção 2: O Padrão CRUD em APIs
    st.markdown("## 5.2. O Padrão CRUD em APIs")

    st.markdown("""
    CRUD é um acrônimo para as quatro operações básicas que podem ser realizadas em dados persistentes:

    - **C**reate (Criar)
    - **R**ead (Ler)
    - **U**pdate (Atualizar)
    - **D**elete (Excluir)

    Na arquitetura REST, mapeamos estas operações para métodos HTTP:

    | Operação CRUD | Método HTTP | Descrição                                   |
    |---------------|-------------|---------------------------------------------|
    | **Create**    | POST        | Cria um novo recurso                        |
    | **Read**      | GET         | Obtém um ou mais recursos                   |
    | **Update**    | PUT/PATCH   | Atualiza um recurso existente              |
    | **Delete**    | DELETE      | Remove um recurso                           |

    ### Exemplo com uma API de tarefas:

    1. **Create**: `POST /tarefas`
       - Cria uma nova tarefa
       - Corpo da requisição: `{"titulo": "Estudar Python", "concluida": false}`

    2. **Read**:
       - `GET /tarefas` - Lista todas as tarefas
       - `GET /tarefas/42` - Obtém detalhes da tarefa com ID 42

    3. **Update**:
       - `PUT /tarefas/42` - Substitui completamente a tarefa 42
         - Corpo: `{"titulo": "Estudar APIs", "concluida": true}`
       - `PATCH /tarefas/42` - Atualiza apenas campos específicos
         - Corpo: `{"concluida": true}`

    4. **Delete**: `DELETE /tarefas/42`
       - Remove a tarefa com ID 42

    Este padrão torna as APIs previsíveis e fáceis de entender.
    """)

    # Pausa para reflexão
    display_encouragement()

    # Seção 3: Implementando Métodos HTTP no Flask
    st.markdown("## 5.3. Implementando Métodos HTTP no Flask")

    st.markdown("""
    Vamos implementar uma API completa com todos os métodos HTTP usando Flask.
    Será uma API de lista de tarefas que permite criar, listar, atualizar e excluir tarefas.
    """)

    display_code_with_explanation(
        HTTP_METHODS_FLASK,
        """
        Este é um exemplo completo de uma API REST para gerenciar tarefas. Vamos analisar cada parte:

        1. **Configuração Inicial**:
           - Importamos as classes necessárias do Flask
           - Criamos uma instância da aplicação
           - Definimos uma lista para armazenar as tarefas (simula um banco de dados)

        2. **Rota GET para listar todas as tarefas** (`/tarefas`):
           - `@app.route("/tarefas", methods=["GET"])` - Esta rota aceita apenas o método GET
           - A função `obter_tarefas()` retorna a lista completa de tarefas
           - `jsonify()` converte a lista Python para JSON

        3. **Rota GET para obter uma tarefa específica** (`/tarefas/<int:tarefa_id>`):
           - O `<int:tarefa_id>` na URL captura o ID da tarefa como um número inteiro
           - Usamos uma expressão geradora com `next()` para encontrar a tarefa pelo ID
           - Se a tarefa for encontrada, retornamos seus detalhes
           - Se não, retornamos um erro 404 (Not Found)

        4. **Rota POST para criar uma tarefa** (`/tarefas`):
           - `@app.route("/tarefas", methods=["POST"])` - Esta rota aceita apenas o método POST
           - `request.json` obtém os dados enviados no corpo da requisição
           - Verificamos se os dados são válidos (se contêm um título)
           - Criamos uma nova tarefa com um ID gerado automaticamente
           - Retornamos a tarefa criada com código 201 (Created)

        5. **Rota PUT para atualizar uma tarefa** (`/tarefas/<int:tarefa_id>`):
           - `@app.route("/tarefas/<int:tarefa_id>", methods=["PUT"])` - Aceita apenas PUT
           - Buscamos a tarefa existente pelo ID
           - Atualizamos seus campos com os novos valores
           - Retornamos a tarefa atualizada

        6. **Rota DELETE para remover uma tarefa** (`/tarefas/<int:tarefa_id>`):
           - `@app.route("/tarefas/<int:tarefa_id>", methods=["DELETE"])` - Aceita apenas DELETE
           - Armazenamos o tamanho inicial da lista
           - Filtramos a lista para remover a tarefa com o ID especificado
           - Verificamos se o tamanho mudou para saber se a tarefa foi removida
           - Retornamos uma mensagem de sucesso ou erro 404

        Esta API segue os princípios RESTful:
        - Usa substantivos plurais para recursos (`/tarefas`)
        - Usa IDs para identificar recursos específicos (`/tarefas/42`)
        - Aplica os métodos HTTP apropriados para cada operação
        - Retorna códigos de status HTTP apropriados (200, 201, 404, etc.)
        - Fornece respostas consistentes em formato JSON
        """
    )

    # Lembrete para pausa
    display_break_reminder()

    # Seção 4: Códigos de Status HTTP
    st.markdown("## 5.4. Códigos de Status HTTP")

    st.markdown("""
    Os **códigos de status HTTP** são números de três dígitos que indicam o resultado de uma requisição.
    Usar códigos corretos é essencial para que os clientes entendam o que aconteceu com sua solicitação.

    ### Categorias principais

    1. **1xx - Informacional**
       - Raramente usados diretamente em APIs
       - Indicam que a requisição foi recebida e está sendo processada

    2. **2xx - Sucesso**
       - **200 OK**: Requisição bem-sucedida
       - **201 Created**: Recurso criado com sucesso
       - **204 No Content**: Sucesso, mas sem conteúdo para retornar

    3. **3xx - Redirecionamento**
       - Raramente usados em APIs modernas
       - Indicam que o cliente precisa tomar uma ação adicional

    4. **4xx - Erro do Cliente**
       - **400 Bad Request**: Requisição malformada ou inválida
       - **401 Unauthorized**: Autenticação necessária
       - **403 Forbidden**: Sem permissão para acessar o recurso
       - **404 Not Found**: Recurso não encontrado
       - **422 Unprocessable Entity**: Dados válidos mas semanticamente incorretos

    5. **5xx - Erro do Servidor**
       - **500 Internal Server Error**: Erro não tratado no servidor
       - **503 Service Unavailable**: Servidor temporariamente indisponível

    ### Códigos mais comuns em APIs REST

    | Método | Sucesso | Erro Comum |
    |--------|---------|------------|
    | GET    | 200 OK  | 404 Not Found |
    | POST   | 201 Created | 400 Bad Request |
    | PUT    | 200 OK | 404 Not Found, 400 Bad Request |
    | DELETE | 200 OK ou 204 No Content | 404 Not Found |

    ### Implementando no Flask

    No Flask, é fácil retornar códigos de status diferentes:

    ```python
    # Sucesso - código 200 (padrão)
    return jsonify({"mensagem": "Operação bem-sucedida"})

    # Criação - código 201
    return jsonify(novo_recurso), 201

    # Erro do cliente - código 400
    return jsonify({"erro": "Dados inválidos"}), 400

    # Recurso não encontrado - código 404
    return jsonify({"erro": "Usuário não encontrado"}), 404

    # Erro interno - código 500
    return jsonify({"erro": "Erro inesperado"}), 500
    ```
    """)

    display_tip("Sempre retorne códigos de status HTTP apropriados! Eles ajudam os clientes a entender o resultado da requisição e a tratar erros adequadamente. Uma API que sempre retorna 200 mesmo em caso de erro é confusa e difícil de usar.")

    # Seção 5: Testando os Diferentes Métodos HTTP
    st.markdown("## 5.5. Testando os Diferentes Métodos HTTP")

    st.markdown("""
    Diferentemente do método GET, os outros métodos HTTP não podem ser facilmente testados
    usando apenas o navegador. Vamos ver como testar cada método:

    ### 1. Usando o Postman (Recomendado)

    O Postman é a ferramenta mais popular para testar APIs:

    1. **Para GET**:
       - Selecione o método GET
       - Digite a URL (ex: `http://localhost:8000/tarefas`)
       - Clique em "Send"

    2. **Para POST**:
       - Selecione o método POST
       - Digite a URL (ex: `http://localhost:8000/tarefas`)
       - Vá para a aba "Body"
       - Selecione "raw" e "JSON"
       - Digite o corpo da requisição, como:
         ```json
         {
             "titulo": "Aprender sobre APIs",
             "concluida": false
         }
         ```
    """)

if __name__ == "__main__":
    main()