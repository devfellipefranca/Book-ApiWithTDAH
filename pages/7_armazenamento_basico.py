import streamlit as st
from utils.helpers import display_chapter_navigation, display_note, display_tip, display_warning, display_code_with_explanation, display_encouragement, display_break_reminder, display_interactive_practice
from utils.code_examples import JSON_STORAGE

# Configuração da página
st.set_page_config(
    page_title="Armazenamento Básico | APIs do Zero ao Avançado",
    page_icon="📚",
    layout="wide"
)

def main():
    # Título principal
    st.title("7. Armazenamento Básico")

    st.markdown("""
    Até agora, nossas APIs armazenam dados apenas na memória. Para aplicações reais,
    precisamos de um armazenamento persistente. Neste capítulo, vamos explorar formas simples
    de armazenar dados em arquivos.
    """)

    # Seção 1: Por que precisamos de armazenamento persistente
    st.markdown("## 7.1. Por que precisamos de armazenamento persistente?")

    st.markdown("""
    Imagine que você desenvolve uma API para um aplicativo de lista de tarefas:

    1. Um usuário cria várias tarefas através da API
    2. O servidor armazena essas tarefas em uma variável na memória
    3. Mais tarde, o servidor é reiniciado (por uma atualização ou erro)
    4. Todas as tarefas são perdidas!

    O armazenamento persistente resolve esse problema salvando os dados em um local
    que não é afetado pelo reinício do servidor.

    ### Tipos de armazenamento persistente

    Existem várias opções, com diferentes níveis de complexidade:

    1. **Arquivos simples**: TXT, CSV, JSON
        - Fáceis de implementar
        - Bons para aplicações pequenas
        - Limitados em performance e concorrência

    2. **Bancos de dados leves**: SQLite
        - Não requerem servidor separado
        - Oferecem recursos SQL
        - Bons para aplicações médias

    3. **Bancos de dados completos**: MySQL, PostgreSQL, MongoDB
        - Requerem servidor separado
        - Alta performance e funcionalidades avançadas
        - Escaláveis para grandes aplicações

    Neste capítulo, focaremos em arquivos simples, especialmente JSON, que são
    perfeitos para começar e entender os conceitos básicos de persistência.
    """)

    display_note("O tipo de armazenamento que você escolhe deve ser baseado nas necessidades da sua aplicação. Nem sempre o mais avançado é o melhor! Para muitas APIs pequenas, um arquivo JSON é mais que suficiente.")

    # Seção 2: Armazenamento em Arquivos JSON
    st.markdown("## 7.2. Armazenamento em Arquivos JSON")

    st.markdown("""
    O JSON (JavaScript Object Notation) é um formato leve de troca de dados que é fácil
    para humanos lerem e escreverem e fácil para máquinas analisarem e gerarem.

    ### Vantagens do JSON para armazenamento simples

    1. **Formato nativo para APIs**: As APIs já trabalham com JSON, então não há conversão complexa
    2. **Legibilidade**: Você pode abrir e entender o arquivo facilmente
    3. **Flexibilidade**: Armazena estruturas de dados complexas sem esquema rígido
    4. **Suporte nativo em Python**: A biblioteca `json` já vem com Python

    ### Operações básicas com arquivos JSON em Python

    ```python
    import json

    # Lendo um arquivo JSON
    def ler_dados():
        try:
            with open("dados.json", "r") as arquivo:
                return json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            # Se o arquivo não existir ou estiver vazio/corrompido
            return []

    # Escrevendo em um arquivo JSON
    def salvar_dados(dados):
        with open("dados.json", "w") as arquivo:
            json.dump(dados, arquivo, indent=4)

    # Exemplo de uso
    # Ler dados existentes
    tarefas = ler_dados()

    # Adicionar uma nova tarefa
    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": "Aprender sobre APIs",
        "concluida": False
    }
    tarefas.append(nova_tarefa)

    # Salvar dados atualizados
    salvar_dados(tarefas)
    ```

    ### Estruturando os dados em arquivos JSON

    Os dados em arquivos JSON geralmente são estruturados como:

    1. **Lista de objetos**: Para coleções do mesmo tipo
    ```json
    [
        {"id": 1, "nome": "Item 1"},
        {"id": 2, "nome": "Item 2"}
    ]
    ```

    2. **Objeto com listas**: Para múltiplas coleções
    ```json
    {
        "usuarios": [
            {"id": 1, "nome": "Usuário 1"},
            {"id": 2, "nome": "Usuário 2"}
        ],
        "produtos": [
            {"id": 1, "nome": "Produto 1"},
            {"id": 2, "nome": "Produto 2"}
        ]
    }
    ```
    """)

if __name__ == "__main__":
    main()