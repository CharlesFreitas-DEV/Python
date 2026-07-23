# Índice

# Parte I — Fundamentos do Modelo de Estatísticas

1. [Objetivo](#objetivo)

2. [Escopo](#escopo)

3. [Papel das Estatísticas na Arquitetura](#papel-das-estatísticas-na-arquitetura)

4. [Princípios Adotados](#princípios-adotados)

   4.1. [Precisão das Informações](#precisão-das-informações)

   4.2. [Baixo Acoplamento](#baixo-acoplamento)

   4.3. [Separação entre Execução e Análise](#separação-entre-execução-e-análise)

   4.4. [Valor Educacional](#valor-educacional)

---

# Parte II — Conceitos Estatísticos do Projeto

1. [Tipos de Estatísticas](#tipos-de-estatísticas)

2. [Métricas de Comparação](#métricas-de-comparação)

3. [Métricas de Movimentação](#métricas-de-movimentação)

4. [Métricas Temporais](#métricas-temporais)

5. [Métricas de Memória](#métricas-de-memória)

6. [Métricas de Complexidade](#métricas-de-complexidade)

---

# Parte III — Modelo Conceitual das Estatísticas

1. [Entidade EstatisticasOrdenacao](#entidade-estatisticasordenacao)

2. [Entidade ResultadoOrdenacao](#entidade-resultadoordenacao)

3. [Entidade EventoOrdenacao](#entidade-eventoordenação)

4. [Relacionamento entre Entidades](#relacionamento-entre-entidades)

5. [Ciclo de Vida das Estatísticas](#ciclo-de-vida-das-estatísticas)

---

# Parte IV — Classes do Modelo de Estatísticas

1. [Classe EstatisticasOrdenacao](#classe-estatisticasordenacao)

2. [Classe ContadorOperacoes](#classe-contadoroperacoes)

3. [Classe MedicaoTempo](#classe-medicaotempo)

4. [Classe ResultadoOrdenacao](#classe-resultadoordenacao)

5. [Classe EventoOrdenacao](#classe-eventoordenação)

6. [Relacionamento entre Classes](#relacionamento-entre-classes)

---

# Parte V — Estruturas de Dados das Estatísticas

1. [Uso de dataclass](#uso-de-dataclass)

2. [Uso de list para histórico de eventos](#uso-de-list-para-histórico-de-eventos)

3. [Uso de dict para agregação de métricas](#uso-de-dict-para-agregação-de-métricas)

4. [Estruturas imutáveis](#estruturas-imutáveis)

5. [Decisões arquiteturais](#decisões-arquiteturais)

---

# Parte VI — Comunicação entre Algoritmos e Estatísticas

1. [Responsabilidade do módulo estatisticas](#responsabilidade-do-módulo-estatisticas)

2. [Contrato de coleta](#contrato-de-coleta)

3. [Eventos produzidos pelos algoritmos](#eventos-produzidos-pelos-algoritmos)

4. [Fluxo Request, Response e Event](#fluxo-request-response-e-event)

5. [Matriz de comunicação](#matriz-de-comunicação)

---

# Parte VII — Modelo de Métricas por Algoritmo

1. [Bubble Sort](#bubble-sort)

2. [Selection Sort](#selection-sort)

3. [Insertion Sort](#insertion-sort)

4. [Merge Sort](#merge-sort)

5. [Quick Sort](#quick-sort)

6. [Heap Sort](#heap-sort)

7. [Comparativo geral dos algoritmos](#comparativo-geral-dos-algoritmos)

---

# Parte VIII — Relatórios e Visualizações

1. [Modelo de relatório estatístico](#modelo-de-relatório-estatístico)

2. [Formato de saída das estatísticas](#formato-de-saída-das-estatísticas)

3. [Dados consumidos pelo módulo visualizacoes](#dados-consumidos-pelo-módulo-visualizacoes)

4. [Evolução futura dos relatórios](#evolução-futura-dos-relatórios)

---

# Parte IX — Diagramas e Arquitetura

1. [Fluxo de coleta de estatísticas](#fluxo-de-coleta-de-estatísticas)

2. [Diagrama de relacionamento](#diagrama-de-relacionamento)

3. [Diagrama de sequência](#diagrama-de-sequência)

4. [Dependências entre módulos](#dependências-entre-módulos)

---

# Parte X — Evolução e Considerações Finais

1. [Regras de evolução](#regras-de-evolução)

2. [Estatísticas planejadas para versões futuras](#estatísticas-planejadas-para-versões-futuras)

3. [Boas práticas](#boas-práticas)

4. [Considerações finais](#considerações-finais)

---

# Catálogo Rápido

## Métricas principais

- [Comparações](#métricas-de-comparação)
- [Trocas](#métricas-de-movimentação)
- [Movimentações](#métricas-de-movimentação)
- [Tempo de execução](#métricas-temporais)
- [Memória utilizada](#métricas-de-memória)
- [Complexidade](#métricas-de-complexidade)

---

## Classes principais

- [EstatisticasOrdenacao](#classe-estatisticasordenacao)
- [ResultadoOrdenacao](#classe-resultadoordenacao)
- [EventoOrdenacao](#classe-eventoordenação)

---

# Parte I — Fundamentos do Modelo de Estatísticas

Esta seção apresenta os fundamentos que orientam o modelo de estatísticas do **LAB EDU SORT V1.0**.

O objetivo é definir a finalidade, o escopo e os princípios arquiteturais que irão nortear a coleta, armazenamento e utilização das informações geradas durante a execução dos algoritmos de ordenação.

As estatísticas não são tratadas como simples contadores auxiliares.

Elas representam uma camada de observabilidade da aplicação, permitindo analisar:

- comportamento dos algoritmos;
- eficiência computacional;
- quantidade de operações realizadas;
- diferenças entre estratégias de ordenação;
- impacto das estruturas utilizadas.

---

# Objetivo

O modelo de estatísticas tem como objetivo fornecer uma representação estruturada das informações produzidas durante a execução dos algoritmos de ordenação.

Ele deverá permitir:

- registrar operações realizadas;
- medir desempenho;
- comparar algoritmos;
- gerar relatórios;
- alimentar visualizações;
- apoiar atividades educacionais.

---

# Escopo

O módulo `estatisticas` será responsável por coletar e organizar informações relacionadas ao processo de ordenação.

Seu escopo inclui:

```text
Coleta

   │

   ▼

Processamento

   │

   ▼

Armazenamento

   │

   ▼

Disponibilização
```

---

# Responsabilidades do Modelo de Estatísticas

O modelo deverá representar:

## Operações realizadas

Exemplos:

- comparações;
- trocas;
- movimentações;
- acessos aos elementos.

---

## Tempo de execução

Exemplos:

- início da execução;
- término da execução;
- duração total.

---

## Características da entrada

Exemplos:

- quantidade de elementos;
- tipo de distribuição;
- grau de ordenação inicial.

---

## Resultado da execução

Exemplos:

- algoritmo utilizado;
- dados ordenados;
- métricas coletadas.

---

# Fora do Escopo

O módulo de estatísticas não será responsável por:

- executar algoritmos;
- modificar dados de entrada;
- realizar validações de domínio;
- criar gráficos;
- controlar interface do usuário.

Essas responsabilidades pertencem a outros módulos.

---

# Papel das Estatísticas na Arquitetura

As estatísticas funcionam como uma camada de observação entre o processamento e a apresentação.

A arquitetura pode ser representada:

```text
                 Entrada

                    │

                    ▼

              Algoritmo

                    │

        ┌───────────┴───────────┐

        │                       │

        ▼                       ▼

   Resultado              Eventos

                                │

                                ▼

                         Estatísticas

                                │

                                ▼

                         Visualizações
```

---

# Relação com os Outros Módulos

O módulo `estatisticas` possui comunicação principalmente com:

---

# algoritmosOrdenacao

## Responsabilidade da comunicação

Receber informações sobre operações realizadas.

Exemplos:

```text
comparação realizada

troca realizada

elemento movimentado
```

---

# Comunicação

Tipo:

```text
Event
```

Fluxo:

```text
Algoritmo

    │

    │ EventoOrdenacao

    ▼

Estatisticas
```

---

# entradaDados

## Responsabilidade da comunicação

Receber informações sobre a entrada utilizada.

Exemplos:

```text
quantidade de elementos

origem dos dados

configuração inicial
```

---

# Comunicação

Tipo:

```text
Request / Response
```

Fluxo:

```text
Estatisticas

      Request

          │

          ▼

EntradaDados

          │

       Response

          │

          ▼

Estatisticas
```

---

# visualizacoes

## Responsabilidade da comunicação

Disponibilizar informações consolidadas.

---

# Comunicação

Tipo:

```text
Response
```

Fluxo:

```text
Estatisticas

       │

       │ ResultadoEstatistico

       ▼

Visualizacoes
```

---

# Princípios Adotados

O modelo de estatísticas segue princípios definidos para toda a arquitetura do LAB EDU SORT.

---

# Precisão das Informações

As métricas devem representar fielmente o comportamento do algoritmo.

Exemplo:

Uma comparação deve ser registrada apenas quando realmente ocorrer:

```text
comparar elemento A

com elemento B
```

não sendo permitido:

```text
incrementar contador artificialmente
```

---

# Objetivo

Garantir que os resultados possam ser utilizados para:

- análise;
- comparação;
- ensino;
- experimentação.

---

# Baixo Acoplamento

O módulo de estatísticas não deve depender diretamente da implementação interna dos algoritmos.

Exemplo incorreto:

```text
estatisticas conhece BubbleSort
estatisticas conhece QuickSort
estatisticas conhece MergeSort
```

---

# Exemplo correto:

```text
Algoritmo

      │

      ▼

EventoOrdenacao

      │

      ▼

Estatisticas
```

---

# Benefício

Permite adicionar novos algoritmos sem modificar o módulo estatístico.

---

# Separação entre Execução e Análise

A execução do algoritmo e a análise do comportamento devem permanecer separadas.

---

# Exemplo

O algoritmo:

```text
QuickSort
```

deve se preocupar com:

```text
ordenar elementos
```

Enquanto o módulo:

```text
estatisticas
```

deve se preocupar com:

```text
medir operações
```

---

# Benefício

Essa separação permite:

- testes independentes;
- melhor manutenção;
- evolução modular.

---

# Valor Educacional

As estatísticas possuem papel fundamental no propósito do projeto.

O LAB EDU SORT não pretende apenas produzir listas ordenadas.

Ele pretende demonstrar:

```text
Como o algoritmo funciona?

Quantas operações realizou?

Qual algoritmo foi mais eficiente?

Qual o impacto da entrada?
```

---

# Exemplo Educacional

Comparação:

Entrada:

```text
[5,4,3,2,1]
```

Resultados:

```text
Bubble Sort

Comparações: 10

Trocas: 10


Insertion Sort

Comparações: 10

Movimentações: 10
```

---

# Benefício

O estudante consegue relacionar:

- implementação;
- comportamento;
- complexidade.

---

# Modelo Conceitual Inicial

A visão inicial do domínio estatístico é:

```text
                 ExecucaoOrdenacao

                         │

                         │ possui

                         ▼

              EstatisticasOrdenacao

                         │

                         │ contém

          ┌──────────────┼──────────────┐

          ▼              ▼              ▼

     Comparacoes      Trocas       TempoExecucao

          │              │              │

          └──────────────┼──────────────┘

                         │

                         ▼

                 ResultadoOrdenacao
```

---

# Considerações da Parte

O modelo de estatísticas do **LAB EDU SORT V1.0** será construído como uma camada independente de observação da execução dos algoritmos.

A arquitetura definida nesta parte estabelece que:

```text
Algoritmos executam

        ↓

Eventos são produzidos

        ↓

Estatísticas são consolidadas

        ↓

Resultados são apresentados
```

Essa separação permite que o projeto mantenha:

- clareza arquitetural;
- baixo acoplamento;
- facilidade de evolução;
- valor pedagógico.

A próxima seção apresentará os **Conceitos Estatísticos do Projeto**, detalhando cada métrica coletada e sua finalidade dentro da análise dos algoritmos de ordenação.

---

# Parte II — Conceitos Estatísticos do Projeto

Esta seção apresenta os conceitos estatísticos utilizados pelo **LAB EDU SORT V1.0** para analisar o comportamento dos algoritmos de ordenação.

O objetivo desta parte é definir quais informações serão coletadas durante uma execução, qual o significado de cada métrica e como esses dados serão utilizados para comparação, análise e visualização.

As estatísticas foram definidas considerando dois objetivos principais:

```text
Objetivo Técnico

        ↓

Medição objetiva do comportamento dos algoritmos


Objetivo Educacional

        ↓

Compreensão prática da complexidade e eficiência
```

---

# Tipos de Estatísticas

As estatísticas do projeto serão organizadas em categorias.

A classificação adotada é:

```text
Estatísticas

│

├── Operacionais

│      ├── Comparações

│      ├── Trocas

│      └── Movimentações

│

├── Temporais

│      └── Tempo de execução

│

├── Estruturais

│      ├── Tamanho da entrada

│      └── Características dos dados

│

├── Computacionais

│      ├── Complexidade

│      └── Uso de memória

│

└── Contextuais

       ├── Algoritmo utilizado

       ├── Configuração

       └── Origem dos dados
```

---

# Estatísticas Operacionais

As estatísticas operacionais representam as ações realizadas diretamente pelos algoritmos.

Elas permitem observar o comportamento interno da ordenação.

---

# Métricas de Comparação

## Definição

Representa a quantidade de vezes que o algoritmo compara dois elementos.

Exemplo:

```text
Comparar:

5 > 3
```

gera:

```text
comparacoes += 1
```

---

# Objetivo

Permitir avaliar:

- quantidade de decisões realizadas;
- custo lógico do algoritmo;
- comportamento em diferentes entradas.

---

# Exemplo

Entrada:

```text
[5,3,1]
```

Bubble Sort:

```text
5 compara com 3

3 compara com 1

5 compara com 1
```

Resultado:

```text
comparacoes = 3
```

---

# Importância Educacional

A métrica demonstra que algoritmos diferentes podem realizar quantidades diferentes de decisões para resolver o mesmo problema.

---

# Métricas de Movimentação

## Definição

Representam alterações realizadas na posição dos elementos.

Incluem:

- troca de elementos;
- deslocamentos;
- cópias internas.

---

# Tipos de movimentação

O projeto diferencia:

```text
Troca

    ↓

Elemento A troca posição com B


Deslocamento

    ↓

Elemento muda posição sem troca direta
```

---

# Métricas de Troca

## Definição

Representam operações onde dois elementos alteram suas posições.

Exemplo:

Antes:

```text
[5,3]
```

Depois:

```text
[3,5]
```

Registro:

```text
trocas += 1
```

---

# Algoritmos relacionados

Possuem grande importância em:

- Bubble Sort;
- Selection Sort;
- Quick Sort.

---

# Métricas de Movimentação

## Definição

Representam operações de movimentação interna dos elementos.

Exemplo:

Insertion Sort:

```text
[5,8,3]

desloca 8

insere 3

[3,5,8]
```

---

# Importância

Algoritmos podem realizar poucas comparações, mas muitas movimentações.

Por isso as métricas devem ser analisadas em conjunto.

---

# Estatísticas Temporais

## Objetivo

Medir o tempo necessário para executar uma ordenação.

---

# Métrica de Tempo de Execução

## Definição

Representa o intervalo entre:

```text
início da execução

        ↓

fim da execução
```

---

# Representação

```text
tempoExecucao =
fim - inicio
```

---

# Unidade

A implementação deverá utilizar:

```text
segundos

ou

milissegundos
```

dependendo da precisão necessária.

---

# Considerações

O tempo de execução depende de:

- hardware;
- sistema operacional;
- carga da máquina;
- implementação.

Portanto, ele não deve ser analisado isoladamente.

---

# Uso Educacional

A métrica permite demonstrar:

```text
Complexidade teórica

        +

Comportamento real
```

---

# Estatísticas Estruturais

Estas métricas descrevem o contexto dos dados utilizados.

---

# Tamanho da Entrada

## Definição

Quantidade de elementos processados.

---

# Representação

Exemplo:

```text
quantidadeElementos = 1000
```

---

# Importância

A complexidade dos algoritmos depende diretamente do tamanho da entrada.

Exemplo:

```text
O(n²)

com 10 elementos

é diferente de

O(n²)

com 100000 elementos
```

---

# Características da Entrada

Além do tamanho, os dados podem possuir diferentes estados.

---

# Classificação

```text
Entrada

│

├── Ordenada

│

├── Invertida

│

├── Parcialmente ordenada

│

└── Aleatória
```

---

# Importância

Permite analisar o comportamento dos algoritmos em diferentes cenários.

---

# Exemplo

Bubble Sort:

Melhor caso:

```text
lista já ordenada
```

Pior caso:

```text
lista invertida
```

---

# Estatísticas Computacionais

Representam informações relacionadas ao custo computacional.

---

# Métricas de Complexidade

## Definição

Representam o comportamento esperado do algoritmo conforme o crescimento da entrada.

---

# Notações utilizadas

O projeto utilizará:

```text
O(1)

O(log n)

O(n)

O(n log n)

O(n²)
```

---

# Exemplos

## Bubble Sort

```text
O(n²)
```

---

## Merge Sort

```text
O(n log n)
```

---

## Quick Sort

Caso médio:

```text
O(n log n)
```

Pior caso:

```text
O(n²)
```

---

# Uso no Projeto

A complexidade será armazenada como informação descritiva.

Exemplo:

```text
ComplexidadeTempo

"O(n²)"
```

---

# Métricas de Memória

## Definição

Representam o espaço adicional utilizado durante a execução.

---

# Exemplos

Bubble Sort:

```text
O(1)
```

Merge Sort:

```text
O(n)
```

---

# Importância

Permite comparar algoritmos não apenas pela velocidade, mas também pelo consumo de recursos.

---

# Estatísticas Contextuais

Representam informações sobre o cenário da execução.

---

# Algoritmo utilizado

Exemplo:

```text
BubbleSort

QuickSort

MergeSort
```

---

# Origem dos dados

Exemplo:

```text
Arquivo

Geração automática

Entrada manual
```

---

# Configuração utilizada

Exemplo:

```text
Quantidade:

10000 elementos


Tipo:

Aleatório
```

---

# Modelo Consolidado de Métricas

A execução de um algoritmo deverá produzir um conjunto de informações semelhante a:

```text
EstatisticasOrdenacao

{

 algoritmo:

    QuickSort


 entrada:

    10000 elementos


 comparacoes:

    120000


 trocas:

    35000


 movimentacoes:

    50000


 tempo:

    0.034 segundos


 memoria:

    O(log n)

}
```

---

# Relação entre Métricas

As métricas não devem ser analisadas individualmente.

A análise correta considera:

```text
Comparações

        +

Movimentações

        +

Tempo

        +

Memória

        +

Entrada utilizada
```

---

# Exemplo Comparativo

Dois algoritmos podem apresentar:

```text
Algoritmo A

Poucas comparações

Muitas movimentações


Algoritmo B

Muitas comparações

Poucas movimentações
```

O melhor resultado depende do contexto.

---

# Considerações da Parte

As métricas definidas nesta seção estabelecem a base estatística do LAB EDU SORT V1.0.

O modelo não busca apenas medir desempenho, mas transformar a execução dos algoritmos em informações compreensíveis.

Através dessas métricas será possível:

- comparar algoritmos;
- demonstrar complexidade;
- analisar comportamento;
- criar visualizações;
- apoiar o aprendizado de estruturas e algoritmos.

A próxima seção apresentará o **Modelo Conceitual das Estatísticas**, definindo as entidades responsáveis por representar essas informações dentro da arquitetura.

---

# Parte III — Modelo Conceitual das Estatísticas

Esta seção apresenta o modelo conceitual das estatísticas do **LAB EDU SORT V1.0**.

O objetivo é definir as entidades responsáveis por representar as informações produzidas durante a execução dos algoritmos de ordenação, bem como seus relacionamentos e ciclo de vida.

O modelo conceitual estabelece uma visão independente da implementação, permitindo que posteriormente as entidades sejam transformadas em classes, estruturas de dados e contratos entre módulos.

---

# Objetivo do Modelo Conceitual

O modelo conceitual de estatísticas tem como finalidade representar:

- uma execução de ordenação;
- os eventos produzidos durante essa execução;
- as métricas coletadas;
- o resultado final obtido.

A visão geral é:

```text
ExecucaoOrdenacao

        │

        │ gera

        ▼

EventoOrdenacao

        │

        │ consolida

        ▼

EstatisticasOrdenacao

        │

        │ compõe

        ▼

ResultadoOrdenacao
```

---

# Entidades Principais

O domínio estatístico será composto pelas seguintes entidades:

```text
Modelo Estatístico

│

├── ExecucaoOrdenacao

│

├── EventoOrdenacao

│

├── EstatisticasOrdenacao

│

├── ResultadoOrdenacao

│

├── ConfiguracaoExecucao

│

└── ConjuntoDados
```

---

# Entidade ExecucaoOrdenacao

## Objetivo

Representa uma execução específica de um algoritmo de ordenação.

Ela funciona como o contexto geral onde todas as informações estatísticas são produzidas.

---

# Responsabilidades

A entidade deve representar:

- algoritmo utilizado;
- configuração aplicada;
- dados processados;
- estado da execução.

---

# Informações conceituais

```text
ExecucaoOrdenacao

idExecucao

algoritmo

dataExecucao

configuracao

dadosEntrada

estado
```

---

# Relacionamentos

```text
ExecucaoOrdenacao

        │

        ├──────── possui ────────► ConjuntoDados

        │

        ├──────── utiliza ───────► ConfiguracaoExecucao

        │

        ├──────── gera ──────────► EventoOrdenacao

        │

        └──────── produz ────────► ResultadoOrdenacao
```

---

# Entidade EventoOrdenacao

## Objetivo

Representa uma ocorrência individual durante a execução de um algoritmo.

Os eventos permitem acompanhar o comportamento interno da ordenação.

---

# Conceito

Um algoritmo não apenas retorna um resultado.

Durante sua execução ele realiza diversas operações:

```text
Comparar

Trocar

Mover

Dividir

Mesclar

Selecionar
```

Cada operação pode gerar um evento.

---

# Responsabilidades

Representar:

- tipo da operação;
- momento da ocorrência;
- elementos envolvidos;
- posição afetada.

---

# Informações conceituais

```text
EventoOrdenacao

idEvento

tipoEvento

indiceOrigem

indiceDestino

valorAnterior

valorAtual

timestamp
```

---

# Tipos de Evento

A classificação inicial será:

```text
EventoOrdenacao

│

├── COMPARACAO

│

├── TROCA

│

├── MOVIMENTACAO

│

├── DIVISAO

│

├── MESCLAGEM

│

└── FINALIZACAO
```

---

# Exemplo Conceitual

Operação:

```text
Comparar posição 0 com posição 1
```

Evento:

```text
EventoOrdenacao

tipo:

COMPARACAO


origem:

0


destino:

1
```

---

# Entidade EstatisticasOrdenacao

## Objetivo

Representa o conjunto consolidado de métricas de uma execução.

É a principal entidade estatística do domínio.

---

# Responsabilidades

Armazenar:

- quantidade de comparações;
- quantidade de trocas;
- quantidade de movimentações;
- tempo de execução;
- informações de memória;
- complexidade estimada.

---

# Informações conceituais

```text
EstatisticasOrdenacao

quantidadeComparacoes

quantidadeTrocas

quantidadeMovimentacoes

tempoExecucao

memoriaUtilizada

complexidadeTempo

complexidadeMemoria
```

---

# Relacionamentos

```text
ExecucaoOrdenacao

        │

        │ possui

        ▼

EstatisticasOrdenacao

        │

        │ consolida

        ▼

EventoOrdenacao
```

---

# Característica Importante

A entidade não executa cálculos.

Ela apenas representa os resultados coletados.

---

# Entidade ResultadoOrdenacao

## Objetivo

Representa o resultado final produzido pelo algoritmo.

---

# Responsabilidades

Armazenar:

- dados ordenados;
- algoritmo utilizado;
- estatísticas associadas;
- status da execução.

---

# Informações conceituais

```text
ResultadoOrdenacao

dadosOrdenados

algoritmo

estatisticas

tempoTotal

status
```

---

# Relacionamentos

```text
ResultadoOrdenacao

        │

        ├──── contém ────► EstatisticasOrdenacao

        │

        └──── utiliza ───► ConjuntoDados
```

---

# Entidade ConfiguracaoExecucao

## Objetivo

Representa as escolhas realizadas antes da execução.

---

# Informações conceituais

```text
ConfiguracaoExecucao

algoritmoSelecionado

origemDados

quantidadeElementos

tipoOrdenacaoInicial
```

---

# Papel no Modelo Estatístico

Permite contextualizar os resultados.

Exemplo:

```text
QuickSort

10000 elementos

entrada aleatória
```

---

# Entidade ConjuntoDados

## Objetivo

Representa os dados submetidos ao algoritmo.

---

# Informações conceituais

```text
ConjuntoDados

valores

quantidade

origem

caracteristicas
```

---

# Papel Estatístico

Fornece informações necessárias para interpretar os resultados.

---

# Relacionamento Geral das Entidades

O modelo completo:

```text
                 ConfiguracaoExecucao

                         │

                         ▼

                  ExecucaoOrdenacao

                         │

        ┌────────────────┼────────────────┐

        │                │                │

        ▼                ▼                ▼

 ConjuntoDados   EventoOrdenacao   EstatisticasOrdenacao

                                          │

                                          ▼

                                ResultadoOrdenacao
```

---

# Ciclo de Vida das Estatísticas

O ciclo completo ocorre em etapas.

---

# Etapa 01 — Preparação

São definidos:

```text
Algoritmo

Entrada

Configuração
```

---

# Etapa 02 — Execução

O algoritmo inicia o processamento.

Durante essa etapa são gerados:

```text
Eventos
```

---

# Etapa 03 — Coleta

Os eventos atualizam:

```text
Contadores

Métricas

Histórico
```

---

# Etapa 04 — Consolidação

Ao final da execução:

```text
Eventos

        ↓

EstatisticasOrdenacao
```

---

# Etapa 05 — Resultado

O sistema produz:

```text
ResultadoOrdenacao
```

contendo:

- dados ordenados;
- métricas;
- informações da execução.

---

# Diagrama Conceitual Simplificado

```text
+---------------------+

| ExecucaoOrdenacao   |

+---------------------+

          |

          |

          +----------------+

          |                |

          ▼                ▼

+----------------+   +----------------------+

| Evento         |   | Estatisticas         |

| Ordenacao      |   | Ordenacao            |

+----------------+   +----------------------+

                            |

                            ▼

                 +--------------------+

                 | Resultado          |

                 | Ordenacao          |

                 +--------------------+

```

---

# Decisões Arquiteturais

## Estatísticas como entidade própria

As métricas não devem ficar espalhadas em algoritmos.

Motivo:

- centralização;
- reutilização;
- padronização.

---

## Eventos separados das métricas

Eventos representam acontecimentos.

Estatísticas representam consolidação.

Exemplo:

```text
Evento:

"houve uma troca"


Estatística:

"foram realizadas 500 trocas"
```

---

## Resultado separado da Estatística

O resultado final contém as estatísticas, mas possui responsabilidade própria.

---

# Considerações da Parte

O modelo conceitual definido nesta seção estabelece a base para implementação das estatísticas no LAB EDU SORT V1.0.

As entidades definidas permitem representar:

```text
O que foi executado?

Como foi executado?

Quais operações ocorreram?

Qual foi o resultado?
```

Essa separação prepara o projeto para a próxima etapa:

**Parte IV — Classes do Modelo de Estatísticas**

onde estas entidades serão transformadas em classes, atributos, responsabilidades e relacionamentos dentro da arquitetura orientada a objetos.

---

# Parte IV — Classes do Modelo de Estatísticas

Esta seção apresenta a definição das classes responsáveis por representar o modelo estatístico do **LAB EDU SORT V1.0**.

A partir do modelo conceitual definido anteriormente, as entidades do domínio são transformadas em classes orientadas a objetos, respeitando os princípios arquiteturais estabelecidos no projeto:

- responsabilidade única;
- baixo acoplamento;
- alta coesão;
- separação entre domínio e implementação;
- facilidade de evolução.

---

# Objetivo do Modelo de Classes

O modelo de classes estatísticas tem como objetivo representar:

```text
Execução

    ↓

Eventos gerados

    ↓

Métricas coletadas

    ↓

Resultado consolidado
```

As classes devem permitir:

- registrar informações durante a execução;
- consolidar métricas;
- disponibilizar resultados;
- alimentar relatórios e visualizações.

---

# Visão Geral das Classes

O modelo será composto pelas seguintes classes:

```text
Modelo Estatístico

│

├── EstatisticasOrdenacao

│

├── ContadorOperacoes

│

├── MedicaoTempo

│

├── ResultadoOrdenacao

│

├── EventoOrdenacao

│

└── TipoEventoOrdenacao
```

---

# Diagrama Geral das Classes

```text
+-------------------------+

| ExecucaoOrdenacao       |

+-------------------------+

            |

            |

            +--------------------+

            |                    |

            ▼                    ▼

+----------------+    +-----------------------+

| EventoOrdenacao|    | EstatisticasOrdenacao |

+----------------+    +-----------------------+

                              |

                              |

              ┌───────────────┼───────────────┐

              │               │               │

              ▼               ▼               ▼

   +----------------+ +--------------+ +----------------+

   | Contador       | | MedicaoTempo | | Resultado      |

   | Operacoes      | |              | | Ordenacao      |

   +----------------+ +--------------+ +----------------+

```

---

# Classe EstatisticasOrdenacao

## Responsabilidade

Representar o conjunto consolidado das métricas geradas durante uma execução de ordenação.

Ela é a principal classe do domínio estatístico.

---

# Objetivos

A classe deve:

- armazenar métricas;
- consolidar informações;
- disponibilizar dados para análise.

---

# Representação Conceitual

```python
EstatisticasOrdenacao

    algoritmo

    quantidadeComparacoes

    quantidadeTrocas

    quantidadeMovimentacoes

    tempoExecucao

    memoriaUtilizada

    complexidadeTempo

    complexidadeMemoria
```

---

# Responsabilidades

A classe é responsável por:

- manter o estado estatístico;
- receber atualizações;
- fornecer resumo da execução.

---

# Não é responsabilidade

A classe não deve:

- executar algoritmos;
- modificar listas;
- gerar gráficos.

---

# Relacionamentos

```text
EstatisticasOrdenacao

        │

        ├──── possui ───► ContadorOperacoes

        │

        ├──── possui ───► MedicaoTempo

        │

        └──── pertence ─► ResultadoOrdenacao
```

---

# Classe ContadorOperacoes

## Responsabilidade

Controlar a quantidade de operações realizadas durante a execução.

---

# Objetivo

Centralizar os contadores utilizados pelos algoritmos.

---

# Representação Conceitual

```python
ContadorOperacoes

    comparacoes

    trocas

    movimentacoes

    acessos
```

---

# Responsabilidades

A classe deve permitir:

- incrementar comparações;
- registrar trocas;
- registrar movimentações;
- consultar totais.

---

# Exemplo Conceitual

Execução:

```text
Comparação

    ↓

incrementa contador

    ↓

comparacoes = 1
```

---

# Decisão Arquitetural

Os contadores ficam isolados para evitar que:

```text
BubbleSort

QuickSort

MergeSort
```

tenham implementações próprias de métricas.

---

# Classe MedicaoTempo

## Responsabilidade

Representar a medição temporal de uma execução.

---

# Objetivo

Controlar informações relacionadas ao tempo.

---

# Representação Conceitual

```python
MedicaoTempo

    inicio

    fim

    duracao
```

---

# Responsabilidades

A classe deve:

- registrar início;
- registrar término;
- calcular duração.

---

# Exemplo

```text
Início:

10:00:00


Fim:

10:00:02


Duração:

2 segundos
```

---

# Decisão Arquitetural

A medição temporal é separada das demais métricas porque possui comportamento próprio.

---

# Classe EventoOrdenacao

## Responsabilidade

Representar uma operação individual ocorrida durante a execução.

---

# Objetivo

Permitir rastrear o comportamento interno dos algoritmos.

---

# Representação Conceitual

```python
EventoOrdenacao

    tipoEvento

    indiceOrigem

    indiceDestino

    valorAnterior

    valorAtual

    momento
```

---

# Responsabilidades

Representar:

- o que ocorreu;
- onde ocorreu;
- quando ocorreu.

---

# Exemplos

## Evento de comparação

```text
Tipo:

COMPARACAO


Origem:

0


Destino:

1
```

---

## Evento de troca

```text
Tipo:

TROCA


Origem:

2


Destino:

5
```

---

# Enum TipoEventoOrdenacao

## Responsabilidade

Representar os tipos possíveis de eventos.

---

# Valores previstos

```python
TipoEventoOrdenacao

COMPARACAO

TROCA

MOVIMENTACAO

DIVISAO

MESCLAGEM

FINALIZACAO
```

---

# Benefício

Evita utilização de strings livres.

Exemplo incorreto:

```python
evento.tipo = "troca"
```

Exemplo correto:

```python
evento.tipo = TipoEventoOrdenacao.TROCA
```

---

# Classe ResultadoOrdenacao

## Responsabilidade

Representar o resultado final produzido pelo algoritmo.

---

# Objetivo

Unificar:

- dados ordenados;
- informações estatísticas;
- informações da execução.

---

# Representação Conceitual

```python
ResultadoOrdenacao

    dadosOrdenados

    algoritmo

    estatisticas

    sucesso

    mensagem
```

---

# Responsabilidades

A classe deve:

- armazenar resultado;
- disponibilizar métricas;
- informar status da execução.

---

# Relacionamentos

```text
ResultadoOrdenacao

        │

        ├──── contém ───► EstatisticasOrdenacao

        │

        └──── contém ───► dadosOrdenados
```

---

# Relacionamento Completo entre Classes

```text
                 ResultadoOrdenacao

                         ▲

                         |

                         |

              EstatisticasOrdenacao

                         |

        ┌────────────────┼────────────────┐

        │                │                │

        ▼                ▼                ▼

 ContadorOperacoes   MedicaoTempo   EventoOrdenacao

```

---

# Fluxo de Atualização das Classes

Durante a execução:

```text
Algoritmo

    │

    │ realiza operação

    ▼

EventoOrdenacao

    │

    │ atualiza

    ▼

ContadorOperacoes

    │

    ▼

EstatisticasOrdenacao

    │

    ▼

ResultadoOrdenacao
```

---

# Decisões de Modelagem

---

# Estatísticas como objeto de domínio

As métricas não serão representadas apenas como variáveis soltas.

Motivo:

- organização;
- reutilização;
- clareza.

---

# Composição ao invés de herança

A arquitetura utiliza composição:

```text
EstatisticasOrdenacao

       possui

ContadorOperacoes
```

ao invés de:

```text
ContadorOperacoes

       herda

EstatisticasOrdenacao
```

---

# Classes pequenas e especializadas

Cada classe possui uma responsabilidade clara:

| Classe | Responsabilidade |
|-|-|
| EstatisticasOrdenacao | Consolidar métricas |
| ContadorOperacoes | Contar operações |
| MedicaoTempo | Medir duração |
| EventoOrdenacao | Registrar eventos |
| ResultadoOrdenacao | Representar saída |

---

# Compatibilidade com os Módulos

As classes possuem relação direta com os módulos definidos anteriormente:

| Classe | Módulo |
|-|-|
| EstatisticasOrdenacao | estatisticas |
| ContadorOperacoes | estatisticas |
| MedicaoTempo | estatisticas |
| EventoOrdenacao | algoritmosOrdenacao / estatisticas |
| ResultadoOrdenacao | modelos |

---

# Considerações da Parte

O modelo de classes apresentado transforma o conceito estatístico em uma estrutura orientada a objetos organizada e extensível.

A separação entre:

```text
Eventos

Operações

Medições

Resultados
```

permite que o sistema acompanhe a execução dos algoritmos sem criar dependências excessivas.

Essa modelagem prepara a arquitetura para:

- coleta automática de métricas;
- geração de relatórios;
- comparação entre algoritmos;
- evolução futura.

A próxima seção apresentará as **Estruturas de Dados das Estatísticas**, detalhando como essas classes serão representadas internamente utilizando `dataclass`, `list`, `dict` e outras estruturas definidas no projeto.

---

# Parte V — Estruturas de Dados das Estatísticas

Esta seção apresenta as estruturas de dados utilizadas para representar, armazenar e manipular as informações estatísticas do **LAB EDU SORT V1.0**.

O objetivo desta parte é definir como as classes do modelo estatístico serão implementadas internamente, mantendo alinhamento com as decisões arquiteturais estabelecidas anteriormente.

As escolhas consideram:

- simplicidade;
- clareza;
- desempenho;
- facilidade de manutenção;
- valor educacional.

---

# Objetivo das Estruturas de Dados

As estruturas de dados do módulo `estatisticas` devem permitir:

- armazenar métricas consolidadas;
- registrar eventos individuais;
- manter histórico de execução;
- disponibilizar informações para relatórios;
- permitir futuras extensões.

A arquitetura seguirá o princípio:

```text
Classe de Domínio

        ↓

Estrutura Interna

        ↓

Dados Estatísticos

        ↓

Relatórios e Visualizações
```

---

# Visão Geral das Estruturas

As principais estruturas utilizadas serão:

```text
Estruturas Estatísticas

│

├── dataclass

│

├── list

│

├── dict

│

├── Enum

│

└── tuple
```

---

# Uso de dataclass

## Objetivo

Representar entidades do domínio estatístico.

As classes que possuem dados estruturados serão implementadas utilizando `dataclass`.

---

# Classes utilizando dataclass

As principais classes serão:

```text
EstatisticasOrdenacao

ContadorOperacoes

MedicaoTempo

EventoOrdenacao

ResultadoOrdenacao
```

---

# Justificativa

A utilização de `dataclass` proporciona:

- declaração clara dos atributos;
- redução de código repetitivo;
- melhor leitura;
- integração com tipagem estática.

---

# Benefício Arquitetural

A estrutura permanece alinhada ao modelo de classes definido anteriormente.

```text
Entidade do domínio

        ↓

Classe Python

        ↓

Objeto estatístico
```

---

# Uso de list para Histórico de Eventos

## Objetivo

Armazenar a sequência de eventos gerados durante uma execução.

---

# Representação

```python
eventos = [

    EventoOrdenacao,

    EventoOrdenacao,

    EventoOrdenacao

]
```

---

# Exemplo

Durante uma execução:

```text
Evento 01

COMPARACAO


Evento 02

TROCA


Evento 03

MOVIMENTACAO
```

Resultado:

```text
[
 Comparacao,

 Troca,

 Movimentacao
]
```

---

# Justificativa

A estrutura `list` foi escolhida porque:

- mantém a ordem cronológica;
- permite iteração sequencial;
- facilita visualização;
- possui acesso simples por índice.

---

# Uso Educacional

A lista de eventos permite demonstrar:

```text
Passo 01

Comparou elementos


Passo 02

Realizou troca


Passo 03

Continuou execução
```

---

# Uso de dict para Agregação de Métricas

## Objetivo

Representar informações agrupadas ou dinâmicas.

---

# Representação

```python
metricas = {

    "comparacoes": 1000,

    "trocas": 200,

    "movimentacoes": 500

}
```

---

# Utilização

O dicionário poderá ser utilizado para:

- relatórios;
- exportações;
- métricas adicionais;
- extensões futuras.

---

# Justificativa

O uso de `dict` facilita:

- inclusão de novas métricas;
- armazenamento flexível;
- conversão para formatos externos.

---

# Uso de Enum

## Objetivo

Representar valores controlados.

---

# Aplicações

Principalmente:

```text
TipoEventoOrdenacao

EstadoExecucao

OrigemDados
```

---

# Exemplo

```python
class TipoEventoOrdenacao(Enum):

    COMPARACAO = 1

    TROCA = 2

    MOVIMENTACAO = 3
```

---

# Justificativa

Evita valores inconsistentes.

Exemplo incorreto:

```python
tipoEvento = "comparacao"
```

Possíveis problemas:

```text
"Comparacao"

"comparação"

"COMPARAR"
```

---

# Exemplo correto

```python
tipoEvento = TipoEventoOrdenacao.COMPARACAO
```

---

# Uso de tuple

## Objetivo

Representar informações imutáveis.

---

# Aplicações

Pode ser utilizada para:

- pares de índices;
- valores antes/depois;
- coordenadas de operação.

---

# Exemplo

Durante uma troca:

```python
(

indiceOrigem,

indiceDestino

)
```

---

# Estruturas Imutáveis

Algumas informações do modelo estatístico devem permanecer protegidas.

Exemplos:

```text
Evento registrado

Configuração da execução

Informações históricas
```

---

# Estratégias utilizadas

Podem ser utilizadas:

```text
dataclass(frozen=True)

tuple

Enum
```

---

# Estrutura Interna das Principais Classes

## EstatisticasOrdenacao

Representação:

```text
EstatisticasOrdenacao

{

 algoritmo: str


 contador:

    ContadorOperacoes


 tempo:

    MedicaoTempo


 memoria:

    float


 complexidade:

    str

}
```

---

## ContadorOperacoes

Representação:

```text
ContadorOperacoes

{

 comparacoes: int


 trocas: int


 movimentacoes: int


 acessos: int

}
```

---

## MedicaoTempo

Representação:

```text
MedicaoTempo

{

 inicio: datetime


 fim: datetime


 duracao: float

}
```

---

## EventoOrdenacao

Representação:

```text
EventoOrdenacao

{

 tipoEvento: Enum


 indiceOrigem: int


 indiceDestino: int


 valores: tuple


 momento: datetime

}
```

---

## ResultadoOrdenacao

Representação:

```text
ResultadoOrdenacao

{

 dadosOrdenados: list


 algoritmo: str


 estatisticas:

    EstatisticasOrdenacao


 sucesso: bool

}
```

---

# Matriz Classe × Estrutura

| Classe | dataclass | list | dict | Enum | tuple |
|---|---|---|---|---|---|
| EstatisticasOrdenacao | ✓ | | ✓ | | |
| ContadorOperacoes | ✓ | | | | |
| MedicaoTempo | ✓ | | | | |
| EventoOrdenacao | ✓ | | | ✓ | ✓ |
| ResultadoOrdenacao | ✓ | ✓ | | | |

---

# Decisões Arquiteturais

## Estruturas simples antes de estruturas especializadas

A V1.0 prioriza:

```text
list

dict

dataclass

Enum
```

pois são suficientes para o domínio inicial.

---

# Separação entre armazenamento e comportamento

As estruturas armazenam dados.

Os algoritmos executam operações.

Exemplo:

```text
ContadorOperacoes

armazena:

comparacoes = 100


Algoritmo

executa:

comparação
```

---

# Evitar estruturas genéricas como modelo principal

Não utilizar:

```python
dictEstatisticas
```

como representação principal.

Preferir:

```text
EstatisticasOrdenacao
```

com atributos definidos.

---

# Flexibilidade para evolução

As estruturas permitem futuras extensões:

```text
V1.0

list

dict

dataclass


V2.0

banco de dados

serialização

grandes volumes


V3.0

processamento distribuído
```

---

# Considerações da Parte

As estruturas de dados escolhidas para o modelo estatístico mantêm equilíbrio entre simplicidade e capacidade de evolução.

A arquitetura utiliza:

```text
dataclass

        ↓

representação do domínio


list

        ↓

histórico de eventos


dict

        ↓

agregação flexível


Enum

        ↓

controle de estados


tuple

        ↓

dados imutáveis
```

Essa organização garante que o módulo `estatisticas` permaneça:

- organizado;
- extensível;
- desacoplado;
- adequado ao propósito educacional.

A próxima seção apresentará a **Comunicação entre Algoritmos e Estatísticas**, detalhando os contratos, eventos produzidos e o fluxo de comunicação entre os módulos.
```

---

# Parte VI — Comunicação entre Algoritmos e Estatísticas

Esta seção apresenta como ocorre a comunicação entre o módulo `algoritmosOrdenacao` e o módulo `estatisticas` dentro da arquitetura do **LAB EDU SORT V1.0**.

O objetivo é definir:

- responsabilidades de cada módulo;
- contratos de comunicação;
- eventos produzidos durante a execução;
- classificação das mensagens como **Request**, **Response** ou **Event**;
- matriz de comunicação entre componentes.

A comunicação foi projetada seguindo os princípios definidos anteriormente:

- baixo acoplamento;
- separação de responsabilidades;
- independência dos algoritmos;
- extensibilidade;
- facilidade de inclusão de novos algoritmos.

---

# Responsabilidade do Módulo estatisticas

O módulo `estatisticas` é responsável por coletar, organizar e disponibilizar informações relacionadas à execução dos algoritmos de ordenação.

Ele deve:

- receber eventos produzidos pelos algoritmos;
- atualizar contadores;
- registrar informações temporais;
- consolidar métricas;
- gerar resultados estatísticos.

---

# O módulo estatisticas não deve:

O módulo não possui responsabilidade sobre:

- escolha do algoritmo;
- execução da ordenação;
- alteração dos dados;
- controle do fluxo principal da aplicação.

Exemplo:

```text
BubbleSort

não chama

estatisticas para ordenar
```

O correto é:

```text
BubbleSort

executa ordenação

        ↓

gera eventos

        ↓

estatisticas registra informações
```

---

# Responsabilidade do Módulo algoritmosOrdenacao

O módulo `algoritmosOrdenacao` é responsável pela execução dos algoritmos.

Ele deve:

- receber os dados;
- aplicar a estratégia de ordenação;
- produzir eventos durante a execução;
- retornar o resultado ordenado.

---

# O módulo algoritmosOrdenacao não deve:

Não deve:

- armazenar métricas internamente;
- gerar relatórios;
- controlar visualizações.

Exemplo incorreto:

```text
BubbleSort

possui:

contadorComparacoes

contadorTrocas

tempoExecucao
```

---

# Exemplo correto:

```text
BubbleSort

executa

        ↓

gera EventoOrdenacao

        ↓

estatisticas contabiliza
```

---

# Modelo de Comunicação Geral

A comunicação entre os módulos segue o fluxo:

```text
                 Aplicacao

                     │

                     │ Request

                     ▼

          algoritmosOrdenacao

                     │

                     │ Event

                     ▼

              estatisticas

                     │

                     │ Response

                     ▼

              ResultadoOrdenacao
```

---

# Tipos de Comunicação

A arquitetura utiliza três tipos principais de comunicação:

```text
Request

Response

Event
```

---

# Comunicação Request

## Conceito

Representa uma solicitação realizada por um módulo.

No contexto do LAB EDU SORT:

A aplicação solicita que um algoritmo execute uma ordenação.

---

# Exemplo

```text
Aplicacao

        Request

            ↓

BubbleSort
```

---

# Dados enviados

A requisição pode conter:

```text
dadosEntrada

configuracaoExecucao

algoritmoSelecionado
```

---

# Comunicação Response

## Conceito

Representa o retorno de uma operação concluída.

---

# Exemplo

Após a ordenação:

```text
algoritmosOrdenacao

        Response

            ↓

Aplicacao
```

---

# Dados retornados

```text
ResultadoOrdenacao

{

 dadosOrdenados

 estatisticas

 statusExecucao

}
```

---

# Comunicação Event

## Conceito

Representa uma ocorrência durante a execução.

Eventos não solicitam uma resposta imediata.

Eles apenas informam que algo aconteceu.

---

# Exemplo

Durante o Bubble Sort:

```text
Comparação realizada

        ↓

EventoOrdenacao

        ↓

estatisticas
```

---

# Fluxo de Eventos

```text
Algoritmo

    │

    │ EventoOrdenacao

    ▼

Estatisticas

    │

    │ Atualização

    ▼

Contadores e Métricas
```

---

# Contrato de Coleta de Estatísticas

O contrato entre algoritmos e estatísticas estabelece que:

Todo algoritmo de ordenação deverá informar eventos relevantes durante sua execução.

---

# Responsabilidade do Algoritmo

O algoritmo informa:

```text
O que aconteceu?
```

Exemplos:

```text
comparei dois elementos

troquei duas posições

movimentei um valor
```

---

# Responsabilidade do módulo estatisticas

O módulo responde:

```text
Quantas vezes isso aconteceu?

Qual impacto dessa operação?

Como isso influencia o desempenho?
```

---

# Modelo do Evento Ordenacao

O evento será representado conceitualmente:

```text
EventoOrdenacao

{

 tipoEvento

 indiceOrigem

 indiceDestino

 valorAnterior

 valorAtual

 momento

}
```

---

# Exemplos de Eventos

## Evento de Comparação

```text
Tipo:

COMPARACAO


Descrição:

Elemento 0 comparado com elemento 1
```

---

## Evento de Troca

```text
Tipo:

TROCA


Descrição:

Elemento 2 trocado com elemento 5
```

---

## Evento de Movimentação

```text
Tipo:

MOVIMENTACAO


Descrição:

Elemento deslocado para nova posição
```

---

# Fluxo Completo de Comunicação

```text
1. Aplicação solicita execução

        │

        ▼

2. Algoritmo recebe dados

        │

        ▼

3. Algoritmo inicia ordenação

        │

        ▼

4. Eventos são produzidos

        │

        ▼

5. Estatísticas atualizam métricas

        │

        ▼

6. Algoritmo finaliza processamento

        │

        ▼

7. Resultado é consolidado

        │

        ▼

8. Aplicação recebe resposta
```

---

# Matriz de Comunicação

| Origem | Destino | Tipo | Informação |
|---|---|---|---|
| Aplicacao | algoritmosOrdenacao | Request | Solicitação de execução |
| algoritmosOrdenacao | estatisticas | Event | Operações realizadas |
| estatisticas | ResultadoOrdenacao | Response | Métricas consolidadas |
| algoritmosOrdenacao | Aplicacao | Response | Dados ordenados |
| entradaDados | Aplicacao | Response | Dados preparados |

---

# Comunicação entre Classes

A comunicação interna segue:

```text
AlgoritmoOrdenacao

        │

        │ cria

        ▼

EventoOrdenacao

        │

        │ envia

        ▼

EstatisticasOrdenacao

        │

        │ utiliza

        ▼

ContadorOperacoes
```

---

# Exemplo de Execução

Considere:

```text
Entrada:

[5,3,1]
```

---

## Passo 01

Algoritmo compara:

```text
5 > 3
```

Evento:

```text
COMPARACAO
```

---

## Passo 02

Algoritmo troca:

```text
5 ↔ 3
```

Evento:

```text
TROCA
```

---

## Passo 03

Estatísticas atualizam:

```text
comparacoes = 1

trocas = 1
```

---

# Benefícios da Arquitetura

A separação entre algoritmos e estatísticas permite:

---

# Inclusão de novos algoritmos

Adicionar:

```text
Shell Sort

Counting Sort

Radix Sort
```

sem alterar:

```text
estatisticas
```

---

# Testes independentes

É possível testar:

```text
algoritmo

isoladamente
```

e:

```text
estatisticas

isoladamente
```

---

# Evolução futura

Permite adicionar:

- armazenamento em banco;
- exportação de relatórios;
- análise gráfica;
- execução comparativa.

---

# Decisões Arquiteturais

## Eventos como mecanismo principal de integração

Os algoritmos não conhecem detalhes internos das estatísticas.

Eles apenas produzem eventos.

---

# Exemplo

Algoritmo:

```text
"realizei uma troca"
```

Estatísticas:

```text
"vou contabilizar essa troca"
```

---

# Separação entre execução e observação

A execução permanece independente da análise.

```text
Executar

        ≠

Medir
```

---

# Contrato estável

Novos algoritmos devem respeitar:

```text
Entrada

        ↓

Processamento

        ↓

Eventos

        ↓

Resultado
```

---

# Considerações da Parte

A comunicação definida entre `algoritmosOrdenacao` e `estatisticas` estabelece uma arquitetura baseada em eventos.

O fluxo principal é:

```text
Algoritmo executa

        ↓

Eventos são produzidos

        ↓

Estatísticas coletam

        ↓

Métricas são consolidadas

        ↓

Resultado é disponibilizado
```

Essa abordagem garante:

- baixo acoplamento;
- facilidade de evolução;
- clareza arquitetural;
- suporte a análises educacionais.

A próxima seção apresentará o **Modelo de Métricas por Algoritmo**, detalhando como cada algoritmo de ordenação previsto no LAB EDU SORT V1.0 deverá ser analisado estatisticamente.

---

# Parte VII — Modelo de Métricas por Algoritmo

Esta seção apresenta o modelo de métricas associado aos algoritmos de ordenação previstos no LAB EDU SORT V1.0.

O objetivo é definir quais informações estatísticas deverão ser observadas durante a execução de cada algoritmo, permitindo:

- comparação de desempenho;
- análise de comportamento;
- demonstração de complexidade;
- geração de relatórios educacionais;
- suporte às visualizações.

As métricas complementam a análise teórica dos algoritmos, permitindo observar:

Complexidade Teórica

+

Comportamento Experimental

+

Características da Entrada

---

# Objetivo das Métricas por Algoritmo

Cada algoritmo possui características próprias e, consequentemente, determinadas métricas possuem maior relevância.

Exemplos:

- Bubble Sort: maior impacto em trocas.
- Insertion Sort: maior impacto em movimentações.
- Merge Sort: maior impacto em divisões e mesclagens.

---

# Modelo Geral de Avaliação

Todos os algoritmos deverão produzir um conjunto mínimo de métricas:

ExecucaoAlgoritmo

{
    algoritmo

    quantidadeElementos

    comparacoes

    trocas

    movimentacoes

    tempoExecucao

    memoriaUtilizada

    complexidadeTempo

    complexidadeMemoria
}

---

# Algoritmos Avaliados

A primeira versão do LAB EDU SORT contemplará:

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort

---

# Bubble Sort

## Características

Algoritmo baseado em comparações sucessivas e trocas entre elementos adjacentes.

Seu comportamento é influenciado principalmente pela quantidade de trocas realizadas.

## Métricas principais

- Comparações
- Trocas
- Movimentações
- Tempo de execução

## Eventos esperados

COMPARACAO

TROCA

MOVIMENTACAO

## Complexidade

Melhor caso:

O(n)

Caso médio:

O(n²)

Pior caso:

O(n²)

## Memória

O(1)

---

# Selection Sort

## Características

Busca o menor elemento restante e realiza uma troca por posição.

## Métricas principais

- Comparações
- Trocas
- Movimentações

## Eventos esperados

COMPARACAO

SELECAO

TROCA

## Complexidade

Melhor caso:

O(n²)

Caso médio:

O(n²)

Pior caso:

O(n²)

## Memória

O(1)

---

# Insertion Sort

## Características

Constrói uma sequência ordenada através do deslocamento dos elementos.

## Métricas principais

- Comparações
- Movimentações
- Deslocamentos

## Eventos esperados

COMPARACAO

MOVIMENTACAO

INSERCAO

## Complexidade

Melhor caso:

O(n)

Caso médio:

O(n²)

Pior caso:

O(n²)

## Memória

O(1)

---

# Merge Sort

## Características

Utiliza a estratégia:

Dividir

↓

Conquistar

↓

Combinar

## Métricas principais

- Comparações
- Movimentações
- Divisões
- Mesclagens

## Eventos esperados

DIVISAO

COMPARACAO

MESCLAGEM

## Complexidade

Melhor caso:

O(n log n)

Caso médio:

O(n log n)

Pior caso:

O(n log n)

## Memória

O(n)

---

# Quick Sort

## Características

Utiliza um elemento pivô para dividir o conjunto de dados.

## Métricas principais

- Comparações
- Trocas
- Partições
- Recursões

## Eventos esperados

COMPARACAO

PARTICAO

TROCA

## Complexidade

Melhor caso:

O(n log n)

Caso médio:

O(n log n)

Pior caso:

O(n²)

## Memória

O(log n)

---

# Heap Sort

## Características

Utiliza uma estrutura heap para organizar os elementos.

## Métricas principais

- Comparações
- Trocas
- Construção do heap
- Ajustes do heap

## Eventos esperados

COMPARACAO

AJUSTE_HEAP

TROCA

## Complexidade

Melhor caso:

O(n log n)

Caso médio:

O(n log n)

Pior caso:

O(n log n)

## Memória

O(1)

---

# Comparativo Geral dos Algoritmos

| Algoritmo | Comparações | Trocas | Movimentações | Tempo Médio | Memória |
|---|---|---|---|---|---|
| Bubble Sort | Alta | Alta | Alta | O(n²) | O(1) |
| Selection Sort | Alta | Baixa | Baixa | O(n²) | O(1) |
| Insertion Sort | Média/Alta | Baixa | Alta | O(n²) | O(1) |
| Merge Sort | Média | Baixa | Alta | O(n log n) | O(n) |
| Quick Sort | Média | Média | Média | O(n log n) | O(log n) |
| Heap Sort | Média | Média | Média | O(n log n) | O(1) |

---

# Modelo de Relatório Comparativo

RelatorioOrdenacao

{
    algoritmo

    quantidadeElementos

    comparacoes

    trocas

    movimentacoes

    tempoExecucao

}

---

# Uso Educacional

O modelo permite responder:

- Qual algoritmo realizou menos comparações?
- Qual algoritmo realizou mais trocas?
- Como a entrada influencia o resultado?
- O comportamento observado confirma a complexidade teórica?

---

# Evolução Futura das Métricas

V1.0

- comparacoes
- trocas
- movimentacoes
- tempoExecucao


V2.0

- recursividade
- profundidade
- uso detalhado de memória


V3.0

- análise estatística avançada
- execuções em lote
- comparações automáticas

---

# Considerações da Parte

O modelo de métricas por algoritmo estabelece uma forma padronizada de observar diferentes estratégias de ordenação.

A arquitetura permite que cada algoritmo mantenha suas características específicas, mas produza informações comparáveis.

Fluxo definido:

Algoritmo

↓

Eventos específicos

↓

Métricas consolidadas

↓

Comparação entre algoritmos

↓

Análise educacional

Com essa definição, o LAB EDU SORT V1.0 poderá demonstrar não apenas o resultado da ordenação, mas também o comportamento interno de cada algoritmo.

A próxima seção apresentará o Modelo de Relatórios e Visualizações, definindo como as estatísticas serão transformadas em informações apresentadas ao usuário.

---

# Parte VIII — Relatórios e Visualizações

Esta seção apresenta o modelo responsável pela transformação dos dados estatísticos coletados durante a execução dos algoritmos em informações compreensíveis para o usuário.

O objetivo é definir como o módulo `estatisticas` disponibilizará informações para:

- relatórios textuais;
- comparações entre algoritmos;
- análises educacionais;
- visualizações gráficas;
- futuras integrações.

A arquitetura segue o princípio:

Dados brutos

↓

Processamento estatístico

↓

Informação consolidada

↓

Relatório / Visualização

---

# Objetivo dos Relatórios

Os relatórios têm como finalidade apresentar:

- desempenho dos algoritmos;
- quantidade de operações realizadas;
- comportamento durante a execução;
- comparação entre estratégias;
- influência do tipo de entrada.

O relatório não deve apenas apresentar números.

Ele deve auxiliar na compreensão do comportamento dos algoritmos.

---

# Responsabilidade do Módulo de Relatórios

O módulo responsável pelos relatórios deverá:

- receber dados estatísticos consolidados;
- organizar informações;
- formatar resultados;
- disponibilizar dados para apresentação.

---

# O módulo de relatórios não deve:

Não deve:

- executar algoritmos;
- alterar dados originais;
- calcular métricas primárias;
- controlar a execução da aplicação.

A separação segue:

Algoritmos

executam

↓

Estatísticas

medem

↓

Relatórios

apresentam

---

# Modelo Conceitual do Relatório

O relatório será representado conceitualmente por:

RelatorioOrdenacao

{

 algoritmo

 dadosEntrada

 quantidadeElementos

 estatisticas

 resultado

 observacoes

}

---

# Estrutura das Informações

Um relatório poderá conter:

## Identificação da Execução

Informações:

- algoritmo utilizado;
- data e hora;
- quantidade de elementos;
- tipo de entrada.

---

## Dados Estatísticos

Informações:

- comparações;
- trocas;
- movimentações;
- tempo de execução;
- consumo de memória.

---

## Análise Comparativa

Informações:

- melhor desempenho;
- pior desempenho;
- diferenças entre algoritmos;
- comportamento observado.

---

# Tipos de Relatórios

A arquitetura prevê três tipos principais:

- relatório individual;
- relatório comparativo;
- relatório experimental.

---

# Relatório Individual

## Objetivo

Apresentar uma única execução de um algoritmo.

Exemplo:

Bubble Sort

Entrada:

[5,3,1]

Resultado:

[1,3,5]

Métricas:

comparacoes = 3

trocas = 2

tempo = 0.002s

---

# Relatório Comparativo

## Objetivo

Comparar diferentes algoritmos utilizando a mesma entrada.

Exemplo:

Entrada:

1000 elementos aleatórios

Resultado:

| Algoritmo | Comparações | Tempo |
|---|---|---|
| Bubble Sort | 499500 | 2.5s |
| Merge Sort | 8500 | 0.08s |
| Quick Sort | 9200 | 0.10s |

---

# Relatório Experimental

## Objetivo

Registrar diversas execuções para análise estatística.

Exemplo:

Execução 01

Entrada:

100 elementos

---

Execução 02

Entrada:

500 elementos

---

Execução 03

Entrada:

1000 elementos

---

Possibilitando análises como:

- crescimento do tempo;
- crescimento das operações;
- comportamento assintótico.

---

# Modelo de Saída Textual

Exemplo:

LAB EDU SORT

Execução:

Algoritmo:

Merge Sort

Quantidade de elementos:

1000


Resultado:

Ordenação concluída.


Estatísticas:

Comparações:

8500


Movimentações:

12000


Tempo:

0.08 segundos

---

# Visualizações

O módulo de visualização tem como objetivo transformar estatísticas em representações gráficas.

---

# Responsabilidade das Visualizações

As visualizações devem:

- apresentar informações graficamente;
- facilitar interpretação;
- permitir comparação visual;
- apoiar o aprendizado.

---

# Tipos de Visualização

A arquitetura prevê:

- gráficos de comparação;
- gráficos de crescimento;
- gráficos de operações;
- animação da ordenação.

---

# Gráfico Comparativo de Algoritmos

Objetivo:

Comparar desempenho entre algoritmos.

Exemplo:

Métrica:

Tempo de execução

Representação:

Algoritmo

↓

Valor medido

---

# Gráfico de Operações

Objetivo:

Demonstrar quantidade de operações realizadas.

Métricas:

- comparações;
- trocas;
- movimentações.

Exemplo:

Bubble Sort:

comparações: ██████████

trocas: ████████

Merge Sort:

comparações: ███

trocas: ██

---

# Gráfico de Crescimento

Objetivo:

Demonstrar comportamento conforme aumenta a entrada.

Exemplo:

Quantidade de elementos:

100

500

1000

5000


Comparando:

Tempo

↓

Quantidade de operações

---

# Animação da Ordenação

A animação tem finalidade exclusivamente educacional.

Ela poderá demonstrar:

- comparação entre elementos;
- troca de posições;
- movimentação;
- estado atual da lista.

---

# Modelo de Comunicação com Visualizações

A comunicação seguirá:

estatisticas

↓

ResultadoOrdenacao

↓

visualizacoes

↓

Representação gráfica

---

# Contrato de Comunicação

O módulo de visualizações receberá:

Request:

Dados estatísticos consolidados.


Response:

Objeto visual ou representação formatada.


Event:

Atualização de estado durante animações.

---

# Matriz de Comunicação

| Origem | Destino | Tipo | Informação |
|---|---|---|---|
| estatisticas | relatorios | Request | Dados consolidados |
| relatorios | aplicacao | Response | Relatório gerado |
| estatisticas | visualizacoes | Request | Métricas para exibição |
| algoritmosOrdenacao | visualizacoes | Event | Estado da execução |

---

# Evolução das Visualizações

## Versão V1.0

Objetivo:

Apresentação simples.

Recursos:

- saída textual;
- tabelas;
- comparações básicas.

---

## Versão V2.0

Objetivo:

Melhoria da análise.

Recursos:

- gráficos;
- exportação;
- relatórios avançados.

---

## Versão V3.0

Objetivo:

Ambiente educacional completo.

Recursos:

- animações;
- dashboards;
- análise interativa.

---

# Princípios Arquiteturais

As visualizações devem permanecer desacopladas dos algoritmos.

O algoritmo não deve conhecer:

- gráficos;
- relatórios;
- interfaces.

Fluxo correto:

Algoritmo

↓

Eventos

↓

Estatísticas

↓

Relatórios

↓

Visualização

---

# Benefícios da Arquitetura

A separação permite:

- adicionar novas formas de apresentação;
- criar interfaces diferentes;
- manter algoritmos independentes;
- facilitar testes.

---

# Considerações da Parte

O modelo de relatórios e visualizações transforma os dados coletados pelo módulo `estatisticas` em informações úteis para análise e aprendizado.

O fluxo final definido é:

Execução do algoritmo

↓

Coleta de eventos

↓

Consolidação estatística

↓

Geração de relatório

↓

Visualização

Essa arquitetura permite que o LAB EDU SORT V1.0 seja não apenas uma biblioteca de algoritmos, mas uma ferramenta educacional capaz de demonstrar o funcionamento interno dos métodos de ordenação.

---

# Parte IX — Diagramas e Arquitetura

Esta seção consolida os principais diagramas arquiteturais relacionados ao modelo de estatísticas do **LAB EDU SORT V1.0**.

O objetivo é representar:

- organização dos módulos;
- comunicação entre componentes;
- fluxo de dados;
- relacionamento entre classes;
- ciclo completo de execução;
- responsabilidades arquiteturais.

Os diagramas utilizam representação textual compatível com Markdown, permitindo futura conversão para ferramentas como:

- Mermaid;
- PlantUML;
- Draw.io;
- Lucidchart.

---

# Visão Arquitetural Geral

A arquitetura do LAB EDU SORT V1.0 segue uma organização modular:

                         Aplicacao

                             |

                             |

              +--------------+--------------+

              |                             |

              v                             v

        entradaDados              algoritmosOrdenacao

                                              |

                                              |

                                              v

                                      eventosOrdenacao

                                              |

                                              |

                                              v

                                      estatisticas

                                              |

                         +--------------------+--------------------+

                         |                                         |

                         v                                         v

                   relatorios                            visualizacoes

---

# Arquitetura em Camadas

O projeto é organizado em camadas de responsabilidade:

+-----------------------------------------------+
|                 Aplicacao                     |
|                                               |
| Controle do fluxo principal                   |
+-----------------------------------------------+

                     |

                     v

+-----------------------------------------------+
|              Camada de Domínio                |
|                                               |
| algoritmosOrdenacao                           |
| modelos                                       |
| estatisticas                                  |
+-----------------------------------------------+

                     |

                     v

+-----------------------------------------------+
|              Camada de Suporte                |
|                                               |
| entradaDados                                  |
| validacoes                                    |
| utilitarios                                   |
| configuracoes                                 |
+-----------------------------------------------+

                     |

                     v

+-----------------------------------------------+
|              Camada de Apresentação           |
|                                               |
| relatorios                                    |
| visualizacoes                                 |
+-----------------------------------------------+

---

# Diagrama de Comunicação entre Módulos

A comunicação principal segue o modelo:

Aplicacao

    |

    | Request

    v

algoritmosOrdenacao

    |

    | Event

    v

estatisticas

    |

    | Response

    v

relatorios / visualizacoes

---

# Classificação das Comunicações

| Origem | Destino | Tipo | Descrição |
|---|---|---|---|
| aplicacao | entradaDados | Request | Solicitação de carregamento ou geração de dados |
| entradaDados | aplicacao | Response | Dados preparados |
| aplicacao | algoritmosOrdenacao | Request | Solicitação de ordenação |
| algoritmosOrdenacao | estatisticas | Event | Operações realizadas |
| estatisticas | relatorios | Response | Métricas consolidadas |
| estatisticas | visualizacoes | Response | Dados para representação gráfica |

---

# Fluxo Completo da Execução

1.

Usuário inicia aplicação.

↓

2.

Aplicacao recebe parâmetros.

↓

3.

entradaDados prepara dados.

↓

4.

Algoritmo recebe lista de entrada.

↓

5.

Algoritmo executa ordenação.

↓

6.

Eventos são produzidos.

↓

7.

estatisticas registra operações.

↓

8.

Execução finalizada.

↓

9.

ResultadoOrdenacao criado.

↓

10.

Relatório e visualização gerados.

---

# Diagrama de Classes Simplificado

ResultadoOrdenacao

    |

    | possui

    v

EstatisticasOrdenacao

    |

    | utiliza

    v

ContadorOperacoes

---

# Relacionamentos Principais

ResultadoOrdenacao:

Responsável por armazenar:

- dados ordenados;
- algoritmo utilizado;
- estatísticas;
- status da execução.

---

EstatisticasOrdenacao:

Responsável por armazenar:

- comparações;
- trocas;
- movimentações;
- tempo;
- informações de desempenho.

---

ContadorOperacoes:

Responsável por contabilizar:

- operações realizadas;
- quantidade de eventos;
- métricas acumuladas.

---

# Diagrama de Eventos

Os algoritmos não enviam métricas diretamente.

Eles produzem eventos.

Fluxo:

AlgoritmoOrdenacao

    |

    | cria

    v

EventoOrdenacao

    |

    | registra

    v

EstatisticasOrdenacao

    |

    v

Contadores Atualizados

---

# Tipos de Eventos

EventoOrdenacao

    |

    +-- COMPARACAO

    |

    +-- TROCA

    |

    +-- MOVIMENTACAO

    |

    +-- DIVISAO

    |

    +-- MESCLAGEM

    |

    +-- AJUSTE_HEAP

---

# Diagrama de Dependências

configuracoes

    |

    v

aplicacao

    |

    +----------------+

    |                |

    v                v

entradaDados   algoritmosOrdenacao

                       |

                       v

                 estatisticas

                       |

              +--------+--------+

              |                 |

              v                 v

          relatorios      visualizacoes

---

# Regras de Dependência

Os módulos devem seguir:

Módulos superiores

podem conhecer

módulos inferiores.

Porém:

Módulos inferiores

não devem depender

de módulos superiores.

---

# Dependências Permitidas

Permitido:

algoritmosOrdenacao

        |

        v

modelos


Permitido:

estatisticas

        |

        v

modelos


Permitido:

relatorios

        |

        v

estatisticas

---

# Dependências Proibidas

Não permitido:

algoritmosOrdenacao

        |

        v

visualizacoes

Motivo:

O algoritmo não deve conhecer detalhes de apresentação.

---

Não permitido:

estatisticas

        |

        v

algoritmosOrdenacao

Motivo:

Estatísticas apenas observam a execução.

---

# Arquitetura de Evolução

A arquitetura foi planejada para crescimento incremental.

V1.0

Algoritmos

+

Estatísticas básicas

+

Relatórios simples


↓

V2.0

Persistência

+

Gráficos

+

Comparações avançadas


↓

V3.0

Dashboard

+

Animações

+

Ambiente educacional completo

---

# Princípios Arquiteturais Aplicados

## Separação de Responsabilidades

Cada módulo possui função específica.

---

## Baixo Acoplamento

Os componentes comunicam-se por contratos definidos.

---

## Alta Coesão

Cada módulo concentra responsabilidades relacionadas.

---

## Extensibilidade

Novos algoritmos e métricas podem ser adicionados sem modificar componentes existentes.

---

## Observabilidade

O comportamento dos algoritmos pode ser analisado durante a execução.

---

# Arquitetura Final Consolidada

                         USUÁRIO

                            |

                            v

                       Aplicacao

                            |

        +-------------------+-------------------+

        |                   |                   |

        v                   v                   v

 entradaDados       algoritmosOrdenacao     configuracoes

                            |

                            v

                  EventosOrdenacao

                            |

                            v

                     estatisticas

                    +-------+--------+

                    |                |

                    v                v

              relatorios       visualizacoes

                    |                |

                    +-------+--------+

                            |

                            v

                     Resultado Final

---

# Considerações da Parte

Os diagramas apresentados consolidam a arquitetura definida para o módulo de estatísticas do LAB EDU SORT V1.0.

A arquitetura estabelece um fluxo claro:

Entrada

↓

Processamento

↓

Eventos

↓

Estatísticas

↓

Relatórios

↓

Visualizações

Essa organização garante que o projeto permaneça:

- modular;
- testável;
- extensível;
- educacional;
- preparado para futuras versões.

Com esta definição, o arquivo **06-modelo-estatisticas.md** possui seu modelo arquitetural completo, incluindo fundamentos, estruturas, comunicação, métricas, relatórios e diagramas.

---

# Parte X — Evolução e Considerações Finais

Esta seção apresenta a visão de evolução do modelo de estatísticas do **LAB EDU SORT V1.0**, consolidando as decisões arquiteturais tomadas e estabelecendo os caminhos futuros para expansão do projeto.

O objetivo desta parte é registrar:

- estado atual do modelo;
- limitações conhecidas;
- possibilidades de evolução;
- princípios preservados;
- conclusão do documento.

---

# Objetivo da Evolução Arquitetural

O modelo de estatísticas foi desenvolvido considerando que o LAB EDU SORT não será apenas uma implementação de algoritmos de ordenação.

A proposta é construir uma plataforma educacional capaz de demonstrar:

- funcionamento interno dos algoritmos;
- comportamento experimental;
- comparação de estratégias;
- análise de desempenho;
- visualização de conceitos de Estruturas de Dados e Algoritmos.

---

# Estado Atual da Arquitetura

Na versão V1.0, o modelo contempla:

- coleta de eventos;
- contadores de operações;
- medição de tempo;
- registro de resultados;
- geração de relatórios;
- preparação para visualizações.

Fluxo consolidado:

Execução do algoritmo

↓

Geração de eventos

↓

Coleta estatística

↓

Consolidação das métricas

↓

Geração de resultados

↓

Apresentação ao usuário

---

# Limitações Conhecidas da V1.0

A primeira versão possui algumas limitações intencionais.

Estas limitações seguem o princípio YAGNI:

"Implementar somente aquilo que é necessário para a versão atual."

---

# Limitação 01 — Persistência

Na V1.0:

- os dados permanecem em memória;
- não existe armazenamento permanente;
- não existe histórico entre execuções.

Possível evolução:

V2.0:

- arquivos de resultados;
- banco de dados;
- histórico de experimentos.

---

# Limitação 02 — Visualizações Básicas

Na V1.0:

- relatórios textuais são prioridade;
- gráficos podem ser adicionados posteriormente.

Possível evolução:

V2.0:

- gráficos estatísticos;
- comparação visual;
- exportação de imagens.

---

# Limitação 03 — Execuções Isoladas

Na V1.0:

Cada execução é analisada individualmente.

Possível evolução:

V2.0:

- execução em lote;
- múltiplos cenários;
- análise estatística agregada.

---

# Limitação 04 — Métricas Avançadas

Na V1.0:

São coletadas métricas essenciais:

- comparações;
- trocas;
- movimentações;
- tempo.

Possível evolução:

V3.0:

- análise de memória detalhada;
- profundidade de recursão;
- comportamento interno avançado.

---

# Roadmap Evolutivo

## V1.0 — Fundação Estatística

Objetivo:

Criar uma base sólida de coleta e análise.

Recursos:

- eventos;
- métricas básicas;
- relatórios;
- comparação simples.

Arquitetura:

algoritmos

↓

eventos

↓

estatisticas

↓

relatorios

---

## V2.0 — Análise Experimental

Objetivo:

Transformar execuções em experimentos comparáveis.

Recursos:

- persistência;
- gráficos;
- exportação;
- histórico;
- análise de múltiplas execuções.

Arquitetura:

execução

↓

coleta

↓

armazenamento

↓

análise

---

## V3.0 — Ambiente Educacional Completo

Objetivo:

Criar uma ferramenta completa para ensino de algoritmos.

Recursos:

- animações;
- dashboards;
- comparações interativas;
- experimentos automatizados;
- acompanhamento visual.

Arquitetura:

usuário

↓

interface

↓

motor de execução

↓

análise estatística

↓

visualização interativa

---

# Princípios Mantidos Durante a Evolução

A evolução do projeto deverá preservar os princípios definidos desde a fundação.

---

# POO Explícita

As responsabilidades devem permanecer representadas por classes.

Exemplo:

Correto:

EstatisticasOrdenacao

ContadorOperacoes

ResultadoOrdenacao


Evitar:

estruturas genéricas sem responsabilidade definida.

---

# DRY

Não duplicar:

- regras de cálculo;
- validações;
- estruturas;
- lógica de processamento.

Cada responsabilidade deve possuir uma única implementação.

---

# YAGNI

Novos recursos somente devem ser adicionados quando houver necessidade real.

Evitar antecipação de complexidade.

Exemplo:

Não criar:

- banco de dados;
- dashboards;
- APIs;

antes da necessidade arquitetural.

---

# Baixo Acoplamento

Novas funcionalidades devem ser adicionadas sem modificar componentes existentes.

Exemplo:

Adicionar um novo algoritmo:

NovoAlgoritmo

↓

Eventos

↓

Estatisticas

Sem alterar o módulo estatístico.

---

# Alta Coesão

Cada módulo deve continuar responsável por seu próprio domínio.

Exemplo:

algoritmosOrdenacao:

executa algoritmos.


estatisticas:

mede comportamento.


visualizacoes:

apresenta informações.

---

# Pontos de Extensão Futuros

O modelo atual permite evolução através de:

---

# Novos Algoritmos

Adicionar:

- Counting Sort;
- Radix Sort;
- Shell Sort;
- Tim Sort.

Sem alterar:

- estatísticas;
- relatórios;
- visualizações.

---

# Novas Métricas

Adicionar:

- número de chamadas recursivas;
- profundidade máxima;
- consumo de memória;
- movimentações internas.

---

# Novas Interfaces

Adicionar:

- interface gráfica;
- aplicação web;
- dashboard;
- API.

---

# Novos Formatos de Saída

Adicionar:

- JSON;
- CSV;
- XML;
- banco de dados.

---

# Avaliação Final da Arquitetura

O modelo de estatísticas definido para o LAB EDU SORT V1.0 atende aos objetivos estabelecidos no Milestone 02.

Foram definidos:

- modelo conceitual;
- estruturas estatísticas;
- classes responsáveis;
- contratos de comunicação;
- eventos;
- métricas;
- relatórios;
- visualizações;
- evolução arquitetural.

---

# Fluxo Arquitetural Final

Usuário

↓

Aplicacao

↓

Entrada de Dados

↓

Algoritmo de Ordenação

↓

Eventos de Execução

↓

Módulo Estatístico

↓

Relatórios

↓

Visualizações

↓

Análise Educacional

---

# Considerações Finais

O modelo de estatísticas do LAB EDU SORT V1.0 estabelece uma base arquitetural organizada, extensível e alinhada aos objetivos educacionais do projeto.

A principal decisão arquitetural foi separar:

Execução

de

Observação

permitindo que os algoritmos permaneçam independentes enquanto suas características de desempenho são analisadas.

Com isso, o projeto deixa de ser apenas uma coleção de algoritmos de ordenação e passa a representar um ambiente de estudo capaz de demonstrar:

- funcionamento interno;
- comportamento experimental;
- análise comparativa;
- conceitos de complexidade.

O modelo definido neste documento servirá como referência para as próximas etapas do projeto, especialmente:

- implementação das classes;
- criação dos algoritmos;
- desenvolvimento das interfaces;
- construção dos relatórios;
- implementação das visualizações.

O Milestone 02 é considerado concluído com a definição completa do modelo de dados, estruturas, contratos e arquitetura estatística do LAB EDU SORT V1.0.

---
