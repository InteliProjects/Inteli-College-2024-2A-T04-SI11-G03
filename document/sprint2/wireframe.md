# Sumário

[Introdução](#c1)

[Ferramenta](#c2)

[Wireframe](#c3)

[Técnicas Avançadas](#c4)

[Privacy By Design](#c5)

[Feedbacks](#c6)

[Conclusão](#c7)

<br>

# <a name="c1"></a>Introdução

Este documento apresenta o wireframe de baixa fidelidade para a tela de acompanhamento de fraudes da AEGEA, desenvolvido para melhorar a detecção de fraudes no consumo de água. O projeto utiliza **Machine Learning**, tecnologia que permite os computadores aprender com dados e identificar padrões sem intervenção humana direta. Isso ajuda a detectar comportamentos suspeitos de forma automática.

Além disso, o design do sistema adota o princípio de **Privacy by Design**, que garante que a proteção da privacidade dos dados dos consumidores seja uma prioridade desde o início do desenvolvimento. Isso significa que medidas para proteger as informações pessoais foram incorporadas desde a concepção do sistema, garantindo segurança e transparência no tratamento dos dados. 

# <a name="c2"></a>Ferramenta

Para o desenvolvimento do wireframe, utilizou-se a plataforma **Figma**, para designs colaborativo, criação de interfaces e protótipos. Permitindo que equipes trabalhem juntas em tempo real e compartilhem projetos facilmente.

## **Funcionalidades Utilizadas**

- **Componentes:** Utilizados para criar elementos reutilizáveis, como o botão de seleção no wireframe.
- **Prototype**: Facilita a criação de conexões entre telas e a simulação de interações, como a abertura de um modal.
- **Frames**: Servem para organizar e estruturar as telas e seções dentro do design.
- **Grupos**: Facilitam a gestão e a movimentação de múltiplos elementos juntos, ajudando a manter a consistência no layout.

## **Como Interagir com o Protótipo?**

1. Acesse o protótipo através do link que será fornecido nos próximos tópicos.
2. Clique no ícone "➤" no canto superior direito.
3. Deslize o cursor na horizontal para navegar na tela.
4. Clique no simbolo "<img src="../../assets/Icon_modal.svg">" para abrir o modal. 
   
5. Clique no botão de seleção "<img src="../../assets/botao_select.svg" width="120" height="auto">" para ver opções disponíveis.
6. Verifique os notes no Figma para informações adicionais sobre cada elemento da tela.

<br>

# <a name="c3"></a>Wireframe

Este wireframe representa a plataforma destinada ao pessoal do atendimento comercial, permitindo o acompanhamento de fraudes detectadas e análises em aberto. A seguir, são descritos os principais elementos e funcionalidades da tela:

<br>

> [!NOTE]
Neste contexto, 'elementos' referem-se às partes funcionais e estruturais da interface, e não a ícones ou seções componentizadas.

<br>

1. **Upload de Arquivos**: Permite o envio de listas de usuários para análise. O objetivo é determinar se os consumidores listados estão envolvidos em fraudes.

2. **Apresentação de Features**: Exibe as features utilizadas no modelo de Machine Learning e quanto cada uma delas influencia na detecção das fraudes.

3. **Divisão das Análises**: A tela apresenta abas de "Análise" e "Concluídos" que permite visualizar tanto as análises de fraudes já realizadas quanto as que ainda estão em aberto.

4. **Tabela de Fraudes**: Apresenta os usuário submetidos a análise. Para proteger a privacidade dos usuários, a matrícula é mascarada e a localização é exibida como coordenadas de latitude e longitude em vez de endereço completo.

5. **Gráficos**: São apresentados gráficos que mostram o consumo médio de água e o consumo identificado como fraudulento. Além do faturamento total e o faturamento associado a consumos fraudulentos.

6. **Modal de Detalhes**: Ao selecionar uma fraude específica, um modal é aberto, permitindo visualizar detalhes adicionais sobre a matrícula e as features mais relevantes para aquela detecção. O modal também inclui um select que permite ao operador alterar o status que aquela análise se encontra dentro da empresa.

<br>

## Desenvolvimento

Apresentam-se as interações desenvolvidas no wireframe. Além disso, <a href="https://www.figma.com/design/mf8lO89R6IttbnAdRuO8ls/Interface?node-id=0-1&t=EwmpgPr2HVOcjlba-1">Link</a> para acessar o protótipo no Figma.

**Imagem 1:** Interações 

<img src="../../assets/Wireframe.gif">

**Fonte:** Autores

<br>

# <a name="c4"></a> Técnicas Avançadas

Esta seção destaca e explica as técnicas e estratégias específicas utilizadas no desenvolvimento do wireframe.

**1. Navegação Hierárquica**, utilizada para organizar a estrutura das informações de forma que o usuário possa acessar facilmente diferentes níveis de conteúdo. No wireframe, isso é feito para organizar as tarefas do usuário de forma prioritária na tela. Primeiro, posicionamos o carregamento dos dados, seguido pelos principais indicadores (big numbers) e, por fim, a consolidação das fraudes na tabela. Isso ajuda a garantir que as informações mais importantes sejam acessíveis de forma lógica.

**2. Padrões de Design Web:**

- **Feedback Visual:** Implementado através de elementos de botões e modais que reagem às ações do usuário, fornecendo confirmação e informações adicionais, como o botão de seleção de status da análise e o modal de detalhes.
- **Hierarquia Visual:** Utilizada para destacar informações importantes e guiar o usuário através da interface, através do contrastes de tamanhos de fonte e espaçamento.

**3. Componentes Reutilizáveis**, permite uma manutenção mais fácil e uma aparência consistente em todo o projeto, reduzindo a necessidade de criar elementos do zero em cada tela. Nesse caso foi utilizado no botão de Select. 

**4. Protótipos Interativos**, permite simular o comportamento da aplicação, como a navegação entre telas e a interação com elementos de botões e modais. Ajudando a validar a usabilidade e a funcionalidade do design antes da implementação.


<br>


# <a name="c5"></a> Privacy By Design

O conceito de **Privacy by Design** foi pensado no desenvolvimento do wireframe com medidas para proteger a privacidade dos usuários. Sendo elas:

1. **Mascaramento de Dados Sensíveis**: Para proteger a identidade dos usuários, a matrícula é mascarada na tabela de fraudes. Isso evita a exposição direta de informações que poderiam ser usadas para identificar consumidores individualmente.

2. **Localização Geográfica Anonimizada**: Em vez de exibir o endereço completo do consumidor, que poderia comprometer a privacidade, o sistema apresenta a localização de maneira anonimizada, utilizando coordenadas geográficas (latitude e longitude). Isso dificulta a identificação precisa do local.

3. **Controle de Acesso e Transparência**: O modal que exibe detalhes específicos da matrícula só é acessível a operadores autorizados. Além disso, o modal explica as features mais relevantes utilizadas para a detecção da fraude, proporcionando transparência sobre o processo de decisão, mas sem expor dados pessoais desnecessários.

4. **Minimização de Dados**: Apenas os dados estritamente necessários para a análise e acompanhamento das fraudes são exibidos. Isso evita a coleta e exposição de informações excessivas que não são essenciais para o processo de detecção de fraudes.

<br>

# <a name="c6"></a> Feedbacks

O feedback foi coletado de forma online com alunos de outros times de Sistemas de Informação que conhecem o projeto. Foram realizados testes de usabilidade para avaliar os aspectos da plataforma, abaixo está uma tabela com as respostas coletadas, casos de testes realizados e os ajustes feitos com base nas respostas de três pessoas que participaram de cada caso:

| **Feedback Coletado**                                  | **Decisão de Design**                                                | **Ajustes Realizados**                                            | **Caso de Teste**                                              | **Respostas**                     |
|--------------------------------------------------------|-----------------------------------------------------------------------|------------------------------------------------------------------|----------------------------------------------------------------|----------------------------------|
| **Dúvidas sobre a funcionalidade dos indicadores.**   | Clarificar a função dos principais indicadores (big numbers).           | Adicionamos descrições explicativas ao lado dos indicadores. | **Teste de Features**: Testar a compreensão dos indicadores e suas funções. | 2 pessoas entenderam melhor após a adição das descrições, 1 ainda teve dúvidas. |
| **O fluxo de dados não estava claro.**                | Melhorar a sequência e a clareza do carregamento de dados.                     | Reestruturamos a navegação hierárquica para destacar o carregamento de dados primeiro. | **Teste de Fluxo de Dados**: Avaliar a clareza do upload de dados e a sequência de informações. | 3 pessoas acharam o fluxo mais claro após a reestruturação. |
| **Dificuldade em interagir com o modal.**             | Facilitar a interação com modais e outros elementos clicáveis.          | Ajustamos o tamanho dos alvos clicáveis e revisamos a disposição do modal. | **Teste de Modal**: Testar a interação com o modal e a utilização do botão de seleção. | 2 pessoas encontraram melhorias, 1 ainda relatou dificuldade. |

<br>

# <a name="c7"></a> Conclusão

Este wireframe, apesar de ser uma versão inicial, demonstra o pensamento do time para construção e tangibilização da interface alinhada com os objetivos do projeto, oferecendo uma base para refinamentos futuros. Conforme o projeto avança, o wireframe poderá ser ajustado e aprimorado, garantindo que ele continue a atender às necessidades do usuário final. 
