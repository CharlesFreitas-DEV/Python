# Modelo Conceitual do Domínio

## Projeto

**LAB EDU SORT V1.0**

---

# Objetivo

Este documento descreve o modelo conceitual do domínio do projeto **LAB EDU SORT V1.0**, apresentando os principais elementos que compõem o sistema, seus relacionamentos e responsabilidades.

Este documento possui caráter exclusivamente arquitetural.

Nenhuma decisão de implementação é definida aqui.

---

# Visão Geral

O LAB EDU SORT é uma biblioteca educacional desenvolvida para o estudo, comparação e análise de algoritmos de ordenação.

O sistema permite:

- gerar conjuntos de dados;
- importar conjuntos de dados;
- executar diferentes algoritmos de ordenação;
- coletar métricas durante a execução;
- comparar algoritmos;
- produzir relatórios;
- gerar visualizações dos resultados.

O objetivo principal é oferecer uma plataforma didática que permita compreender o funcionamento interno dos algoritmos de ordenação de maneira organizada, extensível e reutilizável.

---

# Entidades do Domínio

O domínio do sistema é composto pelas seguintes entidades conceituais.

## Usuário

Representa quem utiliza o sistema.

Responsabilidades:

- fornecer dados de entrada;
- escolher algoritmos;
- definir parâmetros de execução;
- solicitar visualizações;
- analisar resultados.

---

## Entrada de Dados

Representa a origem dos dados que serão ordenados.

A entrada poderá ser proveniente de:

- arquivo;
- geração automática;
- entrada manual;
- listas parcialmente ordenadas;
- listas totalmente ordenadas;
- listas invertidas;
- listas aleatórias.

A entrada sempre produzirá uma coleção de valores válida para processamento.

---

## Conjunto de Dados

Representa a coleção de elementos que será utilizada pelo algoritmo de ordenação.

O conjunto de dados constitui o principal objeto manipulado pelo sistema.

Características:

- quantidade de elementos;
- tipo dos elementos;
- ordem inicial;
- distribuição dos valores.

---

## Algoritmo de Ordenação

Representa um algoritmo responsável por reorganizar os elementos de um conjunto de dados.

Exemplos:

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort
- Shell Sort
- Counting Sort
- Radix Sort

Cada algoritmo possui características próprias de:

- complexidade;
- estabilidade;
- consumo de memória;
- comportamento.

---

## Execução

Representa uma execução individual de um algoritmo sobre um conjunto de dados.

Cada execução possui:

- algoritmo utilizado;
- conjunto de dados;
- parâmetros;
- estatísticas coletadas;
- tempo de execução;
- resultado produzido.

---

## Estatísticas

Representa todas as métricas produzidas durante uma execução.

Exemplos:

- número de comparações;
- número de trocas;
- tempo total;
- tempo de CPU;
- memória utilizada;
- profundidade de recursão;
- estabilidade;
- complexidade observada.

As estatísticas serão utilizadas para fins de comparação e análise.

---

## Resultado

Representa a saída produzida por uma execução.

O resultado é composto por:

- lista ordenada;
- estatísticas;
- informações da execução;
- possíveis relatórios.

---

## Visualização

Representa os mecanismos utilizados para apresentar os resultados ao usuário.

Exemplos:

- terminal;
- tabelas;
- gráficos;
- arquivos;
- relatórios.

---

# Relacionamento entre as Entidades

O fluxo conceitual do domínio pode ser representado da seguinte forma:

```text
Usuário
    │
    ▼
Entrada de Dados
    │
    ▼
Conjunto de Dados
    │
    ▼
Algoritmo de Ordenação
    │
    ▼
Execução
    │
    ├──────────────► Estatísticas
    │
    ▼
Resultado
    │
    ▼
Visualização
```

---

# Fluxo Conceitual

O funcionamento do sistema ocorre conforme o seguinte fluxo:

1. O usuário fornece uma entrada.

2. A entrada é validada.

3. Um conjunto de dados é construído.

4. O algoritmo selecionado é preparado.

5. A execução é iniciada.

6. Durante a execução são coletadas estatísticas.

7. O algoritmo produz uma lista ordenada.

8. O sistema consolida os resultados.

9. Os resultados são apresentados ao usuário.

---

# Limites do Domínio

O modelo conceitual NÃO define:

- implementação dos algoritmos;
- estruturas internas das classes;
- interfaces de programação;
- detalhes de persistência;
- detalhes de visualização;
- organização dos pacotes;
- implementação das estatísticas.

Esses assuntos serão tratados em documentos específicos da arquitetura.

---

# Princípios Arquiteturais

O modelo conceitual foi construído considerando os seguintes princípios:

- Separação clara de responsabilidades.
- Baixo acoplamento entre componentes.
- Alta coesão.
- Extensibilidade.
- Reutilização.
- Modularização.
- Simplicidade.
- Evolução incremental.
- Independência entre domínio e implementação.

---

# Objetos Centrais do Domínio

Os principais objetos manipulados pelo sistema são:

| Entidade | Papel |
|----------|-------|
| Usuário | Inicia a execução |
| Entrada de Dados | Origem das informações |
| Conjunto de Dados | Dados a serem ordenados |
| Algoritmo de Ordenação | Processamento principal |
| Execução | Coordena o processamento |
| Estatísticas | Coleta informações da execução |
| Resultado | Consolida a saída |
| Visualização | Apresenta os resultados |

---

# Modelo Conceitual Resumido

```text
                 +----------------+
                 |    Usuário     |
                 +----------------+
                         |
                         ▼
               +-------------------+
               | Entrada de Dados  |
               +-------------------+
                         |
                         ▼
             +------------------------+
             | Conjunto de Dados      |
             +------------------------+
                         |
                         ▼
           +----------------------------+
           | Algoritmo de Ordenação     |
           +----------------------------+
                         |
                         ▼
                 +---------------+
                 |   Execução    |
                 +---------------+
                  |            |
                  |            ▼
                  |     +--------------+
                  |     | Estatísticas |
                  |     +--------------+
                  |
                  ▼
            +----------------+
            |   Resultado    |
            +----------------+
                    |
                    ▼
            +----------------+
            | Visualização   |
            +----------------+
```

---

# Considerações Finais

Este documento estabelece a visão conceitual do domínio do **LAB EDU SORT V1.0**.

Todas as decisões de modelagem apresentadas aqui servirão como referência para os próximos documentos de arquitetura, especialmente para o modelo de classes, definição das responsabilidades dos módulos e contratos entre componentes.

Este documento não possui dependência de implementação e deverá permanecer estável durante toda a evolução da versão 1.0 do projeto.

---
