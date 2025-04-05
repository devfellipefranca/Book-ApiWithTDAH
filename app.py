import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="APIs do Zero ao Avançado: Um Guia para Pessoas com TDAH",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Título principal
    st.title("APIs do Zero ao Avançado: Um Guia para Pessoas com TDAH")

    # Subtítulo
    st.markdown("### Bem-vindo ao seu guia interativo para aprender desenvolvimento de APIs!")

    # Colunas para melhor layout
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        ## Sobre este livro

        Este livro foi desenvolvido especialmente para pessoas com TDAH que desejam aprender
        sobre desenvolvimento de APIs. A programação pode parecer desafiadora no início, 
        mas vamos dividir tudo em pequenos passos fáceis de seguir!

        Você não precisa ter qualquer experiência prévia em programação - vamos começar 
        do absoluto zero e progredir até conceitos avançados, tudo em um ritmo adequado 
        para você.

        ## Por que Python?

        Decidimos usar Python como linguagem principal deste livro por algumas razões:

        1. **Sintaxe clara e legível**: Python é conhecido por sua simplicidade e legibilidade
        2. **Curva de aprendizado suave**: É considerada uma das melhores linguagens para iniciantes
        3. **Ecossistema rico**: Possui bibliotecas poderosas para desenvolvimento de APIs
        4. **Amplamente utilizada**: É uma das linguagens mais populares na indústria para backend

        ## Como usar este livro

        Na barra lateral, você encontrará todos os capítulos disponíveis. Recomendamos seguir a ordem
        proposta, mas sinta-se à vontade para explorar os tópicos que mais chamarem sua atenção.

        Cada capítulo contém:
        - Explicações claras e diretas
        - Exemplos de código com explicações linha por linha
        - Exercícios práticos
        - Dicas e lembretes para facilitar o aprendizado

        ## Vamos começar!

        Pronto para embarcar nessa jornada? Clique no primeiro capítulo na barra lateral 
        e vamos dar o primeiro passo juntos!

        **Lembre-se**: O aprendizado não é uma corrida. Vá no seu próprio ritmo e não tenha 
        medo de revisitar os capítulos anteriores sempre que necessário.
        """)

    with col2:
        st.markdown("""
        ## Estrutura do Livro

        1. Introdução à Programação e APIs
        2. Fundamentos Básicos
        3. Estruturas de Dados Simples
        4. Primeiros Passos com APIs
        5. Métodos HTTP
        6. Manipulação de Dados
        7. Armazenamento Básico
        8. Validação e Segurança
        9. APIs Avançadas
        10. Projeto Final
        11. Dicas para Seguir Aprendendo

        ## Dicas para leitores com TDAH

        - **Faça pausas regulares**: A cada 25-30 minutos, tire uma pausa curta
        - **Pratique ativamente**: Execute os códigos enquanto aprende
        - **Divida em sessões**: Não tente aprender tudo de uma vez
        - **Use marcadores**: Anote pontos que achou importantes para revisar depois
        - **Celebre as pequenas vitórias**: Cada conceito aprendido é uma conquista!
        """)

    st.markdown("---")

    st.markdown("""
    ## Uma mensagem para você

    > "Você consegue aprender programação! Vamos dividir isso em pequenos pedaços 
    > que são mais fáceis de gerenciar. Lembre-se que todo programador experiente 
    > começou sem saber nada. O que importa é a persistência e a prática."
    """)

if __name__ == "__main__":
    main()