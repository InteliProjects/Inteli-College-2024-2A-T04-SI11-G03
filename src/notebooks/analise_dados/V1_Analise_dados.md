# Análise de Dados de Consumo de Água

Este projeto contém quatro arquivos de análise de dados focados no consumo de água, segmentados por períodos de tempo para otimizar o uso da memória RAM.

## Estrutura do Projeto

### 1. Arquivos de Análise Completos

Os arquivos de análise de dados foram separados em três arquivos distintos devido à impossibilidade de processar todos os anos (2019-2024) em um único arquivo `ipynb`, já que a RAM atingia seu limite e o processo falhava. Para evitar esse problema, fizemos a divisão da seguinte maneira:

- **Análise de Dados 2019-2020**
- **Análise de Dados 2021-2022**
- **Análise de Dados 2023-2024**

Esses arquivos contêm todas as colunas do dataset original, com a análise completa para cada período de dois anos.

### 2. Arquivo de Análise Compacto

Também incluímos um arquivo separado com os dados de todos os anos (2019-2024) que contém apenas as 8 colunas mais relevantes para a análise inicial. Como o tamanho reduzido permite um processamento mais eficiente, esse arquivo pôde ser executado integralmente sem problemas de memória.

## Links para os Colabs

Caso queira verificar as análises completas, os links para os notebooks no Google Colab estão listados abaixo:

- [Análise de Dados 2019-2020](https://colab.research.google.com/drive/1lyDhc3aocLXlEmIVP8xLRUAd55e3V7vP?usp=drive_link)
- [Análise de Dados 2021-2022](https://colab.research.google.com/drive/1vRDvxRZ_RAjGH8HnKGJQduPPjIPh9RgO?usp=drive_link)
- [Análise de Dados 2023-2024](https://colab.research.google.com/drive/1dRy6NMEGryyk7WNkgHXIh9A8st3nCing?usp=drive_link)
- [Análise Compacta (2019-2024)](#)

## Observações

A separação por anos foi feita para contornar as limitações de RAM. As análises completas fornecem uma visão detalhada e abrangente dos dados, enquanto o arquivo compacto concentra-se em uma análise preliminar com um conjunto reduzido de variáveis.

Apesar da redução no número de variáveis, o arquivo compacto ainda oferece uma cobertura significativa, proporcionando uma análise eficiente e relevante para os objetivos do projeto. Ele permite extrair insights valiosos sem comprometer a profundidade da investigação, sendo uma peça essencial para o desenvolvimento contínuo do projeto.