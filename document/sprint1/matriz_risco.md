# Matriz de riscos 

A matriz de riscos é um instrumento que proporciona uma visão geral dos riscos ligados a um projeto. Esses riscos podem ser percebidos tanto como ameaças potenciais quanto como oportunidades em potencial. Essa ferramenta nos auxilia a avaliar cada risco considerando sua probabilidade de ocorrência e o impacto que pode ter sobre o projeto. Segue foto com a extensão dos riscos e das oportunidades, assim com sua descrição:

<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G03/blob/feature/s1/matriz-riscos/assets/MatrizRisco.png"> 

## Riscos

1 - Complexidade no Modelamento de Variáveis Exógenas;

2 - Custos Elevados de Implementação;

3 - Dados Voláteis e Diversificados;

4 - Dados dos Últimos 10 Anos;

5 - Desempenho Insuficiente do Modelo;

6 - Integração com o sistema da Azure para Produção de ML e visualização das informações;

7 - Falta de conhecimento sobre códigos utilizados pelo parceiro;

8 - Riscos de Segurança e Privacidade dos Dados;

9 - Confiabilidade dos Dados Externos;

10 - Dificuldade na Implementação de Redes Neurais.

11 - Qualquer tipo de clusterização por etnia, ou enviesamento do modelo, poderia atribuir um conceito tendencioso e possivelmente preconceituoso em relação à identificação de fraudes.

### Descrição e contextualização dos Riscos

A complexidade no modelamento de variáveis exógenas é um desafio significativo, pois variáveis como índices macroeconômicos e climáticos são difíceis de modelar e correlacionar com fraudes. Esse desafio aumenta a complexidade no desenvolvimento de modelos de Machine Learning, exigindo maior expertise técnica. Além disso, os custos elevados de implementação representam um risco considerável. Custos imprevistos ou subestimados podem comprometer o orçamento do projeto e impactar sua viabilidade, pressionando os recursos disponíveis. A implementação de soluções avançadas requer investimentos significativos em infraestrutura, recursos humanos especializados e ferramentas tecnológicas, o que pode dificultar a continuidade do projeto.

Outro risco importante é a volatilidade e diversidade dos dados. A grande quantidade e a diversidade dos dados utilizados podem gerar variações significativas, dificultando a análise precisa e a detecção de padrões consistentes de fraude. A volatilidade dos dados torna mais desafiador criar um modelo robusto capaz de lidar com a variabilidade e fornecer previsões precisas. Além disso, trabalhar com dados históricos de 10 anos apresenta desafios adicionais. Mudanças nos padrões de consumo, contextos econômicos e avanços tecnológicos ao longo do tempo podem dificultar a identificação de fraudes atuais, pois o modelo precisa considerar a evolução dos comportamentos e das condições externas que afetam o consumo de água.

A integração com o sistema da Azure para a produção de Machine Learning e a visualização das informações também pode ser um desafio. Integrar modelos de Machine Learning e dashboards de visualização com sistemas legados pode ser complicado devido à incompatibilidade de tecnologias, limitações de arquitetura e possíveis restrições de desempenho. Além disso, a falta de conhecimento sobre os códigos utilizados pelo parceiro pode levar a erros na modelagem e nas decisões tomadas com base nesses códigos, afetando a eficácia do projeto. Os riscos de segurança e privacidade dos dados são preocupações importantes, com o potencial de vazamento de dados sensíveis da empresa durante o desenvolvimento e implementação.

A confiabilidade dos dados externos é outro fator crítico. Dados externos, quando integrados à base interna, podem ser inconsistentes, incompletos ou de baixa qualidade, o que afeta a precisão do modelo de Machine Learning e pode resultar em resultados incorretos. Por fim, a dificuldade na implementação de redes neurais pode ser um obstáculo, pois o desenvolvimento e treinamento dessas redes podem exigir habilidades especializadas e recursos computacionais elevados, o que pode dificultar a implementação dentro do prazo e orçamento estabelecidos.

## Mitigação de riscos

1 - Selecionar variáveis exógenas com base em análises estatísticas preliminares e usar métodos de feature engineering para capturar a relação adequada.

2 - Monitorar constantemente os gastos e revisar as estimativas de custo conforme o projeto avança.

3 - Aplicar técnicas de pré-processamento, como normalização e seleção de features, para lidar com a volatilidade. Usar algoritmos robustos que se adaptem bem a diferentes tipos de dados e monitorar continuamente o desempenho do modelo.

4 - Priorizar a análise de dados mais recentes, aplicar técnicas de segmentação temporal para identificar mudanças significativas ao longo do tempo, e ajustar o modelo para refletir as condições atuais.

5 - Usar técnicas de validação cruzada, ajuste de hiperparâmetros e re-treinamento do modelo.

6 - Adotar uma abordagem de integração em camadas, usar APIs para comunicação entre sistemas, e garantir que a arquitetura de ML e visualização seja modular e escalável.

7 - Criar uma base de conhecimento interna que documente os códigos, suas origens, e usos, além de promover conversas com o time de engenharia de dados do parceiro, a fim de esclarecer maiores dúvidas.

8 - Implementar boas práticas de segurança, como adicionar o arquivo .env ao .gitignore, restringir acessos, criptografar informações sensíveis, e realizar auditorias de segurança regulares.

9 - Estabelecer processos rigorosos de validação dos dados externos antes de sua integração, aplicar técnicas de limpeza e imputação para corrigir inconsistências, e realizar testes de qualidade contínuos para garantir a confiabilidade dos dados ao longo do ciclo de vida do projeto.

