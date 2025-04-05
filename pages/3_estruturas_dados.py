import streamlit as st
from utils.helpers import display_chapter_navigation, display_note, display_tip, display_warning, display_code_with_explanation, display_encouragement, display_break_reminder, display_interactive_practice
from utils.code_examples import LIST_EXAMPLE, DICTIONARY_EXAMPLE

# Configuração da página
st.set_page_config(
    page_title="Estruturas de Dados | APIs do Zero ao Avançado",
    page_icon="📚",
    layout="wide"
)

def main():
    # Título principal
    st.title("3. Estruturas de Dados Simples")

    st.markdown("""
    Neste capítulo, vamos aprender sobre estruturas de dados - formas de organizar e armazenar
    informações no seu programa. Estas estruturas são fundamentais para trabalhar com APIs,
    já que precisamos constantemente manipular dados de entrada e saída.
    """)

    # Seção 1: Introdução às Estruturas de Dados
    st.markdown("## 3.1. Por que precisamos de estruturas de dados?")

    st.markdown("""
    Imagine que você está desenvolvendo uma API para uma lista de tarefas. Você precisaria armazenar:

    - Várias tarefas
    - Cada tarefa com diferentes informações (título, status, prazo, etc.)

    Como você organizaria esses dados? É aí que entram as estruturas de dados!

    **Estruturas de dados** são formas organizadas de armazenar e manipular informações. Elas nos permitem:

    - Agrupar dados relacionados
    - Acessar informações de forma eficiente
    - Realizar operações específicas nos dados

    Em Python, as estruturas de dados mais usadas para APIs são:

    1. Listas (lists)
    2. Dicionários (dictionaries)

    Vamos explorar cada uma delas em detalhes.
    """)

    # Seção 2: Listas
    st.markdown("## 3.2. Listas")

    display_code_with_explanation(LIST_EXAMPLE, "Exemplo de operações com listas em Python")

    # Seção 3: Dicionários
    st.markdown("## 3.3. Dicionários")

    display_code_with_explanation(DICTIONARY_EXAMPLE, "Exemplo de operações com dicionários em Python")

if __name__ == "__main__":
    main()