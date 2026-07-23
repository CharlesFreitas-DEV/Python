# Índice

## Parte I — Fundamentos das Estruturas de Dados

1. [Objetivo](#objetivo)

2. [Escopo](#escopo)

3. [Papel das Estruturas de Dados na Arquitetura](#papel-das-estruturas-de-dados-na-arquitetura)

4. [Princípios Adotados](#princípios-adotados)

   4.1. [Adequação ao Domínio](#adequação-ao-domínio)

   4.2. [Simplicidade](#simplicidade)

   4.3. [Desempenho](#desempenho)

   4.4. [Legibilidade](#legibilidade)

   4.5. [Manutenibilidade](#manutenibilidade)

---

# Parte II — Catálogo das Estruturas de Dados

## Estruturas Lineares

1. [Lista (`list`)](#lista-list)

2. [Deque (`deque`)](#deque-deque)

3. [Pilha (`stack`)](#pilha-stack)

4. [Fila (`queue`)](#fila-queue)

---

## Estruturas Associativas

5. [Dicionário (`dict`)](#dicionário-dict)

6. [Conjunto (`set`)](#conjunto-set)

---

## Estruturas de Controle e Modelagem

7. [Dataclass](#dataclass)

8. [Enum](#enum)

9. [NamedTuple](#namedtuple)

---

## Estruturas Hierárquicas

10. [Heap Binária](#heap-binária)

11. [Árvores (futuro)](#árvores-futuro)

12. [Grafos (futuro)](#grafos-futuro)

---

# Parte III — Estruturas por Módulo

## Aplicação

- [Estruturas utilizadas pelo módulo aplicacao](#estruturas-utilizadas-pelo-módulo-aplicacao)

## Entrada de Dados

- [Estruturas utilizadas pelo módulo entradaDados](#estruturas-utilizadas-pelo-módulo-entradadados)

## Algoritmos de Ordenação

- [Estruturas utilizadas pelo módulo algoritmosOrdenacao](#estruturas-utilizadas-pelo-módulo-algoritmosordenacao)

## Estatísticas

- [Estruturas utilizadas pelo módulo estatisticas](#estruturas-utilizadas-pelo-módulo-estatisticas)

## Visualizações

- [Estruturas utilizadas pelo módulo visualizacoes](#estruturas-utilizadas-pelo-módulo-visualizacoes)

## Validações

- [Estruturas utilizadas pelo módulo validacoes](#estruturas-utilizadas-pelo-módulo-validacoes)

## Utilitários

- [Estruturas utilizadas pelo módulo utilitarios](#estruturas-utilizadas-pelo-módulo-utilitarios)

---

# Parte IV — Estruturas Específicas dos Algoritmos

1. [Vetores e Listas Sequenciais](#vetores-e-listas-sequenciais)

2. [Sublistas e Partições](#sublistas-e-partições)

3. [Estruturas Auxiliares Temporárias](#estruturas-auxiliares-temporárias)

4. [Pilha de Recursão](#pilha-de-recursão)

5. [Estruturas para Algoritmos Específicos](#estruturas-para-algoritmos-específicos)

---

# Parte V — Critérios de Escolha

1. [Complexidade Computacional](#complexidade-computacional)

2. [Consumo de Memória](#consumo-de-memória)

3. [Mutabilidade](#mutabilidade)

4. [Localidade de Memória](#localidade-de-memória)

5. [Facilidade de Ensino](#facilidade-de-ensino)

6. [Extensibilidade](#extensibilidade)

---

# Parte VI — Arquitetura das Estruturas

1. [Mapa Geral das Estruturas](#mapa-geral-das-estruturas)

2. [Matriz Estrutura × Módulo](#matriz-estrutura-módulo)

3. [Fluxo de Dados da Aplicação](#fluxo-de-dados-da-aplicação)

4. [Dependências entre Estruturas](#dependências-entre-estruturas)

---

# Parte VII — Evolução e Considerações Finais

1. [Regras de Evolução](#regras-de-evolução)

2. [Estruturas Planejadas para Versões Futuras](#estruturas-planejadas-para-versões-futuras)

3. [Boas Práticas](#boas-práticas)

4. [Considerações Finais](#considerações-finais)

---

# Catálogo Rápido das Estruturas

## Lineares

- [list](#lista-list)
- [deque](#deque-deque)
- [stack](#pilha-stack)
- [queue](#fila-queue)

## Associativas

- [dict](#dicionário-dict)
- [set](#conjunto-set)

## Modelagem

- [dataclass](#dataclass)
- [Enum](#enum)
- [NamedTuple](#namedtuple)

## Hierárquicas

- [Heap Binária](#heap-binária)
- [Árvores](#árvores-futuro)
- [Grafos](#grafos-futuro)

---

# Estruturas de Dados

## Projeto

**LAB EDU SORT V1.0**

---

# Parte I — Fundamentos das Estruturas de Dados

# Objetivo

Este documento define as estruturas de dados utilizadas pelo **LAB EDU SORT V1.0**, estabelecendo quais estruturas serão adotadas, suas responsabilidades dentro da arquitetura e os critérios utilizados para sua escolha.

O objetivo principal é documentar:

- quais estruturas representam os dados manipulados pela aplicação;
- quais estruturas são utilizadas internamente pelos módulos;
- quais estruturas auxiliam a execução dos algoritmos de ordenação;
- quais estruturas serão utilizadas para comunicação entre componentes;
- quais decisões arquiteturais justificam cada escolha.

Este documento não apresenta implementação de código.

Seu objetivo é definir as decisões estruturais que deverão orientar o desenvolvimento da biblioteca.

---

# Escopo

Este documento contempla:

- estruturas de dados utilizadas pelo domínio;
- estruturas internas dos módulos;
- estruturas auxiliares dos algoritmos;
- estruturas utilizadas para armazenamento temporário;
- critérios de escolha das estruturas;
- relacionamentos entre estruturas e módulos;
- possibilidades de evolução futura.

Não fazem parte deste documento:

- implementação dos algoritmos de ordenação;
- detalhes de sintaxe da linguagem Python;
- otimizações específicas de baixo nível;
- benchmarking dos algoritmos.

---

# Papel das Estruturas de Dados na Arquitetura

As estruturas de dados representam a camada responsável pela organização, armazenamento e manipulação das informações utilizadas pela biblioteca.

Enquanto o **Modelo de Classes** define os objetos do domínio, este documento define como esses objetos e suas informações serão representados internamente.

A relação entre os documentos arquiteturais é:

```text
Modelo Conceitual

        │

        ▼

Modelo de Classes

        │

        ▼

Estruturas de Dados

        │

        ▼

Implementação dos Módulos
```

---

# Princípios Adotados

A escolha das estruturas de dados do **LAB EDU SORT V1.0** segue princípios arquiteturais que priorizam equilíbrio entre simplicidade, desempenho e valor educacional.

---

# Adequação ao Domínio

A estrutura escolhida deverá representar corretamente o conceito que está sendo modelado.

Exemplo:

- conjuntos ordenáveis utilizam estruturas sequenciais;
- configurações utilizam estruturas associativas;
- eventos utilizam objetos imutáveis;
- estatísticas utilizam estruturas agregadoras.

---

# Simplicidade

O projeto possui finalidade educacional e deve priorizar estruturas claras e compreensíveis.

Estruturas excessivamente complexas deverão ser utilizadas apenas quando houver justificativa arquitetural.

---

# Desempenho

As estruturas escolhidas deverão permitir execução eficiente dos algoritmos de ordenação.

Serão considerados:

- tempo de acesso;
- custo de inserção;
- custo de remoção;
- consumo de memória;
- comportamento durante grandes volumes de dados.

---

# Legibilidade

A estrutura utilizada deve favorecer a compreensão do código.

Uma solução mais simples e legível deverá ser priorizada quando a diferença de desempenho não for significativa.

---

# Manutenibilidade

As estruturas devem facilitar:

- evolução da biblioteca;
- criação de novos algoritmos;
- testes automatizados;
- reutilização dos componentes.

---

# Classificação Geral das Estruturas

As estruturas utilizadas pelo projeto são classificadas em categorias.

```text
Estruturas de Dados

│

├── Lineares

│     ├── list

│     ├── deque

│     ├── stack

│     └── queue

│

├── Associativas

│     ├── dict

│     └── set

│

├── Modelagem de Dados

│     ├── dataclass

│     ├── Enum

│     └── NamedTuple

│

└── Hierárquicas

      ├── heap

      ├── árvores (futuro)

      └── grafos (futuro)
```

---

# Papel das Estruturas no LAB EDU SORT

As estruturas possuem diferentes papéis dentro da arquitetura.

```text
Entrada de Dados

        │

        ▼

list

        │

        ▼

ConjuntoDados

        │

        ▼

Algoritmos de Ordenação

        │

        ├────────► list auxiliar

        │

        ├────────► stack de recursão

        │

        └────────► heap (algoritmos específicos)

        │

        ▼

ResultadoOrdenacao

        │

        ▼

Estatísticas e Visualizações
```

---

# Regras Gerais de Utilização

As estruturas de dados deverão seguir as seguintes regras:

- nenhuma estrutura interna deverá substituir os objetos do domínio;
- módulos deverão comunicar-se utilizando os contratos definidos;
- estruturas temporárias deverão permanecer restritas ao módulo responsável;
- novas estruturas deverão possuir justificativa arquitetural;
- estruturas escolhidas deverão estar documentadas neste arquivo.

---

# Decisões Arquiteturais Iniciais

As principais decisões definidas para a V1.0 são:

| Necessidade | Estrutura escolhida |
|-------------|---------------------|
| Dados de entrada | list |
| Dados ordenados | list |
| Configurações | dataclass + Enum |
| Estatísticas | dataclass |
| Eventos | dataclass |
| Mapeamentos | dict |
| Controle de estados | Enum |
| Operações FIFO/LIFO futuras | deque |

---

# Considerações Iniciais

As estruturas de dados definidas neste documento representam a base interna do **LAB EDU SORT V1.0**.

A escolha das estruturas busca equilibrar três objetivos principais:

- qualidade arquitetural;
- clareza de implementação;
- valor educacional.

Nas próximas partes serão detalhadas individualmente as estruturas utilizadas, seus objetivos, características, responsabilidades e aplicações dentro dos módulos da biblioteca.

---

# Parte II — Catálogo das Estruturas de Dados

Esta seção apresenta o catálogo das estruturas de dados utilizadas pelo **LAB EDU SORT V1.0**.

Cada estrutura é descrita considerando:

- objetivo;
- características principais;
- comportamento computacional;
- utilização dentro da arquitetura;
- justificativa da escolha;
- possibilidades de evolução.

As estruturas apresentadas nesta seção foram selecionadas considerando os princípios definidos na Parte I:

- simplicidade;
- legibilidade;
- desempenho;
- manutenibilidade;
- valor educacional.

---

# Estruturas Lineares

As estruturas lineares organizam seus elementos em uma sequência lógica.

Cada elemento possui uma posição definida dentro da estrutura, permitindo percorrer os dados de forma ordenada.

No **LAB EDU SORT V1.0**, as estruturas lineares são fundamentais porque os algoritmos de ordenação trabalham principalmente sobre coleções sequenciais.

---

# Lista (`list`)

## Objetivo

Representar coleções ordenáveis de elementos.

A estrutura `list` é a principal estrutura utilizada pelo projeto para armazenamento dos dados manipulados pelos algoritmos de ordenação.

---

## Características

A lista Python possui:

- tamanho dinâmico;
- acesso por índice;
- ordenação dos elementos;
- possibilidade de alteração dos valores;
- suporte a múltiplos tipos de elementos.

---

## Complexidade Principal

| Operação | Complexidade |
|----------|--------------|
| Acesso por índice | O(1) |
| Busca | O(n) |
| Inserção no final | O(1) amortizado |
| Inserção no meio | O(n) |
| Remoção | O(n) |

---

## Utilização no Projeto

A estrutura `list` será utilizada para:

- representar os dados de entrada;
- armazenar conjuntos de elementos;
- representar listas parcialmente ordenadas;
- armazenar resultados dos algoritmos.

Relacionamento:

```text
entradaDados

      │

      ▼

ConjuntoDados

      │

      ▼

list[int]

      │

      ▼

algoritmosOrdenacao
```

---

## Justificativa Arquitetural

A escolha da `list` ocorre porque:

- corresponde ao conceito matemático de vetor/lista sequencial;
- é a estrutura natural para ensino de algoritmos de ordenação;
- possui excelente suporte na linguagem Python;
- permite implementação direta dos algoritmos clássicos.

---

# Deque (`deque`)

## Objetivo

Representar estruturas onde inserções e remoções nas extremidades são frequentes.

---

## Características

A estrutura `deque` fornece:

- inserção rápida no início;
- inserção rápida no final;
- remoção eficiente nas extremidades;
- comportamento semelhante a fila dupla.

---

## Complexidade Principal

| Operação | Complexidade |
|----------|--------------|
| Inserção início | O(1) |
| Inserção final | O(1) |
| Remoção início | O(1) |
| Remoção final | O(1) |

---

## Utilização no Projeto

Na V1.0, será utilizada principalmente para:

- estruturas auxiliares futuras;
- simulação de filas;
- processamento de eventos.

Possíveis utilizações futuras:

```text
Eventos

      │

      ▼

deque

      │

      ▼

Processamento sequencial
```

---

## Justificativa Arquitetural

Apesar de não ser necessária para os algoritmos básicos de ordenação, sua utilização futura permite representar estruturas reais de processamento.

---

# Pilha (`stack`)

## Objetivo

Representar uma estrutura baseada no princípio:

```text
LIFO

Last In, First Out
```

O último elemento inserido é o primeiro removido.

---

## Características

Operações principais:

- empilhar;
- desempilhar;
- consultar topo.

---

## Implementação prevista

No projeto, a pilha será representada utilizando:

```python
list
```

ou

```python
deque
```

dependendo do contexto.

---

## Utilização no Projeto

Será utilizada principalmente para representar:

- controle de chamadas recursivas;
- simulação de execução de algoritmos;
- estruturas auxiliares.

Exemplo:

```text
QuickSort

      │

      ▼

Pilha de chamadas

      │

      ▼

Subproblemas pendentes
```

---

## Justificativa Arquitetural

A pilha possui forte relação conceitual com algoritmos recursivos, sendo importante tanto tecnicamente quanto pedagogicamente.

---

# Fila (`queue`)

## Objetivo

Representar estruturas baseadas no princípio:

```text
FIFO

First In, First Out
```

---

## Características

Operações principais:

- inserir no final;
- remover no início;
- processar em ordem de chegada.

---

## Implementação prevista

A implementação recomendada será:

```python
deque
```

---

## Utilização no Projeto

Possíveis utilizações futuras:

- processamento de eventos;
- filas de execução;
- simulações.

---

## Justificativa Arquitetural

Permite futuras expansões envolvendo processamento assíncrono ou simulação de execução.

---

# Estruturas Associativas

As estruturas associativas armazenam dados relacionados a chaves ou conjuntos.

São utilizadas principalmente para configuração, controle e organização de informações auxiliares.

---

# Dicionário (`dict`)

## Objetivo

Representar associações entre chave e valor.

---

## Características

Possui:

- acesso rápido por chave;
- estrutura dinâmica;
- armazenamento de pares chave/valor.

---

## Complexidade Principal

| Operação | Complexidade média |
|----------|--------------------|
| Busca | O(1) |
| Inserção | O(1) |
| Remoção | O(1) |

---

## Utilização no Projeto

Será utilizado para:

- configurações carregadas;
- tabelas de parâmetros;
- mapeamento de algoritmos;
- associação de estatísticas.

Exemplo:

```text
algoritmos

{

"bubbleSort": ClasseBubbleSort,

"quickSort": ClasseQuickSort

}
```

---

## Justificativa Arquitetural

O `dict` reduz acoplamento quando é necessário localizar componentes dinamicamente.

---

# Conjunto (`set`)

## Objetivo

Representar coleções únicas de elementos.

---

## Características

Possui:

- ausência de duplicidade;
- busca eficiente;
- operações matemáticas de conjunto.

---

## Complexidade Principal

| Operação | Complexidade média |
|----------|--------------------|
| Busca | O(1) |
| Inserção | O(1) |

---

## Utilização no Projeto

Possíveis usos:

- validação de opções permitidas;
- controle de algoritmos disponíveis;
- verificação de elementos únicos.

---

## Justificativa Arquitetural

Utilizado quando a prioridade é unicidade e consulta rápida.

---

# Estruturas de Modelagem

Essas estruturas representam objetos conceituais utilizados pelo domínio.

---

# Dataclass

## Objetivo

Representar classes simples de dados.

---

## Características

Fornece:

- criação simplificada de classes;
- comparação automática;
- representação textual;
- imutabilidade opcional.

---

## Utilização no Projeto

Será utilizada em:

- classes do domínio;
- eventos;
- estatísticas;
- configurações.

Exemplo:

```text
ConfiguracaoExecucao

EventoOrdenacao

EstatisticasOrdenacao
```

---

## Justificativa Arquitetural

As classes do Modelo Canônico possuem predominantemente características de dados, tornando `dataclass` uma escolha natural.

---

# Enum

## Objetivo

Representar conjuntos fixos de valores.

---

## Utilização no Projeto

Será utilizado para:

- tipos de entrada;
- algoritmos disponíveis;
- formatos de visualização;
- estados de execução.

Exemplo:

```text
TipoEntrada

ARQUIVO

GERADO
```

---

## Justificativa Arquitetural

Evita utilização de strings livres e reduz erros de configuração.

---

# NamedTuple

## Objetivo

Representar pequenos objetos imutáveis.

---

## Utilização no Projeto

Possíveis usos:

- retorno simples;
- registros temporários;
- informações auxiliares.

---

## Justificativa Arquitetural

Será utilizado apenas quando uma estrutura simples e imutável for suficiente.

---

# Estruturas Hierárquicas

Estas estruturas não são essenciais para a V1.0, mas possuem importância conceitual e poderão ser incorporadas futuramente.

---

# Heap Binária

## Objetivo

Representar uma árvore completa especializada em operações de prioridade.

---

## Utilização no Projeto

Possível utilização futura:

- implementação do HeapSort;
- filas de prioridade;
- análise de estruturas avançadas.

---

## Justificativa Arquitetural

Permite explorar algoritmos de ordenação baseados em estruturas não lineares.

---

# Árvores (Futuro)

## Objetivo

Representar estruturas hierárquicas.

---

## Possíveis utilizações

- árvores de decisão;
- árvores balanceadas;
- estruturas avançadas de busca.

---

## Versão prevista

Pós V1.0.

---

# Grafos (Futuro)

## Objetivo

Representar relacionamentos complexos entre elementos.

---

## Possíveis utilizações

- dependências;
- redes;
- visualizações avançadas.

---

## Versão prevista

Pós V1.0.

---

# Resumo do Catálogo

| Estrutura | Categoria | Uso na V1.0 |
|-----------|-----------|-------------|
| list | Linear | Principal |
| deque | Linear | Futuro/Auxiliar |
| stack | Linear | Recursão |
| queue | Linear | Futuro |
| dict | Associativa | Configurações e mapas |
| set | Associativa | Validações |
| dataclass | Modelagem | Domínio |
| Enum | Modelagem | Estados |
| NamedTuple | Modelagem | Auxiliares |
| heap | Hierárquica | Futuro |
| árvore | Hierárquica | Futuro |
| grafo | Hierárquica | Futuro |

---

# Considerações da Categoria

O catálogo definido nesta seção estabelece as estruturas fundamentais utilizadas pelo **LAB EDU SORT V1.0**.

A arquitetura prioriza estruturas simples e bem conhecidas, adequadas ao objetivo educacional do projeto, sem comprometer a possibilidade de evolução para estruturas mais avançadas em versões futuras.

A separação entre estruturas principais, auxiliares e futuras permite que a biblioteca evolua gradualmente mantendo clareza arquitetural e consistência com os objetivos do projeto.

---

# Parte III — Estruturas utilizadas por cada módulo

Esta seção apresenta o relacionamento entre os módulos arquiteturais do **LAB EDU SORT V1.0** e as estruturas de dados utilizadas internamente por cada componente.

O objetivo desta parte é documentar:

- quais estruturas cada módulo utiliza;
- qual a finalidade dessas estruturas;
- como elas participam do fluxo da aplicação;
- quais decisões arquiteturais justificam sua utilização.

A definição das estruturas segue os princípios estabelecidos nas partes anteriores:

- responsabilidade única;
- baixo acoplamento;
- clareza arquitetural;
- facilidade de manutenção;
- valor educacional.

---

# Visão Geral

A relação entre módulos e estruturas pode ser representada da seguinte forma:

```text
                     aplicacao

                         │

                         ▼

                 entradaDados

                         │

                         ▼

                  ConjuntoDados

                         │

                         ▼

              algoritmosOrdenacao

                         │

          ┌──────────────┼──────────────┐

          ▼              ▼              ▼

      eventos       estatisticas   visualizacoes

          │              │              │

          ▼              ▼              ▼

       dataclass      dataclass       dict/list

```

---

# Módulo: aplicacao

## Objetivo do módulo

O módulo `aplicacao` representa o ponto de entrada da biblioteca.

Sua responsabilidade é coordenar a execução geral do sistema, recebendo solicitações do usuário ou de outros componentes.

---

# Estruturas utilizadas

| Estrutura | Finalidade |
|-----------|------------|
| dict | Mapeamento de opções e comandos |
| Enum | Controle de estados da aplicação |
| dataclass | Representação de parâmetros de execução |

---

# dict

## Utilização

O dicionário será utilizado para:

- registrar opções disponíveis;
- associar comandos às ações correspondentes;
- localizar algoritmos dinamicamente.

Exemplo conceitual:

```text
{

"bubble": BubbleSort,

"quick": QuickSort,

"merge": MergeSort

}
```

---

## Justificativa

O uso de `dict` permite:

- extensibilidade;
- carregamento dinâmico;
- redução de condicionais extensos.

---

# Enum

## Utilização

Representar estados controlados:

```text
EstadoAplicacao

INICIANDO

EXECUTANDO

FINALIZADO

ERRO
```

---

## Justificativa

Evita estados representados por strings livres.

---

# dataclass

## Utilização

Representar informações de execução:

```text
ParametrosExecucao
```

---

## Justificativa

Mantém os dados de configuração organizados e tipados.

---

# Módulo: entradaDados

## Objetivo do módulo

Responsável por obter, validar inicialmente e preparar os dados utilizados pela aplicação.

---

# Estruturas utilizadas

| Estrutura | Finalidade |
|-----------|------------|
| list | Armazenamento dos elementos |
| dict | Dados temporários de leitura |
| Enum | Origem dos dados |
| dataclass | Modelo dos dados |

---

# list

## Utilização

Representa a coleção principal:

```text
[5, 2, 8, 1, 3]
```

---

## Justificativa

Os algoritmos de ordenação da V1.0 trabalham principalmente sobre listas sequenciais.

---

# dict

## Utilização

Pode representar dados intermediários:

```text
{

"arquivo": "entrada.csv",

"quantidade": 1000

}
```

---

## Justificativa

Facilita manipulação temporária durante leitura e conversão.

---

# Enum

## Utilização

Representar origem:

```text
OrigemDados

ARQUIVO

GERACAO_AUTOMATICA
```

---

# dataclass

## Utilização

Produzir:

```text
ConjuntoDados
```

---

# Módulo: algoritmosOrdenacao

## Objetivo do módulo

Implementar os algoritmos responsáveis pelo processamento dos dados.

---

# Estruturas utilizadas

| Estrutura | Finalidade |
|-----------|------------|
| list | Estrutura principal de ordenação |
| list auxiliar | Processamento temporário |
| stack | Controle recursivo |
| heap | Algoritmos específicos |

---

# list

## Utilização

Representa os dados em processamento.

Exemplo:

```text
dados = [8,4,2,9,1]
```

---

## Justificativa

A maioria dos algoritmos clássicos trabalha sobre estruturas sequenciais.

Exemplos:

- Bubble Sort;
- Selection Sort;
- Insertion Sort;
- Merge Sort;
- Quick Sort.

---

# Listas auxiliares

## Utilização

Algoritmos como Merge Sort podem criar estruturas temporárias.

Exemplo:

```text
lista_original

        │

        ▼

lista_esquerda

lista_direita
```

---

## Justificativa

Permitem dividir problemas sem alterar os dados originais.

---

# Stack

## Utilização

Representar chamadas pendentes.

Exemplo:

```text
QuickSort

        │

        ▼

Pilha de subproblemas
```

---

## Justificativa

Relaciona diretamente a execução dos algoritmos recursivos com estruturas de dados.

---

# Heap

## Utilização

Prevista para algoritmos baseados em prioridade.

Exemplo:

```text
HeapSort
```

---

# Módulo: estatisticas

## Objetivo do módulo

Responsável por coletar, consolidar e disponibilizar métricas da execução.

---

# Estruturas utilizadas

| Estrutura | Finalidade |
|-----------|------------|
| dataclass | Modelos estatísticos |
| dict | Acúmulo de métricas |
| list | Histórico de eventos |

---

# dataclass

## Utilização

Representar:

```text
EstatisticasOrdenacao

EstatisticasOperacoes

EstatisticasTempo
```

---

## Justificativa

As estatísticas possuem estrutura fixa e conhecida.

---

# dict

## Utilização

Mapear contadores:

```text
{

"comparacoes": 100,

"trocas": 20

}
```

---

## Justificativa

Facilita agregação dinâmica.

---

# list

## Utilização

Armazenar histórico de eventos:

```text
[
 Evento1,
 Evento2,
 Evento3
]
```

---

## Justificativa

Mantém ordem cronológica das operações.

---

# Módulo: visualizacoes

## Objetivo do módulo

Transformar resultados e estatísticas em representações visuais.

---

# Estruturas utilizadas

| Estrutura | Finalidade |
|-----------|------------|
| list | Séries de dados |
| dict | Configurações de gráficos |
| dataclass | Modelos de saída |

---

# list

## Utilização

Representar sequências:

```text
dadosOrdenados
```

---

# dict

## Utilização

Configurar visualizações:

```text
{

"titulo": "Bubble Sort",

"tipo": "barra"

}
```

---

## Justificativa

Permite extensão de formatos sem alteração estrutural.

---

# dataclass

## Utilização

Representar:

```text
ConfiguracaoVisualizacao

ResultadoVisualizacao
```

---

# Módulo: validacoes

## Objetivo do módulo

Centralizar regras de validação dos dados e parâmetros.

---

# Estruturas utilizadas

| Estrutura | Finalidade |
|-----------|------------|
| set | Valores permitidos |
| dict | Regras de validação |
| Enum | Estados válidos |

---

# set

## Utilização

Exemplo:

```text
{

"bubble",

"quick",

"merge"

}
```

---

## Justificativa

Busca rápida e garantia de unicidade.

---

# dict

## Utilização

Representar regras:

```text
{

"quantidade": regraQuantidade,

"tipo": regraTipo

}
```

---

# Enum

## Utilização

Representar estados aceitos.

---

# Módulo: utilitarios

## Objetivo do módulo

Fornecer funções auxiliares compartilhadas.

---

# Estruturas utilizadas

| Estrutura | Finalidade |
|-----------|------------|
| list | Manipulação genérica |
| dict | Conversões |
| tuple | Retornos imutáveis |

---

# list

## Utilização

Funções auxiliares sobre coleções.

---

# dict

## Utilização

Conversões e mapeamentos.

---

# tuple

## Utilização

Retornos simples:

```text
(valor, sucesso)
```

---

# Matriz Geral — Módulo × Estrutura

| Módulo | list | dict | set | Enum | dataclass | deque | heap |
|-|-|-|-|-|-|-|-|
| aplicacao | ✓ | ✓ | | ✓ | ✓ | | |
| entradaDados | ✓ | ✓ | | ✓ | ✓ | | |
| algoritmosOrdenacao | ✓ | | | | | ✓ | ✓ |
| estatisticas | ✓ | ✓ | | | ✓ | | |
| visualizacoes | ✓ | ✓ | | | ✓ | | |
| validacoes | | ✓ | ✓ | ✓ | | | |
| utilitarios | ✓ | ✓ | | | | | |

---

# Considerações da Categoria

O mapeamento apresentado nesta seção estabelece uma relação clara entre responsabilidades dos módulos e estruturas utilizadas.

A arquitetura evita que estruturas sejam escolhidas apenas por conveniência de implementação.

Cada escolha possui uma justificativa relacionada a:

- domínio do problema;
- características do algoritmo;
- facilidade de manutenção;
- objetivo educacional.

Esse modelo permite que novas estruturas sejam incorporadas futuramente sem comprometer os contratos existentes entre os módulos.

A próxima seção apresentará as **estruturas específicas utilizadas pelos algoritmos de ordenação**, detalhando vetores, sublistas, estruturas auxiliares, pilha de recursão e estruturas avançadas previstas para evolução.

---

# Parte IV — Estruturas Específicas dos Algoritmos

Esta seção apresenta as estruturas de dados utilizadas especificamente pelos algoritmos de ordenação implementados ou planejados para o **LAB EDU SORT V1.0**.

Enquanto as partes anteriores apresentaram as estruturas sob a perspectiva arquitetural dos módulos, esta seção analisa as estruturas considerando o comportamento interno dos algoritmos.

O objetivo é documentar:

- quais estruturas cada algoritmo utiliza;
- por que determinada estrutura foi escolhida;
- como ocorre a manipulação dos dados durante a execução;
- quais impactos existem em desempenho e memória.

---

# Visão Geral

Os algoritmos de ordenação trabalham principalmente sobre estruturas sequenciais.

A representação principal adotada é:

```text
ConjuntoDados

        │

        ▼

list[int]

        │

        ▼

Algoritmo de Ordenação

        │

        ├────────► Estruturas auxiliares

        │

        └────────► ResultadoOrdenacao
```

---

# Estrutura Principal: Lista Sequencial (`list`)

## Objetivo

Representar a coleção de elementos submetida ao algoritmo de ordenação.

É a estrutura padrão utilizada pelos algoritmos da V1.0.

---

# Representação Conceitual

```text
Índice:

 0     1     2     3     4

[ 8 ] [ 3 ] [ 5 ] [ 1 ] [ 9 ]

```

Cada elemento possui:

- posição;
- valor;
- possibilidade de troca ou movimentação.

---

# Características

A lista sequencial fornece:

- acesso direto por índice;
- alteração dos elementos;
- movimentação eficiente dentro da estrutura;
- compatibilidade com algoritmos clássicos.

---

# Utilização nos Algoritmos

A estrutura `list` será utilizada por:

- Bubble Sort;
- Selection Sort;
- Insertion Sort;
- Merge Sort;
- Quick Sort;
- Heap Sort.

---

# Justificativa Arquitetural

A escolha da lista sequencial ocorre porque:

- representa naturalmente um vetor;
- facilita a visualização dos algoritmos;
- permite acompanhar comparações e trocas;
- é adequada para ensino de análise de complexidade.

---

# Estruturas Auxiliares Temporárias

Alguns algoritmos necessitam criar estruturas auxiliares durante a execução.

Essas estruturas existem apenas durante o processamento.

---

# Cópia Auxiliar da Lista

## Objetivo

Preservar uma versão original dos dados ou permitir processamento independente.

---

# Utilização

Exemplo:

```text
Lista Original

[8,3,5,1,9]


        │

        ▼


Lista Auxiliar

[8,3,5,1,9]
```

---

# Algoritmos que utilizam

Principalmente:

- Merge Sort;
- testes comparativos;
- benchmarking.

---

# Justificativa

Permite:

- comparação entre execuções;
- repetição dos testes;
- preservação dos dados originais.

---

# Sublistas e Partições

## Objetivo

Representar divisões temporárias da coleção principal.

---

# Utilização no Merge Sort

O Merge Sort divide o problema em partes menores:

```text
Lista original

[8,3,5,1,9,2]

        │

        ▼

[8,3,5]

[1,9,2]

        │

        ▼

sublistas menores
```

---

# Utilização no Quick Sort

O Quick Sort utiliza partições:

```text
[8,3,5,1,9]

        │

        ▼

Pivot = 5


Menores:

[3,1]


Maiores:

[8,9]
```

---

# Estrutura utilizada

A implementação prevista utilizará:

```python
list
```

---

# Justificativa

A utilização de listas auxiliares mantém o código:

- simples;
- didático;
- fácil de testar.

---

# Estrutura de Controle: Pilha de Recursão

## Objetivo

Representar o controle de execução dos algoritmos recursivos.

---

# Conceito

Cada chamada recursiva adiciona uma nova camada:

```text
QuickSort

       chamada inicial

             │

             ▼

        sublista esquerda

             │

             ▼

        sublista direita
```

Internamente:

```text
Topo

│
│ chamada atual
│
│ chamada anterior
│
│ chamada inicial
│

Base
```

---

# Algoritmos relacionados

- Quick Sort;
- Merge Sort.

---

# Implementação

A linguagem Python controla automaticamente a pilha de chamadas.

Porém, uma implementação iterativa poderá utilizar:

```python
list
```

ou

```python
deque
```

---

# Justificativa

A documentação dessa estrutura é importante porque permite relacionar:

- recursividade;
- memória;
- análise de complexidade.

---

# Estruturas Específicas por Algoritmo

---

# Bubble Sort

## Estruturas utilizadas

```text
list principal
```

---

## Funcionamento

O algoritmo percorre a lista comparando elementos adjacentes.

Exemplo:

```text
[5,3,8,1]

comparação

5 > 3

troca

[3,5,8,1]
```

---

## Estruturas auxiliares

Não utiliza estruturas adicionais relevantes.

---

## Características

Memória auxiliar:

```text
O(1)
```

---

# Selection Sort

## Estruturas utilizadas

```text
list principal
```

---

## Funcionamento

Seleciona o menor elemento restante.

Exemplo:

```text
[5,3,8,1]

menor = 1

troca

[1,3,8,5]
```

---

## Estruturas auxiliares

Utiliza apenas variáveis temporárias.

---

## Memória auxiliar

```text
O(1)
```

---

# Insertion Sort

## Estruturas utilizadas

```text
list principal
```

---

## Funcionamento

Constrói gradualmente uma sequência ordenada.

Exemplo:

```text
[5,3,8]

insere 3 antes de 5

[3,5,8]
```

---

## Estruturas auxiliares

Utiliza:

- variável temporária;
- índices auxiliares.

---

## Memória auxiliar

```text
O(1)
```

---

# Merge Sort

## Estruturas utilizadas

```text
list principal

listas auxiliares

sublistas
```

---

# Funcionamento

Processo:

```text
Dividir

      │

      ▼

Ordenar partes

      │

      ▼

Mesclar
```

---

# Estruturas auxiliares

Necessita:

- listas temporárias;
- estruturas intermediárias.

---

# Memória auxiliar

```text
O(n)
```

---

# Justificativa

O uso de listas auxiliares simplifica a implementação e facilita a demonstração do algoritmo.

---

# Quick Sort

## Estruturas utilizadas

```text
list principal

sublistas

pilha de recursão
```

---

# Funcionamento

Processo:

```text
Escolher pivô

       │

       ▼

Particionar

       │

       ▼

Ordenar partes
```

---

# Estruturas auxiliares

Pode utilizar:

- índices;
- variáveis temporárias;
- pilha de chamadas.

---

# Memória auxiliar

Implementação recursiva:

```text
O(log n) médio
```

Pior caso:

```text
O(n)
```

---

# Heap Sort

## Estruturas utilizadas

```text
list

heap binária
```

---

# Representação

O heap pode ser representado como vetor:

```text
Índices:

        0

       / \

      1   2

     / \

    3   4
```

Na prática:

```text
[10,5,8,2,1]
```

---

# Relação índice-filho

Para um elemento no índice `i`:

```text
Filho esquerdo:

2*i + 1


Filho direito:

2*i + 2
```

---

# Estrutura utilizada

A própria lista representa a árvore implicitamente.

---

# Memória auxiliar

```text
O(1)
```

---

# Matriz Algoritmo × Estrutura

| Algoritmo | list | Auxiliar | Recursão | Heap |
|-|-|-|-|-|
| Bubble Sort | ✓ | | | |
| Selection Sort | ✓ | | | |
| Insertion Sort | ✓ | | | |
| Merge Sort | ✓ | ✓ | ✓ | |
| Quick Sort | ✓ | ✓ | ✓ | |
| Heap Sort | ✓ | | | ✓ |

---

# Relação Estrutura × Complexidade

| Estrutura | Impacto principal |
|-|-|
| list | acesso sequencial e troca de elementos |
| sublistas | custo adicional de memória |
| pilha | controle de chamadas recursivas |
| heap | operações de prioridade |
| variáveis auxiliares | memória constante |

---

# Considerações da Categoria

As estruturas específicas utilizadas pelos algoritmos foram escolhidas considerando o equilíbrio entre eficiência computacional e clareza pedagógica.

A arquitetura do **LAB EDU SORT V1.0** prioriza implementações que permitam visualizar o comportamento dos algoritmos, acompanhar suas operações e relacionar teoria e prática.

A utilização predominante da estrutura `list` cria uma base comum entre os algoritmos, enquanto estruturas auxiliares específicas são introduzidas somente quando necessárias.

Essa abordagem mantém a biblioteca simples, extensível e adequada ao propósito educacional do projeto.

A próxima seção apresentará os **Critérios de Escolha das Estruturas**, detalhando as decisões relacionadas a complexidade, memória, mutabilidade, localidade, ensino e evolução arquitetural.

---

# Parte V — Critérios de Escolha

Esta seção apresenta os critérios utilizados para selecionar as estruturas de dados adotadas pelo **LAB EDU SORT V1.0**.

A escolha de uma estrutura de dados não deve considerar apenas a facilidade de implementação.

Ela deve levar em conta:

- características do problema;
- comportamento esperado da aplicação;
- impacto computacional;
- clareza do código;
- capacidade de evolução.

No contexto do LAB EDU SORT, existe ainda um fator adicional:

> A estrutura escolhida deve contribuir para o aprendizado dos conceitos de algoritmos e estruturas de dados.

---

# Objetivo dos Critérios

Os critérios definidos nesta seção têm como finalidade:

- justificar as decisões arquiteturais;
- evitar escolhas arbitrárias;
- documentar os trade-offs realizados;
- orientar futuras evoluções da biblioteca.

---

# Visão Geral dos Critérios

As estruturas foram avaliadas considerando:

```text
Critérios de Escolha

│

├── Complexidade Computacional

├── Consumo de Memória

├── Mutabilidade

├── Localidade de Memória

├── Facilidade de Ensino

└── Extensibilidade
```

---

# Complexidade Computacional

## Objetivo

Avaliar o custo das operações realizadas sobre cada estrutura.

A escolha deve considerar:

- tempo de acesso;
- tempo de inserção;
- tempo de remoção;
- frequência das operações.

---

# Aplicação no Projeto

Os algoritmos de ordenação executam grande quantidade de operações sobre os dados.

Portanto, a estrutura principal precisa permitir manipulações eficientes.

---

# Exemplo

Para os algoritmos de ordenação:

```text
Bubble Sort

Selection Sort

Insertion Sort

Merge Sort

Quick Sort
```

a estrutura:

```python
list
```

é adequada porque permite:

- acesso direto por índice;
- troca de elementos;
- movimentação dentro da sequência.

---

# Decisão Arquitetural

A estrutura principal dos algoritmos será:

```text
list
```

porque apresenta equilíbrio entre:

- simplicidade;
- desempenho;
- clareza.

---

# Consumo de Memória

## Objetivo

Avaliar o espaço adicional necessário durante a execução.

---

# Aplicação no Projeto

Cada algoritmo possui necessidades diferentes.

Exemplo:

```text
Bubble Sort

Memória auxiliar:

O(1)
```

Enquanto:

```text
Merge Sort

Memória auxiliar:

O(n)
```

---

# Decisão Arquitetural

A arquitetura deverá documentar quando um algoritmo necessita de estruturas auxiliares.

Exemplo:

| Algoritmo | Estrutura adicional |
|-|-|
| Bubble Sort | Não utiliza |
| Selection Sort | Não utiliza |
| Insertion Sort | Variáveis temporárias |
| Merge Sort | Listas auxiliares |
| Quick Sort | Pilha recursiva |
| Heap Sort | Heap sobre lista |

---

# Mutabilidade

## Objetivo

Avaliar se a estrutura permite alteração dos dados.

---

# Aplicação no Projeto

Os algoritmos de ordenação normalmente realizam:

- troca de elementos;
- movimentação;
- atualização de posições.

Portanto, a estrutura principal precisa permitir alterações.

---

# Decisão Arquitetural

Para dados de processamento:

```text
list
```

será utilizada porque permite:

- alteração direta;
- ordenação in-place;
- operações eficientes.

---

# Estruturas Imutáveis

Algumas informações do sistema devem permanecer imutáveis.

Exemplos:

- eventos;
- configurações;
- estatísticas consolidadas.

Nestes casos serão utilizados:

```text
dataclass(frozen=True)

Enum

tuple
```

---

# Localidade de Memória

## Objetivo

Avaliar o comportamento da estrutura em relação ao armazenamento dos elementos.

---

# Aplicação no Projeto

Estruturas sequenciais possuem melhor aproveitamento de cache em operações iterativas.

---

# Exemplo

Percorrer:

```text
[1,2,3,4,5]
```

possui comportamento previsível:

```text
posição atual

      ↓

próxima posição
```

---

# Decisão Arquitetural

A utilização de listas sequenciais favorece:

- percursos lineares;
- comparação entre elementos;
- visualização dos algoritmos.

---

# Facilidade de Ensino

## Objetivo

Avaliar o valor pedagógico da estrutura escolhida.

---

# Aplicação no Projeto

O LAB EDU SORT possui finalidade educacional.

Portanto, a estrutura deve facilitar a compreensão do estudante.

---

# Exemplo

Uma lista:

```text
[8,4,2,9]
```

permite visualizar:

- comparações;
- trocas;
- deslocamentos;
- partições.

---

# Decisão Arquitetural

A arquitetura prioriza estruturas:

- simples;
- conhecidas;
- visualmente compreensíveis.

---

# Extensibilidade

## Objetivo

Avaliar a capacidade da estrutura suportar crescimento futuro.

---

# Aplicação no Projeto

O LAB EDU SORT poderá incorporar:

- novos algoritmos;
- novos formatos de entrada;
- novas visualizações;
- novos relatórios.

---

# Decisão Arquitetural

A arquitetura evita estruturas excessivamente específicas.

Exemplo:

Ao invés de:

```text
BubbleSortDados
```

utilizar:

```text
list
```

permitindo:

```text
Bubble Sort

Quick Sort

Merge Sort

Heap Sort
```

utilizarem a mesma representação.

---

# Comparativo Geral das Estruturas

| Estrutura | Desempenho | Simplicidade | Ensino | Evolução |
|-|-|-|-|-|
| list | Alto | Alto | Alto | Alto |
| deque | Alto em extremidades | Médio | Médio | Alto |
| dict | Alto para busca | Alto | Alto | Alto |
| set | Alto para validação | Alto | Médio | Alto |
| dataclass | Não aplicável | Alto | Alto | Alto |
| Enum | Não aplicável | Alto | Alto | Alto |
| heap | Alto em prioridade | Médio | Alto | Alto |
| árvore | Variável | Baixo | Alto | Alto |
| grafo | Variável | Baixo | Alto | Alto |

---

# Matriz Decisão Estrutura × Critério

| Estrutura | Complexidade | Memória | Clareza | Evolução |
|-|-|-|-|-|
| list | ✓ | ✓ | ✓ | ✓ |
| dict | ✓ | ✓ | ✓ | ✓ |
| set | ✓ | ✓ | ✓ | ✓ |
| dataclass | | ✓ | ✓ | ✓ |
| Enum | | ✓ | ✓ | ✓ |
| deque | ✓ | ✓ | | ✓ |
| heap | ✓ | ✓ | | ✓ |

---

# Regras para Novas Estruturas

A inclusão de uma nova estrutura deverá responder às seguintes perguntas:

```text
1. Qual problema ela resolve?

2. Qual módulo necessita dela?

3. Existe uma estrutura existente que atende?

4. Qual o ganho arquitetural?

5. Qual o impacto na manutenção?

6. Qual o valor educacional?
```

---

# Critérios para Evolução

Uma nova estrutura poderá ser adicionada quando:

- houver necessidade real;
- melhorar a arquitetura;
- reduzir complexidade;
- representar um conceito importante;
- contribuir para o aprendizado.

---

# Considerações da Categoria

Os critérios definidos nesta seção garantem que as estruturas de dados do **LAB EDU SORT V1.0** sejam escolhidas de forma consciente e documentada.

A arquitetura não busca utilizar a estrutura teoricamente mais sofisticada em todos os cenários.

O objetivo é selecionar a estrutura mais adequada considerando simultaneamente:

- problema;
- desempenho;
- clareza;
- manutenção;
- ensino.

Essa abordagem permite que a biblioteca permaneça simples na V1.0, mas preparada para incorporar estruturas mais avançadas em versões futuras.

A próxima seção apresentará a **Arquitetura das Estruturas**, contendo mapas, diagramas, matriz de relacionamento e fluxo completo dos dados.

---

# Parte VI — Arquitetura das Estruturas

Esta seção apresenta a visão arquitetural consolidada das estruturas de dados utilizadas pelo **LAB EDU SORT V1.0**.

O objetivo desta parte é demonstrar como as estruturas definidas anteriormente se relacionam com:

- os módulos da biblioteca;
- os objetos do domínio;
- os algoritmos de ordenação;
- o fluxo de execução;
- os contratos estabelecidos.

Enquanto as partes anteriores apresentaram estruturas individualmente, esta seção apresenta a visão integrada da arquitetura.

---

# Objetivo da Arquitetura das Estruturas

A arquitetura das estruturas tem como objetivos:

- definir o fluxo dos dados dentro da aplicação;
- demonstrar a comunicação entre estruturas e módulos;
- identificar dependências;
- garantir coerência entre modelo conceitual e implementação;
- orientar futuras evoluções.

---

# Mapa Geral das Estruturas

A visão geral das estruturas pode ser representada da seguinte forma:

```text
                         Usuário

                            │

                            ▼

                     aplicacao

                            │

                            │

                 ConfiguracaoExecucao

                    (dataclass)

                            │

                            ▼

                    entradaDados

                            │

                            │

                            ▼

                    ConjuntoDados

                    (dataclass)

                            │

                            │

                            ▼

                      list[int]

                            │

                            ▼

               algoritmosOrdenacao

                            │

        ┌───────────────────┼───────────────────┐

        │                   │                   │

        ▼                   ▼                   ▼

      list            estruturas           eventos

   principal          auxiliares        (dataclass)

        │                   │                   │

        │                   │                   │

        └───────────────────┼───────────────────┘

                            │

                            ▼

                      estatisticas

                            │

                            ▼

                EstatisticasOrdenacao

                    (dataclass)

                            │

                            ▼

                    visualizacoes

                            │

                            ▼

                     Saída final
```

---

# Arquitetura por Camadas

As estruturas de dados estão distribuídas em camadas arquiteturais.

---

# Camada de Configuração

## Estruturas utilizadas

```text
dataclass

Enum

dict
```

---

## Responsabilidade

Representar:

- parâmetros de execução;
- opções selecionadas;
- estados da aplicação.

---

## Exemplo conceitual

```text
ConfiguracaoExecucao

{

 algoritmo = QUICK_SORT

 origem = ARQUIVO

 quantidade = 1000

}
```

---

# Camada de Entrada

## Estruturas utilizadas

```text
list

dataclass

Enum
```

---

## Responsabilidade

Produzir os dados que serão processados.

---

## Fluxo

```text
Arquivo

  │

  ▼

list[int]

  │

  ▼

ConjuntoDados
```

---

# Camada de Processamento

## Estruturas utilizadas

```text
list

list auxiliar

stack

heap
```

---

## Responsabilidade

Executar os algoritmos de ordenação.

---

## Fluxo

```text
ConjuntoDados

        │

        ▼

list

        │

        ▼

Algoritmo

        │

        ▼

ResultadoOrdenacao
```

---

# Camada de Observação

## Estruturas utilizadas

```text
dataclass

list

dict
```

---

## Responsabilidade

Registrar informações produzidas durante a execução.

---

## Fluxo

```text
Algoritmo

        │

        ▼

EventoOrdenacao

        │

        ▼

EstatisticasOrdenacao
```

---

# Camada de Apresentação

## Estruturas utilizadas

```text
list

dict

dataclass
```

---

## Responsabilidade

Transformar resultados em formatos visuais.

---

# Matriz Estrutura × Módulo

A tabela abaixo apresenta a utilização das estruturas pelos módulos principais.

| Estrutura | aplicacao | entradaDados | algoritmosOrdenacao | estatisticas | visualizacoes | validacoes | utilitarios |
|-|-|-|-|-|-|-|-|
| list | | ✓ | ✓ | ✓ | ✓ | | ✓ |
| dict | ✓ | ✓ | | ✓ | ✓ | ✓ | ✓ |
| set | | | | | | ✓ | |
| Enum | ✓ | ✓ | | | | ✓ | |
| dataclass | ✓ | ✓ | ✓ | ✓ | ✓ | | |
| tuple | | | | | | | ✓ |
| deque | | | ✓ | | | | |
| heap | | | ✓ | | | | |

---

# Fluxo Completo dos Dados

O fluxo completo da aplicação pode ser representado:

```text
1. Usuário define execução

        │

        ▼

2. aplicacao cria ConfiguracaoExecucao

        │

        ▼

3. entradaDados obtém dados

        │

        ▼

4. Dados são convertidos em ConjuntoDados

        │

        ▼

5. Algoritmo recebe list[int]

        │

        ▼

6. Algoritmo executa ordenação

        │

        ├────────► produz eventos

        │

        ├────────► atualiza estatísticas

        │

        ▼

7. ResultadoOrdenacao é criado

        │

        ▼

8. visualizacoes processa resultado

        │

        ▼

9. Saída apresentada
```

---

# Dependências entre Estruturas

A arquitetura possui as seguintes dependências:

```text
Enum

 │

 ▼

dataclass

 │

 ▼

Objetos do Domínio

 │

 ▼

list / dict / set

 │

 ▼

Algoritmos

 │

 ▼

Eventos e Estatísticas
```

---

# Regras de Dependência

As dependências deverão seguir estas regras:

## Regra 1

Estruturas simples podem ser utilizadas por estruturas complexas.

Exemplo:

```text
list

      ▼

ConjuntoDados
```

---

## Regra 2

Estruturas internas não devem substituir modelos do domínio.

Exemplo incorreto:

```text
dict representando ResultadoOrdenacao
```

Exemplo correto:

```text
ResultadoOrdenacao

        contém

        dict auxiliar
```

---

## Regra 3

Algoritmos não devem conhecer estruturas de apresentação.

Exemplo:

```text
BubbleSort

não conhece

Gráfico
```

---

# Diagrama Arquitetural Consolidado

```text
                 +----------------+

                 | Configuração   |

                 | dataclass      |

                 +----------------+

                         │

                         ▼

                 +----------------+

                 | Entrada Dados |

                 | list          |

                 +----------------+

                         │

                         ▼

                 +----------------+

                 | Domínio       |

                 | dataclass     |

                 +----------------+

                         │

                         ▼

          +-------------------------------+

          | Algoritmos Ordenação          |

          |                               |

          | list                          |

          | stack                         |

          | heap                          |

          +-------------------------------+

                         │

                         ▼

          +-------------------------------+

          | Eventos                       |

          | dataclass                     |

          +-------------------------------+

                         │

                         ▼

          +-------------------------------+

          | Estatísticas                  |

          | dataclass + dict              |

          +-------------------------------+

                         │

                         ▼

          +-------------------------------+

          | Visualizações                 |

          | list + dict                   |

          +-------------------------------+
```

---

# Compatibilidade com o Modelo de Classes

As estruturas definidas neste documento estão alinhadas ao Modelo de Classes.

| Classe | Estrutura principal |
|-|-|
| ConfiguracaoExecucao | dataclass + Enum |
| ConjuntoDados | dataclass + list |
| ResultadoOrdenacao | dataclass + list |
| EventoOrdenacao | dataclass |
| EstatisticasOrdenacao | dataclass |
| Configuracoes | dataclass + dict |

---

# Evolução Arquitetural

A arquitetura permite incorporar novas estruturas sem impacto nos contratos existentes.

Exemplos futuros:

```text
Versão 1.0

list

dict

dataclass


Versão 2.0

heap

árvores


Versão 3.0

grafos

estruturas distribuídas
```

---

# Considerações da Categoria

A arquitetura das estruturas define uma organização clara entre:

- armazenamento;
- processamento;
- observação;
- apresentação.

O **LAB EDU SORT V1.0** utiliza predominantemente estruturas simples e eficientes, mantendo o foco educacional sem comprometer a qualidade arquitetural.

A separação entre estruturas do domínio e estruturas auxiliares garante:

- baixo acoplamento;
- facilidade de evolução;
- melhor compreensão dos algoritmos;
- maior qualidade da implementação.

A próxima seção apresentará as **Regras de Evolução e Considerações Finais**, encerrando o documento `05-estruturas-dados.md`.

---

# Parte VII — Evolução e Considerações Finais

Esta seção apresenta as regras de evolução das estruturas de dados do **LAB EDU SORT V1.0**, bem como as diretrizes que deverão orientar futuras versões da biblioteca.

O objetivo é garantir que novas estruturas possam ser incorporadas de forma planejada, mantendo a consistência arquitetural definida durante o Milestone 02.

---

# Regras de Evolução

A evolução das estruturas de dados deverá seguir critérios técnicos e arquiteturais.

A inclusão de uma nova estrutura não deverá ocorrer apenas por conveniência de implementação.

Toda alteração deverá considerar:

- necessidade real;
- impacto arquitetural;
- compatibilidade com os contratos existentes;
- benefício educacional;
- custo de manutenção.

---

# Regra 01 — Manter simplicidade como prioridade

A estrutura escolhida deverá ser a mais simples capaz de resolver o problema.

Exemplo:

Preferencialmente:

```text
list
```

ao invés de uma estrutura especializada quando ambas atendem ao requisito.

---

# Regra 02 — Evitar complexidade prematura

Estruturas avançadas não deverão ser adicionadas sem necessidade.

Exemplo:

Não utilizar:

```text
árvores

grafos

estruturas distribuídas
```

apenas por serem conceitos importantes.

Sua inclusão deverá ocorrer quando existir:

- necessidade funcional;
- objetivo pedagógico;
- justificativa arquitetural.

---

# Regra 03 — Preservar contratos existentes

A evolução das estruturas não deverá quebrar os contratos definidos entre módulos.

Exemplo:

Contrato atual:

```text
algoritmosOrdenacao

recebe

ConjuntoDados
```

Uma nova estrutura interna poderá ser adicionada, desde que o contrato externo permaneça estável.

---

# Regra 04 — Separar estrutura de implementação

Os módulos deverão depender de abstrações do domínio e não diretamente de detalhes internos.

Exemplo:

Correto:

```text
Algoritmo

recebe

ConjuntoDados

que internamente utiliza list
```

Incorreto:

```text
Todos os módulos manipulam listas diretamente
```

---

# Regra 05 — Documentar toda nova estrutura

Toda nova estrutura adicionada deverá possuir:

- objetivo;
- módulo responsável;
- justificativa;
- impacto computacional;
- impacto arquitetural;
- exemplos de utilização.

---

# Estruturas Planejadas para Versões Futuras

O LAB EDU SORT V1.0 foi projetado para permitir evolução gradual.

Algumas estruturas não fazem parte da implementação inicial, mas possuem espaço arquitetural reservado.

---

# Heap Binária

## Previsão

Versão futura próxima.

---

## Objetivos

Permitir:

- implementação completa do Heap Sort;
- estudo de filas de prioridade;
- demonstração de estruturas hierárquicas.

---

## Representação prevista

A estrutura poderá continuar utilizando uma lista:

```text
heap

        ↓

list
```

com interpretação hierárquica dos índices.

---

# Árvores

## Previsão

Pós V1.0.

---

## Possíveis aplicações

- árvores binárias de busca;
- árvores balanceadas;
- estruturas avançadas de pesquisa.

---

## Valor educacional

Permitir a expansão do projeto para disciplinas relacionadas a:

- estruturas de dados não lineares;
- busca;
- indexação.

---

# Grafos

## Previsão

Pós V1.0.

---

## Possíveis aplicações

- representação de relacionamentos;
- visualizações avançadas;
- algoritmos de caminhos.

---

## Valor educacional

Possibilitar integração futura com conteúdos de:

- teoria dos grafos;
- algoritmos em redes;
- otimização.

---

# Evolução por Versões

A evolução esperada das estruturas segue o planejamento:

```text
LAB EDU SORT

│

├── V1.0

│     │

│     ├── list

│     ├── dict

│     ├── set

│     ├── dataclass

│     └── Enum

│

├── V2.0

│     │

│     ├── heap

│     ├── estruturas auxiliares avançadas

│     └── novas visualizações

│

└── V3.0

      │

      ├── árvores

      ├── grafos

      └── simulações complexas
```

---

# Boas Práticas

As seguintes práticas deverão ser mantidas durante o desenvolvimento.

---

# Utilizar nomes representativos

Exemplo:

Correto:

```text
dadosEntrada

estatisticasExecucao

eventosOrdenacao
```

Evitar:

```text
x

temp

dados2
```

---

# Evitar estruturas genéricas sem contexto

Exemplo:

Evitar:

```python
dictDados
```

quando existe um modelo específico:

```text
ConjuntoDados
```

---

# Utilizar estruturas imutáveis quando apropriado

Informações históricas ou de configuração devem evitar alterações acidentais.

Exemplo:

```text
EventoOrdenacao

ConfiguracaoExecucao
```

---

# Centralizar regras estruturais

As decisões sobre estruturas devem permanecer documentadas e centralizadas.

Evitar decisões independentes dentro de cada módulo.

---

# Relação com os Objetivos do Projeto

As estruturas definidas neste documento atendem aos objetivos principais do LAB EDU SORT:

## Objetivo técnico

Fornecer uma arquitetura organizada, modular e extensível.

---

## Objetivo educacional

Permitir que estudantes relacionem:

- algoritmos;
- estruturas de dados;
- complexidade;
- implementação.

---

## Objetivo arquitetural

Criar uma base sólida para evolução futura.

---

# Conclusão Geral do Documento

As estruturas de dados definidas no **LAB EDU SORT V1.0** representam uma escolha consciente baseada em critérios técnicos e pedagógicos.

A arquitetura utiliza estruturas simples como:

```text
list

dict

set

dataclass

Enum
```

porque elas oferecem o melhor equilíbrio entre:

- facilidade de compreensão;
- desempenho;
- manutenção;
- evolução.

As estruturas mais avançadas permanecem planejadas para versões futuras, evitando complexidade desnecessária na primeira versão do projeto.

O resultado é uma arquitetura preparada para ensinar algoritmos de ordenação de forma prática, organizada e evolutiva.

---

# Estado Final do Milestone 02

Com a conclusão deste documento, o Milestone 02 possui definido:

```text
✓ Modelo conceitual

✓ Modelo de classes

✓ Responsabilidades dos módulos

✓ Contratos entre módulos

✓ Estruturas de dados utilizadas

✓ Critérios de escolha

✓ Arquitetura das estruturas

✓ Estratégia de evolução
```

O projeto possui agora uma base conceitual suficiente para iniciar o próximo estágio:

```text
Milestone 03

Implementação da Fundação da Biblioteca
```

---
