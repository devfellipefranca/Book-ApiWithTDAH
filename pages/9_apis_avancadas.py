
import streamlit as st
from utils.helpers import display_chapter_navigation, display_note, display_tip, display_warning, display_code_with_explanation, display_encouragement, display_break_reminder, display_interactive_practice
from utils.code_examples import API_WITH_DATABASE

# Configuração da página
st.set_page_config(
    page_title="APIs Avançadas | APIs do Zero ao Avançado",
    page_icon="📚",
    layout="wide"
)

def main():
    # Título principal
    st.title("9. APIs Avançadas")

    st.markdown("""
    Agora que já dominamos os conceitos básicos e intermediários de APIs,
    vamos explorar técnicas avançadas para criar APIs mais robustas e escaláveis.
    """)

    # Seção 1: Conectando APIs a Bancos de Dados
    st.markdown("## 9.1. Conectando APIs a Bancos de Dados")

    display_code_with_explanation(
        API_WITH_DATABASE,
        "Exemplo de API conectada a um banco de dados SQLite"
    )

if __name__ == "__main__":
    main()
