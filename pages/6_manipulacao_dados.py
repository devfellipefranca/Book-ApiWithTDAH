import streamlit as st
from utils.helpers import display_chapter_navigation, display_note, display_tip, display_warning, display_code_with_explanation, display_encouragement, display_break_reminder, display_interactive_practice
from utils.code_examples import DATA_VALIDATION

# Configuração da página
st.set_page_config(
    page_title="Manipulação de Dados | APIs do Zero ao Avançado",
    page_icon="📚",
    layout="wide"
)

def main():
    # Título principal
    st.title("6. Manipulação de Dados")

    st.markdown("""
    Nas APIs que criamos até agora, trabalhamos com dados fixos ou muito simples. Em aplicações
    reais, no entanto, precisamos lidar com dados enviados pelos usuários, processá-los e
    devolver respostas dinâmicas. Neste capítulo, vamos aprender como manipular dados em nossas APIs.
    """)

    # Seção 1: Recebendo Dados do Usuário
    st.markdown("## 6.1. Recebendo Dados do Usuário")

    st.markdown("""
    Existem várias formas de receber dados em uma API. Vamos explorar as principais:
    """)

    ### 1. Parâmetros de URL

    st.markdown("""
    Os parâmetros de URL (também chamados de query parameters) são adicionados após o "?" na URL:
    """)

    st.code("""
    GET /produtos?categoria=eletronicos&ordem=preco
    """, language='http')

    st.markdown("""
    No Flask, você acessa esses parâmetros usando `request.args`:
    """)

    st.code(
        """python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/produtos")
def listar_produtos():
    # Obter parâmetros da URL
    categoria = request.args.get("categoria")
    ordem = request.args.get("ordem", "nome")  # valor padrão "nome"

    # Usar os parâmetros para filtrar ou ordenar
    if categoria:
        print(f"Filtrando por categoria: {categoria}")

    print(f"Ordenando por: {ordem}")

    # ... lógica para buscar produtos ...

    return jsonify({"mensagem": "Produtos filtrados"})
""", language='python'
    )

    st.markdown("""
    Parâmetros de URL são ideais para:
    - Filtrar listas de recursos (`?categoria=eletronicos`)
    - Paginar resultados (`?pagina=2&itens_por_pagina=20`)
    - Definir ordenação (`?ordem=preco_desc`)
    """)

    ### 2. Parâmetros de Rota

    st.markdown("""
    Os parâmetros de rota (também chamados de path parameters) são parte do caminho da URL:
    """)


if __name__ == "__main__":
    main()