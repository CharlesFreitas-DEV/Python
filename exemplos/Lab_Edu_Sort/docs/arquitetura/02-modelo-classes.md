# Índice

## Parte I — Fundamentos Arquiteturais

1. [Objetivo](#objetivo)

2. [Papel do Modelo Canônico do Domínio](#papel-do-modelo-canônico-do-domínio)

3. [Escopo](#escopo)

4. [Objetivos da Modelagem](#objetivos-da-modelagem)

5. [Princípios de Modelagem](#princípios-de-modelagem)

   5.1. [Responsabilidade Única](#responsabilidade-única)

   5.2. [Baixo Acoplamento](#baixo-acoplamento)

   5.3. [Alta Coesão](#alta-coesão)

   5.4. [Encapsulamento](#encapsulamento)

   5.5. [Extensibilidade](#extensibilidade)

   5.6. [Reutilização](#reutilização)

6. [Organização das Classes](#organização-das-classes)

7. [Relacionamento entre as Categorias](#relacionamento-entre-as-categorias)

8. [Convenções de Modelagem](#convenções-de-modelagem)

9. [Evolução do Modelo](#evolução-do-modelo)

---

# Referência das Classes

## Parte II — Classes de Configuração

- [ConfiguracaoExecucao](#classe-configuracaoexecucao)
- [ConfiguracaoEntrada](#classe-configuracaoentrada)
- [ConfiguracaoVisualizacao](#classe-configuracaovisualizacao)

---

## Parte III — Classes do Domínio

- [ConjuntoDados](#classe-conjuntodados)
- [ResultadoOrdenacao](#classe-resultadoordenacao)

---

## Parte IV — Classes de Eventos

- [EventoOrdenacao](#classe-abstrata-eventoordenacao)
- [ComparacaoRealizada](#classe-comparacaorealizada)
- [TrocaRealizada](#classe-trocarealizada)
- [ElementoLido](#classe-elementolido)
- [ElementoEscrito](#classe-elementoescrito)
- [ChamadaRecursivaIniciada](#classe-chamadarecursivainiciada)
- [ChamadaRecursivaFinalizada](#classe-chamadarecursivafinalizada)
- [AlgoritmoIniciado](#classe-algoritmoiniciado)
- [AlgoritmoFinalizado](#classe-algoritmofinalizado)

---

## Parte V — Classes de Estatísticas

- [EstatisticasOrdenacao](#classe-estatisticasordenacao)
- [EstatisticasOperacoes](#classe-estatisticasoperacoes)
- [EstatisticasTempo](#classe-estatisticastempo)
- [EstatisticasRecursao](#classe-estatisticasrecursao)
- [EstatisticasMemoria](#classe-estatisticasmemoria)

---

## Parte VI — Classes de Exceções

### Classe Base

- [LabEduSortError](#classe-base-labedusorterror)

### Configuração

- [ParametroInvalidoError](#classe-parametroinvalidoerror)
- [ConfiguracaoInvalidaError](#classe-configuracaoinvalidaerror)

### Entrada de Dados

- [ArquivoNaoEncontradoError](#classe-arquivonaoencontradoerror)
- [ArquivoInvalidoError](#classe-arquivoinvalidoerror)
- [TipoListaInvalidoError](#classe-tipolistainvalidoerror)
- [QuantidadeElementosInvalidaError](#classe-quantidadeelementosinvalidaerror)
- [IntervaloValoresInvalidoError](#classe-intervalovaloresinvalidoerror)

### Algoritmos

- [AlgoritmoNaoImplementadoError](#classe-algoritmonaoimplementadoerror)
- [ListaVaziaError](#classe-listavaziaerror)
- [TipoElementoInvalidoError](#classe-tipoelementoinvalidoerror)
- [ErroExecucaoAlgoritmoError](#classe-erroexecucaoalgoritmoerror)

### Eventos e Estatísticas

- [EventoDesconhecidoError](#classe-eventodesconhecidoerror)
- [EstatisticaInconsistenteError](#classe-estatisticainconsistenteerror)
- [TempoExecucaoInvalidoError](#classe-tempoexecucaoinvalidoerror)

### Visualizações

- [FormatoVisualizacaoInvalidoError](#classe-formatovisualizacaoinvalidoerror)
- [ExportacaoNaoSuportadaError](#classe-exportacaonaosuportadaerror)
- [ErroGeracaoRelatorioError](#classe-errogeracaorelatorioerror)

---

# Parte VII — Arquitetura Consolidada

1. [Diagrama Geral do Modelo Canônico](#diagrama-geral-do-modelo-canônico)

2. [Dependência entre Categorias](#dependência-entre-categorias)

3. [Regras de Evolução](#regras-de-evolução)

4. [Alterações Compatíveis](#alterações-compatíveis)

5. [Alterações Incompatíveis](#alterações-incompatíveis)

6. [Versionamento](#versionamento)

7. [Checklist de Conformidade](#checklist-de-conformidade)

8. [Considerações Finais](#considerações-finais)

---

# Modelo de Classes

## Projeto

**LAB EDU SORT V1.0**

---

# Objetivo

Este documento define o **Modelo Canônico do Domínio** do **LAB EDU SORT V1.0**.

Seu objetivo é especificar todas as classes que representam o domínio da aplicação, estabelecendo:

- os objetos utilizados pela biblioteca;
- as responsabilidades de cada classe;
- os relacionamentos entre os objetos;
- a organização hierárquica das classes;
- as regras estruturais que deverão ser preservadas durante toda a evolução do projeto.

Este documento não descreve a implementação das classes.

Seu propósito é definir a estrutura conceitual da biblioteca e servir como referência oficial para todas as implementações futuras.

---

# Papel do Modelo Canônico do Domínio

O **Modelo Canônico do Domínio** representa a única fonte oficial para definição dos objetos compartilhados entre os módulos da biblioteca.

Todos os componentes do sistema deverão utilizar exclusivamente as classes aqui especificadas.

Os demais documentos arquiteturais do projeto utilizam este modelo como referência.

Em especial:

- **01-modelo-conceitual.md** define os conceitos do domínio;
- **03-responsabilidades-modulos.md** define as responsabilidades de cada módulo;
- **04-contratos-modulos.md** estabelece a comunicação entre os módulos utilizando os objetos definidos neste documento.

Qualquer alteração em uma classe do domínio deverá ser refletida simultaneamente nos demais documentos arquiteturais.

---

# Escopo

O Modelo Canônico contempla exclusivamente as classes pertencentes ao domínio do **LAB EDU SORT V1.0**.

Fazem parte deste documento:

- classes de configuração;
- classes do domínio;
- classes de eventos;
- classes de estatísticas;
- classes de exceções;
- relacionamentos entre as classes;
- regras arquiteturais aplicáveis ao domínio.

Não fazem parte deste documento:

- implementação das classes;
- código-fonte;
- algoritmos de ordenação;
- estruturas internas dos módulos;
- funções utilitárias;
- detalhes específicos das interfaces da aplicação.

---

# Objetivos da Modelagem

A modelagem das classes possui os seguintes objetivos:

- representar corretamente o domínio da aplicação;
- padronizar os objetos compartilhados pela biblioteca;
- reduzir o acoplamento entre os módulos;
- promover reutilização;
- facilitar testes automatizados;
- permitir evolução incremental da arquitetura;
- manter consistência entre todos os artefatos arquiteturais.

---

# Princípios de Modelagem

Todas as classes pertencentes ao Modelo Canônico deverão respeitar os princípios arquiteturais definidos para o projeto.

---

## Responsabilidade Única

Cada classe deverá representar apenas um conceito do domínio.

Nenhuma classe deverá acumular responsabilidades distintas.

---

## Baixo Acoplamento

As classes deverão depender apenas das abstrações estritamente necessárias ao seu funcionamento.

Dependências desnecessárias deverão ser evitadas.

---

## Alta Coesão

Todos os atributos e responsabilidades de uma classe deverão estar relacionados ao mesmo conceito do domínio.

---

## Encapsulamento

O estado interno das classes deverá permanecer protegido.

Toda interação deverá ocorrer exclusivamente através de sua interface pública.

---

## Extensibilidade

Novas classes poderão ser adicionadas sem necessidade de alterar a estrutura das classes existentes.

A arquitetura deverá favorecer evolução incremental.

---

## Reutilização

Sempre que possível, as classes deverão representar conceitos reutilizáveis por diferentes módulos da biblioteca.

---

# Organização das Classes

As classes do Modelo Canônico estão organizadas em categorias conceituais.

Cada categoria representa uma responsabilidade arquitetural específica.

```text
Modelo Canônico do Domínio

│

├── Configuração
│      ├── ConfiguracaoExecucao
│      ├── ConfiguracaoEntrada
│      └── ConfiguracaoVisualizacao
│
├── Domínio
│      ├── ConjuntoDados
│      └── ResultadoOrdenacao
│
├── Eventos
│      ├── EventoOrdenacao
│      ├── ComparacaoRealizada
│      ├── TrocaRealizada
│      ├── ElementoLido
│      ├── ElementoEscrito
│      ├── ChamadaRecursivaIniciada
│      ├── ChamadaRecursivaFinalizada
│      ├── AlgoritmoIniciado
│      └── AlgoritmoFinalizado
│
├── Estatísticas
│      ├── EstatisticasOrdenacao
│      ├── EstatisticasOperacoes
│      ├── EstatisticasTempo
│      ├── EstatisticasRecursao
│      └── EstatisticasMemoria
│
└── Exceções
       ├── LabEduSortError
       ├── ParametroInvalidoError
       ├── ConfiguracaoInvalidaError
       ├── ArquivoNaoEncontradoError
       ├── ArquivoInvalidoError
       ├── TipoListaInvalidoError
       ├── QuantidadeElementosInvalidaError
       ├── IntervaloValoresInvalidoError
       ├── AlgoritmoNaoImplementadoError
       ├── ListaVaziaError
       ├── TipoElementoInvalidoError
       ├── ErroExecucaoAlgoritmoError
       ├── EventoDesconhecidoError
       ├── EstatisticaInconsistenteError
       ├── TempoExecucaoInvalidoError
       ├── FormatoVisualizacaoInvalidoError
       ├── ExportacaoNaoSuportadaError
       └── ErroGeracaoRelatorioError
```

---

# Relacionamento entre as Categorias

As categorias do Modelo Canônico relacionam-se conforme o diagrama abaixo.

```text
                  Configuração
                        │
                        ▼
                    Domínio
                        │
           ┌────────────┴────────────┐
           ▼                         ▼
       Eventos                 Estatísticas
           │
           ▼
      Visualizações

Exceções
▲
Utilizadas por todas as categorias.
```

---

# Convenções de Modelagem

Todas as classes do domínio deverão seguir as convenções descritas a seguir.

## Nomeação

- utilizar nomenclatura em **CamelCase**;
- utilizar nomes representativos do domínio;
- evitar abreviações desnecessárias;
- manter consistência com os padrões adotados pela biblioteca.

---

## Atributos

Os atributos deverão representar exclusivamente informações pertencentes ao conceito modelado.

Informações derivadas deverão ser calculadas pelos módulos apropriados, nunca armazenadas desnecessariamente nas classes.

---

## Relacionamentos

Os relacionamentos deverão privilegiar composição e associação.

Herança será utilizada apenas quando representar corretamente uma relação do tipo **"é um" (is-a)**.

---

## Independência

Nenhuma classe do domínio deverá conhecer detalhes de implementação dos módulos da biblioteca.

As classes representam exclusivamente conceitos do domínio.

---

# Evolução do Modelo

O Modelo Canônico deverá evoluir preservando compatibilidade sempre que possível.

Sempre que uma nova classe for criada deverão ser atualizados simultaneamente:

- este documento;
- o modelo conceitual;
- os contratos entre módulos;
- as responsabilidades dos módulos;
- a documentação técnica correspondente.

Alterações incompatíveis deverão ser tratadas como evolução arquitetural da biblioteca.

---

# Considerações Iniciais

O **Modelo Canônico do Domínio** constitui a base estrutural do **LAB EDU SORT V1.0**.

Todas as classes apresentadas nas próximas seções serão especificadas individualmente, incluindo:

- objetivo;
- responsabilidades;
- atributos;
- relacionamentos;
- diagramas UML;
- regras arquiteturais;
- observações de utilização.

Este documento representa a referência oficial para implementação das classes da biblioteca e deverá permanecer sincronizado com todos os demais artefatos arquiteturais do projeto.

---

# Parte II — Classes de Configuração

As classes desta seção representam as configurações utilizadas durante todo o ciclo de vida da aplicação.

Essas classes não executam processamento, não implementam regras de negócio e não possuem conhecimento sobre os módulos da biblioteca.

Sua responsabilidade é exclusivamente encapsular as informações necessárias para parametrizar uma execução do **LAB EDU SORT V1.0**.

Todas pertencem ao **Modelo Canônico do Domínio**.

---

# Visão Geral

```text
Configuração

│

├── ConfiguracaoExecucao

├── ConfiguracaoEntrada

└── ConfiguracaoVisualizacao
```

---

# Objetivos da Categoria

As classes de configuração possuem os seguintes objetivos:

- centralizar todos os parâmetros de execução;
- desacoplar a configuração da implementação dos módulos;
- permitir reutilização por diferentes interfaces (CLI, GUI, API, notebooks etc.);
- facilitar validação e testes;
- padronizar a criação dos objetos do domínio.

---

# Relacionamento Geral

```text
ConfiguracaoExecucao

        │

        ├────────► ConfiguracaoEntrada

        │

        └────────► ConfiguracaoVisualizacao
```

A classe `ConfiguracaoExecucao` representa o ponto central das configurações da aplicação.

Ela agrega todas as configurações necessárias para uma execução completa da biblioteca.

---

# Classe: ConfiguracaoExecucao

## Objetivo

Representar todas as configurações necessárias para iniciar uma execução do **LAB EDU SORT**.

Esta é a primeira classe criada pela camada de aplicação e funciona como objeto agregador das demais configurações.

---

## Responsabilidades

A classe é responsável por:

- armazenar as configurações gerais da execução;
- identificar o algoritmo de ordenação selecionado;
- agregar as configurações de entrada;
- agregar as configurações de visualização;
- indicar se estatísticas deverão ser coletadas;
- disponibilizar uma configuração única para toda a aplicação.

---

## Principais Atributos

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| algoritmo | String | Nome do algoritmo selecionado |
| configuracaoEntrada | ConfiguracaoEntrada | Configuração da origem dos dados |
| configuracaoVisualizacao | ConfiguracaoVisualizacao | Configuração da apresentação dos resultados |
| coletarEstatisticas | Boolean | Indica se as estatísticas deverão ser produzidas |

---

## Relacionamentos

```text
ConfiguracaoExecucao

│

├────► ConfiguracaoEntrada

│

└────► ConfiguracaoVisualizacao
```

---

## Diagrama UML

```text
+------------------------------------------------------+
| ConfiguracaoExecucao                                 |
+------------------------------------------------------+
| algoritmo                                             |
| configuracaoEntrada                                   |
| configuracaoVisualizacao                              |
| coletarEstatisticas                                   |
+------------------------------------------------------+
```

---

## Regras Arquiteturais

A classe deverá:

- ser criada antes do início da execução;
- agregar todas as demais configurações;
- permanecer independente dos módulos;
- não executar validações;
- não executar processamento.

---

## Observações

Esta classe representa o principal objeto de configuração da biblioteca.

Toda execução deverá ser completamente descrita por uma única instância desta classe.

---

# Classe: ConfiguracaoEntrada

## Objetivo

Representar todas as informações necessárias para criação do objeto `ConjuntoDados`.

Esta classe descreve **como** os dados deverão ser obtidos, mas não realiza sua leitura nem geração.

---

## Responsabilidades

A classe é responsável por:

- definir a origem dos dados;
- parametrizar geração automática;
- informar localização de arquivos;
- definir características do conjunto de dados.

---

## Principais Atributos

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| origem | Enum | Arquivo ou geração automática |
| caminhoArquivo | String | Caminho do arquivo de entrada |
| quantidadeElementos | Integer | Quantidade de elementos |
| valorMinimo | Integer | Menor valor permitido |
| valorMaximo | Integer | Maior valor permitido |
| tipoDistribuicao | Enum | Aleatória, crescente, decrescente ou parcialmente ordenada |

---

## Relacionamentos

```text
ConfiguracaoEntrada

        │

        ▼

ConjuntoDados
```

---

## Diagrama UML

```text
+------------------------------------------------------+
| ConfiguracaoEntrada                                  |
+------------------------------------------------------+
| origem                                                |
| caminhoArquivo                                        |
| quantidadeElementos                                   |
| valorMinimo                                           |
| valorMaximo                                           |
| tipoDistribuicao                                      |
+------------------------------------------------------+
```

---

## Regras Arquiteturais

A classe deverá:

- descrever apenas a origem dos dados;
- não conhecer algoritmos;
- não criar objetos de domínio;
- não realizar leitura de arquivos;
- não gerar listas automaticamente.

---

## Observações

A interpretação desta configuração é responsabilidade exclusiva do módulo **entradaDados**.

---

# Classe: ConfiguracaoVisualizacao

## Objetivo

Representar todas as configurações relacionadas à apresentação dos resultados produzidos pela biblioteca.

Esta classe descreve **como** os resultados deverão ser apresentados, sem executar qualquer operação de visualização.

---

## Responsabilidades

A classe é responsável por:

- definir o formato de saída;
- configurar exportação;
- controlar exibição das estatísticas;
- parametrizar relatórios.

---

## Principais Atributos

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| formato | Enum | Texto, tabela, gráfico ou exportação |
| mostrarEstatisticas | Boolean | Indica se as estatísticas serão exibidas |
| exportarArquivo | Boolean | Indica se os resultados serão exportados |
| caminhoSaida | String | Diretório de exportação |

---

## Relacionamentos

```text
ConfiguracaoVisualizacao

        │

        ▼

visualizacoes
```

---

## Diagrama UML

```text
+------------------------------------------------------+
| ConfiguracaoVisualizacao                             |
+------------------------------------------------------+
| formato                                               |
| mostrarEstatisticas                                   |
| exportarArquivo                                       |
| caminhoSaida                                          |
+------------------------------------------------------+
```

---

## Regras Arquiteturais

A classe deverá:

- descrever apenas parâmetros de apresentação;
- não produzir gráficos;
- não gerar relatórios;
- não exportar arquivos;
- permanecer independente da implementação das visualizações.

---

## Observações

Esta classe permite que diferentes mecanismos de apresentação utilizem exatamente a mesma configuração.

---

# Diagrama UML da Categoria

```text
                         ConfiguracaoExecucao
                         +-------------------+
                         | algoritmo         |
                         | coletarEstatisticas|
                         +-------------------+
                           /               \
                          /                 \
                         ▼                   ▼

          ConfiguracaoEntrada      ConfiguracaoVisualizacao
          +-------------------+    +-------------------------+
          | origem            |    | formato                 |
          | caminhoArquivo    |    | mostrarEstatisticas     |
          | quantidadeElementos|   | exportarArquivo         |
          | valorMinimo       |    | caminhoSaida            |
          | valorMaximo       |    +-------------------------+
          | tipoDistribuicao  |
          +-------------------+
```

---

# Fluxo de Utilização

```text
Aplicação

     │

     ▼

ConfiguracaoExecucao

     │

     ├────────► ConfiguracaoEntrada

     │              │

     │              ▼

     │       entradaDados

     │

     └────────► ConfiguracaoVisualizacao

                    │

                    ▼

              visualizacoes
```

---

# Relação com os Módulos

| Classe | Principal Produtor | Principais Consumidores |
|---------|--------------------|--------------------------|
| ConfiguracaoExecucao | aplicacao | aplicacao |
| ConfiguracaoEntrada | aplicacao | entradaDados |
| ConfiguracaoVisualizacao | aplicacao | visualizacoes |

---

# Princípios Arquiteturais da Categoria

As classes de configuração deverão obedecer aos seguintes princípios:

- representar exclusivamente parâmetros de configuração;
- não implementar regras de negócio;
- não executar processamento;
- não conhecer detalhes dos módulos;
- possuir responsabilidade única;
- favorecer reutilização;
- permitir evolução incremental da arquitetura.

---

# Considerações da Categoria

As classes de configuração representam o primeiro grupo de objetos do **Modelo Canônico do Domínio**.

Elas estabelecem uma separação clara entre configuração, processamento e apresentação, reduzindo o acoplamento entre os módulos e permitindo que novas interfaces utilizem a biblioteca sem necessidade de alterações na arquitetura.

Nas próximas seções serão apresentadas as **Classes do Domínio**, responsáveis por representar os principais objetos manipulados durante a execução dos algoritmos de ordenação.

---

# Parte III — Classes do Domínio

As classes desta seção representam os principais conceitos manipulados pela biblioteca durante uma execução.

Diferentemente das classes de configuração, estas classes descrevem o **estado do domínio** e representam os objetos produzidos e consumidos pelos módulos internos do **LAB EDU SORT V1.0**.

Nesta versão do projeto, o domínio é composto por duas classes fundamentais:

- `ConjuntoDados`;
- `ResultadoOrdenacao`.

Essas classes constituem o núcleo da biblioteca e servem como base para a comunicação entre os módulos.

---

# Visão Geral

```text
Domínio

│

├── ConjuntoDados

└── ResultadoOrdenacao
```

---

# Objetivos da Categoria

As classes do domínio possuem os seguintes objetivos:

- representar os dados manipulados pela biblioteca;
- encapsular o resultado produzido pelos algoritmos;
- padronizar a comunicação entre os módulos;
- manter independência entre processamento e apresentação;
- fornecer objetos reutilizáveis por toda a arquitetura.

---

# Relacionamento Geral

```text
ConfiguracaoEntrada

        │

        ▼

ConjuntoDados

        │

        ▼

algoritmosOrdenacao

        │

        ▼

ResultadoOrdenacao

        │

        ├────────► estatisticas

        └────────► visualizacoes
```

O fluxo acima representa o ciclo de vida principal dos objetos do domínio.

---

# Classe: ConjuntoDados

## Objetivo

Representar o conjunto de elementos que será submetido ao algoritmo de ordenação.

Esta classe encapsula todas as informações relacionadas aos dados de entrada da execução.

Ela constitui o principal objeto de entrada dos algoritmos de ordenação.

---

## Responsabilidades

A classe é responsável por:

- armazenar os elementos da coleção;
- representar o estado inicial dos dados;
- preservar informações sobre sua origem;
- disponibilizar os elementos para processamento.

---

## Principais Atributos

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| elementos | List<Integer> | Coleção de elementos a serem ordenados |
| quantidade | Integer | Quantidade total de elementos |
| origem | Enum | Arquivo ou geração automática |
| distribuicao | Enum | Aleatória, crescente, decrescente ou parcialmente ordenada |

---

## Relacionamentos

```text
ConfiguracaoEntrada

        │

        ▼

ConjuntoDados

        │

        ▼

algoritmosOrdenacao
```

---

## Diagrama UML

```text
+------------------------------------------------------+
| ConjuntoDados                                        |
+------------------------------------------------------+
| elementos                                             |
| quantidade                                            |
| origem                                                |
| distribuicao                                          |
+------------------------------------------------------+
```

---

## Regras Arquiteturais

A classe deverá:

- representar exclusivamente os dados de entrada;
- não conhecer algoritmos;
- não realizar ordenação;
- não calcular estatísticas;
- permanecer independente dos módulos internos.

---

## Observações

Os algoritmos de ordenação deverão operar exclusivamente sobre instâncias desta classe.

Nenhum algoritmo deverá depender diretamente da origem dos dados.

---

# Classe: ResultadoOrdenacao

## Objetivo

Representar o resultado produzido por uma execução completa de um algoritmo de ordenação.

Esta classe consolida todas as informações relevantes da execução em um único objeto do domínio.

---

## Responsabilidades

A classe é responsável por:

- armazenar a coleção ordenada;
- identificar o algoritmo executado;
- associar as estatísticas produzidas;
- representar o resultado final da execução.

---

## Principais Atributos

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| algoritmo | String | Nome do algoritmo executado |
| dadosOrdenados | List<Integer> | Coleção ordenada |
| estatisticas | EstatisticasOrdenacao | Estatísticas produzidas durante a execução |
| sucesso | Boolean | Indica se a execução foi concluída com sucesso |

---

## Relacionamentos

```text
ResultadoOrdenacao

        │

        ├────────► EstatisticasOrdenacao

        │

        └────────► visualizacoes
```

---

## Diagrama UML

```text
+------------------------------------------------------+
| ResultadoOrdenacao                                   |
+------------------------------------------------------+
| algoritmo                                             |
| dadosOrdenados                                        |
| estatisticas                                          |
| sucesso                                               |
+------------------------------------------------------+
```

---

## Regras Arquiteturais

A classe deverá:

- representar exclusivamente o resultado da execução;
- não executar processamento;
- não recalcular estatísticas;
- não conhecer detalhes da interface da aplicação;
- permanecer imutável após sua construção.

---

## Observações

A utilização de uma única classe para representar o resultado completo simplifica a comunicação entre os módulos e facilita futuras extensões da biblioteca.

---

# Diagrama UML da Categoria

```text
                     ConfiguracaoEntrada

                              │

                              ▼

                    +----------------------+
                    |   ConjuntoDados      |
                    +----------------------+
                    | elementos            |
                    | quantidade           |
                    | origem               |
                    | distribuicao         |
                    +----------------------+

                              │

                              ▼

                 algoritmosOrdenacao

                              │

                              ▼

                  +------------------------+
                  | ResultadoOrdenacao     |
                  +------------------------+
                  | algoritmo              |
                  | dadosOrdenados         |
                  | estatisticas           |
                  | sucesso                |
                  +------------------------+

                              │

             ┌────────────────┴────────────────┐

             ▼                                 ▼

 EstatisticasOrdenacao                 visualizacoes
```

---

# Fluxo de Utilização

```text
ConfiguracaoEntrada

        │

        ▼

ConjuntoDados

        │

        ▼

algoritmosOrdenacao

        │

        ▼

ResultadoOrdenacao

        │

        ├────────► estatisticas

        │

        └────────► visualizacoes
```

---

# Relação com os Módulos

| Classe | Principal Produtor | Principais Consumidores |
|---------|--------------------|--------------------------|
| ConjuntoDados | entradaDados | algoritmosOrdenacao |
| ResultadoOrdenacao | algoritmosOrdenacao | aplicacao, estatisticas, visualizacoes |

---

# Princípios Arquiteturais da Categoria

As classes do domínio deverão obedecer aos seguintes princípios:

- representar exclusivamente conceitos do domínio;
- permanecer independentes dos módulos da biblioteca;
- não executar regras de negócio;
- favorecer reutilização;
- possuir responsabilidade única;
- utilizar composição para agregar informações relacionadas;
- servir como contratos naturais entre os módulos.

---

# Considerações da Categoria

As classes do domínio representam o núcleo funcional do **LAB EDU SORT V1.0**.

Enquanto `ConjuntoDados` modela os dados de entrada utilizados pelos algoritmos, `ResultadoOrdenacao` consolida o resultado produzido durante a execução, incluindo o algoritmo utilizado, a coleção ordenada e as estatísticas associadas.

Essa separação estabelece uma fronteira clara entre **entrada**, **processamento** e **resultado**, mantendo baixo acoplamento entre os módulos e facilitando futuras evoluções da arquitetura.

Na próxima seção serão apresentadas as **Classes de Eventos**, responsáveis por implementar a comunicação orientada a eventos entre os algoritmos de ordenação e os módulos observadores da biblioteca.

---

# Parte IV — Classes de Eventos

As classes desta seção representam todas as ocorrências produzidas durante a execução dos algoritmos de ordenação.

Essas classes constituem a base da arquitetura orientada a eventos do **LAB EDU SORT V1.0**, permitindo que diferentes componentes observem a execução dos algoritmos sem criar dependências diretas entre eles.

Todos os eventos pertencem ao **Modelo Canônico do Domínio**.

---

# Visão Geral

```text
Eventos

│

└── EventoOrdenacao (abstrata)

      │

      ├── ComparacaoRealizada

      ├── TrocaRealizada

      ├── ElementoLido

      ├── ElementoEscrito

      ├── ChamadaRecursivaIniciada

      ├── ChamadaRecursivaFinalizada

      ├── AlgoritmoIniciado

      └── AlgoritmoFinalizado
```

---

# Objetivos da Categoria

As classes de eventos possuem os seguintes objetivos:

- representar fatos ocorridos durante a execução dos algoritmos;
- desacoplar os algoritmos dos módulos consumidores;
- padronizar a comunicação interna da biblioteca;
- permitir múltiplos observadores;
- favorecer extensibilidade da arquitetura.

---

# Papel dos Eventos na Arquitetura

Os algoritmos de ordenação produzem eventos.

Os módulos interessados observam esses eventos.

Os algoritmos nunca conhecem quem está consumindo essas informações.

```text
algoritmosOrdenacao

        │

        │ Publica

        ▼

EventoOrdenacao

        │

        ├────────► estatisticas

        ├────────► logs (futuro)

        ├────────► auditoria (futuro)

        ├────────► animações (futuro)

        └────────► outros observadores
```

Essa arquitetura implementa o padrão **Observer**, reduzindo significativamente o acoplamento entre os módulos.

---

# Hierarquia das Classes

Todas as classes de eventos derivam de uma única classe abstrata.

```text
EventoOrdenacao (abstrata)

│

├── ComparacaoRealizada

├── TrocaRealizada

├── ElementoLido

├── ElementoEscrito

├── ChamadaRecursivaIniciada

├── ChamadaRecursivaFinalizada

├── AlgoritmoIniciado

└── AlgoritmoFinalizado
```

A classe base reúne todas as informações comuns aos eventos da biblioteca.

---

# Classe Abstrata: EventoOrdenacao

## Objetivo

Representar um evento genérico produzido durante a execução de um algoritmo.

Nenhuma instância direta desta classe deverá existir.

Ela representa apenas a abstração comum de todos os eventos.

---

## Responsabilidades

A classe é responsável por:

- representar um evento da execução;
- padronizar a comunicação entre produtores e observadores;
- fornecer informações comuns a todos os eventos.

---

## Principais Atributos

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| algoritmo | String | Nome do algoritmo responsável pelo evento |
| instante | DateTime | Momento da ocorrência |
| indiceAtual | Integer | Índice principal relacionado ao evento |
| descricao | String | Descrição resumida do evento |

---

## Diagrama UML

```text
                 <<abstract>>

+------------------------------------------------------+
| EventoOrdenacao                                      |
+------------------------------------------------------+
| algoritmo                                             |
| instante                                              |
| indiceAtual                                           |
| descricao                                             |
+------------------------------------------------------+
```

---

## Regras Arquiteturais

A classe deverá:

- representar exclusivamente um acontecimento;
- não executar processamento;
- não alterar estruturas de dados;
- permanecer imutável após sua criação.

---

# Classe: ComparacaoRealizada

## Objetivo

Representar uma comparação realizada entre dois elementos.

---

## Responsabilidades

- registrar uma comparação;
- transportar informações para os observadores.

---

## Principais Atributos

| Atributo | Tipo |
|----------|------|
| indiceOrigem | Integer |
| indiceDestino | Integer |
| valorOrigem | Integer |
| valorDestino | Integer |

---

## Diagrama UML

```text
+------------------------------------------------------+
| ComparacaoRealizada                                  |
+------------------------------------------------------+
| indiceOrigem                                          |
| indiceDestino                                         |
| valorOrigem                                           |
| valorDestino                                          |
+------------------------------------------------------+
```

---

# Classe: TrocaRealizada

## Objetivo

Representar uma troca entre dois elementos da coleção.

---

## Responsabilidades

- registrar a troca efetuada;
- informar quais posições foram alteradas.

---

## Principais Atributos

| Atributo | Tipo |
|----------|------|
| indiceA | Integer |
| indiceB | Integer |

---

## Diagrama UML

```text
+------------------------------------------------------+
| TrocaRealizada                                       |
+------------------------------------------------------+
| indiceA                                               |
| indiceB                                               |
+------------------------------------------------------+
```

---

# Classe: ElementoLido

## Objetivo

Representar a leitura de um elemento da coleção.

---

## Responsabilidades

- registrar uma operação de leitura.

---

## Principais Atributos

| Atributo | Tipo |
|----------|------|
| indice | Integer |
| valor | Integer |

---

## Diagrama UML

```text
+------------------------------------------------------+
| ElementoLido                                         |
+------------------------------------------------------+
| indice                                                 |
| valor                                                  |
+------------------------------------------------------+
```

---

# Classe: ElementoEscrito

## Objetivo

Representar a escrita de um elemento da coleção.

---

## Responsabilidades

- registrar uma operação de escrita.

---

## Principais Atributos

| Atributo | Tipo |
|----------|------|
| indice | Integer |
| valor | Integer |

---

## Diagrama UML

```text
+------------------------------------------------------+
| ElementoEscrito                                      |
+------------------------------------------------------+
| indice                                                 |
| valor                                                  |
+------------------------------------------------------+
```

---

# Classe: ChamadaRecursivaIniciada

## Objetivo

Representar o início de uma chamada recursiva.

---

## Responsabilidades

- registrar a entrada em um novo nível de recursão.

---

## Principais Atributos

| Atributo | Tipo |
|----------|------|
| nivelRecursao | Integer |

---

## Diagrama UML

```text
+------------------------------------------------------+
| ChamadaRecursivaIniciada                             |
+------------------------------------------------------+
| nivelRecursao                                         |
+------------------------------------------------------+
```

---

# Classe: ChamadaRecursivaFinalizada

## Objetivo

Representar o término de uma chamada recursiva.

---

## Responsabilidades

- registrar a saída de um nível de recursão.

---

## Principais Atributos

| Atributo | Tipo |
|----------|------|
| nivelRecursao | Integer |

---

## Diagrama UML

```text
+------------------------------------------------------+
| ChamadaRecursivaFinalizada                           |
+------------------------------------------------------+
| nivelRecursao                                         |
+------------------------------------------------------+
```

---

# Classe: AlgoritmoIniciado

## Objetivo

Representar o início da execução de um algoritmo.

---

## Responsabilidades

- sinalizar o início da execução.

---

## Principais Atributos

| Atributo | Tipo |
|----------|------|
| algoritmo | String |

---

## Diagrama UML

```text
+------------------------------------------------------+
| AlgoritmoIniciado                                    |
+------------------------------------------------------+
| algoritmo                                              |
+------------------------------------------------------+
```

---

# Classe: AlgoritmoFinalizado

## Objetivo

Representar o encerramento da execução de um algoritmo.

---

## Responsabilidades

- sinalizar o término da execução;
- informar se a execução foi concluída com sucesso.

---

## Principais Atributos

| Atributo | Tipo |
|----------|------|
| algoritmo | String |
| sucesso | Boolean |

---

## Diagrama UML

```text
+------------------------------------------------------+
| AlgoritmoFinalizado                                  |
+------------------------------------------------------+
| algoritmo                                              |
| sucesso                                                |
+------------------------------------------------------+
```

---

# Diagrama UML da Categoria

```text
                       <<abstract>>

                  EventoOrdenacao

                          ▲

      ┌───────────┬────────┼────────┬────────────┐

      │           │        │        │            │

      ▼           ▼        ▼        ▼            ▼

Comparacao   Troca   ElementoLido   ElementoEscrito

                                      │

                                      ▼

                      ChamadaRecursivaIniciada

                                      │

                                      ▼

                     ChamadaRecursivaFinalizada

                                      │

                                      ▼

                         AlgoritmoIniciado

                                      │

                                      ▼

                        AlgoritmoFinalizado
```

---

# Fluxo de Utilização

```text
algoritmosOrdenacao

        │

        ▼

EventoOrdenacao

        │

        ├────────► estatisticas

        ├────────► visualizacoes (futuro)

        ├────────► logs (futuro)

        ├────────► auditoria (futuro)

        └────────► outros observadores
```

---

# Relação com os Módulos

| Classe | Principal Produtor | Principais Consumidores |
|---------|--------------------|--------------------------|
| EventoOrdenacao | algoritmosOrdenacao | estatisticas |
| ComparacaoRealizada | algoritmosOrdenacao | estatisticas |
| TrocaRealizada | algoritmosOrdenacao | estatisticas |
| ElementoLido | algoritmosOrdenacao | estatisticas |
| ElementoEscrito | algoritmosOrdenacao | estatisticas |
| ChamadaRecursivaIniciada | algoritmosOrdenacao | estatisticas |
| ChamadaRecursivaFinalizada | algoritmosOrdenacao | estatisticas |
| AlgoritmoIniciado | algoritmosOrdenacao | estatisticas |
| AlgoritmoFinalizado | algoritmosOrdenacao | estatisticas |

---

# Princípios Arquiteturais da Categoria

As classes de eventos deverão obedecer aos seguintes princípios:

- representar exclusivamente acontecimentos;
- permanecer imutáveis após sua criação;
- não executar processamento;
- não conhecer os observadores;
- permitir múltiplos consumidores;
- favorecer baixo acoplamento;
- permitir expansão por especialização da classe base.

---

# Evolução da Categoria

Novos eventos poderão ser adicionados sem necessidade de alterar os algoritmos existentes.

Exemplos previstos para futuras versões:

- ParticaoCriada;
- MergeExecutado;
- HeapReconstruido;
- PivotSelecionado;
- RotacaoRealizada.

Essa evolução preserva a compatibilidade da arquitetura e mantém os algoritmos desacoplados dos módulos consumidores.

---

# Considerações da Categoria

As classes de eventos representam um dos principais pilares arquiteturais do **LAB EDU SORT V1.0**.

Ao adotar uma hierarquia baseada em uma classe abstrata (`EventoOrdenacao`), a biblioteca estabelece um mecanismo uniforme para comunicação entre produtores e observadores, permitindo que estatísticas, auditorias, registros de execução e futuras animações sejam implementados de forma independente.

Essa abordagem reduz o acoplamento entre os módulos, aumenta a extensibilidade da arquitetura e mantém os algoritmos de ordenação concentrados exclusivamente em sua responsabilidade principal: ordenar os dados.

---

# Parte V — Classes de Estatísticas

As classes desta seção representam as informações produzidas durante a execução dos algoritmos de ordenação.

Enquanto as **Classes de Eventos** registram cada ocorrência individual da execução, as **Classes de Estatísticas** consolidam essas ocorrências em métricas, indicadores e informações quantitativas que descrevem o comportamento do algoritmo.

Essas classes pertencem ao **Modelo Canônico do Domínio** e constituem a principal saída analítica da biblioteca.

---

# Visão Geral

```text
Estatísticas

│

├── EstatisticasOrdenacao

├── EstatisticasOperacoes

├── EstatisticasTempo

├── EstatisticasRecursao

└── EstatisticasMemoria
```

---

# Objetivos da Categoria

As classes de estatísticas possuem os seguintes objetivos:

- consolidar os eventos produzidos pelos algoritmos;
- representar métricas quantitativas da execução;
- fornecer informações para comparação entre algoritmos;
- servir de base para relatórios e visualizações;
- manter independência entre processamento e apresentação.

---

# Papel das Estatísticas na Arquitetura

As estatísticas são produzidas a partir da observação dos eventos publicados pelos algoritmos.

```text
algoritmosOrdenacao

        │

        ▼

EventoOrdenacao

        │

        ▼

estatisticas

        │

        ▼

EstatisticasOrdenacao

        │

        ├────────► visualizacoes

        ├────────► relatorios (futuro)

        └────────► exportadores (futuro)
```

Os algoritmos não calculam estatísticas diretamente.

Eles apenas publicam eventos.

---

# Relacionamento Geral

```text
EstatisticasOrdenacao

│

├── EstatisticasOperacoes

├── EstatisticasTempo

├── EstatisticasRecursao

└── EstatisticasMemoria
```

`EstatisticasOrdenacao` funciona como objeto agregador das demais estatísticas.

---

# Classe: EstatisticasOrdenacao

## Objetivo

Representar todas as estatísticas produzidas durante uma execução completa de um algoritmo.

Esta classe consolida todas as métricas da execução em um único objeto.

---

## Responsabilidades

A classe é responsável por:

- agregar todas as estatísticas;
- representar o resultado analítico da execução;
- disponibilizar métricas para outros módulos.

---

## Principais Atributos

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| algoritmo | String | Nome do algoritmo |
| operacoes | EstatisticasOperacoes | Estatísticas de operações |
| tempo | EstatisticasTempo | Estatísticas temporais |
| recursao | EstatisticasRecursao | Estatísticas de recursão |
| memoria | EstatisticasMemoria | Estatísticas de memória |

---

## Diagrama UML

```text
+------------------------------------------------------+
| EstatisticasOrdenacao                                |
+------------------------------------------------------+
| algoritmo                                             |
| operacoes                                             |
| tempo                                                 |
| recursao                                              |
| memoria                                               |
+------------------------------------------------------+
```

---

## Regras Arquiteturais

A classe deverá:

- agregar todas as estatísticas produzidas;
- permanecer imutável após sua construção;
- não recalcular métricas;
- não depender dos algoritmos.

---

# Classe: EstatisticasOperacoes

## Objetivo

Representar as operações executadas durante a ordenação.

---

## Responsabilidades

- contabilizar comparações;
- contabilizar trocas;
- contabilizar leituras;
- contabilizar escritas.

---

## Principais Atributos

| Atributo | Tipo |
|----------|------|
| comparacoes | Integer |
| trocas | Integer |
| leituras | Integer |
| escritas | Integer |

---

## Diagrama UML

```text
+------------------------------------------------------+
| EstatisticasOperacoes                                |
+------------------------------------------------------+
| comparacoes                                           |
| trocas                                                |
| leituras                                              |
| escritas                                              |
+------------------------------------------------------+
```

---

## Regras Arquiteturais

Esta classe deverá representar apenas contadores de operações realizadas.

---

# Classe: EstatisticasTempo

## Objetivo

Representar informações relacionadas ao tempo de execução.

---

## Responsabilidades

- registrar início da execução;
- registrar término da execução;
- calcular tempo total.

---

## Principais Atributos

| Atributo | Tipo |
|----------|------|
| inicio | DateTime |
| fim | DateTime |
| tempoTotal | Double |

---

## Diagrama UML

```text
+------------------------------------------------------+
| EstatisticasTempo                                    |
+------------------------------------------------------+
| inicio                                                |
| fim                                                   |
| tempoTotal                                            |
+------------------------------------------------------+
```

---

## Regras Arquiteturais

A classe deverá representar exclusivamente métricas temporais.

---

# Classe: EstatisticasRecursao

## Objetivo

Representar métricas relacionadas ao comportamento recursivo dos algoritmos.

---

## Responsabilidades

- registrar profundidade máxima;
- contabilizar chamadas recursivas;
- registrar retornos.

---

## Principais Atributos

| Atributo | Tipo |
|----------|------|
| profundidadeMaxima | Integer |
| chamadas | Integer |
| retornos | Integer |

---

## Diagrama UML

```text
+------------------------------------------------------+
| EstatisticasRecursao                                 |
+------------------------------------------------------+
| profundidadeMaxima                                    |
| chamadas                                              |
| retornos                                              |
+------------------------------------------------------+
```

---

## Regras Arquiteturais

Esta classe somente será utilizada por algoritmos recursivos.

---

# Classe: EstatisticasMemoria

## Objetivo

Representar métricas relacionadas ao uso de memória durante a execução.

---

## Responsabilidades

- registrar memória utilizada;
- registrar memória auxiliar;
- representar consumo total.

---

## Principais Atributos

| Atributo | Tipo |
|----------|------|
| memoriaPrincipal | Integer |
| memoriaAuxiliar | Integer |
| memoriaTotal | Integer |

---

## Diagrama UML

```text
+------------------------------------------------------+
| EstatisticasMemoria                                  |
+------------------------------------------------------+
| memoriaPrincipal                                      |
| memoriaAuxiliar                                       |
| memoriaTotal                                          |
+------------------------------------------------------+
```

---

## Regras Arquiteturais

A classe deverá representar exclusivamente métricas de memória.

---

# Diagrama UML da Categoria

```text
                 EstatisticasOrdenacao

                          │

        ┌─────────────────┼─────────────────┐

        ▼                 ▼                 ▼

EstatisticasOperacoes  EstatisticasTempo  EstatisticasRecursao

                                            │

                                            ▼

                                  EstatisticasMemoria
```

---

# Fluxo de Utilização

```text
algoritmosOrdenacao

        │

        ▼

EventoOrdenacao

        │

        ▼

estatisticas

        │

        ▼

EstatisticasOrdenacao

        │

        ├────────► ResultadoOrdenacao

        │

        └────────► visualizacoes
```

---

# Relação com os Módulos

| Classe | Principal Produtor | Principais Consumidores |
|---------|--------------------|--------------------------|
| EstatisticasOrdenacao | estatisticas | ResultadoOrdenacao, visualizacoes |
| EstatisticasOperacoes | estatisticas | EstatisticasOrdenacao |
| EstatisticasTempo | estatisticas | EstatisticasOrdenacao |
| EstatisticasRecursao | estatisticas | EstatisticasOrdenacao |
| EstatisticasMemoria | estatisticas | EstatisticasOrdenacao |

---

# Princípios Arquiteturais da Categoria

As classes de estatísticas deverão obedecer aos seguintes princípios:

- representar exclusivamente métricas da execução;
- permanecer independentes dos algoritmos;
- não modificar eventos;
- não executar ordenação;
- favorecer composição em vez de herança;
- consolidar informações produzidas pelos observadores;
- permanecer imutáveis após sua construção.

---

# Evolução da Categoria

Novas estatísticas poderão ser adicionadas sem impacto na arquitetura existente.

Exemplos previstos para futuras versões:

- EstatisticasCache;
- EstatisticasCPU;
- EstatisticasComplexidade;
- EstatisticasEnergia;
- EstatisticasParalelismo.

A composição adotada por `EstatisticasOrdenacao` permite incorporar novas métricas preservando compatibilidade com versões anteriores.

---

# Considerações da Categoria

As classes de estatísticas representam a camada analítica do **LAB EDU SORT V1.0**.

Enquanto os algoritmos permanecem responsáveis apenas pelo processamento dos dados e os eventos registram cada operação executada, as estatísticas consolidam essas informações em indicadores que podem ser utilizados para análise de desempenho, comparação entre algoritmos, geração de relatórios e visualizações.

A utilização da classe agregadora `EstatisticasOrdenacao` estabelece um ponto único de acesso às métricas da execução, simplificando a comunicação entre os módulos e favorecendo a evolução incremental da arquitetura.

Na próxima seção serão apresentadas as **Classes de Exceções**, responsáveis por padronizar o tratamento de erros e garantir a consistência das operações realizadas pela biblioteca.

---

# Parte VI — Classes de Exceções

As classes desta seção representam todas as exceções utilizadas pelo **LAB EDU SORT V1.0**.

Seu objetivo é padronizar o tratamento de erros da biblioteca, permitindo que todas as falhas sejam representadas por exceções específicas do domínio.

Ao utilizar uma hierarquia própria de exceções, a biblioteca torna-se mais previsível, facilita a depuração, melhora a documentação do código e reduz o acoplamento com exceções genéricas da linguagem.

Todas as exceções derivam de uma única classe base pertencente ao **Modelo Canônico do Domínio**.

---

# Visão Geral

```text
Exceções

│

└── LabEduSortError

      │

      ├── ParametroInvalidoError

      ├── ConfiguracaoInvalidaError

      ├── ArquivoNaoEncontradoError

      ├── ArquivoInvalidoError

      ├── TipoListaInvalidoError

      ├── QuantidadeElementosInvalidaError

      ├── IntervaloValoresInvalidoError

      ├── AlgoritmoNaoImplementadoError

      ├── ListaVaziaError

      ├── TipoElementoInvalidoError

      ├── ErroExecucaoAlgoritmoError

      ├── EventoDesconhecidoError

      ├── EstatisticaInconsistenteError

      ├── TempoExecucaoInvalidoError

      ├── FormatoVisualizacaoInvalidoError

      ├── ExportacaoNaoSuportadaError

      └── ErroGeracaoRelatorioError
```

---

# Objetivos da Categoria

As classes de exceções possuem os seguintes objetivos:

- padronizar o tratamento de erros da biblioteca;
- representar erros específicos do domínio;
- facilitar depuração e manutenção;
- permitir captura seletiva das exceções;
- documentar as condições de erro previstas pela arquitetura.

---

# Papel das Exceções na Arquitetura

As exceções podem ser lançadas por qualquer módulo da biblioteca.

```text
               aplicacao

                    │

      ┌─────────────┼─────────────┐

      ▼             ▼             ▼

entradaDados algoritmosOrdenacao visualizacoes

      │             │             │

      └─────────────┼─────────────┘

                    ▼

            LabEduSortError

                    │

                    ▼

             Tratamento Global
```

Toda exceção propagada pela biblioteca deverá pertencer à hierarquia `LabEduSortError`.

---

# Hierarquia das Exceções

```text
                           Exception
                               │
                               ▼
                     LabEduSortError
                               │
      ┌────────────────────────┼────────────────────────┐
      ▼                        ▼                        ▼

 Configuração             Entrada de Dados          Algoritmos

      │                        │                        │

ParametroInvalidoError   ArquivoNaoEncontradoError  AlgoritmoNaoImplementadoError

ConfiguracaoInvalidaError ArquivoInvalidoError      ListaVaziaError

                          TipoListaInvalidoError    TipoElementoInvalidoError

                          QuantidadeElementosInvalidaError

                          IntervaloValoresInvalidoError

                                                   ErroExecucaoAlgoritmoError

      ┌────────────────────────┼────────────────────────┐

      ▼                        ▼

Eventos/Estatísticas       Visualizações

EventoDesconhecidoError    FormatoVisualizacaoInvalidoError

EstatisticaInconsistenteError

TempoExecucaoInvalidoError ExportacaoNaoSuportadaError

                           ErroGeracaoRelatorioError
```

---

# Classe Base: LabEduSortError

## Objetivo

Representar a exceção base da biblioteca.

Todas as demais exceções especializam esta classe.

---

## Responsabilidades

- padronizar todas as exceções do projeto;
- permitir captura global;
- representar erros pertencentes ao domínio.

---

## Principais Atributos

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| mensagem | String | Descrição do erro |
| causa | Exception | Exceção original (opcional) |

---

## Diagrama UML

```text
                 Exception

                     ▲

                     │

         +----------------------------+

         |     LabEduSortError        |

         +----------------------------+

         | mensagem                   |

         | causa                      |

         +----------------------------+
```

---

## Regras Arquiteturais

A classe deverá:

- herdar de `Exception`;
- servir exclusivamente como classe base;
- nunca representar um erro específico;
- permitir extensão por especialização.

---

# Grupo: Configuração

## ParametroInvalidoError

Representa parâmetros inválidos informados pelo usuário ou pela aplicação.

### Situações típicas

- algoritmo inexistente;
- parâmetro obrigatório ausente;
- valor incompatível.

---

## ConfiguracaoInvalidaError

Representa inconsistências detectadas nas configurações da execução.

### Situações típicas

- configuração contraditória;
- diretórios inexistentes;
- parâmetros incompatíveis.

---

# Grupo: Entrada de Dados

## ArquivoNaoEncontradoError

Representa tentativa de leitura de arquivo inexistente.

---

## ArquivoInvalidoError

Representa arquivo com formato incompatível.

---

## TipoListaInvalidoError

Representa utilização de tipo de estrutura não suportado.

---

## QuantidadeElementosInvalidaError

Representa quantidade inválida de elementos.

---

## IntervaloValoresInvalidoError

Representa intervalo inválido para geração dos dados.

---

# Grupo: Algoritmos

## AlgoritmoNaoImplementadoError

Representa solicitação de algoritmo inexistente.

---

## ListaVaziaError

Representa tentativa de ordenar coleção vazia.

---

## TipoElementoInvalidoError

Representa elementos incompatíveis com o algoritmo.

---

## ErroExecucaoAlgoritmoError

Representa falhas inesperadas durante a execução do algoritmo.

---

# Grupo: Eventos e Estatísticas

## EventoDesconhecidoError

Representa evento não reconhecido pelos observadores.

---

## EstatisticaInconsistenteError

Representa inconsistências nas métricas calculadas.

---

## TempoExecucaoInvalidoError

Representa valores temporais inconsistentes.

---

# Grupo: Visualizações

## FormatoVisualizacaoInvalidoError

Representa formato de saída não suportado.

---

## ExportacaoNaoSuportadaError

Representa tentativa de exportação incompatível.

---

## ErroGeracaoRelatorioError

Representa falhas durante geração de relatórios.

---

# Diagrama UML da Categoria

```text
                       Exception

                           ▲

                           │

                 LabEduSortError

                           ▲

        ┌──────────┬────────┼────────┬─────────┐

        ▼          ▼        ▼        ▼         ▼

 Configuração  Entrada  Algoritmos Eventos Visualizações

        │          │        │        │         │

        ▼          ▼        ▼        ▼         ▼

Exceções específicas do domínio
```

---

# Fluxo de Utilização

```text
Módulos da Biblioteca

        │

        ▼

Validação

        │

        ├────────► Operação válida

        │

        └────────► Lança LabEduSortError

                            │

                            ▼

                   Aplicação / CLI

                            │

                            ▼

                  Tratamento da Exceção
```

---

# Relação com os Módulos

| Grupo de Exceções | Principais Produtores | Principais Consumidores |
|-------------------|-----------------------|--------------------------|
| Configuração | configuracoes, validacoes | aplicacao |
| Entrada de Dados | entradaDados | aplicacao |
| Algoritmos | algoritmosOrdenacao | aplicacao |
| Eventos | estatisticas | aplicacao |
| Visualizações | visualizacoes | aplicacao |

---

# Princípios Arquiteturais da Categoria

As classes de exceções deverão obedecer aos seguintes princípios:

- representar exclusivamente condições de erro;
- utilizar nomenclatura específica do domínio;
- evitar utilização de exceções genéricas;
- favorecer especialização em vez de mensagens ambíguas;
- permitir captura seletiva por categoria;
- preservar compatibilidade da hierarquia.

---

# Evolução da Categoria

Novas exceções poderão ser adicionadas por especialização da classe `LabEduSortError`, sem impacto nas implementações existentes.

A criação de novos grupos deverá ocorrer apenas quando representar uma nova responsabilidade arquitetural da biblioteca.

---

# Considerações da Categoria

A hierarquia de exceções do **LAB EDU SORT V1.0** estabelece um mecanismo uniforme para tratamento de erros em todos os módulos da biblioteca.

Ao centralizar todas as exceções na classe base `LabEduSortError`, a arquitetura facilita a captura global de falhas, ao mesmo tempo em que permite o tratamento específico de situações particulares por meio das subclasses especializadas.

Essa abordagem aumenta a clareza do código, melhora a documentação das condições de erro e favorece a evolução incremental da biblioteca, mantendo consistência entre implementação, arquitetura e documentação.

Na próxima seção será apresentada a **Arquitetura Consolidada**, reunindo os diagramas gerais do Modelo Canônico, as dependências entre categorias, as regras de evolução arquitetural, o versionamento do modelo e as considerações finais do documento.

---
