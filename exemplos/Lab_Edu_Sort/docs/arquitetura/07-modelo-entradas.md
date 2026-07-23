# Índice

- [Parte I — Fundamentos do Modelo de Entradas](#parte-i--fundamentos-do-modelo-de-entradas)
  - [Objetivo do módulo de entradaDados](#objetivo-do-módulo-de-entradadados)
  - [Papel arquitetural das entradas](#papel-arquitetural-das-entradas)
  - [Princípios adotados](#princípios-adotados)
  - [Responsabilidades e limites do módulo](#responsabilidades-e-limites-do-módulo)

- [Parte II — Conceitos de Entrada de Dados no Projeto](#parte-ii--conceitos-de-entrada-de-dados-no-projeto)
  - [Tipos de entrada suportados](#tipos-de-entrada-suportados)
  - [Dados completos e parcialmente desordenados](#dados-completos-e-parcialmente-desordenados)
  - [Dados gerados automaticamente](#dados-gerados-automaticamente)
  - [Dados carregados por arquivo](#dados-carregados-por-arquivo)

- [Parte III — Modelo Conceitual das Entradas](#parte-iii--modelo-conceitual-das-entradas)
  - [Entidade EntradaDados](#entidade-entradadados)
  - [Entidade ConfiguracaoEntrada](#entidade-configuracaoentrada)
  - [Entidade DadosEntrada](#entidade-dadosentrada)
  - [Relacionamentos entre entidades](#relacionamentos-entre-entidades)

- [Parte IV — Classes do Modelo de Entradas](#parte-iv--classes-do-modelo-de-entradas)
  - [Classe DadosEntrada](#classe-dadosentrada)
  - [Classe ConfiguracaoEntrada](#classe-configuracaoentrada)
  - [Classe GeradorDados](#classe-geradordados)
  - [Classe LeitorArquivoEntrada](#classe-leitorarquivoentrada)
  - [Classe PreparadorEntrada](#classe-preparadorentrada)

- [Parte V — Contratos do Módulo entradaDados](#parte-v--contratos-do-módulo-entradadados)
  - [Contrato de geração de dados](#contrato-de-geração-de-dados)
  - [Contrato de leitura de arquivos](#contrato-de-leitura-de-arquivos)
  - [Contrato de preparação dos dados](#contrato-de-preparação-dos-dados)
  - [Contrato de comunicação com aplicacao](#contrato-de-comunicação-com-aplicacao)

- [Parte VI — Validações e Regras de Entrada](#parte-vi--validações-e-regras-de-entrada)
  - [Validação da quantidade de elementos](#validação-da-quantidade-de-elementos)
  - [Validação dos dados recebidos](#validação-dos-dados-recebidos)
  - [Validação dos arquivos](#validação-dos-arquivos)
  - [Tratamento de erros de entrada](#tratamento-de-erros-de-entrada)

- [Parte VII — Fluxos de Entrada de Dados](#parte-vii--fluxos-de-entrada-de-dados)
  - [Fluxo de geração automática](#fluxo-de-geração-automática)
  - [Fluxo de leitura de arquivo](#fluxo-de-leitura-de-arquivo)
  - [Fluxo de entrada parcial](#fluxo-de-entrada-parcial)
  - [Matriz de comunicação](#matriz-de-comunicação)

- [Parte VIII — Estruturas de Dados Utilizadas](#parte-viii--estruturas-de-dados-utilizadas)
  - [Listas de entrada](#listas-de-entrada)
  - [Metadados da entrada](#metadados-da-entrada)
  - [Configurações de geração](#configurações-de-geração)
  - [Representação dos estados](#representação-dos-estados)

- [Parte IX — Diagramas e Arquitetura](#parte-ix--diagramas-e-arquitetura)
  - [Arquitetura do módulo entradaDados](#arquitetura-do-módulo-entradadados)
  - [Diagrama de classes](#diagrama-de-classes)
  - [Diagrama de comunicação](#diagrama-de-comunicação)
  - [Dependências permitidas e proibidas](#dependências-permitidas-e-proibidas)

- [Parte X — Evolução e Considerações Finais](#parte-x--evolução-e-considerações-finais)
  - [Estado atual da V1.0](#estado-atual-da-v10)
  - [Limitações conhecidas](#limitações-conhecidas)
  - [Roadmap evolutivo](#roadmap-evolutivo)
  - [Considerações finais](#considerações-finais)

---

# Parte I — Fundamentos do Modelo de Entradas

<ul>
Esta seção apresenta os fundamentos arquiteturais do módulo `entradaDados` do **LAB EDU SORT V1.0**.
</ul>

<ul>
O objetivo desta parte é estabelecer a base conceitual para o tratamento das entradas utilizadas pelos algoritmos de ordenação, definindo:
</ul>

<ul>
<li>responsabilidade do módulo;</li>
<li>papel dentro da arquitetura geral;</li>
<li>princípios de desenvolvimento;</li>
<li>limites de atuação;</li>
<li>integração com os demais componentes.</li>
</ul>

<ul>
O módulo de entrada representa a primeira etapa do fluxo de execução do sistema, sendo responsável por disponibilizar dados adequados para processamento pelos algoritmos de ordenação.
</ul>
---

## Objetivo do Módulo entradaDados

O módulo `entradaDados` tem como objetivo controlar todo o ciclo de preparação dos dados que serão utilizados pelo LAB EDU SORT V1.0.

Suas responsabilidades incluem:

- receber configurações de entrada;
- gerar conjuntos de dados;
- carregar dados externos;
- validar informações recebidas;
- preparar dados para processamento;
- fornecer entradas padronizadas aos algoritmos.

O módulo deve garantir que os algoritmos recebam dados consistentes, independentemente da origem da entrada.

---

## Papel Arquitetural das Entradas

Dentro da arquitetura do LAB EDU SORT V1.0, o módulo `entradaDados` atua como uma camada intermediária entre a interação do usuário e o domínio dos algoritmos.

Fluxo arquitetural:

Usuário

↓

Aplicacao

↓

entradaDados

↓

algoritmosOrdenacao

↓

estatisticas

↓

relatorios / visualizacoes

---

O módulo possui papel fundamental porque os algoritmos de ordenação não devem conhecer detalhes sobre a origem dos dados.

Exemplo:

O algoritmo não deve saber se os dados vieram de:

- arquivo;
- geração automática;
- entrada manual;
- teste automatizado.

Ele deve receber apenas uma estrutura de dados válida para processamento.

---

### Separação entre Origem e Consumo dos Dados

Uma decisão arquitetural importante é separar:

Origem dos dados

de

Consumo dos dados.

A origem pode variar:

- arquivo CSV;
- geração aleatória;
- entrada pelo usuário;
- dados produzidos por testes.

Porém, a saída do módulo deve permanecer padronizada.

Exemplo:

Arquivo CSV

        |

        v

LeitorArquivoEntrada

        |

        v

DadosEntrada

        |

        v

AlgoritmoOrdenacao

---

### Responsabilidade Principal

A responsabilidade principal do módulo é:

"Preparar e disponibilizar dados válidos para execução dos algoritmos de ordenação."

---

### Responsabilidades Secundárias

O módulo também deve:

- controlar formatos de entrada;
- aplicar regras de validação;
- informar erros encontrados;
- manter informações sobre a origem dos dados;
- registrar configurações utilizadas.

---

### O módulo entradaDados deve conhecer

O módulo pode conhecer:

- modelos de dados;
- regras de validação;
- configurações de geração;
- estruturas utilizadas para armazenamento temporário.

Exemplo:

entradaDados

↓

modelos

↓

validacoes

---

### O módulo entradaDados não deve conhecer

O módulo não deve conhecer:

- implementação interna dos algoritmos;
- detalhes de estatísticas;
- regras de apresentação;
- gráficos;
- relatórios.

Exemplo incorreto:

entradaDados

↓

algoritmosOrdenacao

↓

visualizacoes

---

## Princípios Adotados

A arquitetura do módulo segue os mesmos princípios definidos para o LAB EDU SORT V1.0.

---

### Programação Orientada a Objetos Explícita

O módulo deve representar responsabilidades através de classes.

Exemplo:

Correto:

DadosEntrada

ConfiguracaoEntrada

GeradorDados

LeitorArquivoEntrada


Evitar:

funções isoladas sem responsabilidade definida.

---

### Separação de Responsabilidades

Cada componente possui uma função específica.

Exemplo:

GeradorDados

Responsável por:

- criar dados;

Não responsável por:

- executar algoritmos;
- gerar relatórios;
- calcular estatísticas.

---

### DRY — Don't Repeat Yourself

As regras de entrada devem existir em um único local.

Exemplo:

Evitar:

- validação duplicada em vários módulos;
- regras diferentes para arquivos e geração automática;
- conversões repetidas.

A validação deve ser centralizada.

---

### YAGNI — You Aren't Gonna Need It

A implementação inicial deve conter apenas os recursos necessários para a V1.0.

Não serão adicionados inicialmente:

- banco de dados;
- APIs externas;
- interfaces gráficas;
- mecanismos complexos de importação.

Esses recursos poderão ser incorporados em versões futuras.

---

### Baixo Acoplamento

O módulo deve possuir pouca dependência externa.

O objetivo é permitir que novas formas de entrada sejam adicionadas sem modificar os algoritmos existentes.

Exemplo:

Adicionar:

EntradaJSON

ou

EntradaBancoDados

não deve exigir alteração em:

- algoritmos;
- estatísticas;
- relatórios.

---

### Alta Coesão

Cada classe deve possuir responsabilidades relacionadas.

Exemplo:

DadosEntrada

Responsável por:

- representar os dados.

GeradorDados

Responsável por:

- criar dados.

LeitorArquivoEntrada

Responsável por:

- carregar dados externos.

---

## Responsabilidades e limites do módulo

Para manter a arquitetura organizada, o módulo possui limites bem definidos.

---

### Responsabilidades incluídas

O módulo inclui:

- geração de dados;
- carregamento de dados;
- preparação;
- validação inicial;
- organização das entradas.

---

### Responsabilidades excluídas

O módulo não inclui:

- ordenação;
- análise estatística;
- geração de gráficos;
- persistência definitiva;
- interface com usuário.

---

### Integração com Outros Módulos

O módulo `entradaDados` possui comunicação principalmente com:

#### aplicacao

Responsabilidade:

Receber solicitações e devolver dados preparados.

Tipo:

Request / Response

---

#### validacoes

Responsabilidade:

Garantir consistência das informações.

Tipo:

Request / Response

---

#### algoritmosOrdenacao

Responsabilidade:

Entregar dados prontos para processamento.

Tipo:

Response

---

### Fluxo Conceitual do Módulo

O funcionamento geral é:

Configuração de entrada

↓

Recebimento da solicitação

↓

Definição da origem dos dados

↓

Carregamento ou geração

↓

Validação

↓

Preparação

↓

Entrega ao algoritmo

---

## Considerações da Parte

O módulo `entradaDados` representa a porta de entrada do LAB EDU SORT V1.0.

Sua principal função é garantir que os algoritmos trabalhem com dados confiáveis, mantendo o isolamento entre:

- origem dos dados;
- preparação;
- processamento;
- análise.

A arquitetura definida permite evolução futura sem comprometer os módulos existentes.

Com essa organização, o LAB EDU SORT V1.0 mantém os princípios fundamentais do projeto:

- modularidade;
- clareza de responsabilidades;
- baixo acoplamento;
- extensibilidade;
- foco educacional.

---

# Parte II — Conceitos de Entrada de Dados no Projeto

Esta seção apresenta os conceitos relacionados ao tratamento das entradas de dados no **LAB EDU SORT V1.0**.

O objetivo é definir como os dados serão obtidos, organizados e preparados antes de serem submetidos aos algoritmos de ordenação.

A entrada de dados possui papel fundamental no projeto porque diferentes características da entrada podem influenciar diretamente o comportamento dos algoritmos.

Exemplos:

- quantidade de elementos;
- grau de ordenação inicial;
- distribuição dos valores;
- presença de elementos repetidos;
- origem dos dados.

---

# Conceito de Entrada de Dados no LAB EDU SORT

No contexto do projeto, uma entrada de dados representa um conjunto de valores que será submetido a um algoritmo de ordenação.

Uma entrada possui:

- dados;
- quantidade de elementos;
- origem;
- configuração utilizada;
- características do conjunto.

Modelo conceitual:

Entrada

+

Metadados

+

Configuração

=

Dados preparados para execução

---

# Importância das Entradas na Análise dos Algoritmos

Os algoritmos de ordenação não possuem o mesmo comportamento para todos os tipos de entrada.

A análise experimental depende diretamente das características dos dados fornecidos.

Exemplo:

Bubble Sort:

Entrada ordenada:

- poucas trocas;
- menor quantidade de operações.

Entrada inversamente ordenada:

- muitas trocas;
- maior quantidade de operações.

---

# Tipos de Entrada Suportados

O LAB EDU SORT V1.0 prevê inicialmente três formas principais de entrada:

- entrada manual;
- entrada por arquivo;
- geração automática.

Cada tipo possui uma finalidade específica.

---

# Entrada Manual

A entrada manual permite que o usuário forneça diretamente os valores que serão utilizados.

Exemplo:

Usuário informa:

10, 5, 8, 2, 7

Resultado:

Lista recebida:

[10, 5, 8, 2, 7]

---

# Características da Entrada Manual

Vantagens:

- simples para testes pequenos;
- permite experimentação rápida;
- facilita demonstrações em sala de aula.

Limitações:

- inadequada para grandes volumes;
- depende da interação humana;
- maior possibilidade de erro de digitação.

---

# Entrada por Arquivo

A entrada por arquivo permite carregar conjuntos de dados previamente preparados.

Exemplo:

arquivo:

dados_1000.csv

Conteúdo:

1000 valores numéricos.

---

# Características da Entrada por Arquivo

Vantagens:

- permite testes repetíveis;
- facilita comparação entre algoritmos;
- possibilita grandes volumes de dados.

Aplicações:

- experimentos;
- avaliações;
- demonstrações acadêmicas.

---

# Formatos de Arquivo

A V1.0 poderá trabalhar inicialmente com formatos simples.

Exemplo:

CSV:

10;5;8;2;7

ou

TXT:

10
5
8
2
7

---

# Geração Automática de Dados

A geração automática permite criar entradas controladas pelo sistema.

Ela será utilizada principalmente para:

- testes;
- experimentos;
- comparação de desempenho.

---

# Configurações da Geração

A geração poderá considerar:

- quantidade de elementos;
- intervalo de valores;
- tipo de distribuição;
- grau de desordenação.

Exemplo:

Quantidade:

1000 elementos

Intervalo:

0 até 9999

Tipo:

aleatório

---

# Dados Totalmente Ordenados

Representam entradas já organizadas.

Exemplo:

[1, 2, 3, 4, 5, 6]

Características:

- ordem crescente;
- melhor caso para alguns algoritmos;
- utilizada para análise comparativa.

---

# Dados Inversamente Ordenados

Representam entradas em ordem decrescente.

Exemplo:

[6, 5, 4, 3, 2, 1]

Características:

- pior cenário para alguns algoritmos;
- grande quantidade de movimentações;
- importante para análise de complexidade.

---

# Dados Aleatórios

Representam conjuntos sem padrão definido.

Exemplo:

[8, 2, 9, 1, 5, 4]

Características:

- aproximam situações reais;
- utilizados em testes gerais;
- representam comportamento médio.

---

# Dados Parcialmente Desordenados

Representam entradas que possuem algum grau de organização.

Exemplo:

[1, 2, 8, 4, 5, 3, 7]

Características:

- simulam situações intermediárias;
- permitem analisar algoritmos adaptativos;
- importantes para Insertion Sort.

---

# Grau de Desordenação

A arquitetura prevê a possibilidade de controlar o nível de desordenação.

Exemplo:

0%

↓

Lista totalmente ordenada


50%

↓

Lista parcialmente desordenada


100%

↓

Lista totalmente aleatória

---

# Características Associadas às Entradas

Cada entrada poderá possuir informações complementares:

- tamanho;
- origem;
- tipo;
- grau de ordenação;
- data de criação;
- configuração utilizada.

Essas informações serão utilizadas posteriormente pelos módulos:

- estatisticas;
- relatorios;
- visualizacoes.

---

# Relação entre Entrada e Estatísticas

As características da entrada influenciam diretamente as métricas coletadas.

Fluxo:

Características da entrada

↓

Execução do algoritmo

↓

Eventos gerados

↓

Métricas coletadas

↓

Análise comparativa

---

# Exemplos de Influência da Entrada

## Bubble Sort

Entrada ordenada:

Poucas trocas.

Entrada inversa:

Muitas trocas.

---

## Insertion Sort

Entrada quase ordenada:

Excelente desempenho.

Entrada aleatória:

Maior quantidade de movimentações.

---

## Merge Sort

Independentemente da entrada:

Mantém comportamento próximo de:

O(n log n)

---

# Modelo de Entrada Padronizada

Independentemente da origem, toda entrada deve ser convertida para um modelo comum.

Modelo:

DadosEntrada

{

 valores

 quantidadeElementos

 origem

 tipoEntrada

 configuracao

}

---

# Normalização das Entradas

Antes de serem enviadas aos algoritmos, as entradas devem passar pelo processo de normalização.

Fluxo:

Entrada original

↓

Validação

↓

Conversão

↓

Padronização

↓

DadosEntrada

↓

Algoritmo

---

# Princípio de Independência da Origem

Os algoritmos devem receber sempre a mesma estrutura de dados.

Exemplo:

Arquivo CSV

        |

        v

DadosEntrada


Entrada manual

        |

        v

DadosEntrada


Geração automática

        |

        v

DadosEntrada

---

# Preparação para Experimentos

A arquitetura permite criar cenários experimentais:

Exemplo:

Experimento 01:

Algoritmo:

Bubble Sort

Entrada:

100 elementos aleatórios


Experimento 02:

Algoritmo:

Merge Sort

Entrada:

100 elementos aleatórios

---

# Considerações da Parte

O modelo conceitual de entradas estabelece uma base flexível para o LAB EDU SORT V1.0.

A arquitetura permite trabalhar com diferentes origens de dados mantendo uma interface única para os algoritmos.

O fluxo definido é:

Origem dos dados

↓

Preparação

↓

Validação

↓

Padronização

↓

Execução dos algoritmos

↓

Análise estatística

Essa abordagem permite que o projeto seja utilizado tanto para demonstrações educacionais quanto para experimentos comparativos de desempenho.

---

# Parte III — Modelo Conceitual das Entradas

Esta seção apresenta o modelo conceitual das entradas do **LAB EDU SORT V1.0**.

O objetivo é definir as entidades responsáveis por representar os dados de entrada, suas configurações, origens e características antes da execução dos algoritmos de ordenação.

O modelo conceitual estabelece uma camada intermediária entre:

- origem dos dados;
- preparação das informações;
- execução dos algoritmos;
- análise estatística.

Fluxo conceitual:

Origem da Entrada

↓

Configuração da Entrada

↓

Dados Preparados

↓

Algoritmo de Ordenação

↓

Estatísticas

---

# Objetivos do Modelo Conceitual

O modelo de entradas deve permitir:

- representar diferentes fontes de dados;
- padronizar informações recebidas;
- armazenar características da entrada;
- permitir validação;
- facilitar testes;
- possibilitar evolução futura.

A principal decisão arquitetural é:

"Todos os tipos de entrada devem produzir o mesmo modelo de dados para consumo dos algoritmos."

---

# Entidade DadosEntrada

A entidade `DadosEntrada` representa o conjunto de dados efetivamente utilizado na execução dos algoritmos.

Ela é a principal entidade do módulo `entradaDados`.

Responsabilidades:

- armazenar os valores de entrada;
- registrar informações da origem;
- manter metadados;
- disponibilizar dados preparados.

---

# Estrutura Conceitual

DadosEntrada

{

 valores

 quantidadeElementos

 origem

 tipoEntrada

 configuracao

 dataGeracao

}

---

# Atributos Conceituais

## valores

Representa os elementos que serão ordenados.

Exemplo:

[8, 3, 1, 7, 5]

---

## quantidadeElementos

Representa o tamanho do conjunto.

Exemplo:

500 elementos

---

## origem

Indica como os dados foram obtidos.

Exemplos:

- manual;
- arquivo;
- gerado automaticamente.

---

## tipoEntrada

Representa a característica da entrada.

Exemplos:

- ordenada;
- inversamente ordenada;
- aleatória;
- parcialmente desordenada.

---

## configuracao

Mantém as informações utilizadas para criação da entrada.

Exemplo:

- quantidade;
- intervalo;
- percentual de desordenação.

---

# Entidade ConfiguracaoEntrada

A entidade `ConfiguracaoEntrada` representa as regras utilizadas para criação ou carregamento dos dados.

Ela não contém os dados propriamente ditos.

Sua responsabilidade é definir como a entrada será obtida.

---

# Estrutura Conceitual

ConfiguracaoEntrada

{

 quantidadeElementos

 valorMinimo

 valorMaximo

 tipoGeracao

 grauDesordenacao

 origem

}

---

# Atributos Conceituais

## quantidadeElementos

Quantidade de elementos desejada.

Exemplo:

1000

---

## valorMinimo

Menor valor permitido na geração.

Exemplo:

0

---

## valorMaximo

Maior valor permitido na geração.

Exemplo:

9999

---

## tipoGeracao

Define a estratégia de criação.

Exemplos:

- aleatória;
- ordenada;
- inversa;
- parcial.

---

## grauDesordenacao

Define o percentual de alteração da ordem original.

Exemplo:

50%

---

## origem

Define a fonte dos dados.

Exemplos:

- arquivo;
- usuário;
- gerador.

---

# Entidade OrigemEntrada

A entidade conceitual `OrigemEntrada` representa a procedência dos dados.

Ela permite que o sistema saiba como a entrada foi criada.

---

# Valores Possíveis

OrigemEntrada

{

MANUAL

ARQUIVO

GERADA

TESTE

}

---

# Importância da Origem

A origem permite:

- rastreabilidade;
- reprodução de experimentos;
- geração de relatórios;
- análise comparativa.

Exemplo:

Relatório:

Algoritmo:

Quick Sort

Entrada:

Gerada automaticamente

Quantidade:

10000 elementos

---

# Entidade TipoEntrada

A entidade `TipoEntrada` representa o estado inicial dos dados.

Ela descreve a organização inicial antes da ordenação.

---

# Valores Possíveis

TipoEntrada

{

ORDENADA

INVERTIDA

ALEATORIA

PARCIALMENTE_DESORDENADA

}

---

# Importância do Tipo de Entrada

O tipo de entrada influencia diretamente:

- quantidade de comparações;
- número de trocas;
- movimentações;
- tempo de execução.

---

# Entidade EntradaOrdenacao

A entidade `EntradaOrdenacao` representa a composição completa utilizada em uma execução.

Ela reúne:

- dados;
- configuração;
- informações de origem.

---

# Estrutura Conceitual

EntradaOrdenacao

{

 dadosEntrada

 configuracaoEntrada

 origemEntrada

 tipoEntrada

}

---

# Relacionamento entre Entidades

O relacionamento conceitual é:

ConfiguracaoEntrada

        |

        | define

        v

DadosEntrada

        |

        | possui

        v

OrigemEntrada


DadosEntrada

        |

        | classificado por

        v

TipoEntrada

---

# Modelo Conceitual Completo

Representação geral:

EntradaOrdenacao

        |

        +----------------+

        |                |

        v                v

ConfiguracaoEntrada   DadosEntrada

                         |

          +--------------+--------------+

          |                             |

          v                             v

   OrigemEntrada                 TipoEntrada

---

# Comunicação com Outros Módulos

O modelo de entradas possui integração principalmente com:

---

# Aplicacao

Responsabilidade:

Solicitar criação ou carregamento dos dados.

Comunicação:

Request / Response

---

# Validacoes

Responsabilidade:

Garantir que os dados estejam corretos.

Comunicação:

Request / Response

---

# AlgoritmosOrdenacao

Responsabilidade:

Receber os dados preparados.

Comunicação:

Response

---

# Estatisticas

Responsabilidade:

Receber informações contextuais da entrada.

Comunicação:

Request

---

# Regras Conceituais

O modelo estabelece algumas regras:

---

# Regra 01 — Entrada deve ser padronizada

Independentemente da origem:

Arquivo

Entrada manual

Geração automática

↓

Devem resultar em:

DadosEntrada

---

# Regra 02 — Configuração não contém dados

A configuração define como criar a entrada.

Ela não armazena:

- valores;
- resultados;
- estatísticas.

---

# Regra 03 — Algoritmos não conhecem a origem

O algoritmo recebe:

DadosEntrada

Não recebe:

Arquivo

ou

Configuração de geração.

---

# Regra 04 — Entrada é imutável durante execução

Após entregue ao algoritmo:

- a configuração não muda;
- os metadados permanecem;
- a origem é preservada.

---

# Preparação para o Modelo de Classes

O modelo conceitual servirá como base para a definição das classes:

- `DadosEntrada`;
- `ConfiguracaoEntrada`;
- `OrigemEntrada`;
- `TipoEntrada`;
- `GeradorDados`;
- `LeitorArquivoEntrada`.

---

# Considerações da Parte

O modelo conceitual das entradas define uma estrutura organizada para representar todos os dados utilizados pelo LAB EDU SORT V1.0.

A principal decisão arquitetural é a padronização da entrada:

Diferentes origens

↓

Mesmo modelo conceitual

↓

Mesmo contrato de consumo

↓

Algoritmos independentes

Essa abordagem garante:

- flexibilidade;
- extensibilidade;
- facilidade de testes;
- isolamento entre módulos;
- preparação adequada para evolução futura do projeto.

---

# Parte IV — Classes do Modelo de Entradas

Esta seção apresenta as classes responsáveis pela implementação do modelo conceitual de entradas do **LAB EDU SORT V1.0**.

O objetivo é transformar as entidades conceituais definidas anteriormente em componentes orientados a objetos, mantendo os princípios arquiteturais do projeto:

- Programação Orientada a Objetos explícita;
- separação de responsabilidades;
- baixo acoplamento;
- alta coesão;
- facilidade de testes;
- possibilidade de evolução.

O modelo de classes do módulo `entradaDados` será responsável por controlar:

- representação dos dados;
- configuração das entradas;
- geração de dados;
- leitura de arquivos;
- preparação das informações para os algoritmos.

---

# Visão Geral das Classes

O módulo `entradaDados` será composto inicialmente pelas seguintes classes:

DadosEntrada

Responsabilidade:

Representar os dados preparados para execução.

---

ConfiguracaoEntrada

Responsabilidade:

Definir como os dados serão obtidos.

---

GeradorDados

Responsabilidade:

Criar conjuntos de dados conforme configuração.

---

LeitorArquivoEntrada

Responsabilidade:

Realizar leitura de dados externos.

---

PreparadorEntrada

Responsabilidade:

Normalizar e preparar os dados finais.

---

# Relacionamento Geral das Classes

Fluxo de geração:

ConfiguracaoEntrada

↓

GeradorDados

↓

DadosEntrada


Fluxo de arquivo:

Arquivo

↓

LeitorArquivoEntrada

↓

PreparadorEntrada

↓

DadosEntrada

---

# Classe DadosEntrada

## Responsabilidade

A classe `DadosEntrada` representa o conjunto de dados preparado para execução dos algoritmos de ordenação.

Ela é o principal objeto de comunicação entre:

- entradaDados;
- algoritmosOrdenacao;
- estatisticas.

---

# Objetivos da Classe

A classe deve:

- armazenar os valores;
- disponibilizar informações da entrada;
- manter metadados;
- representar uma entrada válida.

---

# Atributos Conceituais

DadosEntrada

- valores
- quantidadeElementos
- origem
- tipoEntrada
- configuracao

---

# Descrição dos Atributos

## valores

Representa a lista de elementos que serão ordenados.

Exemplo:

[10, 5, 8, 2]

---

## quantidadeElementos

Representa o tamanho do conjunto de dados.

Exemplo:

4 elementos.

---

## origem

Indica a procedência dos dados.

Exemplos:

- MANUAL;
- ARQUIVO;
- GERADA.

---

## tipoEntrada

Representa o estado inicial dos dados.

Exemplos:

- ORDENADA;
- INVERTIDA;
- ALEATORIA;
- PARCIALMENTE_DESORDENADA.

---

## configuracao

Mantém as informações utilizadas para criação da entrada.

Exemplo:

- quantidade;
- intervalo;
- grau de desordenação.

---

# Métodos Esperados

A classe poderá disponibilizar:

- obterValores();
- obterQuantidade();
- obterOrigem();
- obterTipoEntrada();
- obterConfiguracao();

---

# Regras da Classe

A classe deve garantir:

- quantidade compatível com a lista;
- dados válidos;
- informações consistentes;
- preservação dos metadados.

---

# Classe ConfiguracaoEntrada

## Responsabilidade

A classe `ConfiguracaoEntrada` representa os parâmetros utilizados para criação ou carregamento de uma entrada.

Ela define as características desejadas dos dados.

---

# Objetivos da Classe

Permitir configurar:

- quantidade de elementos;
- intervalo de valores;
- tipo de geração;
- grau de desordenação;
- origem da entrada.

---

# Atributos Conceituais

ConfiguracaoEntrada

- quantidadeElementos
- valorMinimo
- valorMaximo
- tipoGeracao
- grauDesordenacao
- origem

---

# Descrição dos Atributos

## quantidadeElementos

Define quantos elementos serão gerados ou carregados.

---

## valorMinimo

Define o menor valor permitido.

---

## valorMaximo

Define o maior valor permitido.

---

## tipoGeracao

Define a estratégia utilizada.

Exemplos:

- aleatória;
- ordenada;
- invertida;
- parcial.

---

## grauDesordenacao

Define o percentual de alteração da ordem inicial.

Exemplo:

50%.

---

## origem

Define a procedência dos dados.

Exemplos:

- arquivo;
- usuário;
- gerador.

---

# Métodos Esperados

A classe poderá disponibilizar:

- validarConfiguracao();
- obterQuantidade();
- obterIntervalo();
- obterTipoGeracao();
- obterOrigem();

---

# Regras da Classe

A configuração deve impedir:

- quantidade negativa;
- intervalo inválido;
- valores inconsistentes;
- tipos inexistentes.

---

# Classe GeradorDados

## Responsabilidade

A classe `GeradorDados` é responsável pela criação de conjuntos de dados conforme uma configuração recebida.

---

# Objetivos da Classe

Permitir gerar:

- dados aleatórios;
- dados ordenados;
- dados invertidos;
- dados parcialmente desordenados.

---

# Comunicação

Entrada:

ConfiguracaoEntrada

Saída:

DadosEntrada

---

# Fluxo

ConfiguracaoEntrada

↓

GeradorDados

↓

DadosEntrada

---

# Métodos Esperados

- gerarDados();
- gerarAleatorio();
- gerarOrdenado();
- gerarInvertido();
- gerarParcialmenteDesordenado();

---

# Regras da Classe

O gerador deve:

- respeitar quantidade solicitada;
- respeitar intervalo;
- registrar origem;
- definir tipo da entrada.

---

# Classe LeitorArquivoEntrada

## Responsabilidade

A classe `LeitorArquivoEntrada` é responsável por carregar dados externos.

---

# Objetivos da Classe

Permitir:

- leitura de arquivos;
- interpretação dos dados;
- conversão para modelo interno.

---

# Comunicação

Entrada:

Caminho do arquivo.

Saída:

DadosEntrada.

---

# Fluxo

Arquivo

↓

LeitorArquivoEntrada

↓

DadosEntrada

---

# Métodos Esperados

- lerArquivo();
- validarFormato();
- converterDados();

---

# Regras da Classe

A classe deve validar:

- existência do arquivo;
- formato esperado;
- valores válidos;
- quantidade de elementos.

---

# Classe PreparadorEntrada

## Responsabilidade

A classe `PreparadorEntrada` realiza a etapa final de transformação dos dados antes da execução.

---

# Objetivos da Classe

Responsável por:

- normalizar dados;
- aplicar ajustes necessários;
- garantir compatibilidade.

---

# Comunicação

Entrada:

Dados originais.

Saída:

DadosEntrada.

---

# Fluxo

Dados originais

↓

PreparadorEntrada

↓

DadosEntrada

---

# Métodos Esperados

- preparar();
- normalizar();
- validar();
- criarModeloEntrada();

---

# Regras da Classe

O preparador deve garantir:

- estrutura correta;
- dados consistentes;
- modelo padronizado.

---

# Relação com AlgoritmosOrdenacao

Os algoritmos não devem conhecer como os dados foram criados.

Fluxo correto:

entradaDados

↓

DadosEntrada

↓

AlgoritmosOrdenacao

---

# Relação com Estatisticas

A entrada deve fornecer informações auxiliares para análise.

Exemplos:

- quantidade de elementos;
- tipo de entrada;
- origem dos dados.

---

# Dependências Permitidas

Configuração:

ConfiguracaoEntrada

↓

GeradorDados


Geração:

GeradorDados

↓

DadosEntrada


Arquivo:

LeitorArquivoEntrada

↓

PreparadorEntrada

↓

DadosEntrada

---

# Dependências Proibidas

Não permitido:

GeradorDados

↓

AlgoritmosOrdenacao

Motivo:

A geração não deve executar processamento.

---

Não permitido:

DadosEntrada

↓

Estatisticas

Motivo:

O modelo de dados não deve calcular métricas.

---

# Evolução Futura das Classes

## V1.0

Classes previstas:

- DadosEntrada;
- ConfiguracaoEntrada;
- GeradorDados;
- LeitorArquivoEntrada;
- PreparadorEntrada.

---

## V2.0

Possíveis extensões:

- EntradaBancoDados;
- EntradaJSON;
- EntradaAPI;
- GerenciadorExperimentos.

---

## V3.0

Possíveis extensões:

- EntradaInterativa;
- EntradaVisual;
- Ambiente experimental completo.

---

# Considerações da Parte

O modelo de classes de entrada estabelece uma estrutura orientada a objetos para controlar todo o ciclo de preparação dos dados.

A arquitetura separa claramente:

Configuração

↓

Criação ou leitura

↓

Preparação

↓

Modelo padronizado

↓

Execução dos algoritmos

Essa separação permite adicionar novas formas de entrada sem modificar os algoritmos existentes.

O módulo permanece alinhado aos princípios definidos no projeto:

- modularidade;
- extensibilidade;
- baixo acoplamento;
- alta coesão;
- clareza arquitetural.

---

# Parte V — Contratos do Módulo entradaDados

Esta seção apresenta os contratos de comunicação do módulo `entradaDados` do **LAB EDU SORT V1.0**.

O objetivo é definir claramente como o módulo de entradas se comunica com os demais componentes da arquitetura, estabelecendo:

- responsabilidades;
- dados recebidos;
- dados produzidos;
- classificação das comunicações;
- regras de utilização;
- limites de dependência.

Os contratos representam a interface arquitetural entre os módulos, permitindo que novas implementações sejam adicionadas sem modificar componentes existentes.

---

# Objetivo dos Contratos

Os contratos do módulo `entradaDados` têm como finalidade garantir que:

- os dados sejam produzidos de forma padronizada;
- os algoritmos recebam entradas consistentes;
- a origem dos dados seja preservada;
- as validações ocorram antes do processamento;
- a comunicação entre módulos seja previsível.

---

# Princípio de Comunicação

O módulo `entradaDados` segue o princípio:

"Os módulos devem conhecer contratos, não implementações."

Isso significa que:

- algoritmos não conhecem geradores;
- estatísticas não conhecem arquivos;
- aplicação não conhece detalhes internos de preparação.

Fluxo:

Aplicacao

↓

Contrato de Entrada

↓

entradaDados

↓

Contrato de Dados

↓

AlgoritmosOrdenacao

---

# Classificação das Comunicações

Todas as comunicações do módulo seguem uma classificação explícita:

## Request

Representa uma solicitação realizada por um módulo.

Exemplo:

Aplicacao solicita criação de uma entrada.

---

## Response

Representa uma resposta produzida após uma solicitação.

Exemplo:

entradaDados retorna um objeto `DadosEntrada`.

---

## Event

Representa uma informação gerada durante o fluxo.

Exemplo:

Entrada criada com determinada configuração.

---

# Contrato de Geração de Dados

## Objetivo

Definir como o sistema solicita a criação de novos conjuntos de dados.

---

# Comunicação

Origem:

Aplicacao

Destino:

GeradorDados

Tipo:

Request

---

# Solicitação

A aplicação informa:

- quantidade de elementos;
- intervalo de valores;
- tipo de geração;
- grau de desordenação.

Exemplo conceitual:

Criar entrada:

Quantidade:

1000 elementos

Tipo:

ALEATORIA

Intervalo:

0 até 9999

---

# Processamento Esperado

O `GeradorDados` deve:

- interpretar a configuração;
- gerar os valores;
- criar modelo de entrada;
- registrar metadados.

---

# Resposta

Origem:

GeradorDados

Destino:

Aplicacao

Tipo:

Response

---

# Resultado Produzido

Retorna:

DadosEntrada

contendo:

- valores;
- quantidade;
- origem;
- tipo;
- configuração utilizada.

---

# Contrato de Leitura de Arquivos

## Objetivo

Definir como arquivos externos são convertidos em entradas internas.

---

# Comunicação

Origem:

Aplicacao

Destino:

LeitorArquivoEntrada

Tipo:

Request

---

# Solicitação

A aplicação informa:

- caminho do arquivo;
- formato esperado;
- parâmetros adicionais.

---

# Processamento Esperado

O leitor deve:

- localizar arquivo;
- validar existência;
- interpretar conteúdo;
- converter valores.

---

# Resposta

Origem:

LeitorArquivoEntrada

Destino:

Aplicacao

Tipo:

Response

---

# Resultado Produzido

Retorna:

DadosEntrada

ou

erro de entrada.

---

# Contrato de Preparação dos Dados

## Objetivo

Definir a etapa de normalização dos dados.

---

# Comunicação

Origem:

LeitorArquivoEntrada

ou

GeradorDados

Destino:

PreparadorEntrada

Tipo:

Request

---

# Solicitação

Recebe:

- dados brutos;
- informações de origem;
- configuração utilizada.

---

# Processamento Esperado

O preparador deve:

- validar estrutura;
- normalizar valores;
- criar modelo padronizado.

---

# Resposta

Origem:

PreparadorEntrada

Destino:

entradaDados

Tipo:

Response

---

# Resultado Produzido

Retorna:

DadosEntrada válido.

---

# Contrato de Entrega aos Algoritmos

## Objetivo

Definir como os dados preparados são enviados para os algoritmos de ordenação.

---

# Comunicação

Origem:

entradaDados

Destino:

algoritmosOrdenacao

Tipo:

Response

---

# Dados Enviados

O módulo entrega:

DadosEntrada

contendo:

- lista de valores;
- quantidade de elementos;
- tipo da entrada;
- origem;
- informações contextuais.

---

# Regra Principal

O algoritmo deve receber somente:

Dados preparados.

O algoritmo não deve receber:

- arquivo;
- configuração;
- parâmetros de geração;
- informações de interface.

---

# Contrato com Estatisticas

## Objetivo

Permitir que o módulo estatístico conheça características da entrada.

---

# Comunicação

Origem:

entradaDados

Destino:

estatisticas

Tipo:

Event

---

# Evento Gerado

Evento:

EntradaPreparada

---

# Informações Produzidas

O evento pode conter:

- quantidade de elementos;
- tipo de entrada;
- origem;
- configuração utilizada.

---

# Motivo do Evento

O módulo de estatísticas deve conseguir relacionar:

Entrada

+

Algoritmo

+

Resultado

para análise posterior.

---

# Contrato de Validação

## Objetivo

Garantir que todas as entradas sejam verificadas antes do processamento.

---

# Comunicação

Origem:

entradaDados

Destino:

validacoes

Tipo:

Request

---

# Solicitação

Envia:

- valores recebidos;
- configuração;
- informações da entrada.

---

# Resposta

Origem:

validacoes

Destino:

entradaDados

Tipo:

Response

---

# Resultado

Retorna:

Entrada válida

ou

erro de validação.

---

# Matriz de Comunicação do Módulo

| Origem | Destino | Tipo | Objetivo |
|---|---|---|---|
| aplicacao | entradaDados | Request | Solicitar entrada |
| entradaDados | aplicacao | Response | Retornar dados preparados |
| aplicacao | GeradorDados | Request | Solicitar geração |
| GeradorDados | entradaDados | Response | Retornar dados criados |
| LeitorArquivoEntrada | PreparadorEntrada | Request | Solicitar preparação |
| PreparadorEntrada | entradaDados | Response | Retornar modelo padronizado |
| entradaDados | algoritmosOrdenacao | Response | Entregar dados |
| entradaDados | estatisticas | Event | Informar características da entrada |
| entradaDados | validacoes | Request | Validar dados |

---

# Regras dos Contratos

## Regra 01 — Padronização

Toda origem deve produzir:

DadosEntrada

---

## Regra 02 — Independência

Os consumidores não devem conhecer a origem dos dados.

---

## Regra 03 — Validação Antes da Execução

Nenhuma entrada inválida deve chegar aos algoritmos.

---

## Regra 04 — Contratos Estáveis

Alterações internas não devem modificar a comunicação externa.

---

# Evolução dos Contratos

## V1.0

Contratos definidos:

- geração;
- leitura;
- preparação;
- entrega aos algoritmos;
- comunicação estatística.

---

## V2.0

Possíveis extensões:

- contratos para persistência;
- importação de novos formatos;
- experimentos automatizados.

---

## V3.0

Possíveis extensões:

- API externa;
- interface gráfica;
- integração distribuída.

---

# Considerações da Parte

Os contratos do módulo `entradaDados` estabelecem uma comunicação organizada entre os componentes do LAB EDU SORT V1.0.

A arquitetura garante que:

- diferentes fontes produzam o mesmo modelo;
- algoritmos permaneçam independentes;
- estatísticas recebam informações suficientes;
- novas formas de entrada possam ser adicionadas.

O módulo passa a funcionar como uma camada de adaptação entre o mundo externo e o domínio dos algoritmos, mantendo os princípios fundamentais do projeto:

- baixo acoplamento;
- alta coesão;
- extensibilidade;
- clareza arquitetural.

---

# Parte VI — Validações e Regras de Entrada

Esta seção apresenta as validações e regras aplicadas ao módulo `entradaDados` do **LAB EDU SORT V1.0**.

O objetivo é garantir que todos os dados utilizados pelos algoritmos de ordenação estejam em condições adequadas de processamento, evitando inconsistências, erros de execução e resultados inválidos.

As validações representam uma etapa fundamental da arquitetura porque estabelecem uma barreira entre:

Dados externos

e

Dados confiáveis para processamento.

Fluxo:

Entrada recebida

↓

Validação

↓

Preparação

↓

DadosEntrada

↓

AlgoritmosOrdenacao

---

# Objetivo das Validações

As validações do módulo `entradaDados` possuem como objetivos:

- garantir integridade dos dados;
- evitar entradas inválidas;
- proteger os algoritmos contra informações inconsistentes;
- padronizar comportamentos;
- facilitar identificação de erros.

---

# Princípio Fundamental

O módulo segue a regra:

"Nenhum dado deve ser processado antes de ser validado."

Isso significa que:

- arquivos devem ser verificados;
- configurações devem ser analisadas;
- valores devem ser conferidos;
- estruturas devem ser validadas.

---

# Tipos de Validação

As validações serão organizadas em categorias:

- validação da configuração;
- validação dos dados;
- validação dos arquivos;
- validação estrutural;
- validação de consistência.

---

# Validação da Configuração de Entrada

A configuração define como uma entrada será criada ou carregada.

Antes da geração ou leitura, ela deve ser validada.

---

# Quantidade de Elementos

Regra:

A quantidade de elementos deve ser um valor positivo.

Exemplos inválidos:

Quantidade:

0

ou

Quantidade:

-100

---

# Comportamento Esperado

Caso a quantidade seja inválida:

- a operação deve ser interrompida;
- uma exceção deve ser gerada;
- uma mensagem clara deve ser apresentada.

---

# Intervalo de Valores

A configuração deve garantir que:

valorMinimo

seja menor ou igual a:

valorMaximo

---

# Exemplos Inválidos

valorMinimo:

100

valorMaximo:

10

---

# Comportamento Esperado

A configuração deve ser rejeitada.

---

# Tipo de Geração

O tipo de geração deve pertencer ao conjunto permitido.

Valores aceitos:

- ALEATORIA;
- ORDENADA;
- INVERTIDA;
- PARCIALMENTE_DESORDENADA.

---

# Grau de Desordenação

Quando utilizado, deve respeitar o intervalo:

0%

até

100%

---

# Exemplos Inválidos

-10%

150%

---

# Validação dos Dados Recebidos

Após geração ou leitura, os dados devem ser analisados.

---

# Validação da Estrutura

A entrada deve possuir:

- lista de valores;
- quantidade definida;
- informações de origem;
- tipo de entrada.

---

# Exemplo Inválido

DadosEntrada

sem:

quantidadeElementos

---

# Validação dos Valores

Os elementos devem possuir tipos compatíveis.

Na V1.0:

Tipo esperado:

inteiro

---

# Exemplos Inválidos

Valores:

"ABC"

ou

3.14

---

# Validação da Quantidade

A quantidade declarada deve corresponder ao número real de elementos.

Exemplo:

Metadado:

Quantidade:

10

Lista:

8 elementos

Resultado:

Entrada inválida.

---

# Validação de Dados Vazios

Uma entrada vazia não deve ser processada.

Exemplo:

Lista:

[]

---

# Comportamento Esperado

Gerar erro:

Entrada sem elementos.

---

# Validação de Arquivos

Quando a origem for arquivo, regras adicionais são aplicadas.

---

# Existência do Arquivo

Antes da leitura:

o sistema deve verificar se o arquivo existe.

---

# Caso Inválido

Arquivo inexistente.

Resultado:

Erro de entrada.

---

# Permissão de Leitura

O arquivo deve possuir permissão adequada.

---

# Caso Inválido

Arquivo sem acesso.

Resultado:

Falha de leitura.

---

# Formato do Arquivo

O arquivo deve estar em formato suportado.

Exemplos:

- CSV;
- TXT.

---

# Caso Inválido

Arquivo com estrutura incompatível.

---

# Conteúdo do Arquivo

O conteúdo deve conter apenas valores válidos.

Exemplo inválido:

10;20;ABC;40

---

# Validação de Consistência

Além das validações individuais, o conjunto completo deve ser consistente.

---

# Regra de Origem

Toda entrada deve possuir uma origem definida.

Valores possíveis:

- MANUAL;
- ARQUIVO;
- GERADA;
- TESTE.

---

# Regra de Tipo de Entrada

Toda entrada deve informar seu estado inicial.

Valores possíveis:

- ORDENADA;
- INVERTIDA;
- ALEATORIA;
- PARCIALMENTE_DESORDENADA.

---

# Regra de Configuração

Quando uma entrada for gerada automaticamente, deve possuir configuração associada.

Exemplo:

Entrada gerada

sem configuração

Resultado:

Entrada inconsistente.

---

# Validação Antes do Algoritmo

O módulo `algoritmosOrdenacao` deve receber apenas entradas aprovadas.

Fluxo correto:

Dados recebidos

↓

Validação

↓

DadosEntrada válido

↓

Algoritmo

---

# Fluxo de Tratamento de Erros

Quando uma validação falhar:

Entrada

↓

Validador

↓

Erro identificado

↓

ExcecaoEntrada

↓

Aplicacao

---

# Exceções Relacionadas

Possíveis exceções do módulo:

- EntradaInvalidaException;
- ArquivoEntradaException;
- ConfiguracaoEntradaException;
- FormatoEntradaException.

---

# Responsabilidade das Exceções

As exceções devem:

- indicar o problema;
- facilitar diagnóstico;
- evitar falhas silenciosas.

---

# Mensagens de Erro

As mensagens devem ser claras.

Exemplos:

"Quantidade de elementos deve ser maior que zero."

"Arquivo informado não foi encontrado."

"Formato de entrada não suportado."

---

# Matriz de Validação

| Elemento | Validação | Resultado |
|---|---|---|
| quantidade | valor positivo | Entrada válida |
| valores | tipo correto | Entrada válida |
| arquivo | existência | Leitura permitida |
| configuração | parâmetros consistentes | Geração permitida |
| tipo entrada | valor permitido | Processamento permitido |

---

# Responsabilidades por Classe

## ConfiguracaoEntrada

Responsável por:

- validar parâmetros de criação.

---

## LeitorArquivoEntrada

Responsável por:

- validar arquivos externos.

---

## PreparadorEntrada

Responsável por:

- validar estrutura final.

---

## Validacoes

Responsável por:

- regras compartilhadas.

---

# Regras Arquiteturais

## Regra 01 — Validar antes de processar

Nenhum algoritmo recebe dados sem validação.

---

## Regra 02 — Centralizar validações

Regras comuns não devem ser duplicadas.

---

## Regra 03 — Mensagens claras

Erros devem facilitar correção.

---

## Regra 04 — Não esconder falhas

Problemas devem ser informados explicitamente.

---

# Evolução das Validações

## V1.0

Validações previstas:

- tipos;
- quantidade;
- arquivos;
- configurações;
- estrutura.

---

## V2.0

Possíveis evoluções:

- validação de grandes volumes;
- validação estatística;
- regras configuráveis.

---

## V3.0

Possíveis evoluções:

- validação distribuída;
- regras externas;
- validação por perfil de usuário.

---

# Considerações da Parte

As validações do módulo `entradaDados` garantem que somente dados consistentes participem do fluxo de execução do LAB EDU SORT V1.0.

A arquitetura estabelece uma separação clara:

Dados externos

↓

Validação

↓

Modelo interno confiável

↓

Processamento

Essa abordagem reduz erros, melhora a confiabilidade dos experimentos e mantém os algoritmos independentes das particularidades das fontes de entrada.

O módulo permanece alinhado aos princípios do projeto:

- segurança dos dados;
- previsibilidade;
- modularidade;
- baixo acoplamento;
- facilidade de evolução.

---

# Parte VII — Fluxos de Entrada de Dados

Esta seção apresenta os principais fluxos de entrada de dados do **LAB EDU SORT V1.0**.

O objetivo é documentar como os dados percorrem o sistema desde sua origem até sua entrega aos algoritmos de ordenação, considerando:

- geração automática;
- leitura de arquivos;
- entradas parcialmente desordenadas;
- validações;
- preparação;
- comunicação entre módulos.

A definição destes fluxos garante que todas as formas de entrada sigam o mesmo padrão arquitetural.

---

# Visão Geral do Fluxo de Entrada

Independentemente da origem, todas as entradas seguem um fluxo comum:

Origem dos Dados

↓

Validação Inicial

↓

Preparação

↓

Modelo DadosEntrada

↓

Entrega ao Algoritmo

↓

Coleta Estatística

---

# Princípio de Padronização dos Fluxos

O módulo `entradaDados` deve garantir que diferentes origens produzam o mesmo resultado estrutural.

Exemplo:

Arquivo CSV

↓

DadosEntrada


Geração automática

↓

DadosEntrada


Entrada manual

↓

DadosEntrada

---

# Fluxo de Geração Automática

O fluxo de geração automática é utilizado quando o usuário deseja criar conjuntos de dados controlados pelo sistema.

Esse fluxo permite experimentos reproduzíveis e comparação entre algoritmos.

---

# Objetivo

Criar uma entrada conforme uma configuração definida.

Exemplos:

- quantidade de elementos;
- intervalo de valores;
- tipo de distribuição;
- grau de desordenação.

---

# Comunicação do Fluxo

Aplicacao

↓

Request

↓

GeradorDados


GeradorDados

↓

Response

↓

Aplicacao


entradaDados

↓

Event

↓

estatisticas

---

# Etapas do Fluxo

## Etapa 01 — Solicitação

A aplicação recebe a solicitação do usuário.

Informações:

- algoritmo escolhido;
- quantidade de elementos;
- tipo de entrada.

---

## Etapa 02 — Criação da Configuração

A aplicação cria uma:

ConfiguracaoEntrada

contendo:

- quantidade;
- intervalo;
- estratégia de geração.

---

## Etapa 03 — Validação da Configuração

A configuração é analisada.

São verificadas:

- quantidade válida;
- intervalo correto;
- tipo permitido.

---

## Etapa 04 — Geração dos Dados

O:

GeradorDados

executa a criação dos valores.

---

## Etapa 05 — Construção do Modelo

Os dados são encapsulados em:

DadosEntrada

contendo:

- valores;
- origem;
- tipo;
- configuração.

---

## Etapa 06 — Entrega

O objeto:

DadosEntrada

é enviado para:

algoritmosOrdenacao

---

# Fluxo Completo de Geração

Configuração

↓

ConfiguracaoEntrada

↓

Validação

↓

GeradorDados

↓

DadosEntrada

↓

Algoritmo

---

# Fluxo de Leitura de Arquivo

O fluxo de arquivo permite utilizar dados previamente preparados.

É utilizado principalmente para:

- experimentos;
- testes repetíveis;
- comparação entre execuções.

---

# Objetivo

Converter dados externos em uma estrutura interna compatível.

---

# Comunicação do Fluxo

Aplicacao

↓

Request

↓

LeitorArquivoEntrada


LeitorArquivoEntrada

↓

Request

↓

PreparadorEntrada


PreparadorEntrada

↓

Response

↓

Aplicacao

---

# Etapas do Fluxo

## Etapa 01 — Solicitação do Arquivo

A aplicação recebe:

- caminho do arquivo;
- formato esperado.

---

## Etapa 02 — Localização do Arquivo

O leitor verifica:

- existência;
- permissão;
- extensão.

---

## Etapa 03 — Leitura dos Dados

O conteúdo é carregado.

Exemplo:

Arquivo:

dados.csv

Conteúdo:

10;20;30;40

---

## Etapa 04 — Conversão

Os valores são convertidos para estruturas internas.

---

## Etapa 05 — Preparação

O:

PreparadorEntrada

realiza:

- normalização;
- validação;
- criação do modelo.

---

## Etapa 06 — Entrega

Resultado:

DadosEntrada

---

# Fluxo Completo de Arquivo

Arquivo

↓

LeitorArquivoEntrada

↓

Validação

↓

PreparadorEntrada

↓

DadosEntrada

↓

Algoritmo

---

# Fluxo de Entrada Parcialmente Desordenada

Este fluxo representa uma situação intermediária entre:

- totalmente ordenado;
- totalmente aleatório.

É importante para avaliar algoritmos adaptativos.

Exemplo:

Entrada original:

[1,2,3,4,5,6,7]

Aplicação de perturbações:

[1,5,3,4,2,6,7]

---

# Objetivo

Criar dados com determinado grau de desordenação.

---

# Comunicação do Fluxo

Aplicacao

↓

Request

↓

GeradorDados


GeradorDados

↓

Response

↓

DadosEntrada

---

# Etapas do Fluxo

## Etapa 01 — Definição do Grau

Usuário informa:

Percentual de desordenação.

Exemplo:

30%

---

## Etapa 02 — Criação da Entrada Base

O sistema cria uma lista ordenada inicial.

Exemplo:

[1,2,3,4,5,6,7]

---

## Etapa 03 — Aplicação das Alterações

O gerador modifica parcialmente a ordem.

---

## Etapa 04 — Classificação

A entrada recebe:

Tipo:

PARCIALMENTE_DESORDENADA

---

## Etapa 05 — Entrega

Resultado:

DadosEntrada

---

# Fluxo Completo Parcial

Configuração

↓

Entrada Ordenada

↓

Perturbações Controladas

↓

Validação

↓

DadosEntrada

↓

Algoritmo

---

# Fluxo de Entrada Manual

Embora não seja prioridade inicial da V1.0, o modelo permite entrada manual.

---

# Comunicação

Usuário

↓

Aplicacao

↓

entradaDados

---

# Etapas

## Recebimento

Usuário informa valores.

---

## Validação

Sistema verifica:

- tipos;
- quantidade;
- valores.

---

## Preparação

Criação do:

DadosEntrada

---

# Matriz Geral de Comunicação

| Origem | Destino | Tipo | Objetivo |
|---|---|---|---|
| Usuário | Aplicacao | Request | Informar entrada |
| Aplicacao | entradaDados | Request | Solicitar dados |
| Aplicacao | GeradorDados | Request | Gerar dados |
| GeradorDados | Aplicacao | Response | Retornar dados |
| LeitorArquivoEntrada | PreparadorEntrada | Request | Preparar dados |
| PreparadorEntrada | Aplicacao | Response | Entregar entrada |
| entradaDados | AlgoritmosOrdenacao | Response | Fornecer dados |
| entradaDados | Estatisticas | Event | Informar características |

---

# Estados da Entrada

Durante o fluxo, a entrada pode assumir estados:

---

# Estado 01 — Recebida

Dados foram obtidos da origem.

---

# Estado 02 — Validando

Dados estão sendo analisados.

---

# Estado 03 — Preparada

Dados estão no modelo interno.

---

# Estado 04 — Disponível

Dados podem ser enviados ao algoritmo.

---

# Estado 05 — Processada

Algoritmo já utilizou os dados.

---

# Regras dos Fluxos

## Regra 01 — Toda entrada deve passar por validação

Nenhum fluxo pode ignorar esta etapa.

---

## Regra 02 — Todos os fluxos devem gerar DadosEntrada

A origem não influencia o contrato final.

---

## Regra 03 — Algoritmos recebem apenas entradas preparadas

Detalhes de criação permanecem isolados.

---

## Regra 04 — Estatísticas recebem contexto da entrada

A análise deve considerar as características do conjunto utilizado.

---

# Evolução dos Fluxos

## V1.0

Fluxos previstos:

- geração automática;
- arquivo;
- entrada manual básica.

---

## V2.0

Possíveis evoluções:

- múltiplas fontes simultâneas;
- experimentos automatizados;
- carregamento em lote.

---

## V3.0

Possíveis evoluções:

- integração externa;
- interface gráfica;
- fluxo interativo.

---

# Considerações da Parte

Os fluxos de entrada definidos estabelecem uma arquitetura uniforme para aquisição e preparação dos dados.

Independentemente da origem, o caminho permanece:

Origem

↓

Validação

↓

Preparação

↓

DadosEntrada

↓

Algoritmos

↓

Estatísticas

Essa padronização permite que novos formatos de entrada sejam adicionados sem impacto nos módulos existentes.

O módulo `entradaDados` funciona como uma camada de adaptação entre o usuário e o domínio dos algoritmos, garantindo:

- consistência;
- rastreabilidade;
- flexibilidade;
- evolução arquitetural.

---

# Parte VIII — Estruturas de Dados Utilizadas

Esta seção apresenta as estruturas de dados utilizadas pelo módulo `entradaDados` do **LAB EDU SORT V1.0**.

O objetivo é documentar as estruturas escolhidas para representar:

- valores de entrada;
- configurações;
- metadados;
- estados de processamento;
- informações auxiliares.

A escolha das estruturas segue os princípios definidos no projeto:

- simplicidade;
- clareza;
- eficiência;
- adequação ao domínio;
- facilidade de manutenção.

---

# Objetivo das Estruturas de Entrada

As estruturas utilizadas pelo módulo devem permitir:

- armazenar conjuntos de dados;
- preservar informações contextuais;
- facilitar validações;
- permitir comunicação entre módulos;
- preparar os dados para os algoritmos de ordenação.

---

# Princípio de Escolha das Estruturas

A estrutura deve ser escolhida considerando:

- comportamento esperado;
- operações realizadas;
- necessidade de alteração;
- facilidade de leitura;
- compatibilidade com algoritmos.

---

# Estrutura Principal — Lista de Valores

A estrutura principal do módulo é uma lista de elementos.

Representação conceitual:

DadosEntrada

↓

valores

↓

Lista de elementos

---

# Motivo da Escolha

A lista foi escolhida porque:

- representa naturalmente uma sequência;
- mantém ordem dos elementos;
- possui acesso sequencial;
- é compatível com todos os algoritmos de ordenação.

---

# Operações Principais

A lista permite:

- percorrer elementos;
- comparar valores;
- trocar posições;
- movimentar elementos;
- aplicar algoritmos de ordenação.

---

# Aplicação no Projeto

Exemplo conceitual:

DadosEntrada

valores:

[10, 4, 8, 2, 6]

---

# Relação com Algoritmos de Ordenação

A lista de entrada será diretamente utilizada pelos algoritmos.

Exemplo:

Bubble Sort:

Lista

↓

Comparações

↓

Trocas

↓

Lista Ordenada

---

# Estrutura de Metadados

Além dos valores, cada entrada possui informações complementares.

Essas informações são representadas como atributos do modelo.

---

# Metadados Principais

DadosEntrada

possui:

- quantidadeElementos;
- origem;
- tipoEntrada;
- configuração.

---

# Quantidade de Elementos

Representa o tamanho da entrada.

Estrutura:

Inteiro

---

# Justificativa

O valor é armazenado separadamente porque:

- evita cálculo repetido;
- facilita relatórios;
- permite validação rápida.

---

# Origem da Entrada

Representa a procedência dos dados.

Estrutura conceitual:

Enumerador

Valores:

- MANUAL;
- ARQUIVO;
- GERADA;
- TESTE.

---

# Justificativa

O uso de valores controlados evita:

- textos inconsistentes;
- erros de comparação;
- duplicidade de informações.

---

# Tipo da Entrada

Representa o comportamento inicial dos dados.

Estrutura conceitual:

Enumerador

Valores:

- ORDENADA;
- INVERTIDA;
- ALEATORIA;
- PARCIALMENTE_DESORDENADA.

---

# Justificativa

Permite identificar o cenário experimental utilizado.

---

# Estrutura de Configuração

A configuração da entrada será representada por uma classe específica.

Estrutura:

ConfiguracaoEntrada

contém:

- quantidade;
- intervalo;
- tipo de geração;
- grau de desordenação.

---

# Motivo da Separação

A configuração não deve ser misturada com os dados.

Exemplo:

Configuração:

Criar 1000 elementos aleatórios.

Dados:

[453, 21, 987, ...]

---

# Estrutura de Intervalos

O intervalo de geração será representado por dois valores.

Estrutura:

valorMinimo

+

valorMaximo

---

# Justificativa

Essa abordagem:

- é simples;
- reduz complexidade;
- atende a V1.0.

---

# Estrutura de Estado da Entrada

O fluxo de entrada necessita controlar a situação atual dos dados.

Estados possíveis:

- RECEBIDA;
- VALIDANDO;
- PREPARADA;
- DISPONIVEL;
- PROCESSADA.

---

# Representação

Estrutura conceitual:

EnumeradorEstadoEntrada

---

# Justificativa

Evita estados representados por textos livres.

---

# Estruturas Auxiliares

O módulo poderá utilizar estruturas auxiliares para processamento interno.

---

# Estruturas Temporárias

Utilizadas durante:

- leitura;
- conversão;
- preparação.

Exemplos:

- listas temporárias;
- buffers de leitura;
- coleções auxiliares.

---

# Uso Controlado

Essas estruturas não fazem parte do contrato externo.

Elas existem apenas dentro do módulo.

---

# Estrutura de Configuração de Experimento

Para evolução futura, poderá existir uma estrutura agrupando informações experimentais.

Exemplo conceitual:

ConfiguracaoExperimento

contendo:

- algoritmo;
- entrada;
- quantidade;
- repetição.

---

# Uso Futuro

Essa estrutura poderá apoiar:

- comparações automáticas;
- execução em lote;
- relatórios estatísticos.

---

# Estruturas Não Utilizadas na V1.0

Algumas estruturas foram consideradas, porém não serão utilizadas inicialmente.

---

# Banco de Dados

Não utilizado.

Motivo:

A V1.0 trabalha com execução local e temporária.

---

# Estruturas em Árvore

Não utilizadas.

Motivo:

O domínio inicial envolve sequências lineares.

---

# Grafos

Não utilizados.

Motivo:

Não representam o problema atual.

---

# Filas e Pilhas

Não utilizadas como estruturas principais.

Motivo:

A ordenação trabalha diretamente sobre sequências.

---

# Critérios de Escolha das Estruturas

As decisões seguem:

---

# Simplicidade

Utilizar estruturas fáceis de compreender pelos estudantes.

---

# Compatibilidade

As estruturas devem funcionar com todos os algoritmos de ordenação.

---

# Desempenho

Evitar estruturas que adicionem complexidade desnecessária.

---

# Manutenção

A estrutura deve facilitar evolução futura.

---

# Relação com Outros Módulos

## AlgoritmosOrdenacao

Recebem:

Lista de valores.

---

## Estatisticas

Recebem:

Metadados da entrada.

---

## Relatorios

Recebem:

Informações consolidadas.

---

## Visualizacoes

Recebem:

Dados preparados para apresentação.

---

# Fluxo das Estruturas

Configuração

↓

ConfiguracaoEntrada

↓

Gerador ou Leitor

↓

Lista de valores

↓

DadosEntrada

↓

Algoritmo

↓

Resultado

---

# Regras Arquiteturais

## Regra 01 — Dados e configuração separados

A configuração define.

Os dados armazenam.

---

## Regra 02 — Estruturas internas não vazam

Detalhes de implementação permanecem encapsulados.

---

## Regra 03 — Contratos utilizam modelos estáveis

A comunicação utiliza:

DadosEntrada

e não estruturas temporárias.

---

# Evolução das Estruturas

## V1.0

Estruturas:

- listas;
- atributos simples;
- enumeradores;
- classes de modelo.

---

## V2.0

Possíveis evoluções:

- estruturas persistentes;
- histórico de experimentos;
- armazenamento estruturado.

---

## V3.0

Possíveis evoluções:

- grandes volumes;
- processamento distribuído;
- estruturas especializadas.

---

# Considerações da Parte

As estruturas de dados definidas para o módulo `entradaDados` foram escolhidas para equilibrar:

- simplicidade educacional;
- eficiência computacional;
- clareza arquitetural.

A decisão principal foi utilizar uma estrutura baseada em listas associadas a modelos orientados a objetos.

Essa escolha mantém o projeto alinhado com seus objetivos:

- ensinar algoritmos de ordenação;
- permitir experimentação;
- facilitar análise de desempenho;
- possibilitar evolução futura.

O módulo permanece preparado para crescimento sem introduzir complexidade prematura.

---

# Parte IX — Diagramas e Arquitetura

Esta seção apresenta os diagramas arquiteturais e os principais fluxos do módulo `entradaDados` do **LAB EDU SORT V1.0**.

O objetivo é consolidar visualmente:

- responsabilidades das classes;
- comunicação entre módulos;
- fluxo completo dos dados;
- dependências permitidas;
- isolamento arquitetural.

Os diagramas representam a arquitetura lógica do módulo e servem como referência para implementação e evolução.

---

# Visão Arquitetural do Módulo entradaDados

O módulo `entradaDados` funciona como uma camada intermediária entre:

- fontes externas de dados;
- aplicação;
- algoritmos de ordenação;
- módulo de estatísticas.

Responsabilidade principal:

Receber, validar, preparar e entregar dados padronizados.

---

# Arquitetura Geral

Fluxo principal:

Usuário

↓

Aplicacao

↓

entradaDados

↓

DadosEntrada

↓

algoritmosOrdenacao

↓

estatisticas

---

# Responsabilidades por Camada

## Camada de Entrada

Responsável por:

- receber informações externas;
- interpretar solicitações;
- iniciar fluxo.

Componentes:

- Aplicacao;
- Interface de usuário.

---

## Camada entradaDados

Responsável por:

- gerar dados;
- carregar arquivos;
- validar;
- preparar modelo.

Componentes:

- ConfiguracaoEntrada;
- GeradorDados;
- LeitorArquivoEntrada;
- PreparadorEntrada;
- DadosEntrada.

---

## Camada de Domínio

Responsável por:

- executar ordenações;
- coletar métricas;
- gerar análises.

Componentes:

- AlgoritmosOrdenacao;
- Estatisticas.

---

# Diagrama de Componentes

Representação conceitual:

Aplicacao

|

| Request

v

entradaDados

|

+-----------------------------+

|                             |

v                             v

GeradorDados          LeitorArquivoEntrada

|                             |

|                             v

|                    PreparadorEntrada

|                             |

+-------------+---------------+

              |

              v

        DadosEntrada

              |

              |

              v

    algoritmosOrdenacao

              |

              v

        estatisticas

---

# Diagrama de Classes Simplificado

Modelo:

DadosEntrada

Responsabilidade:

Representar dados preparados.

Relacionamentos:

recebe:

ConfiguracaoEntrada


é utilizado por:

AlgoritmosOrdenacao

Estatisticas


---

ConfiguracaoEntrada

Responsabilidade:

Definir regras de criação.

Utilizado por:

GeradorDados

---

GeradorDados

Responsabilidade:

Criar entradas.

Depende de:

ConfiguracaoEntrada

Produz:

DadosEntrada

---

LeitorArquivoEntrada

Responsabilidade:

Carregar dados externos.

Produz:

DadosEntrada

---

PreparadorEntrada

Responsabilidade:

Normalizar dados.

Recebe:

Dados brutos

Produz:

DadosEntrada

---

# Diagrama de Sequência — Geração Automática

Fluxo:

1. Usuário solicita criação de dados.

2. Aplicacao cria ConfiguracaoEntrada.

3. Configuração é validada.

4. GeradorDados recebe solicitação.

5. GeradorDados cria valores.

6. DadosEntrada é criado.

7. Entrada é enviada ao algoritmo.

---

Representação:

Usuário

↓

Aplicacao

↓

ConfiguracaoEntrada

↓

GeradorDados

↓

DadosEntrada

↓

AlgoritmoOrdenacao

---

# Diagrama de Sequência — Leitura de Arquivo

Fluxo:

1. Usuário informa arquivo.

2. Aplicacao solicita leitura.

3. LeitorArquivoEntrada acessa arquivo.

4. Dados são convertidos.

5. PreparadorEntrada normaliza.

6. DadosEntrada é criado.

7. Algoritmo recebe dados.

---

Representação:

Usuário

↓

Aplicacao

↓

LeitorArquivoEntrada

↓

PreparadorEntrada

↓

DadosEntrada

↓

AlgoritmoOrdenacao

---

# Diagrama de Comunicação entre Módulos

Módulos:

Aplicacao

entradaDados

validacoes

algoritmosOrdenacao

estatisticas


Comunicação:

Aplicacao

↓

Request

↓

entradaDados


entradaDados

↓

Request

↓

validacoes


validacoes

↓

Response

↓

entradaDados


entradaDados

↓

Response

↓

algoritmosOrdenacao


entradaDados

↓

Event

↓

estatisticas

---

# Matriz Arquitetural de Comunicação

| Origem | Destino | Tipo | Responsabilidade |
|---|---|---|---|
| Aplicacao | entradaDados | Request | Solicitar entrada |
| entradaDados | Validacoes | Request | Validar dados |
| Validacoes | entradaDados | Response | Informar resultado |
| entradaDados | AlgoritmosOrdenacao | Response | Entregar dados |
| entradaDados | Estatisticas | Event | Informar características |
| GeradorDados | DadosEntrada | Response | Criar modelo |
| LeitorArquivoEntrada | PreparadorEntrada | Request | Preparar dados |

---

# Diagrama de Estados da Entrada

A entrada possui um ciclo de vida.

Estados:

RECEBIDA

↓

VALIDANDO

↓

PREPARADA

↓

DISPONIVEL

↓

PROCESSADA

---

# Descrição dos Estados

## RECEBIDA

Dados foram obtidos da origem.

---

## VALIDANDO

Dados estão sendo analisados.

---

## PREPARADA

Modelo interno foi criado.

---

## DISPONIVEL

Dados podem ser utilizados.

---

## PROCESSADA

Algoritmo finalizou utilização.

---

# Diagrama de Dependências

Dependências permitidas:

ConfiguracaoEntrada

↓

GeradorDados


GeradorDados

↓

DadosEntrada


LeitorArquivoEntrada

↓

PreparadorEntrada

↓

DadosEntrada


DadosEntrada

↓

AlgoritmosOrdenacao


DadosEntrada

↓

Estatisticas

---

# Dependências Proibidas

Não permitido:

AlgoritmosOrdenacao

↓

GeradorDados

Motivo:

Algoritmos não devem conhecer origem dos dados.

---

Não permitido:

DadosEntrada

↓

GeradorDados

Motivo:

Modelo de dados não deve criar informações.

---

Não permitido:

Estatisticas

↓

LeitorArquivoEntrada

Motivo:

Estatísticas não devem depender da origem.

---

# Princípios Arquiteturais Aplicados

## Separação de Responsabilidades

Cada classe possui uma função específica.

---

## Encapsulamento

Detalhes internos permanecem protegidos.

---

## Baixo Acoplamento

Módulos dependem de contratos.

---

## Alta Coesão

Classes possuem responsabilidades relacionadas.

---

## Evolução Incremental

Novas funcionalidades podem ser adicionadas sem reestruturação.

---

# Evolução Arquitetural

## V1.0

Arquitetura:

Entrada local

↓

DadosEntrada

↓

Algoritmos

↓

Estatísticas

---

## V2.0

Possíveis evoluções:

- novos formatos de arquivo;
- persistência;
- execução automatizada.

---

## V3.0

Possíveis evoluções:

- API;
- interface gráfica;
- processamento distribuído.

---

# Considerações da Parte

Os diagramas apresentados consolidam a arquitetura do módulo `entradaDados`.

A arquitetura definida estabelece um fluxo claro:

Origem

↓

Entrada

↓

Validação

↓

Preparação

↓

Modelo interno

↓

Algoritmos

↓

Análise

Essa organização garante que:

- os algoritmos permaneçam independentes;
- as entradas sejam padronizadas;
- novos formatos possam ser incorporados;
- a comunicação entre módulos seja previsível.

O módulo `entradaDados` torna-se uma camada de adaptação responsável por transformar informações externas em dados confiáveis para o domínio de ordenação.

---

# Parte X — Evolução e Considerações Finais

Esta seção apresenta a visão de evolução do módulo `entradaDados` do **LAB EDU SORT V1.0**, consolidando as decisões arquiteturais tomadas e estabelecendo possíveis caminhos futuros.

O objetivo é registrar:

- estado atual do módulo;
- funcionalidades previstas;
- possibilidades de expansão;
- princípios que devem ser preservados;
- conclusão arquitetural.

O módulo `entradaDados` foi projetado para ser uma camada flexível de adaptação entre diferentes fontes de dados e os algoritmos de ordenação.

---

# Estado Atual do Módulo na V1.0

Na primeira versão do projeto, o módulo contempla:

- criação de entradas em memória;
- geração automática de dados;
- leitura de arquivos simples;
- validação das informações;
- preparação dos dados;
- entrega de um modelo padronizado.

O fluxo consolidado é:

Origem dos Dados

↓

Validação

↓

Preparação

↓

DadosEntrada

↓

AlgoritmosOrdenacao

↓

Estatisticas

---

# Componentes Implementados na V1.0

Classes previstas:

## DadosEntrada

Responsável por representar os dados preparados.

---

## ConfiguracaoEntrada

Responsável por armazenar parâmetros de criação ou carregamento.

---

## GeradorDados

Responsável pela geração automática dos conjuntos.

---

## LeitorArquivoEntrada

Responsável pela leitura de dados externos.

---

## PreparadorEntrada

Responsável pela normalização e criação do modelo final.

---

# Princípios Mantidos

O desenvolvimento do módulo segue os princípios arquiteturais definidos no projeto.

---

# Separação de Responsabilidades

Cada componente possui uma função específica.

Exemplo:

GeradorDados:

cria dados.

PreparadorEntrada:

normaliza dados.

DadosEntrada:

representa dados.

---

# Independência dos Algoritmos

Os algoritmos de ordenação não conhecem:

- arquivos;
- geração;
- configuração;
- validação.

Eles recebem somente:

DadosEntrada.

---

# Padronização das Entradas

Todas as fontes de dados convergem para o mesmo modelo.

Exemplo:

Arquivo

↓

DadosEntrada


Geração

↓

DadosEntrada


Entrada manual

↓

DadosEntrada

---

# Baixo Acoplamento

As classes se comunicam através de contratos definidos.

Alterações internas não devem afetar consumidores externos.

---

# Evolução Planejada

A arquitetura foi preparada para crescimento gradual.

---

# Evolução V1.1

Possíveis melhorias:

- melhorias nas mensagens de erro;
- expansão dos validadores;
- novos formatos de arquivo;
- melhorias na documentação.

---

# Evolução V2.0

Possíveis funcionalidades:

- carregamento de arquivos JSON;
- integração com banco de dados;
- geração de grandes volumes;
- execução de experimentos automatizados;
- histórico de entradas utilizadas.

---

# Evolução V3.0

Possíveis funcionalidades:

- API de entrada de dados;
- interface gráfica;
- processamento paralelo;
- ambiente completo de experimentação.

---

# Novas Fontes de Entrada

A arquitetura permite adicionar novas fontes sem modificar os algoritmos.

Possíveis exemplos:

- banco de dados;
- arquivos XML;
- APIs externas;
- sensores;
- streams de dados.

---

# Estratégia de Evolução

A inclusão de novas fontes deve seguir o fluxo:

Nova Fonte

↓

Conversor

↓

Validação

↓

DadosEntrada

↓

Algoritmos

---

# Melhorias Futuras de Validação

Possíveis evoluções:

- validações configuráveis;
- regras específicas por experimento;
- validação estatística;
- validação de grandes volumes.

---

# Melhorias Futuras de Desempenho

Possíveis otimizações:

- leitura em blocos;
- geração paralela;
- redução de cópias temporárias;
- processamento incremental.

---

# Melhorias Futuras de Experimentação

O módulo poderá evoluir para suportar:

- conjuntos padronizados;
- baterias de testes;
- comparação automática;
- reprodução de cenários.

---

# Integração com Estatísticas

A evolução futura poderá ampliar a comunicação com o módulo `estatisticas`.

Possibilidades:

- registrar características detalhadas da entrada;
- associar entrada e algoritmo;
- comparar diferentes cenários;
- gerar relatórios completos.

---

# Integração com Visualizações

O módulo poderá fornecer informações para representação gráfica.

Exemplos:

- tamanho da entrada;
- distribuição dos valores;
- estado inicial;
- evolução durante ordenação.

---

# Regras para Evolução do Módulo

Qualquer alteração futura deve respeitar:

---

# Regra 01 — Preservar o Contrato DadosEntrada

Novas funcionalidades não devem quebrar o modelo principal.

---

# Regra 02 — Evitar Dependências Diretas

Novos componentes devem utilizar contratos.

---

# Regra 03 — Não Antecipar Complexidade

Novas estruturas devem ser adicionadas somente quando houver necessidade real.

Princípio aplicado:

YAGNI

(You Aren't Gonna Need It)

---

# Regra 04 — Manter Clareza Educacional

O projeto possui finalidade didática.

A arquitetura deve permanecer compreensível para estudantes.

---

# Regra 05 — Documentar Alterações

Toda evolução deve registrar:

- motivo;
- impacto;
- decisão arquitetural.

---

# Pontos de Atenção Futuros

Durante a evolução do módulo, devem ser observados:

---

# Controle de Memória

Grandes volumes podem exigir estratégias diferentes de armazenamento.

---

# Reprodutibilidade

Experimentos devem poder ser repetidos utilizando as mesmas entradas.

---

# Rastreabilidade

As entradas devem manter informações suficientes para análise posterior.

---

# Compatibilidade

Novas fontes devem continuar produzindo DadosEntrada.

---

# Síntese Arquitetural

O módulo `entradaDados` representa uma camada de abstração entre o mundo externo e o núcleo do sistema.

Sua função pode ser resumida em:

Receber

↓

Validar

↓

Preparar

↓

Padronizar

↓

Entregar

---

# Conclusão Geral do Documento

O modelo de entradas do LAB EDU SORT V1.0 estabelece uma base sólida para o desenvolvimento de um ambiente educacional de análise de algoritmos de ordenação.

As decisões tomadas garantem:

- organização arquitetural;
- facilidade de manutenção;
- clareza das responsabilidades;
- independência entre módulos;
- possibilidade de evolução.

A arquitetura permite iniciar com uma implementação simples e evoluir progressivamente para um ambiente experimental mais completo.

---

# Princípios Finais do Módulo

O módulo `entradaDados` deve sempre seguir:

- dados devem ser validados antes do processamento;
- origens diferentes devem produzir modelos iguais;
- algoritmos não devem conhecer detalhes de entrada;
- contratos devem permanecer estáveis;
- complexidade deve ser adicionada somente quando necessária.

---

# Encerramento

Com a definição do modelo de entradas, o LAB EDU SORT V1.0 possui uma base arquitetural preparada para integrar:

- algoritmos de ordenação;
- estatísticas;
- visualizações;
- relatórios;
- experimentos educacionais.

O módulo `entradaDados` torna-se, portanto, o ponto inicial confiável do fluxo de execução do sistema, garantindo que todo processamento posterior utilize informações organizadas, consistentes e rastreáveis.

---
