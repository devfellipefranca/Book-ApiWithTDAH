import streamlit as st
from utils.helpers import display_chapter_navigation, display_note, display_tip, display_warning, display_code_with_explanation, display_encouragement, display_break_reminder, display_interactive_practice
from utils.code_examples import FLASK_HELLO_WORLD, FASTAPI_HELLO_WORLD

# Configuração da página
st.set_page_config(
    page_title="Primeiros Passos com APIs | APIs do Zero ao Avançado",
    page_icon="📚",
    layout="wide"
)

def main():
    # Título principal
    st.title("4. Primeiros Passos com APIs")

    st.markdown("""
    Chegou o momento que você estava esperando! Neste capítulo, vamos criar nossa primeira API.
    Vamos começar com algo simples e, ao longo do livro, iremos expandir esse conhecimento.

    Você verá que criar uma API básica é mais fácil do que parece!
    """)

    # Seção 1: Frameworks para APIs em Python
    st.markdown("## 4.1. Frameworks para APIs em Python")

    st.markdown("""
    Para criar APIs em Python, usamos **frameworks** - bibliotecas que fornecem ferramentas
    e estruturas para facilitar o desenvolvimento. Os mais populares são:

    ### Flask

    **Flask** é um microframework leve e flexível. É ótimo para começar porque:
    - É simples e fácil de aprender
    - Tem uma curva de aprendizado suave
    - Oferece apenas o essencial, deixando você escolher as extensões que precisar

    ### FastAPI

    **FastAPI** é um framework mais recente, focado em alto desempenho:
    - É extremamente rápido
    - Tem validação automática de dados
    - Gera documentação automaticamente
    - Suporta operações assíncronas

    ### Django Rest Framework

    Baseado no Django, é uma solução mais completa:
    - Oferece muitas funcionalidades prontas
    - Ideal para projetos maiores e mais complexos
    - Tem uma curva de aprendizado mais acentuada

    **Neste livro, usaremos Flask** para os exemplos porque:
    1. É mais simples para iniciantes
    2. Permite entender o que está acontecendo "por baixo do capô"
    3. Os conceitos aprendidos são transferíveis para outros frameworks

    No entanto, também mencionaremos FastAPI ocasionalmente, já que ele está ganhando
    popularidade rapidamente.
    """)

    display_note("Embora existam vários frameworks, a escolha entre eles muitas vezes se resume à preferência pessoal e ao caso de uso específico. O importante é que os conceitos fundamentais das APIs são os mesmos independentemente do framework.")

    # Seção 2: Instalando as ferramentas necessárias
    st.markdown("## 4.2. Instalando as ferramentas necessárias")

    st.markdown("""
    Antes de começarmos a codificar, precisamos configurar nosso ambiente. Se você já tem Python
    instalado, esse processo será bem simples!

    ### Instalando o Flask

    Abra o terminal (ou prompt de comando no Windows) e execute:

    ```
    pip install flask
    ```

    Se você quiser também experimentar o FastAPI mais tarde:

    ```
    pip install fastapi uvicorn
    ```

    O `uvicorn` é um servidor ASGI (Asynchronous Server Gateway Interface) que o FastAPI usa.

    ### Verificando a instalação

    Para confirmar que tudo está funcionando, você pode criar um arquivo Python simples e
    importar o Flask:

    ```python
    from flask import Flask

    print("Flask importado com sucesso!")
    ```

    Se executar este arquivo sem erros, significa que o Flask está instalado corretamente.
    """)

    display_tip("Se você estiver usando um ambiente virtual (o que é recomendado para projetos Python), não se esqueça de ativá-lo antes de instalar as bibliotecas!")

    # Pausa para reflexão
    display_encouragement()

    # Seção 3: Nossa primeira API "Hello World"
    st.markdown("## 4.3. Nossa primeira API: 'Hello World'")

    st.markdown("""
    Vamos criar nossa primeira API! Será um simples "Hello World" para entendermos os conceitos básicos.

    ### Usando Flask
    """)

    display_code_with_explanation(
        FLASK_HELLO_WORLD,
        """
        Vamos analisar este código linha por linha:

        1. `from flask import Flask` - Importamos a classe Flask, que é o coração do framework

        2. `app = Flask(__name__)` - Criamos uma instância da aplicação Flask
           - `__name__` é uma variável especial em Python que contém o nome do módulo atual
           - Isso ajuda o Flask a encontrar recursos associados à aplicação

        3. `@app.route("/")` - Este é um **decorador** que associa a URL "/" à função que vem logo após
           - A URL "/" representa a rota raiz da sua API (como "https://minha-api.com/")
           - Quando alguém acessar essa URL, o Flask chamará a função `hello_world()`

        4. `def hello_world():` - Esta função será executada quando a rota "/" for acessada
           - Ela retorna um dicionário `{"mensagem": "Olá, Mundo! Esta é minha primeira API!"}`
           - O Flask automaticamente converte este dicionário em JSON para a resposta

        5. `if __name__ == "__main__":` - Esta parte só executa quando rodamos o arquivo diretamente
           - `app.run(debug=True, host="0.0.0.0", port=8000)` inicia o servidor
           - `debug=True` habilita o modo de desenvolvimento (recarrega ao modificar o código)
           - `host="0.0.0.0"` permite acesso de qualquer endereço
           - `port=8000` define a porta onde o servidor estará disponível

        Quando executado, este código inicia um servidor web que pode receber requisições HTTP.
        Quando alguém acessa a URL raiz ("/"), o servidor responde com o JSON: `{"mensagem": "Olá, Mundo! Esta é minha primeira API!"}`
        """
    )

    st.markdown("""
    ### Usando FastAPI

    Para comparação, assim seria a mesma API usando FastAPI:
    """)

    display_code_with_explanation(
        FASTAPI_HELLO_WORLD,
        """
        Este código faz exatamente a mesma coisa que o exemplo do Flask, mas usando FastAPI:

        1. `from fastapi import FastAPI` - Importamos a classe FastAPI

        2. `import uvicorn` - Importamos o servidor ASGI que executará nossa aplicação

        3. `app = FastAPI()` - Criamos uma instância da aplicação FastAPI

        4. `@app.get("/")` - Este decorador associa a URL "/" com o método HTTP GET à função abaixo
           - Note que o FastAPI especifica o método HTTP diretamente no decorador

        5. `def hello_world():` - A função que será executada, assim como no Flask

        6. `uvicorn.run(app, host="0.0.0.0", port=8000)` - Inicia o servidor usando o Uvicorn

        A grande diferença é que o FastAPI:
        - É mais explícito sobre os métodos HTTP
        - Usa um servidor ASGI (Uvicorn) que é mais rápido
        - Gera automaticamente documentação (acessível em "/docs" quando o servidor está rodando)
        """
    )

    # Lembrete para pausa
    display_break_reminder()

    # Seção 4: Executando e testando sua primeira API
    st.markdown("## 4.4. Executando e testando sua primeira API")

    st.markdown("""
    Vamos aprender como executar e testar nossa API recém-criada.

    ### Executando a API

    1. Salve o código em um arquivo (por exemplo, `app.py`)

    2. Abra o terminal na pasta onde salvou o arquivo

    3. Execute o comando:

    ```
    python app.py
    ```
    """)

if __name__ == "__main__":
    main()