10 - Avaliar a necessidade real de redes neurais versus outras abordagens de ML menos complexas, investir em treinamento especializado para a equipe, e garantir o acesso a recursos computacionais adequados.

11 - Antes do treinamento do modelo, será realizada uma análise rigorosa dos dados para garantir que variáveis relacionadas à etnia ou outros aspectos sensíveis não influenciem os resultados e haja monitoramento contínuo.

## Plano de Ação

# Plano de Ação

| Id  | Descrição do Impacto                                                                                           | Responsável               | Ação      | Descrição da Ação                                                                                                                                                                    | Previsão      |
|-----|----------------------------------------------------------------------------------------------------------------|----------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| 1   | A complexidade pode levar a um modelo ineficiente ou subutilizado.                                              | Giovanna                   | Mitigar   | Selecionar variáveis exógenas com base em análises estatísticas preliminares e usar métodos de feature engineering para capturar a relação adequada.                                   | N/A           |
| 2   | Custos não controlados podem inviabilizar o projeto, quebrando a expectativa de seu retorno.                    | Vinícius                   | Prevenir  | Monitorar constantemente os gastos e revisar as estimativas de custo conforme o projeto avança.                                                                                      | Todas as Sprints |
| 3   | Dados voláteis podem afetar a estabilidade do modelo, e impactar diretamente sua eficiência.                   | Todos integrantes          | Mitigar   | Aplicar técnicas de pré-processamento, como normalização e seleção de features, para lidar com a volatilidade.                                                                        | 12/08 à 16/08  |
| 4   | Há uma possibilidade de dados antigos não refletir as condições atuais e isso deve ser considerado.             | Giovanna                   | Mitigar   | Priorizar a análise de dados mais recentes, aplicar técnicas de segmentação temporal para identificar mudanças significativas ao longo do tempo, e ajustar o modelo para refletir as condições atuais. | Sprint 2 a 4   |
| 5   | Um modelo com desempenho ruim prejudicará as decisões de negócios, e vai guiar a empresa de forma equivocada.   | Dayllan                    | Prevenir  | Usar técnicas de validação cruzada, ajuste de hiperparâmetros e re-treinamento do modelo.                                                                                           | Todas as Sprints |
| 6   | Problemas de integração podem atrasar ou comprometer o desenvolvimento do modelo, sua eficácia e a visualização de dados. | Todos os integrantes | Prevenir  | Adotar uma abordagem de integração em camadas, usar APIs para comunicação entre sistemas, e garantir que a arquitetura de ML e visualização seja modular e escalável.                | Todas as Sprints |
| 7   | A falta de conhecimento sobre o código do parceiro pode resultar em atrasos e falhas na implementação de funções e outras tarefas na sprint. | Scrum Master da Sprint | Mitigar   | Criar uma base de conhecimento interna que documente os códigos, suas origens, e usos, e promover conversas com o time de engenharia do parceiro, a fim de esclarecer dúvidas.          | Todas as Sprints |
| 8   | Qualquer violação de segurança pode impactar o projeto como um todo e há danos à reputação, em ambas as partes. | PO da Sprint               | Prevenir  | Implementar boas práticas de segurança, como adicionar o arquivo .env ao .gitignore, restringir acessos, criptografar informações sensíveis, e realizar auditorias de segurança regulares. | Todas as Sprints |
| 9   | É importante mapear os dados externos a serem utilizados, pois dados não confiáveis podem distorcer os resultados do modelo e até enviesá-lo. | Malu                     | Prevenir  | Estabelecer processos rigorosos de validação dos dados externos antes de sua integração, aplicar técnicas de limpeza e imputação para corrigir inconsistências, e realizar testes de qualidade contínuos. | Sprint 2 a 4   |
| 10  | A dificuldade na implementação de redes neurais pode resultar em atrasados e o desenvolvimento de um modelo ineficaz. | Guto                   | Mitigar   | Avaliar a necessidade real de redes neurais versus outras abordagens de ML menos complexas, investir em treinamento especializado para a equipe, e garantir acesso a recursos computacionais adequados. | Todas as Sprints |
| 11  | Há uma preocupação direta com o uso do modelo desenvolvido, o principal risco é do mesmo direcionar ou embasar a empresa a decisões equivocadas. | Thainá                  | Mitigar   | Antes do treinamento do modelo, será realizada uma análise rigorosa dos dados para garantir que variáveis exógenas estejam de acordo, além de monitorar o impacto nas inferências do modelo. | Todas as Sprints |


# Oportunidades

1- Adoção de tecnologias emergentes de IA e Big Data

2- Participação em programas de iniciação científica

3- Concursos e competições acadêmicas

4- Interesse crescente em soluções de saneamento e meio ambiente


### Descrição e contextualização das oportunidades

Diante do cenário de combate às fraudes, existem oportunidades que podem auxiliar no desenvolvimento do projeto. Uma importante é a possibilidade de participação em programas de iniciação científica e tecnológica, onde o projeto pode ser beneficiado por editais de fomento à pesquisa acadêmica, como bolsas de iniciação científica, atraindo novos talentos e facilitando a continuidade do trabalho. Além disso, há a oportunidade de aproveitar tecnologias emergentes de Inteligência Artificial e Big Data, utilizando recursos computacionais de baixo custo e acesso gratuito a plataformas como Azure e Google Cloud, que oferecem créditos para treinamento e experimentação de modelos mais sofisticados, sem onerar financeiramente os estudantes. Outra oportunidade é a participação em hackathons e desafios de ciência de dados, que não só geram reconhecimento para o projeto, mas também proporcionam novas ideias e feedbacks de especialistas da área, impulsionando o desenvolvimento do modelo. 
