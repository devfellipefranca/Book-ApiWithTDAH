import streamlit as st

def display_chapter_navigation(prev_chapter=None, next_chapter=None):
    """
    Exibe botões de navegação para os capítulos anterior e próximo.
    
    Args:
        prev_chapter (str, optional): Nome do capítulo anterior. None se for o primeiro capítulo.
        next_chapter (str, optional): Nome do capítulo seguinte. None se for o último capítulo.
    """
    st.markdown("---")
    cols = st.columns([1, 1, 1])
    
    with cols[0]:
        if prev_chapter:
            prev_url = f"/{prev_chapter}"
            st.markdown(f"[← Capítulo Anterior]({prev_url})")
    
    with cols[1]:
        st.markdown("[Página Inicial](/)")
    
    with cols[2]:
        if next_chapter:
            next_url = f"/{next_chapter}"
            st.markdown(f"[Próximo Capítulo →]({next_url})")

def display_note(text):
    """
    Exibe uma nota destacada no estilo TDAH-friendly.
    
    Args:
        text (str): Texto da nota a ser exibida.
    """
    st.info(f"📝 **Nota**: {text}")

def display_tip(text):
    """
    Exibe uma dica destacada no estilo TDAH-friendly.
    
    Args:
        text (str): Texto da dica a ser exibida.
    """
    st.success(f"💡 **Dica**: {text}")

def display_warning(text):
    """
    Exibe um aviso destacado no estilo TDAH-friendly.
    
    Args:
        text (str): Texto do aviso a ser exibido.
    """
    st.warning(f"⚠️ **Atenção**: {text}")

def display_encouragement():
    """
    Exibe uma mensagem de encorajamento aleatória.
    """
    import random
    
    messages = [
        "Você está indo muito bem! Continue assim!",
        "Um passo de cada vez. Você consegue!",
        "Está achando difícil? Faça uma pausa curta e volte com a mente renovada.",
        "Lembre-se: todos os programadores experientes já estiveram no seu lugar.",
        "Celebre cada pequena vitória! Cada conceito novo é uma conquista.",
        "A prática leva à perfeição. Continue experimentando!",
        "Você está construindo habilidades valiosas. Tenha orgulho do seu progresso!",
        "Se algo não faz sentido imediatamente, não se preocupe. Às vezes precisamos ver várias vezes."
    ]
    
    st.markdown(f"## 🌟 {random.choice(messages)}")

def display_break_reminder():
    """
    Exibe um lembrete para fazer uma pausa.
    """
    st.markdown("---")
    with st.expander("🧘 Hora de uma pausa?"):
        st.markdown("""
        Se você está lendo há mais de 25-30 minutos, considere fazer uma pequena pausa:
        
        - Levante-se e estique o corpo
        - Beba um copo d'água
        - Olhe para longe da tela por alguns minutos
        - Respire profundamente algumas vezes
        
        Depois, volte com a mente renovada!
        """)
    st.markdown("---")

def display_code_with_explanation(code, explanation, language="python"):
    """
    Exibe um bloco de código com explicação detalhada.
    
    Args:
        code (str): O código a ser exibido.
        explanation (str): Explicação do código.
        language (str, optional): Linguagem do código. Padrão: "python".
    """
    st.code(code, language=language)
    with st.expander("Explicação detalhada", expanded=True):
        st.markdown(explanation)

def display_interactive_practice(instructions, solution_code, solution_explanation):
    """
    Exibe um exercício interativo com instruções e solução.
    
    Args:
        instructions (str): Instruções para o exercício.
        solution_code (str): Código da solução.
        solution_explanation (str): Explicação da solução.
    """
    st.markdown("## 🏋️ Exercício Prático")
    st.markdown(instructions)
    
    user_code = st.text_area("Escreva seu código aqui:", height=200)
    
    if st.button("Verificar solução"):
        with st.expander("Solução", expanded=True):
            st.code(solution_code, language="python")
            st.markdown("### Explicação")
            st.markdown(solution_explanation)
