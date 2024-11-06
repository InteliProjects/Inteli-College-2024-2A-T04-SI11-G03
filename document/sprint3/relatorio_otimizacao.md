# Sumário

[1. Relatório de Otimização](#c1)

[2. Hiperparâmetros](#c2)

[3. Busca de Hiperparâmetros](#c3)

[4. Conclusão](#c4)

[5.Referências](#c5)

# <a name="c1"></a>Relatório de Otimização

&emsp;&emsp; A fraude no consumo de água é um desafio enfrentado pela Aegea, com impactos tanto no faturamento quanto na qualidade do serviço prestado. Essas fraudes ocorrem quando consumidores manipulam hidrômetros ou realizam ligações clandestinas, reduzindo ou eliminando os valores cobrados pelo consumo real. Além das perdas financeiras, essas práticas comprometem a eficiência da distribuição de água, causando danos à infraestrutura e aumentando o risco de contaminação.

&emsp;&emsp; Para enfrentar este desafio, a Aegea utiliza estratégias de fiscalização, porém, métodos mais eficazes são necessários para otimizar o processo. Neste contexto, este projeto visa desenvolver um modelo de Deep Learning capaz de identificar comportamentos fraudulentos com maior assertividade, utilizando variáveis exógenas como fatores macroeconômicos, climáticos e geográficos.

## Objetivo

&emsp;&emsp; O objetivo deste relatório é descrever o processo de otimização dos hiperparâmetros do modelo de Deep Learning desenvolvido para a detecção de fraudes no consumo de água. Este relatório abordará as estratégias de busca de hiperparâmetros adotadas, como grid search e random search, detalhará os hiperparâmetros testados, e analisará como essas variações influenciaram o desempenho do modelo, com base em métricas de desempenho F1-Score, AUC-ROC e precisão.

# <a name="c2"></a> Hiperparâmetros

&emsp;&emsp; Os **hiperparâmetros** são configurações definidas antes de treinar o modelo. Eles controlam o comportamento do modelo durante o treinamento, mas não são aprendidos a partir dos dados. No tópico abaixo explica-se os dois métodos utilizados no modelo em questão, Random Search e Otimização Bayesiana. 

## Métodos de Busca de Hiperparâmetros

### Random Search

&emsp;&emsp; O **Random Search** é um método simples para encontrar os melhores hiperparâmetros. Em vez de testar todas as combinações possíveis (como no Grid Search), ele seleciona aleatoriamente combinações de hiperparâmetros e avalia o desempenho do modelo para cada uma delas. Isso permite explorar uma variedade maior de combinações em menos tempo.

### Otimização Bayesiana

&emsp;&emsp; A **Otimização Bayesiana** é um método mais avançado que utiliza modelos probabilísticos para encontrar os melhores hiperparâmetros. Ela constrói um modelo que mapeia os hiperparâmetros para o desempenho do modelo e usa esse modelo para escolher os próximos hiperparâmetros a serem testados. Isso torna o processo mais eficiente, pois foca nas áreas do espaço de hiperparâmetros que têm maior probabilidade de melhorar o desempenho.

# <a name="c3"></a> Busca de Hiperparâmetros

&emsp;&emsp; Para garantir uma análise mais precisa e evitar vieses nos dados, desenvolveu-se dois modelos distintos: um para Pessoa Física (PF) e outro para Pessoa Jurídica (PJ). Essa separação foi feita porque, durante a análise dos dados, identificou-se que os padrões de consumo de água entre esses dois grupos são bastante diferentes, o que poderia enviesar o modelo caso fosse utilizado um único modelo para ambos. Dessa forma, a divisão permite analisar melhor esses comportamentos distintos, aprimorando a capacidade preditiva dos modelos. Abaixo, detalha-se o processo de construção para PJ e PF, com os hiperparâmetros ajustados e os respectivos resultados obtidos.

## Modelo Pessoa Física (PF)

&emsp;&emsp; Neste modelo para clientes PF, adotamos a técnica de **Random Search** para encontrar a melhor combinação de hiperparâmetros. A função de otimização de hiperparâmetros foi definida utilizando a biblioteca **Keras Tuner**, que permitiu testar múltiplas configurações.

Os principais hiperparâmetros explorados foram:

- Número de camadas densas no modelo, variando entre 2 e 4 camadas.
- Número de unidades em cada camada, variando de 64 a 512.
- Taxa de dropout, variando entre 0.2 e 0.5, para prevenir overfitting.
- Taxa de aprendizado do otimizador Adam, variando entre 1e-4 e 1e-2 em uma escala logarítmica.

### Resultados dos hiperparâmetros testados

&emsp;&emsp; Abaixo estão as arquiteturas dos três melhores modelos testados durante o processo de tuning, com a quantidade de parâmetros treináveis e o desempenho em termos de acurácia e precisão:

#### **Modelo 1 (Arquitetura Complexa)**
- **Camadas**: 4
- **Unidades por camada**: 448, 448, 320
- **Dropout**: 0.3, 0.4, 0.5
- **Parâmetros treináveis**: 375,617
- **Taxa de aprendizado**: 1e-3

#### **Modelo 2 (Arquitetura Moderada)**
- **Camadas**: 3
- **Unidades por camada**: 384, 64
- **Dropout**: 0.3, 0.4
- **Parâmetros treináveis**: 50,817
- **Taxa de aprendizado**: 5e-4

#### **Modelo 3 (Arquitetura Simplificada)**
- **Camadas**: 4
- **Unidades por camada**: 256, 512, 192
- **Dropout**: 0.3, 0.4, 0.4
- **Parâmetros treináveis**: 247,681
- **Taxa de aprendizado**: 2e-4

### Análise de impacto dos hiperparâmetros

- **Número de Unidades**: Modelos com um número maior de unidades nas camadas iniciais apresentaram melhor desempenho, uma vez que capturam mais nuances dos dados, particularmente o **Modelo 1**, que apresentou maior acurácia e precisão. No entanto, há um ponto de diminuição dos retornos, como observado no **Modelo 2**, onde uma camada intermediária com poucas unidades levou a uma queda de desempenho.
  
- **Dropout**: A aplicação de dropout foi utilizada para evitar overfitting, especialmente no **Modelo 1**. Modelos com dropout em torno de 0.4 e 0.5 demonstraram maior estabilidade durante o treinamento, com melhores resultados em dados de validação.

- **Taxa de Aprendizado**: Modelos com taxas de aprendizado mais baixas, como o **Modelo 3**, convergiram mais lentamente, mas apresentaram resultados mais consistentes, especialmente em termos de precisão. Modelos com taxas mais altas, como o **Modelo 2**, tiveram uma convergência mais rápida, mas também apresentaram uma oscilação maior nas métricas de validação.

### Hiperparâmetros final escolhido (PF)

&emsp;&emsp; Com base nos resultados das iterações de hiperparâmetros, optamos por utilizar a arquitetura do **Modelo 1** como a configuração final para o modelo de detecção de fraudes em PF. A decisão foi baseada no fato de que o **Modelo 1** apresentou a melhor combinação de acurácia (0.945) e precisão (0.870), o que permite um bom balanceamento entre desempenho e complexidade.

Os hiperparâmetros finais escolhidos são:

- **Número de camadas densas**: 4
- **Unidades por camada**: 448, 448, 320
- **Dropout**: 0.3, 0.4, 0.5
- **Taxa de aprendizado**: 1e-3
- **Otimizador**: Adam

&emsp;&emsp; Esses hiperparâmetros foram os escolhidos porque permitiram o modelo capturar melhor as complexidades dos padrões de consumo de água em PF, enquanto minimizavam o risco de overfitting e asseguravam uma boa capacidade de generalização para novos dados.

## Modelo Pessoa Jurídica (PJ)

&emsp;&emsp; Para o modelo voltado a Pessoa Jurídica (PJ), utilizamos a **otimização Bayesiana** como método de busca dos hiperparâmetros. Esse método foi escolhido por ser mais eficiente em relação a abordagens como grid search ou random search, pois ele explora de maneira mais inteligente o espaço dos hiperparâmetros, fazendo escolhas baseadas em resultados anteriores, otimizando a performance do modelo.

Neste caso, foram ajustados quatro principais hiperparâmetros:
- **Taxa de aprendizado** (`learning_rate`): variando dentro de um intervalo contínuo para encontrar o valor ideal.
- **Número de neurônios** em cada camada: ajustado para identificar a quantidade mais adequada para o desempenho da rede.
- **Tamanho do lote** (`batch_size`): utilizado para controlar a quantidade de dados processados antes de atualizar os pesos do modelo.
- **Taxa de dropout**: ajustada para evitar overfitting, balanceando a capacidade de generalização do modelo.

A otimização foi feita com a função de perda (`val_loss`) como critério, e os melhores parâmetros encontrados foram:
- **Taxa de aprendizado**: 0.0039
- **Número de neurônios**: 60
- **Batch size**: 64
- **Taxa de dropout**: 0.34

&emsp;&emsp; Dessa forma, a abordagem bayesiana garantiu uma busca mais eficiente, ajustando os hiperparâmetros com base em um balanceamento entre exploração e exploração do espaço de busca.

# <a name="c4"></a> Conclusão

&emsp;&emsp; O processo de otimização de hiperparâmetros foi utilizado para garantir que os modelos sejam capazes de identificar comportamentos fraudulentos de maneira mais precisa. Essas estratégias demonstram como a personalização dos modelos para diferentes tipos de consumidores possibilita uma detecção mais assertiva e eficiente de fraudes.

# <a name="c5"></a> Referências

(1) Optimización de hiperparámetros en modelos de Deep Learning. https://www.mundoposgrado.com/optimizacion-de-hiperparametros-modelos-deep-learning/.

(2) Machine Learning Hyperparameter: Hiperparâmetros em Aprendizado de Máquina. https://awari.com.br/machine-learning-hyperparameter-hiperparametros-em-aprendizado-de-maquina/.

(3) Hiperparâmetros em Machine Learning: Otimização e Ajuste - Awari. https://awari.com.br/hiperparametros-em-machine-learning-otimizacao-e-ajuste/.

(4) How to Grid Search Hyperparameters for Deep Learning Models in Python .... https://machinelearningmastery.com/grid-search-hyperparameters-deep-learning-models-python-keras/.
