# Análise de Custo - Prevenção de Fraudes no Consumo de Água

## 1. Introdução
Este documento detalha os custos envolvidos no desenvolvimento e execução do projeto de prevenção de fraudes no consumo de água. O projeto visa identificar e prevenir fraudes no consumo de água, gerando uma economia financeira significativa para a empresa. Utilizamos um modelo preditivo para detectar fraudes antes que ocorram, otimizando o tempo de trabalho e os recursos operacionais.

## 2. Recursos Humanos
Os recursos humanos representam uma parcela expressiva dos custos do projeto. Com uma equipe composta por 6 desenvolvedores juniores, estimamos o custo total de recursos humanos com base nas seguintes premissas:

- **Salário mensal de desenvolvedor júnior**: R$ 5.000,00
- **Carga horária de trabalho**: 22 dias úteis, 5 horas por dia

### 2.1 Cálculo do custo por hora
- **Salário por hora** = R$ 5.000,00 / (22 * 5) = **R$ 45,45** por hora

### 2.2 Cálculo total de recursos humanos
- **Custo total** = R$ 45,45 * 6 desenvolvedores * 5 horas por dia * 22 dias úteis
- **Total de recursos humanos** = **R$ 29.997,00**

## 3. Infraestrutura
A infraestrutura do projeto envolveu o uso de um **job scheduler** para agendamento de tarefas automáticas e o uso do **Colab Pro** para rodar os modelos com GPU.

### 3.1 Job Scheduler
- **Custo por execução**: US$ 0,003
- **Taxa de câmbio**: US$ 1,00 = R$ 5,51
- **Custo total**: R$ 0,01653 por execução
- **Número de execuções**: 44 (22 dias úteis por mês, 2 meses)
- **Custo total** = **R$ 0,73**

### 3.2 Colab Pro
O Colab Pro foi utilizado por 2 meses (4 sprints), com um custo mensal de R$ 58,00.

- **Custo total Colab Pro** = R$ 58,00 * 2 = **R$ 116,00**

### 3.3 Custo total de infraestrutura
- **Custo total da infraestrutura** = R$ 0,73 (job scheduler) + R$ 116,00 (Colab Pro) = **R$ 116,73**

## 4. Stakeholders
Os stakeholders do projeto desempenharam um papel fundamental no acompanhamento e na tomada de decisões. Seus custos de deslocamento e tempo dedicado ao projeto foram calculados.

### 4.1 Tempo de acompanhamento
Cada stakeholder dedicou 3 horas por visita (1 hora de deslocamento e 2 horas no Inteli). Com um salário mensal de R$ 19.000,00 para um diretor de TI, o custo por hora foi calculado:

- **Custo por hora** = R$ 19.000,00 / (4 semanas * 40 horas) = **R$ 118,75** por hora
- **Custo por visita** = R$ 118,75 * 3 horas = **R$ 356,25**
- **Custo total por pessoa (5 visitas)** = R$ 356,25 * 5 = **R$ 1.781,25**

### 4.2 Cálculo do custo de combustível
**Deslocamento local (São Paulo)**  
Os stakeholders percorreram 17 km (ida e volta) entre a Aegea Saneamento e o Inteli. O consumo de combustível foi calculado para etanol e gasolina.

- **Etanol**:
    - Custo por ida e volta: 1,7 litros * R$ 3,42 = **R$ 5,81**
    - Custo total para 5 visitas: R$ 5,81 * 5 = **R$ 29,05**

- **Gasolina**:
    - Custo por ida e volta: 1,42 litros * R$ 5,76 = **R$ 8,18**
    - Custo total para 5 visitas: R$ 8,18 * 5 = **R$ 40,90**

### 4.3 Cálculo total dos custos dos stakeholders
**Cenário 1: Todos os stakeholders utilizam gasolina**
- **Custo por stakeholder** = **R$ 1.822,15**
- **Custo total para 3 stakeholders** = **R$ 5.466,45**

**Cenário 2: Todos os stakeholders utilizam etanol**
- **Custo por stakeholder** = **R$ 1.810,30**
- **Custo total para 3 stakeholders** = **R$ 5.430,90**

## 5. Resumo dos custos totais

1. **Recursos Humanos**: **R$ 29.997,00**
2. **Infraestrutura**: **R$ 116,73**
3. **Stakeholders (máximo)**: **R$ 5.466,45**

### **Total do Projeto**: **R$ 35.580,18**

## 6. Deploy na Azure (Extra)

Para hospedar o sistema na plataforma **Azure**, os custos são calculados com base nos seguintes componentes:

- **Máquina virtual básica (Standard_B1s)**:  
  - Custo: **US\$ 0,008** por hora
  - **Custo mensal estimado**: 730 horas * US\$ 0,008 ≈ **US\$ 5,84**
  - **Custo em reais**: US\$ 5,84 * R\$ 5,51 ≈ **R\$ 32,15**

- **Banco de dados SQL Azure (Basic Tier)**:  
  - **Custo mensal**: **US\$ 5,00**  
  - **Custo em reais**: US\$ 5,00 * R\$ 5,51 ≈ **R\$ 27,55**

