
import streamlit as st
from utils.helpers import display_chapter_navigation, display_note, display_tip, display_warning, display_code_with_explanation, display_encouragement, display_break_reminder

# Configuração da página
st.set_page_config(
    page_title="Projeto Final | APIs do Zero ao Avançado",
    page_icon="📚",
    layout="wide"
)

def main():
    st.title("10. Projeto Final: Sistema de Gerenciamento de Tarefas")

    st.markdown("""
    Chegou o momento de aplicar tudo que aprendemos! Vamos desenvolver uma API completa
    para um sistema de gerenciamento de tarefas com autenticação, categorias e estatísticas.

    ## Funcionalidades do Projeto

    1. **Autenticação de Usuários**
       - Registro
       - Login/Logout
       - Tokens JWT

    2. **Gerenciamento de Tarefas**
       - CRUD completo de tarefas
       - Filtros por status e categoria
       - Prioridades
       - Datas de criação e conclusão

    3. **Categorias**
       - CRUD de categorias
       - Cores personalizadas
       - Vinculação com tarefas

    4. **Estatísticas**
       - Total de tarefas
       - Tarefas por status
       - Distribuição por categoria
       - Tempo médio de conclusão

    ## Estrutura do Projeto

    ```
    projeto_final/
    ├── app.py           # Arquivo principal
    ├── config.py        # Configurações
    ├── models/          # Modelos de dados
    ├── routes/          # Rotas da API
    ├── services/        # Lógica de negócio
    └── utils/           # Funções auxiliares
    ```

    ## Tecnologias Utilizadas

    - Flask para a API
    - SQLite para o banco de dados
    - JWT para autenticação
    - SQLAlchemy como ORM

    ## Implementação

    O código completo do projeto está disponível nos exemplos anteriores.
    Sugerimos que você:

    1. Comece implementando a autenticação
    2. Adicione o CRUD básico de tarefas
    3. Implemente as categorias
    4. Adicione as estatísticas
    5. Refine a API com validações e tratamento de erros

    ## Próximos Passos

    Após completar o projeto base, você pode expandir com:

    - Adicionar tags às tarefas
    - Implementar subtarefas
    - Criar lembretes/notificações
    - Adicionar compartilhamento de tarefas
    - Implementar histórico de alterações
    """)

    display_encouragement()

if __name__ == "__main__":
    main()
