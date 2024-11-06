## Sumário

[1. Introdução](#c1)

[2. User Story 1: Padrões anômalos](#c2)

[3. User Story 2: Interface intuitiva](#c3)

[4. User Story 3: PDFs das visualizações](#c4)

[5. Conclusão](#c4)

<br>

# <a name="c1"></a>1. Introdução

&emsp;&emsp; João Silva, de 32 anos, trabalha como atendente comercial na Aegea e possui experiência anterior como atendente em uma agência bancária. Ele é casado, de classe média, e tem interesse por soluções práticas que facilitem o trabalho diário. Apesar de seu interesse, João enfrenta dificuldades em lidar com processos técnicos complexos e deseja ferramentas que simplifiquem e tornem mais claro o trabalho de análise de fraudes, permitindo uma participação mais ativa nas decisões. <br>
&emsp;&emsp; João valoriza plataformas que sejam acessíveis e intuitivas, com uma linguagem prática que se adapte ao seu nível de entendimento. Ele busca soluções que agilizem a identificação de casos suspeitos, economizando tempo e reduzindo o estresse causado pela complexidade das tarefas administrativas. O cenário ideal para ele é poder revisar relatórios e lidar com suspeitas de fraude de forma mais eficiente e sem a necessidade de realizar análises complexas.

# <a name="c2"></a>2. User Story 1: Padrões anômalos

&emsp;&emsp; A primeira user story é:

"Como atendente comercial, quero uma **plataforma que identifique padrões anômalos de consumo para agir rapidamente em casos suspeitos**, evitando fraudes e reduzindo análises manuais."

&emsp;&emsp; Ela tem como objetivo exemplificar a necessidade do usuário, o João, que precisa de uma plataforma que ajude na identificação de padrões suspeitos de consumo, que assim auxilia os analistas comerciais a identificar fraudes rapidamente e de forma eficaz. Para essa história temos alguns critérios de aceitação que devem ocorrer para que seja verdadeira, para cada critério, temos alguns testes para validar o acontecimento.

## 2.1 Detecção Automática de Anomalias

Prioridade: Alta
Estimativa de Esforço: 8 pontos

&emsp;&emsp; Este critério foca na capacidade da plataforma de identificar automaticamente padrões de consumo que sejam anômalos. A ideia é que a plataforma seja eficiente em detectar comportamentos suspeitos ou fora do comum sem a necessidade de intervenção manual constante, garantindo que fraudes ou problemas possam ser identificados de maneira rápida e precisa.

**Teste 1: Validação de Precisão na Detecção**  

&emsp;&emsp; Neste teste, a plataforma é desafiada com um conjunto de dados que contém anomalias conhecidas. O objetivo é verificar quantas dessas anomalias a plataforma consegue detectar corretamente, com a expectativa de que pelo menos 80% sejam identificadas. (Esse número pode mudar de acordo com o andamento do projeto.)

**Teste 2: Detecção de Falsos Positivos**  

&emsp;&emsp; A plataforma é testada com um conjunto de dados que não contém anomalias. O objetivo é medir quantos falsos positivos a plataforma gera, com o limite aceitável de no máximo 5%, garantindo que a plataforma não sinalize erroneamente dados normais como anômalos. (Esse número pode mudar de acordo com o andamento do projeto.)

## 2.2 Alerta Utilizando Cores no Sistema

Prioridade: Média
Estimativa de Esforço: 5 pontos

&emsp;&emsp; Este critério é descreve a forma como as anomalias identificadas são destacadas visualmente no sistema. A utilização de cores é fundamental para ajudar os usuários a reconhecer rapidamente o nível de risco associado a uma anomalia. O sistema deve ser capaz de usar cores de maneira eficaz para comunicar diferentes níveis de perigo, e essas cores devem ser claramente visíveis e compreensíveis por todos os usuários, incluindo aqueles com deficiências visuais.

**Teste 1: Verificação de Cores Correspondentes aos Níveis de Anomalia**  

&emsp;&emsp; Este teste verifica se as cores utilizadas para destacar as anomalias no sistema correspondem adequadamente ao nível de risco associado a cada uma delas. O sistema deve ser capaz de representar visualmente as anomalias com cores que indiquem claramente o grau de severidade.

**Teste 2: Usabilidade e Visibilidade das Cores no Sistema**  

&emsp;&emsp; A plataforma é avaliada em diferentes condições de iluminação e por usuários com deficiência visual para assegurar que as cores dos alertas são visíveis e distinguíveis por todos. O teste garante que a usabilidade do sistema seja mantida para todos os usuários. (Utilizar : https://www.guia-wcag.com/)

## 2.3 Visualização Gráfica de Anomalias

Prioridade: Alta
Estimativa de Esforço: 8 pontos

&emsp;&emsp; A visualização gráfica das anomalias deve ser clara e intuitiva, permitindo que os usuários vejam de forma direta os padrões anômalos detectados. Este critério se refere à capacidade do sistema de apresentar os dados de forma que facilite a identificação rápida de problemas e permita uma análise mais detalhada e interativa das anomalias ao longo do tempo.

**Teste 1: Clareza da Visualização Gráfica**  

&emsp;&emsp; Neste teste, o objetivo é verificar se as anomalias são claramente representadas nos gráficos, permitindo que o usuário identifique rapidamente problemas. A clareza visual é essencial para que os dados façam sentido para o usuário e sejam úteis na tomada de decisões.

**Teste 2: Interatividade da Visualização Gráfica**  

&emsp;&emsp; A interatividade é testada verificando se o gráfico permite a filtragem dos dados por períodos de tempo. O teste garante que a visualização gráfica seja não apenas clara, mas também dinâmica, permitindo uma análise mais aprofundada e personalizada.

## 2.4 Classificação de Anomalias

&emsp;&emsp; Aqui, o foco está em como a plataforma classifica as anomalias detectadas. A plataforma deve ser capaz de atribuir corretamente um nível de risco a cada anomalia, com base em parâmetros configuráveis. Isso permite que as anomalias sejam tratadas com a seriedade apropriada e que os usuários possam priorizar as ações necessárias.

**Teste 1: Precisão na Classificação das Anomalias**  

&emsp;&emsp; Este teste verifica se a plataforma é capaz de classificar corretamente as anomalias em diferentes níveis de risco. O objetivo é garantir que pelo menos 80% das anomalias sejam classificadas de acordo com o nível de risco apropriado. (Esse número pode mudar de acordo com o andamento do projeto.)

**Teste 2: Flexibilidade e Configuração da Classificação**  

&emsp;&emsp; Este teste verifica a capacidade da plataforma de filtrar a classificação das anomalias com base em parâmetros configuráveis. A flexibilidade é essencial para adaptar o sistema a diferentes cenários e garantir que os ajustes sejam refletidos corretamente na classificação das anomalias.

## 2.5 Sugestões de Ação**  

&emsp;&emsp; Este critério se refere à capacidade da plataforma de não apenas detectar e classificar anomalias, mas também fornecer sugestões de ação relevantes e específicas para cada tipo de anomalia. Isso ajuda os usuários a tomarem decisões informadas rapidamente, baseadas em recomendações que são diretamente aplicáveis ao cenário em questão.
 
**Teste 1: Relevância das Sugestões de Ação**  

&emsp;&emsp; O teste avalia se a plataforma fornece sugestões de ação que sejam específicas e relevantes para o tipo de anomalia detectada. A plataforma deve ser capaz de oferecer recomendações que ajudem o usuário a tomar decisões informadas rapidamente, contribuindo para a eficácia na resolução das anomalias detectadas.

# <a name="c3"></a>3. User Story 2: Interface intuitiva

&emsp;&emsp; A segunda user story é:

"Como um **atendente comercial, quero uma interface intuitiva para que eu possa identificar rapidamente possíveis fraudes e reportá-las sem precisar entender jargões técnicos**."

&emsp;&emsp; Essa user story visa a criação de uma interface amigável e acessível, especialmente para profissionais como os analistas do comercial, que necessitam de uma ferramenta que permita a identificação rápida de fraudes sem a necessidade de conhecimentos técnicos profundos. Para essa história, foram definidos critérios de aceitação específicos para garantir que a solução atenda às necessidades do usuário final.

## 3.1 Navegação Simplificada

Prioridade: Alta
Estimativa de Esforço: 5 pontos

&emsp;&emsp; Este critério foca na simplicidade da navegação dentro da plataforma. A interface deve permitir que os usuários encontrem e utilizem funcionalidades importantes sem a necessidade de múltiplos cliques ou assistência externa.

**Teste 1: Verificação da Profundidade da Navegação**

&emsp;&emsp; Neste teste, diferentes usuários realizam testes de usabilidade onde são instruídos a navegar até uma função específica dentro da plataforma. A execução do teste envolve observar se os usuários conseguem acessar a função dentro do limite de cliques e sem assistência.

**Resultado esperado:** Todos os analistas devem conseguir navegar até a função especificada de maneira independente.

## 3.2 Terminologia Não Técnica

Prioridade: Média
Estimativa de Esforço: 3 pontos

&emsp;&emsp; Este critério aborda a clareza dos textos e rótulos utilizados na interface, garantindo que os termos sejam compreensíveis para todos os usuários, independentemente de seu nível de conhecimento técnico.

**Teste 1: Revisão de Conteúdo**

&emsp;&emsp; Neste teste, todos os textos e rótulos presentes na interface são revisados para garantir que estão livres de jargões técnicos. Pessoas sem conhecimento especializado são envolvidas para testar a compreensão dos termos utilizados.

**Resultado esperado:** Textos e rótulos devem estar livres de jargões técnicos e serem compreensíveis por usuários sem conhecimento especializado.

**Teste 2: Feedback de Usuários**

&emsp;&emsp; Um grupo de analistas comerciais é convidado a utilizar a plataforma para identificar quaisquer termos que considerem técnicos. O feedback é então coletado e analisado para verificar se os termos utilizados são claros.

**Resultado esperado:** O feedback deve indicar que os termos usados são claros e compreensíveis.

## 3.3 Feedback Visual Imediato

Prioridade: Alta
Estimativa de Esforço: 4 pontos

&emsp;&emsp; Este critério assegura que a interface ofereça um feedback visual claro e imediato em resposta às ações dos usuários, o que é essencial para uma navegação fluida e eficiente.

**Teste 1: Verificação de Feedback Visual**

&emsp;&emsp; O teste avalia se cada ação realizada pelo atendente comercial na plataforma é seguida por um feedback visual claro e imediato. 

**Resultado esperado:** Todas as ações devem gerar um feedback visual imediato e claro, garantindo que o usuário saiba que sua ação foi registrada corretamente pela plataforma.

# <a name="c3"></a>3. User Story 3: Interface intuitiva

&emsp;&emsp; A terceira user story é:

"Como um **atendente comercial, quero uma ferramenta que gere PDFs das visualizações das fraudes de água, para que eu possa compartilhá-los com os meus gestores e fiscalizadores da empresa**."

&emsp;&emsp; Essa user story tem como objetivo fornecer aos analistas do comercial a capacidade de gerar documentos PDF que contenham visualizações detalhadas e precisas sobre fraudes de água. Esses documentos são essenciais para comunicação interna e relatórios formais que são compartilhados com gestores e fiscalizadores. A seguir, são descritos os critérios de aceitação e os testes necessários para garantir que essa funcionalidade atenda às expectativas.

## 4.1 Geração de PDFs com Visualizações Precisas

Prioridade: Alta
Estimativa de Esforço: 6 pontos

&emsp;&emsp; Este critério foca na qualidade das visualizações geradas em PDF, assegurando que a precisão e a consistência da informação sejam mantidas, independentemente do formato de saída.

**Teste 1: Verificação de Qualidade Gráfica**

&emsp;&emsp; Neste teste, o atendente comercial gera um PDF de uma visualização complexa do consumo de água. A execução do teste envolve comparar a visualização na ferramenta com o PDF gerado para verificar a qualidade.

**Resultado esperado:** O PDF deve manter a mesma qualidade gráfica e precisão dos dados presentes na visualização original.

**Teste 2: Consistência de Formatação**

&emsp;&emsp; Neste teste, o atendente comercial utiliza diferentes tipos de gráficos para gerar PDFs e verificar se a formatação dos gráficos é consistente.

**Resultado esperado:** A formatação deve ser consistente e fiel ao design original, assegurando que todos os gráficos mantenham a integridade visual.

## 4.2 Facilidade de Geração de PDFs

Prioridade: Média
Estimativa de Esforço: 4 pontos

&emsp;&emsp; Este critério aborda a usabilidade da ferramenta, garantindo que a geração de PDFs seja acessível e eficiente para os usuários.

**Teste 1: Acessibilidade do Botão de Geração de PDF**

&emsp;&emsp; Neste teste, o atendente comercial navega até uma visualização de consumo de água e verifica a presença e a acessibilidade do botão ou opção para gerar o PDF.

**Resultado esperado:** O botão de geração de PDF deve estar visível e acessível, garantindo que os usuários possam facilmente encontrar e utilizar essa funcionalidade.

**Teste 2: Tempo de Geração de PDF**

&emsp;&emsp; Neste teste, o atendente comercial clica para gerar um PDF de uma visualização, e o tempo necessário para que o PDF seja gerado e esteja pronto para download é medido.

**Resultado esperado:** O PDF deve ser gerado rapidamente, assegurando uma experiência de usuário eficiente e sem atrasos desnecessários.


# <a name="c5"></a>5. Conclusão

&emsp;&emsp; O desenvolvimento das funcionalidades descritas nas três user stories visa atender às necessidades dos analistas do comercial, garantindo uma plataforma robusta, intuitiva e eficaz para a detecção e comunicação de fraudes de água. A primeira user story aborda a **detecção de padrões anômalos**, permitindo que os analistas identifiquem rapidamente situações suspeitas e tomem as devidas providências com base em alertas visuais claros e acessíveis. A segunda user story foca na **interface intuitiva**, assegurando que a navegação e a terminologia da plataforma sejam acessíveis e compreensíveis para todos os usuários, independentemente de seu nível técnico. Por fim, a terceira user story trata da **geração de PDFs das visualizações**, facilitando a comunicação e o compartilhamento de informações críticas com gestores e fiscalizadores de maneira eficiente e visualmente consistente.

Figma: https://www.figma.com/design/yriDV7XtMmgQnbQJMfAVuw/User-Story?node-id=205-3&t=uBbC4tsqw5YlmuvZ-1