- **Custo total do deploy na Azure**: R\$ 32,15 + R\$ 27,55 = **R\$ 59,70**


## 7. Como o projeto se paga

O projeto visa a prevenção de fraudes no consumo de água. Com a previsão de **5% das fraudes detectadas**, a economia gerada pode ser significativa.

| **Métrica**                    | **Valor**                |
|---------------------------------|--------------------------|
| Número de fraudes prevenidas    | 11.300 fraudes           |
| Tarifa por m³ de água e esgoto  | R\$ 9,27                 |
| Perda por fraude (10 m³)        | R\$ 92,70                |
| **Economia total**              | R\$ 1.047.510,00         |
| **Custo total do projeto**      | R\$ 35.580,18            |
| **Lucro líquido**               | R\$ 1.011.929,82         |

## 8. ROI
Para calcular o ROI (Return on Investment), utilizamos a seguinte fórmula:

<b>ROI = (Lucro Líquido / Custo Total do Projeto) x 100</b>


Dados:
- Lucro Líquido: R$ 1.011.929,82
- Custo Total do Projeto: R$ 35.580,18
Substituindo esses valores na fórmula:

<b>ROI = (1.011.929,82 / 35.580,18) x 100</b>

## ROI do Projeto: 2843,76%

## 9. Conclusão
O custo total estimado para o projeto de prevenção de fraudes no consumo de água é de **R$35.580,18**, com uma economia potencial de **R$1.047.510,00** ao prever 5% das fraudes antes que elas ocorram. Isso gera um lucro líquido de **R$1.011.929,82**, o que demonstra o forte impacto financeiro positivo do projeto. Além disso, o custo adicional para o deploy na Azure seria de **R$59,70** por mês, um valor bastante acessível para garantir a infraestrutura necessária à operação contínua do sistema.

- Benefícios do Projeto
  - **Redução de perdas financeiras**: O principal benefício do projeto é a mitigação das fraudes no consumo de água, que representam uma perda significativa para as empresas de saneamento. A capacidade de prever e evitar 5% dessas fraudes resulta em uma economia direta de mais de R$ 1 milhão no curto prazo, trazendo estabilidade financeira e aumentando a eficiência operacional.

  - **Retorno sobre o investimento (ROI)**: O projeto apresenta um ROI impressionante de **2843,76%**, o que significa que para cada <i><b>R$1,00 investido, a empresa gera aproximadamente R$28,44 em retorno</i></b>. Isso torna o projeto extremamente rentável, demonstrando que a aplicação de tecnologias de inteligência artificial e automação na detecção de fraudes pode ser altamente lucrativa.

  - **Eficiência operacional**: A implementação do sistema preditivo reduz a necessidade de investigações manuais e processos reativos à fraude, liberando recursos humanos para atividades mais estratégicas. Isso permite que a equipe técnica se concentre em melhorias contínuas e inovação, em vez de gastar tempo em tarefas operacionais.

  - **Escalabilidade e flexibilidade**: O projeto pode ser facilmente escalado para prever um percentual maior de fraudes ou ser adaptado para outras áreas operacionais, como controle de perdas, monitoramento de consumo e previsão de demanda. O uso da plataforma Azure para deploy também proporciona uma infraestrutura flexível, permitindo o aumento de capacidade conforme a necessidade da empresa sem um custo fixo elevado.

  - **Sustentabilidade e responsabilidade social**: Ao reduzir as fraudes no consumo de água, a empresa não só melhora sua posição financeira, mas também contribui para a sustentabilidade ambiental. O uso mais eficiente da água, um recurso finito e essencial, gera um impacto positivo na sociedade, reforçando a responsabilidade social da empresa e sua imagem pública.

  - **Vantagens financeiras a longo prazo**: Além da economia inicial com a prevenção de fraudes, o projeto traz benefícios financeiros contínuos ao longo dos anos. Com o sistema de prevenção em operação, a empresa reduz os custos associados à recuperação de perdas e ao tratamento de dados fraudulentos. A solução também melhora a previsão de demanda, otimizando o uso de recursos e evitando desperdícios.
  
  Em suma, o projeto é uma ferramenta essencial para aumentar a rentabilidade, a eficiência e a sustentabilidade da operação.

## 10. Referências
- GLASSDOOR. *Isola Group - Salário Mensal de Diretor de TI no Brasil*. Disponível em: [Glassdoor](https://www.glassdoor.com.br/Pagamento-mensal/Isola-Group-Diretor-TI-Brasil-Pagamento-mensal-EJI_IE28063.0,11_KO12,22_IL.23,29.htm). Acesso em: 07 out. 2024.

- GLASSDOOR. *Salário de Desenvolvedor Júnior no Brasil*. Disponível em: [Glassdoor](https://www.glassdoor.com.br/Sal%C3%A1rios/desenvolvedor-junior-sal%C3%A1rio-SRCH_KO0,20.htm). Acesso em: 07 out. 2024.
