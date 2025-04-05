
import streamlit as st
from utils.helpers import display_chapter_navigation, display_note, display_tip, display_warning

# Configuração da página
st.set_page_config(
    page_title="Dicas para Seguir Aprendendo | APIs do Zero ao Avançado",
    page_icon="📚",
    layout="wide"
)

def main():
    st.title("11. Dicas para Seguir Aprendendo")

    st.markdown("""
    Parabéns por chegar até aqui! 🎉 Agora que você já tem uma base sólida em APIs,
    vamos ver como continuar evoluindo seus conhecimentos.

    ## Práticas Recomendadas

    1. **Código todos os dias**
       - Mesmo que por 15 minutos
       - Mantenha a consistência
       - Foque em pequenos projetos

    2. **Projetos Pessoais**
       - Crie APIs para problemas reais
       - Implemente novas funcionalidades
       - Experimente diferentes padrões

    3. **Documentação e Boas Práticas**
       - Documente seu código
       - Siga padrões estabelecidos
       - Escreva testes automatizados

    ## Próximos Tópicos para Estudar

    1. **Padrões de Projeto**
       - Repository Pattern
       - Factory Pattern
       - Dependency Injection

    2. **Arquitetura**
       - Clean Architecture
       - Domain-Driven Design
       - Microserviços

    3. **Tecnologias Complementares**
       - Cache (Redis)
       - Message Queues
       - WebSockets

    ## Dicas para TDAH

    1. **Mantenha o foco**
       - Use técnica Pomodoro (25min trabalho, 5min pausa)
       - Elimine distrações
       - Defina objetivos claros e pequenos

    2. **Organize seu aprendizado**
       - Mantenha uma lista de tópicos para estudar
       - Use mapas mentais
       - Faça anotações do seu jeito

    3. **Celebre o progresso**
       - Mantenha um diário de aprendizado
       - Compartilhe suas conquistas
       - Revise seu crescimento

    ## Recursos Úteis

    1. **Documentações Oficiais**
       - Flask: https://flask.palletsprojects.com/
       - FastAPI: https://fastapi.tiangolo.com/
       - SQLAlchemy: https://www.sqlalchemy.org/

    2. **Ferramentas**
       - Postman para testar APIs
       - Git para controle de versão
       - VSCode ou PyCharm como IDE

    3. **Comunidade**
       - Participe de grupos de estudo
       - Compartilhe conhecimento
       - Faça code reviews

    ## Lembre-se

    > "O sucesso em programação não é sobre memorizar tudo,
    > mas sim sobre saber onde encontrar as informações
    > e como aplicá-las."

    Continue praticando, seja paciente consigo mesmo e
    mantenha a curiosidade viva! 🚀
    """)

    display_encouragement()

if __name__ == "__main__":
    main()
