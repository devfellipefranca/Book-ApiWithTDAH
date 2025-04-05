import streamlit as st
from utils.helpers import display_chapter_navigation, display_note, display_tip, display_warning, display_code_with_explanation, display_encouragement, display_break_reminder, display_interactive_practice
from utils.code_examples import VARIABLES_EXAMPLE, CONDITIONAL_EXAMPLE, LOOP_EXAMPLE, FUNCTION_EXAMPLE

# Configuração da página
st.set_page_config(
    page_title="Fundamentos Básicos | APIs do Zero ao Avançado",
    page_icon="📚",
    layout="wide"
)

def main():
    # Título principal
    st.title("2. Fundamentos Básicos")

    st.markdown("""
    Neste capítulo, vamos aprender os blocos fundamentais da programação. 
    Esses conceitos são a base de tudo que construiremos ao longo do livro.

    Vamos começar com os elementos mais simples e gradualmente avançar para 
    estruturas mais complexas. Não se preocupe - vamos dar um passo de cada vez!
    """)

    # Seção 1: Variáveis e Tipos de Dados
    st.markdown("## 2.1. Variáveis e Tipos de Dados")

    st.markdown("""
    ### O que são variáveis?

    **Variáveis** são como caixas etiquetadas onde guardamos informações no programa. 
    Essas informações podem ser números, textos, listas ou outros tipos de dados.

    **Pense assim:** Se você precisa lembrar o nome de um usuário da sua API para 
    cumprimentá-lo mais tarde, você guarda esse nome em uma variável.

    Em Python, criamos variáveis de forma simples:

    ```python
    nome = "Maria"
    ```

    Neste exemplo:
    - `nome` é o nome da variável (a etiqueta da caixa)
    - `=` é o operador de atribuição (coloca o valor dentro da caixa)
    - `"Maria"` é o valor armazenado (o conteúdo da caixa)

    ### Principais tipos de dados em Python

    Python tem vários tipos de dados embutidos. Os mais comuns são:

    1. **Strings (str)** - Textos:
       ```python
       nome = "Carlos"
       mensagem = 'Olá, mundo!'
       ```

    2. **Inteiros (int)** - Números inteiros:
       ```python
       idade = 25
       quantidade = -10
       ```

    3. **Números de ponto flutuante (float)** - Números decimais:
       ```python
       altura = 1.75
       temperatura = -2.5
       ```

    4. **Booleanos (bool)** - Valores verdadeiro/falso:
       ```python
       esta_ativo = True
       tarefa_concluida = False
       ```

    5. **Listas (list)** - Coleções ordenadas de itens:
       ```python
       frutas = ["maçã", "banana", "laranja"]
       numeros = [1, 2, 3, 4, 5]
       ```

    6. **Dicionários (dict)** - Coleções de pares chave-valor:
       ```python
       pessoa = {"nome": "Ana", "idade": 30, "profissao": "Desenvolvedora"}
       ```

    7. **Nenhum (None)** - Representa a ausência de valor:
       ```python
       resultado = None
       ```

    Vamos ver um exemplo que utiliza diferentes tipos de variáveis:
    """)

    display_code_with_explanation(
        VARIABLES_EXAMPLE,
        """
        Neste exemplo:

        1. Criamos quatro variáveis com diferentes tipos de dados:
           - `nome`: uma string (texto)
           - `idade`: um inteiro (número inteiro)
           - `altura`: um float (número decimal)
           - `is_programadora`: um booleano (verdadeiro/falso)

        2. Depois usamos a função `print()` para exibir essas variáveis.
           - Observe o uso de `f-strings` (o `f` antes das aspas) que permite incluir variáveis diretamente no texto usando `{variavel}`

        Este tipo de código é comum em APIs quando precisamos armazenar informações temporariamente antes de processá-las ou enviá-las como resposta.
        """
    )

    display_tip("As variáveis em Python são dinâmicas - isso significa que o mesmo nome de variável pode armazenar diferentes tipos de dados em momentos diferentes. Porém, é uma boa prática manter o tipo consistente para evitar confusão.")

    # Pausa para reflexão
    display_encouragement()

    # Seção 2: Operadores
    st.markdown("## 2.2. Operadores")

    st.markdown("""
    Os operadores são símbolos especiais que realizam operações em variáveis e valores.

    ### Operadores Aritméticos

    Usados para operações matemáticas básicas:

    - `+` : Adição (`5 + 3` resulta em `8`)
    - `-` : Subtração (`5 - 3` resulta em `2`)
    - `*` : Multiplicação (`5 * 3` resulta em `15`)
    - `/` : Divisão (`5 / 2` resulta em `2.5`)
    - `//`: Divisão inteira (`5 // 2` resulta em `2`)
    - `%` : Módulo (resto da divisão) (`5 % 2` resulta em `1`)
    - `**`: Exponenciação (`5 ** 2` resulta em `25`)

    ### Operadores de Comparação

    Usados para comparar valores:

    - `==`: Igual a (`5 == 5` é `True`)
    - `!=`: Diferente de (`5 != 3` é `True`)
    - `>` : Maior que (`5 > 3` é `True`)
    - `<` : Menor que (`5 < 3` é `False`)
    - `>=`: Maior ou igual a (`5 >= 5` é `True`)
    - `<=`: Menor ou igual a (`5 <= 3` é `False`)

    ### Operadores Lógicos

    Usados para combinar condições:

    - `and`: Retorna `True` se ambas as condições forem verdadeiras
      ```python
      (5 > 3) and (10 < 20)  # True
      ```

    - `or`: Retorna `True` se pelo menos uma das condições for verdadeira
      ```python
      (5 < 3) or (10 < 20)  # True
      ```

    - `not`: Inverte o resultado (verdadeiro vira falso, falso vira verdadeiro)
      ```python
      not (5 < 3)  # True
      ```

    ### Operadores de Atribuição

    Usados para atribuir valores a variáveis:

    - `=`: Atribuição simples (`x = 5`)
    - `+=`: Atribuição com adição (`x += 3` é o mesmo que `x = x + 3`)
    - `-=`: Atribuição com subtração (`x -= 3` é o mesmo que `x = x - 3`)
    - `*=`: Atribuição com multiplicação (`x *= 3` é o mesmo que `x = x * 3`)
    - `/=`: Atribuição com divisão (`x /= 3` é o mesmo que `x = x / 3`)

    ### Exemplo prático com operadores:

    ```python
    # Operadores aritméticos
    preco_produto = 50.0
    quantidade = 3
    total = preco_produto * quantidade
    print(f"Total da compra: R${total}")  # Total da compra: R$150.0

    # Verificando desconto
    tem_desconto = total > 100
    print(f"Cliente tem direito a desconto? {tem_desconto}")  # True

    # Aplicando desconto se o valor for alto E o cliente for premium
    valor_alto = total > 100
    cliente_premium = True

    if valor_alto and cliente_premium:
        total -= 15  # Desconto de R$15 (usando operador de atribuição -=)

    print(f"Total final após possíveis descontos: R${total}")  # R$135.0
    ```

    Em uma API, frequentemente usamos operadores para:
    - Calcular valores (como totais, médias, porcentagens)
    - Verificar condições (se um usuário tem permissão, se um valor está dentro de limites)
    - Combinar dados de diferentes fontes
    """)

    # Seção 3: Estruturas Condicionais
    st.markdown("## 2.3. Estruturas Condicionais")

    st.markdown("""
    As estruturas condicionais permitem que seu programa tome decisões baseadas em condições.

    ### if, elif, else

    A estrutura básica é:

    ```python
    if condição:
        # código executado se a condição for verdadeira
    elif outra_condição:
        # código executado se a primeira condição for falsa e esta for verdadeira
    else:
        # código executado se todas as condições anteriores forem falsas
    ```

    **Nota importante:** Em Python, a indentação (os espaços no início de cada linha) é obrigatória e determina
    quais linhas pertencem a cada bloco de código.
    """)

    display_code_with_explanation(
        CONDITIONAL_EXAMPLE,
        """
        Neste exemplo:

        1. Criamos uma variável `idade` com o valor `18`

        2. Usamos uma estrutura condicional `if` para verificar se a idade é maior ou igual a 18:
           - Se for verdadeiro (como é neste caso), o programa exibe "Você é maior de idade!"
           - Se fosse falso, o programa exibiria "Você é menor de idade."

        Nas APIs, usamos condicionais para:
        - Verificar se um usuário tem permissão para acessar um recurso
        - Validar se os dados recebidos são válidos
        - Decidir qual resposta enviar baseado em diferentes situações
        """
    )

    st.markdown("""
    ### Exemplo mais complexo:

    ```python
    # Verificação de acesso em uma API
    nivel_acesso = "admin"
    recurso_solicitado = "dados_financeiros"

    if nivel_acesso == "admin":
        print("Acesso total concedido.")
    elif nivel_acesso == "gerente" and recurso_solicitado != "dados_financeiros":
        print("Acesso parcial concedido.")
    elif nivel_acesso == "usuario" and recurso_solicitado == "perfil_pessoal":
        print("Acesso limitado concedido.")
    else:
        print("Acesso negado.")
    ```

    Este tipo de verificação é extremamente comum em APIs para controlar quem pode acessar quais recursos.
    """)

    display_tip("Você pode encadear quantos `elif` precisar, mas tente manter a estrutura simples. Se sua condição estiver ficando muito complexa, considere dividir em funções menores ou usar uma estrutura diferente.")

    # Lembrete para pausa
    display_break_reminder()

    # Seção 4: Estruturas de Repetição (Loops)
    st.markdown("## 2.4. Estruturas de Repetição (Loops)")

    st.markdown("""
    Loops são estruturas que permitem executar um bloco de código repetidamente. Em Python, temos dois tipos principais:

    ### Loop for

    O loop `for` é usado para iterar sobre uma sequência (como lista, tupla, dicionário, string) ou outros objetos iteráveis.

    Sintaxe básica:
    ```python
    for item in sequencia:
        # código a ser executado para cada item
    ```

    ### Loop while

    O loop `while` executa um bloco de código enquanto uma condição for verdadeira.

    Sintaxe básica:
    ```python
    while condição:
        # código a ser executado enquanto a condição for verdadeira
    ```

    Vamos ver exemplos de ambos:
    """)

    display_code_with_explanation(
        LOOP_EXAMPLE,
        """
        Este exemplo mostra duas formas de contar de 1 a 5:

        1. Usando o loop `for`:
           - `range(1, 6)` cria uma sequência de números de 1 até 5 (o último número, 6, não é incluído)
           - Para cada número nessa sequência, o código dentro do loop é executado
           - A variável `numero` assume cada valor da sequência, um de cada vez

        2. Usando o loop `while`:
           - Primeiro definimos `contador = 1` para começar
           - Enquanto `contador <= 5` for verdadeiro, o código dentro do loop é executado
           - Dentro do loop, aumentamos o contador com `contador += 1` para evitar um loop infinito

        Em APIs, usamos loops para:
        - Processar múltiplos registros de um banco de dados
        - Iterar sobre itens em uma requisição (como uma lista de produtos em um pedido)
        - Realizar verificações repetitivas enquanto uma condição for atendida
        """
    )

    st.markdown("""
    ### Controle de Loop: break e continue

    Às vezes, precisamos de mais controle sobre nossos loops:

    - `break`: Interrompe completamente o loop
    - `continue`: Pula para a próxima iteração do loop

    Exemplo:

    ```python
    # Processando uma lista de usuários, mas pulando usuários inativos
    usuarios = [
        {"id": 1, "nome": "Ana", "ativo": True},
        {"id": 2, "nome": "Bruno", "ativo": False},
        {"id": 3, "nome": "Carla", "ativo": True},
        {"id": 4, "nome": "Daniel", "ativo": True}
    ]

    print("Processando usuários ativos:")
    for usuario in usuarios:
        if not usuario["ativo"]:
            print(f"Usuário {usuario['nome']} inativo. Pulando...")
            continue

        print(f"Processando dados do usuário {usuario['nome']}...")

        # Se encontrarmos o ID 3, interrompemos o loop
        if usuario["id"] == 3:
            print("Usuário específico encontrado. Interrompendo processamento.")
            break
    ```

    Este padrão é comum em APIs quando estamos processando lotes de dados e precisamos lidar com casos especiais.
    """)

    display_warning("Cuidado com loops infinitos! Se um loop `while` nunca tiver sua condição alterada para `False`, ele continuará rodando para sempre e pode travar seu programa.")

    # Pausa para reflexão
    display_encouragement()

    # Seção 5: Funções
    st.markdown("## 2.5. Funções")

    st.markdown("""
    Funções são blocos de código reutilizáveis que executam uma tarefa específica. Elas são fundamentais para organizar código, evitar repetição e tornar o programa mais legível.

    ### Definindo funções

    Em Python, definimos funções com a palavra-chave `def`:

    ```python
    def nome_da_funcao(parametro1, parametro2):
        # código da função
        return resultado
    ```

    - `def`: palavra-chave que indica o início da definição de uma função
    - `nome_da_funcao`: o nome que você escolhe para a função
    - `parametro1, parametro2`: dados que a função precisa para executar (opcionais)
    - `return`: palavra-chave para devolver um valor (opcional)
    """)

    display_code_with_explanation(
        FUNCTION_EXAMPLE,
        """
        Neste exemplo:

        1. Definimos uma função chamada `saudacao` que:
           - Recebe um parâmetro: `nome`
           - Tem um comentário de documentação (docstring) entre aspas triplas que explica o que a função faz
           - Retorna uma string personalizada de saudação

        2. Chamamos a função com o argumento `"Ana"` e armazenamos o resultado na variável `mensagem`

        3. Exibimos a mensagem retornada

        Em APIs, usamos funções para:
        - Organizar código para diferentes rotas e endpoints
        - Processar dados recebidos nas requisições
        - Formatar respostas para serem enviadas
        - Reutilizar lógica comum em diferentes partes da aplicação
        """
    )

    st.markdown("""
    ### Parâmetros e Argumentos

    - **Parâmetros** são as variáveis listadas na definição da função
    - **Argumentos** são os valores reais que passamos para a função

    Python oferece várias formas de trabalhar com parâmetros:

    #### Parâmetros com valores padrão:

    ```python
    def saudacao(nome, mensagem="Olá"):
        return f"{mensagem}, {nome}!"

    # Podemos chamar de diferentes formas:
    print(saudacao("Maria"))            # Olá, Maria!
    print(saudacao("João", "Bem-vindo")) # Bem-vindo, João!
    ```
    """)

    # Adicione aqui o restante do seu código, caso haja...
    

main()