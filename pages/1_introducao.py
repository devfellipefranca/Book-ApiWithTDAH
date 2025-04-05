import streamlit as st
from utils.helpers import display_chapter_navigation, display_note, display_tip, display_code_with_explanation, display_encouragement, display_break_reminder
from utils.code_examples import HELLO_WORLD

# Configuração da página
st.set_page_config(
    page_title="Introdução | APIs do Zero ao Avançado",
    page_icon="📚",
    layout="wide"
)

def main():
    # Título principal
    st.title("1. Introdução à Programação e APIs")
    
    st.markdown("""
    Bem-vindo ao primeiro capítulo da nossa jornada! Vamos começar entendendo os conceitos básicos
    que serão o alicerce para tudo que vamos aprender. Não se preocupe se alguns termos parecerem
    estranhos agora - iremos explorar cada um deles com calma.
    """)
    
    # Seção 1: O que é Programação
    st.markdown("## 1.1. O que é Programação?")
    
    st.markdown("""
    **Programação** é como dar instruções para um computador fazer algo. Imagine que você está
    ensinando uma receita para alguém que nunca cozinhou na vida e que segue exatamente o que
    você diz, sem improvisar:
    
    - "Pegue dois ovos"
    - "Quebre-os em uma tigela"
    - "Bata os ovos até ficarem homogêneos"
    
    A programação funciona de forma similar: você escreve uma sequência de instruções precisas
    que o computador vai seguir na ordem exata que você determinar. Essas instruções são escritas
    em linguagens de programação.
    
    ### Linguagens de Programação
    
    São idiomas especiais criados para nos comunicarmos com computadores. Assim como existem
    português, inglês e espanhol para comunicação entre pessoas, existem Python, JavaScript,
    Java e muitas outras linguagens para nos comunicarmos com máquinas.
    
    Neste livro, vamos usar **Python** - uma linguagem conhecida por ser:
    
    - Fácil de aprender e ler
    - Muito parecida com a linguagem humana
    - Amplamente usada em desenvolvimento web e APIs
    - Versátil para diferentes tipos de aplicações
    
    ### Vamos ver como é um programa simples em Python:
    """)
    
    display_code_with_explanation(
        HELLO_WORLD,
        """
        Este é o código mais básico que podemos escrever em Python:
        
        `print("Olá, Mundo!")` - Esta linha está dizendo ao computador: "Mostre a mensagem 'Olá, Mundo!' na tela". 
        
        - `print` é uma função (um comando) que exibe mensagens
        - As aspas `"..."` indicam um texto (chamado de string em programação)
        - Os parênteses `(...)` contêm o que queremos mostrar
        
        Este simples programa já tem todos os ingredientes básicos da programação: damos uma instrução 
        clara para o computador executar!
        """
    )
    
    # Pausa para reflexão
    display_encouragement()
    
    # Seção 2: O que são APIs
    st.markdown("## 1.2. O que são APIs?")
    
    st.markdown("""
    Agora que sabemos o que é programação, vamos entender o que são APIs.
    
    **API** significa **Interface de Programação de Aplicações** (Application Programming Interface). 
    Parece complicado, mas o conceito é mais simples do que o nome sugere.
    
    ### Usando uma analogia:
    
    Imagine um restaurante:
    - Você (cliente) não vai até a cozinha preparar sua própria comida
    - Em vez disso, você faz seu pedido através de um garçom
    - O garçom leva seu pedido para a cozinha
    - Os cozinheiros preparam a comida
    - O garçom traz o prato pronto para você
    
    Nessa analogia:
    - A **cozinha** é como um sistema ou banco de dados
    - O **garçom** é a API
    - O **menu** é a documentação da API
    - Você é o **desenvolvedor** querendo usar um serviço
    
    A API é um intermediário que permite que diferentes sistemas se comuniquem entre si de forma organizada. 
    Ela define quais pedidos podem ser feitos, como fazer esses pedidos e qual formato de resposta esperar.
    
    ### Por que as APIs são importantes?
    
    1. **Acesso a recursos externos**: Permitem que seu programa use dados ou funcionalidades de outros serviços
    2. **Ocultam complexidade**: Você não precisa saber como o sistema funciona internamente
    3. **Padronização**: Estabelecem regras claras para comunicação entre sistemas
    4. **Segurança**: Controlam quem pode acessar quais dados e como
    
    ### Exemplos do dia a dia:
    
    - Quando um aplicativo de clima mostra a previsão do tempo, ele está usando uma API de serviço meteorológico
    - Quando você faz login em um site usando sua conta do Google, o site está usando a API do Google
    - Quando você faz um pagamento online, o site está se comunicando com a API do banco ou serviço de pagamento
    """)
    
    display_note("As APIs estão em toda parte no mundo digital, mesmo que você não perceba. Na verdade, a maioria dos aplicativos que você usa diariamente depende de várias APIs para funcionar!")
    
    # Seção 3: Tipos de APIs
    st.markdown("## 1.3. Tipos de APIs")
    
    st.markdown("""
    Existem diferentes tipos de APIs, cada uma com suas características e propósitos específicos:
    
    ### 1. APIs Web (REST, GraphQL, SOAP)
    
    São as mais comuns e permitem a comunicação através da internet usando o protocolo HTTP.
    
    - **REST** (Representational State Transfer): 
      - É o tipo mais usado atualmente
      - Utiliza métodos HTTP padrão (GET, POST, PUT, DELETE)
      - Fácil de entender e implementar
      - O que vamos focar neste livro!
    
    - **GraphQL**:
      - Mais moderna e flexível
      - Permite que o cliente especifique exatamente quais dados quer receber
      - Útil para aplicações complexas com muitos tipos de dados inter-relacionados
    
    - **SOAP** (Simple Object Access Protocol):
      - Mais antiga e estruturada
      - Usa XML para formatação de mensagens
      - Geralmente mais verbosa e complexa que REST
    
    ### 2. APIs de Biblioteca/Framework
    
    São conjuntos de funções e procedimentos que você pode usar no seu código:
    
    - A biblioteca padrão do Python (como `math`, `datetime`, etc.)
    - Frameworks como Django ou Flask para criar aplicações web
    
    ### 3. APIs de Sistema Operacional
    
    Permitem que os programas interajam com o sistema operacional:
    
    - Acesso a arquivos
    - Gestão de processos
    - Operações de rede
    """)
    
    # Seção 4: Como funcionam as APIs Web
    st.markdown("## 1.4. Como funcionam as APIs Web")
    
    st.markdown("""
    Como vamos focar em APIs Web (especificamente REST) neste livro, vamos entender melhor como elas funcionam:
    
    ### O modelo Cliente-Servidor
    
    1. **Cliente**: Quem faz a solicitação (request)
       - Pode ser um navegador, um aplicativo mobile, ou outro sistema
    
    2. **Servidor**: Quem responde à solicitação (response)
       - Processa o pedido
       - Acessa dados conforme necessário
       - Retorna uma resposta
    
    ### O fluxo básico:
    
    1. O cliente envia uma **requisição** para um **endpoint** (um URL específico)
    2. A requisição inclui um **método HTTP** (GET, POST, etc.) que indica a ação desejada
    3. O servidor processa a requisição
    4. O servidor envia uma **resposta** que contém:
       - Um **código de status** (como 200 para sucesso, 404 para "não encontrado")
       - Os **dados** solicitados (geralmente em formato JSON ou XML)
    5. O cliente recebe e processa a resposta
    
    ### Um exemplo prático:
    
    Imagine um app de lista de tarefas:
    
    1. Para **ver todas as tarefas**:
       - Requisição: `GET /tarefas`
       - Resposta: Lista de tarefas em formato JSON
    
    2. Para **adicionar uma nova tarefa**:
       - Requisição: `POST /tarefas` com dados da tarefa no corpo
       - Resposta: Confirmação de criação e dados da nova tarefa
    
    3. Para **atualizar uma tarefa**:
       - Requisição: `PUT /tarefas/42` com novos dados
       - Resposta: Dados atualizados da tarefa
    
    4. Para **excluir uma tarefa**:
       - Requisição: `DELETE /tarefas/42`
       - Resposta: Confirmação de exclusão
    
    Este modelo de interação é poderoso porque é simples, stateless (não guarda estado entre requisições) 
    e permite que diferentes sistemas se comuniquem independentemente de como foram implementados internamente.
    """)
    
    display_tip("Pense nas APIs como contratos: elas definem como dois sistemas devem se comunicar, mas não como cada sistema funciona internamente. Isso permite que cada lado evolua independentemente, desde que mantenha o 'contrato' da API.")
    
    # Lembrete para pausa
    display_break_reminder()
    
    # Seção 5: Por que aprender sobre APIs
    st.markdown("## 1.5. Por que aprender sobre APIs?")
    
    st.markdown("""
    Agora que sabemos o que são APIs e como funcionam, por que é importante aprender a criá-las? Existem vários motivos:
    
    ### 1. Habilidade muito valorizada no mercado
    
    A criação de APIs é uma das habilidades mais procuradas para desenvolvedores backend. Muitas empresas 
    precisam de pessoas que saibam construir e manter APIs robustas para seus produtos e serviços.
    
    ### 2. Base para aplicações modernas
    
    A maioria das aplicações modernas são construídas como:
    - **Frontend**: A interface que os usuários veem e interagem
    - **Backend**: A lógica e processamento de dados que acontece no servidor
    - **API**: A ponte que conecta os dois
    
    Ao aprender a construir APIs, você entende como esses componentes se comunicam e pode trabalhar em qualquer parte desse ecossistema.
    
    ### 3. Integração de sistemas
    
    As APIs permitem que diferentes sistemas se comuniquem. Essa habilidade é crucial para:
    - Conectar serviços internos de uma empresa
    - Integrar com serviços externos (pagamentos, mapas, redes sociais)
    - Criar automações entre diferentes ferramentas
    
    ### 4. Ampliação de possibilidades
    
    Quando você cria uma API para seu serviço:
    - Outros desenvolvedores podem construir sobre seu trabalho
    - É possível ter diferentes interfaces (web, mobile, desktop) usando o mesmo backend
    - Você pode escalar diferentes partes do sistema independentemente
    
    ### 5. Compreensão do ecossistema digital
    
    Entender APIs te dá uma visão mais clara de como a internet e os serviços digitais funcionam nos bastidores, 
    mesmo que você não trabalhe diretamente com elas no futuro.
    """)
    
    # Seção 6: Nossa jornada de aprendizado
    st.markdown("## 1.6. Nossa jornada de aprendizado")
    
    st.markdown("""
    Neste livro, vamos seguir um caminho estruturado para aprender a criar APIs do zero:
    
    1. Começaremos com os **fundamentos da programação** em Python
    2. Aprenderemos sobre **estruturas de dados** essenciais
    3. Daremos os **primeiros passos** criando APIs simples
    4. Entenderemos os **métodos HTTP** e como usá-los
    5. Aprenderemos a **manipular dados** recebidos e enviados
    6. Implementaremos **armazenamento** para nossas APIs
    7. Abordaremos **validação e segurança**
    8. Criaremos **APIs mais avançadas** com bancos de dados
    9. Desenvolveremos um **projeto final** completo
    
    Ao longo dessa jornada, vamos construir exemplos práticos e úteis, sempre explicando cada passo 
    do processo. Nosso foco será em aprender de forma gradual, sem sobrecarregar com muita informação de uma vez.
    """)
    
    display_note("Este livro foi especialmente projetado para pessoas com TDAH. Por isso, usamos exemplos concretos, dividimos o conteúdo em partes gerenciáveis e incluímos lembretes para pausas. Se algum conceito parecer difícil, não se preocupe - vamos revisitá-lo de diferentes maneiras ao longo do livro.")
    
    # Seção 7: Conclusão e preparação
    st.markdown("## 1.7. Preparando-se para a jornada")
    
    st.markdown("""
    Antes de avançarmos para o próximo capítulo, vamos garantir que você está pronto para começar:
    
    ### O que você vai precisar:
    
    1. **Um computador** com acesso à internet
    2. **Python instalado** - usaremos a versão 3.6 ou superior
    3. **Um editor de código** - recomendamos VSCode, PyCharm ou até mesmo o Jupyter Notebook para iniciantes
    4. **Paciência e curiosidade** - as habilidades mais importantes para aprender programação!
    
    ### Dicas para um aprendizado eficaz:
    
    - **Pratique ativamente**: Não apenas leia o código, digite-o e experimente modificá-lo
    - **Faça pausas regulares**: A cada 25-30 minutos, levante-se e descanse por 5 minutos
    - **Experimente por conta própria**: Tente resolver os desafios antes de olhar as respostas
    - **Não se compare aos outros**: Cada pessoa tem seu próprio ritmo de aprendizado
    - **Celebre pequenas vitórias**: Cada novo conceito aprendido é uma conquista!
    
    No próximo capítulo, vamos começar com os fundamentos básicos da programação em Python.
    Mal posso esperar para continuar essa jornada com você!
    """)
    
    display_encouragement()
    
    # Navegação entre capítulos
    display_chapter_navigation(None, "2_fundamentos_basicos")

if __name__ == "__main__":
    main()
