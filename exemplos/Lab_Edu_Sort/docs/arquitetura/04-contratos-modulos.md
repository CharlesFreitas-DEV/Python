# Contratos entre os Módulos

## Projeto

**LAB EDU SORT V1.0**

---

# Objetivo

Este documento define os contratos arquiteturais existentes entre os módulos do **LAB EDU SORT V1.0**.

Um contrato representa o conjunto de regras que estabelece como os módulos se comunicam, definindo:

- objetos recebidos;
- objetos produzidos;
- responsabilidades;
- dependências permitidas;
- dependências proibidas;
- exceções previstas;
- garantias oferecidas.

Os contratos representam a interface arquitetural da biblioteca e permanecem independentes da implementação interna dos módulos.

---

# Conceito de Contrato

Um contrato descreve o comportamento esperado de um módulo dentro da arquitetura.

Ele define:

- **o que o módulo fornece**;
- **o que o módulo consome**;
- **como ocorre a comunicação com outros módulos**;
- **quais regras devem ser preservadas durante a evolução do sistema**.

Um contrato não descreve detalhes de implementação.

Ele define apenas o comportamento público esperado.

---

# Comunicação baseada em Objetos do Domínio

A comunicação entre módulos ocorre exclusivamente através de objetos pertencentes ao domínio da aplicação.

Nenhum módulo poderá:

- acessar estruturas internas de outro módulo;
- depender de detalhes de implementação;
- manipular atributos privados de outro componente.

Os objetos utilizados na comunicação serão definidos no documento:

```text
02-modelo-classes.md
```

Esse documento representa o **Modelo Canônico do Domínio** do projeto.

---

# Objetos Arquiteturais do Domínio

Os principais objetos utilizados nos contratos da V1.0 são:

| Objeto | Responsabilidade |
|---|---|
| ConfiguracaoExecucao | Representa os parâmetros gerais de uma execução |
| ConfiguracaoEntrada | Representa a configuração da origem dos dados |
| ConjuntoDados | Representa os elementos que serão processados pelos algoritmos |
| ResultadoOrdenacao | Representa o resultado produzido por um algoritmo |
| EventoOrdenacao | Representa eventos produzidos durante a execução |
| EstatisticasOrdenacao | Representa as métricas coletadas durante o processamento |
| ConfiguracaoVisualizacao | Representa parâmetros de apresentação dos resultados |

A definição detalhada destes objetos pertence ao documento:

```text
02-modelo-classes.md
```

---

# Princípios dos Contratos

Todos os contratos seguem os princípios arquiteturais definidos para a biblioteca.

---

## Estabilidade

Os contratos devem permanecer estáveis durante a evolução do projeto.

Alterações frequentes nos contratos devem ser evitadas.

---

## Baixo Acoplamento

Um módulo deve conhecer apenas o contrato público de outro módulo.

Detalhes internos não devem ser compartilhados.

---

## Alta Coesão

Cada módulo deve possuir uma responsabilidade claramente definida.

---

## Encapsulamento

Os módulos devem proteger suas estruturas internas.

A comunicação ocorre somente através dos objetos definidos pelos contratos.

---

## Extensibilidade

Novos módulos poderão ser adicionados sem modificar contratos existentes.

---

## Independência da Implementação

A implementação interna poderá mudar desde que o contrato permaneça válido.

---

# Estrutura de um Contrato

Cada contrato possui os seguintes elementos:

## Objetivo

Define a finalidade do módulo.

---

## Objetos Recebidos

Define os objetos consumidos pelo módulo.

---

## Objetos Produzidos

Define os objetos criados pelo módulo.

---

## Dependências Permitidas

Define quais módulos podem ser utilizados.

---

## Dependências Proibidas

Define quais módulos não podem ser acessados.

---

## Exceções Previstas

Define erros específicos que podem ocorrer.

---

## Garantias

Define o comportamento que o módulo assegura aos consumidores.

---

# Contrato do Módulo: aplicacao

## Objetivo

Coordenar o fluxo geral de execução da biblioteca.

O módulo `aplicacao` representa a camada responsável pela orquestração da aplicação.

Ele substitui o conceito de uma CLI fixa, permitindo futuramente diferentes formas de interação:

- linha de comando;
- interface gráfica;
- aplicação Web;
- API;
- notebooks.

O módulo não implementa regras de negócio.

---

# Responsabilidades

O módulo `aplicacao` é responsável por:

- iniciar o fluxo de execução;
- receber configurações da execução;
- coordenar os demais módulos;
- encaminhar objetos entre componentes;
- controlar o ciclo de vida da aplicação.

---

# Objetos Recebidos

```text
ConfiguracaoExecucao
```

Representa os parâmetros necessários para iniciar uma execução.

---

# Objetos Produzidos

```text
ConfiguracaoEntrada
```

Representa a configuração necessária para criação dos dados de entrada.

---

# Objetos Consumidos

O módulo consome:

```text
ConjuntoDados

ResultadoOrdenacao

EstatisticasOrdenacao
```

Esses objetos são produzidos pelos módulos responsáveis pelo processamento.

---

# Objetos Encaminhados

O fluxo coordenado pelo módulo é:

```text
ConfiguracaoEntrada
        │
        ▼
entradaDados


ConjuntoDados
        │
        ▼
algoritmosOrdenacao


ResultadoOrdenacao
        │
        ▼
visualizacoes


EstatisticasOrdenacao
        │
        ▼
visualizacoes
```

---

# Dependências Permitidas

O módulo poderá depender apenas de:

```text
entradaDados

algoritmosOrdenacao

visualizacoes
```

---

# Dependências Proibidas

O módulo não deverá acessar diretamente:

```text
estatisticas

modelos

utilitarios

configuracoes

excecoes
```

Esses componentes pertencem às camadas internas da biblioteca.

---

# Exceções Previstas

Podem ser propagadas:

```text
ParametroInvalidoError

ConfiguracaoInvalidaError

ArquivoInvalidoError

AlgoritmoNaoImplementadoError

ErroExecucaoAlgoritmoError
```

---

# Garantias

O módulo garante que:

- não implementa algoritmos;
- não realiza validações específicas;
- não calcula estatísticas;
- não altera objetos do domínio;
- apenas coordena o fluxo da aplicação.

---

# Contrato do Módulo: entradaDados

## Objetivo

Construir objetos `ConjuntoDados` válidos para processamento pelos algoritmos de ordenação.

Este módulo representa a camada responsável pela obtenção e preparação dos dados de entrada.

---

# Responsabilidades

O módulo `entradaDados` é responsável por:

- ler arquivos de entrada;
- interpretar configurações de geração;
- criar conjuntos automaticamente;
- gerar listas ordenadas;
- gerar listas parcialmente ordenadas;
- gerar listas aleatórias;
- preparar dados para processamento.

---

# Objetos Recebidos

```text
ConfiguracaoEntrada
```

Representa as informações necessárias para criação dos dados.

---

# Objetos Produzidos

```text
ConjuntoDados
```

Representa a coleção de elementos pronta para processamento.

---

# Objetos Consumidos

O módulo consome:

```text
ConfiguracaoEntrada
```

---

# Objetos Encaminhados

O fluxo produzido é:

```text
ConjuntoDados

        │

        ▼

algoritmosOrdenacao
```

---

# Dependências Permitidas

O módulo poderá depender de:

```text
validacoes

utilitarios

modelos

excecoes
```

---

# Dependências Proibidas

O módulo não poderá acessar:

```text
algoritmosOrdenacao

estatisticas

visualizacoes

aplicacao
```

---

# Exceções Previstas

Podem ocorrer:

```text
ArquivoNaoEncontradoError

ArquivoInvalidoError

TipoListaInvalidoError

QuantidadeElementosInvalidaError

IntervaloValoresInvalidoError
```

---

# Garantias

O módulo garante que:

- todo `ConjuntoDados` produzido será válido;
- nenhum algoritmo será executado;
- nenhuma estatística será coletada;
- nenhuma apresentação será gerada;
- nenhuma regra de ordenação será aplicada.

---

# Considerações Parciais

Os contratos definidos nesta primeira parte estabelecem as regras de comunicação da camada de orquestração e preparação dos dados.

O módulo `aplicacao` controla o fluxo da biblioteca, enquanto o módulo `entradaDados` é responsável exclusivamente pela construção dos objetos `ConjuntoDados`.

A comunicação entre esses componentes ocorre exclusivamente através de objetos do domínio definidos no Modelo Canônico do Domínio.

As próximas partes deste documento irão especificar os contratos dos módulos responsáveis pelo processamento, coleta de métricas, apresentação dos resultados e infraestrutura de suporte.

---

# Contrato do Módulo: algoritmosOrdenacao

## Objetivo

Executar os algoritmos de ordenação disponibilizados pela biblioteca.

O módulo `algoritmosOrdenacao` representa o núcleo funcional do **LAB EDU SORT V1.0**, sendo responsável exclusivamente pelo processamento dos dados.

Sua responsabilidade é transformar um objeto `ConjuntoDados` em um objeto `ResultadoOrdenacao`.

O módulo não possui conhecimento sobre:

- origem dos dados;
- apresentação dos resultados;
- coleta direta de estatísticas;
- observadores registrados.

---

# Responsabilidades

O módulo `algoritmosOrdenacao` é responsável por:

- disponibilizar os algoritmos de ordenação implementados;
- executar o algoritmo selecionado;
- controlar o processamento dos elementos;
- produzir o resultado ordenado;
- publicar eventos durante a execução.

---

# Objetos Recebidos

```text
ConjuntoDados
```

Representa os dados que serão submetidos ao algoritmo de ordenação.

---

# Objetos Produzidos

```text
ResultadoOrdenacao
```

Representa o resultado final produzido pelo algoritmo.

---

# Eventos Publicados

Durante a execução, o módulo publica eventos de domínio.

Esses eventos representam ocorrências importantes do processamento.

Exemplos:

```text
EventoOrdenacao

    ├── ComparacaoRealizada
    │
    ├── TrocaRealizada
    │
    ├── ElementoLido
    │
    ├── ElementoEscrito
    │
    ├── ChamadaRecursivaIniciada
    │
    ├── ChamadaRecursivaFinalizada
    │
    ├── AlgoritmoIniciado
    │
    └── AlgoritmoFinalizado
```

A definição formal desses objetos pertence ao:

```text
02-modelo-classes.md
```

---

# Objetos Consumidos

```text
ConjuntoDados
```

---

# Objetos Encaminhados

O módulo encaminha:

```text
ResultadoOrdenacao
```

para o módulo responsável pela aplicação.

---

# Comunicação com Outros Módulos

## Response

Ao finalizar uma execução:

```text
algoritmosOrdenacao

        │

        ▼

ResultadoOrdenacao
```

---

## Event

Durante a execução:

```text
algoritmosOrdenacao

        │

        ▼

EventoOrdenacao
```

Os eventos poderão ser consumidos por qualquer observador registrado.

---

# Dependências Permitidas

O módulo poderá depender de:

```text
modelos

utilitarios

excecoes
```

---

# Dependências Proibidas

O módulo não poderá acessar:

```text
entradaDados

estatisticas

visualizacoes

aplicacao

configuracoes
```

---

# Exceções Previstas

Podem ocorrer:

```text
AlgoritmoNaoImplementadoError

ListaVaziaError

TipoElementoInvalidoError

ErroExecucaoAlgoritmoError
```

---

# Garantias

O módulo garante que:

- produzirá exatamente um `ResultadoOrdenacao`;
- publicará os eventos necessários durante a execução;
- não conhecerá seus observadores;
- não realizará coleta direta de métricas;
- permanecerá independente da forma de apresentação dos resultados.

---

# Contrato do Módulo: estatisticas

## Objetivo

Coletar e consolidar as métricas produzidas durante a execução dos algoritmos de ordenação.

O módulo `estatisticas` implementa o papel de **Observador (Observer)** dentro da arquitetura baseada em eventos.

Ele recebe eventos publicados pelos algoritmos e transforma essas informações em um objeto `EstatisticasOrdenacao`.

---

# Responsabilidades

O módulo `estatisticas` é responsável por:

- observar eventos de execução;
- registrar métricas;
- contabilizar operações realizadas;
- medir informações temporais;
- consolidar os dados coletados.

---

# Modelo de Funcionamento

O fluxo segue o padrão Observer:

```text
algoritmosOrdenacao

        │

        │ Publica EventoOrdenacao

        ▼

estatisticas

        │

        ▼

EstatisticasOrdenacao
```

O produtor dos eventos não possui conhecimento sobre o observador.

---

# Objetos Recebidos

Eventos produzidos durante a execução:

```text
EventoOrdenacao
```

Exemplos:

```text
ComparacaoRealizada

TrocaRealizada

ElementoLido

ElementoEscrito

ChamadaRecursivaIniciada

ChamadaRecursivaFinalizada

AlgoritmoIniciado

AlgoritmoFinalizado
```

---

# Objetos Produzidos

```text
EstatisticasOrdenacao
```

Representa todas as métricas consolidadas da execução.

---

# Objetos Consumidos

```text
EventoOrdenacao
```

---

# Objetos Encaminhados

O módulo encaminha:

```text
EstatisticasOrdenacao
```

para a camada de aplicação.

---

# Comunicação com Outros Módulos

## Event

Recebe:

```text
EventoOrdenacao
```

de:

```text
algoritmosOrdenacao
```

---

## Response

Produz:

```text
EstatisticasOrdenacao
```

para:

```text
aplicacao
```

---

# Dependências Permitidas

O módulo poderá depender de:

```text
modelos
```

---

# Dependências Proibidas

O módulo não poderá acessar:

```text
entradaDados

algoritmosOrdenacao

visualizacoes

aplicacao
```

---

# Exceções Previstas

Podem ocorrer:

```text
EstatisticaInconsistenteError

EventoDesconhecidoError

TempoExecucaoInvalidoError
```

---

# Garantias

O módulo garante que:

- nenhuma métrica interfere no algoritmo;
- todos os eventos recebidos serão processados;
- as estatísticas serão consistentes;
- novas métricas poderão ser adicionadas sem modificar algoritmos existentes.

---

# Contrato do Módulo: visualizacoes

## Objetivo

Apresentar os resultados produzidos pela biblioteca.

O módulo `visualizacoes` representa a camada responsável pela apresentação das informações ao usuário.

Ele não executa processamento e não altera objetos do domínio.

---

# Responsabilidades

O módulo é responsável por:

- apresentar resultados;
- gerar relatórios;
- produzir tabelas;
- produzir gráficos;
- exportar informações.

---

# Objetos Recebidos

```text
ResultadoOrdenacao

EstatisticasOrdenacao

ConfiguracaoVisualizacao
```

---

# Objetos Produzidos

Representações finais dos resultados.

Exemplos:

```text
Relatorio

Tabela

Grafico

ArquivoExportado

SaidaTextual
```

---

# Objetos Consumidos

```text
ResultadoOrdenacao

EstatisticasOrdenacao

ConfiguracaoVisualizacao
```

---

# Objetos Encaminhados

Nenhum.

Este módulo representa a etapa final do fluxo da aplicação.

---

# Comunicação com Outros Módulos

## Request

Recebe solicitações da aplicação:

```text
aplicacao

        │

        ▼

visualizacoes
```

---

# Dependências Permitidas

O módulo poderá depender de:

```text
modelos
```

---

# Dependências Proibidas

O módulo não poderá acessar:

```text
entradaDados

algoritmosOrdenacao

estatisticas

aplicacao
```

---

# Exceções Previstas

Podem ocorrer:

```text
FormatoVisualizacaoInvalidoError

ExportacaoNaoSuportadaError

ErroGeracaoRelatorioError
```

---

# Garantias

O módulo garante que:

- nunca modificará objetos recebidos;
- não executará algoritmos;
- não coletará estatísticas;
- utilizará exclusivamente informações fornecidas pelos objetos do domínio;
- permanecerá independente da origem dos dados.

---

# Considerações Parciais

Os contratos definidos nesta seção representam o núcleo funcional do **LAB EDU SORT V1.0**.

O módulo `algoritmosOrdenacao` permanece responsável exclusivamente pelo processamento, enquanto o módulo `estatisticas` atua como observador independente através da publicação de eventos.

Essa separação elimina o acoplamento entre algoritmo e medição, permitindo evolução independente dos componentes.

O módulo `visualizacoes` encerra o fluxo da aplicação consumindo apenas os resultados produzidos, mantendo a separação entre processamento e apresentação.

A arquitetura resultante permanece alinhada aos princípios:

- responsabilidade única;
- baixo acoplamento;
- alta coesão;
- extensibilidade;
- separação de responsabilidades.

---

# Contrato do Módulo: validacoes

## Objetivo

Garantir a consistência e validade dos objetos utilizados pela biblioteca.

O módulo `validacoes` centraliza as regras de validação necessárias para garantir que os dados utilizados pelos demais componentes estejam em condições adequadas de processamento.

Nenhum outro módulo deverá implementar validações de domínio duplicadas.

---

# Responsabilidades

O módulo `validacoes` é responsável por:

- validar parâmetros recebidos;
- validar configurações;
- validar objetos do domínio;
- garantir consistência dos dados;
- impedir processamento de informações inválidas.

---

# Objetos Recebidos

O módulo poderá receber objetos do domínio que necessitem de validação.

Exemplos:

```text
ConfiguracaoExecucao

ConfiguracaoEntrada

ConjuntoDados

ConfiguracaoVisualizacao
```

---

# Objetos Produzidos

O módulo não produz novos objetos de domínio.

Após uma validação bem-sucedida, o objeto recebido permanece válido para utilização.

---

# Objetos Consumidos

```text
Objetos do domínio
```

---

# Objetos Encaminhados

O módulo retorna o próprio objeto validado.

Exemplo:

```text
Entrada:

ConfiguracaoEntrada

        │

        ▼

validacoes

        │

        ▼

ConfiguracaoEntrada válida
```

---

# Comunicação com Outros Módulos

## Request

Recebe solicitações de validação dos módulos autorizados.

Exemplo:

```text
entradaDados

        │

        ▼

validacoes
```

---

# Dependências Permitidas

O módulo poderá depender de:

```text
modelos

excecoes
```

---

# Dependências Proibidas

O módulo não poderá acessar:

```text
algoritmosOrdenacao

estatisticas

visualizacoes

entradaDados

aplicacao
```

---

# Exceções Previstas

Podem ocorrer:

```text
ParametroInvalidoError

ValorInvalidoError

TipoInvalidoError

ConfiguracaoInvalidaError

ConjuntoDadosInvalidoError
```

---

# Garantias

O módulo garante que:

- todos os objetos validados estarão consistentes;
- nenhuma regra de negócio será executada;
- nenhum processamento será realizado;
- nenhuma dependência circular será criada.

---

# Contrato do Módulo: utilitarios

## Objetivo

Disponibilizar funcionalidades auxiliares reutilizáveis pelos demais módulos da biblioteca.

O módulo `utilitarios` contém recursos genéricos que não pertencem diretamente ao domínio da ordenação.

---

# Responsabilidades

O módulo é responsável por:

- fornecer funções auxiliares;
- disponibilizar operações genéricas;
- reduzir duplicação de código;
- oferecer serviços compartilhados.

---

# Exemplos de Responsabilidades

Podem ser disponibilizados:

```text
Manipulação de arquivos

Conversões de dados

Operações auxiliares

Funções matemáticas genéricas

Formatações comuns
```

---

# Objetos Recebidos

Pode receber objetos diversos conforme a necessidade do serviço utilizado.

---

# Objetos Produzidos

Pode produzir:

```text
Valores auxiliares

Estruturas temporárias

Resultados intermediários
```

---

# Objetos Consumidos

Objetos necessários para execução de funções auxiliares.

---

# Comunicação com Outros Módulos

O módulo atua como fornecedor de serviços.

Exemplo:

```text
entradaDados

        │

        ▼

utilitarios
```

---

# Dependências Permitidas

O módulo poderá depender de:

```text
modelos
```

somente quando necessário.

---

# Dependências Proibidas

O módulo não poderá acessar:

```text
algoritmosOrdenacao

estatisticas

visualizacoes

entradaDados

aplicacao
```

---

# Exceções Previstas

Podem ocorrer:

```text
ErroConversaoError

ErroFormatoError

ErroArquivoError
```

---

# Garantias

O módulo garante que:

- não implementa regras de negócio;
- não conhece fluxo da aplicação;
- não possui dependência de módulos superiores;
- suas funcionalidades podem ser reutilizadas.

---

# Contrato do Módulo: modelos

## Objetivo

Representar todos os objetos pertencentes ao domínio do **LAB EDU SORT V1.0**.

O módulo `modelos` representa o **Modelo Canônico do Domínio**.

Todos os contratos da arquitetura utilizam objetos definidos neste módulo.

---

# Responsabilidades

O módulo é responsável por:

- definir entidades do domínio;
- definir objetos de comunicação;
- representar estados da aplicação;
- garantir consistência estrutural dos objetos.

---

# Organização Conceitual

Os objetos serão organizados nas seguintes categorias:

```text
Configuração

Domínio

Resultados

Eventos

Estatísticas

Exceções
```

A definição detalhada pertence ao:

```text
02-modelo-classes.md
```

---

# Objetos Produzidos

Exemplos:

```text
ConfiguracaoExecucao

ConfiguracaoEntrada

ConjuntoDados

ResultadoOrdenacao

EventoOrdenacao

EstatisticasOrdenacao

ConfiguracaoVisualizacao
```

---

# Objetos Recebidos

Nenhum.

O módulo representa a origem das estruturas do domínio.

---

# Dependências Permitidas

Nenhuma.

O módulo constitui a base estrutural da arquitetura.

---

# Dependências Proibidas

O módulo não poderá depender de:

```text
aplicacao

entradaDados

algoritmosOrdenacao

estatisticas

visualizacoes

configuracoes

utilitarios

excecoes
```

---

# Exceções Previstas

Nenhuma.

---

# Garantias

O módulo garante que:

- todos os objetos do domínio possuem definição única;
- não existem duplicidades de modelos;
- nenhum processamento é realizado;
- nenhum fluxo de aplicação é conhecido.

---

# Contrato do Módulo: configuracoes

## Objetivo

Centralizar configurações utilizadas pela biblioteca.

O módulo `configuracoes` mantém parâmetros gerais necessários para execução e funcionamento do sistema.

---

# Responsabilidades

O módulo é responsável por:

- disponibilizar configurações padrão;
- armazenar constantes de configuração;
- fornecer parâmetros globais autorizados.

---

# Objetos Recebidos

```text
ConfiguracaoExecucao
```

---

# Objetos Produzidos

```text
ConfiguracaoExecucao

ConfiguracaoEntrada

ConfiguracaoVisualizacao
```

---

# Objetos Consumidos

Configurações utilizadas durante a execução.

---

# Comunicação com Outros Módulos

Exemplo:

```text
aplicacao

        │

        ▼

configuracoes
```

---

# Dependências Permitidas

```text
modelos
```

---

# Dependências Proibidas

O módulo não poderá acessar:

```text
algoritmosOrdenacao

estatisticas

visualizacoes

entradaDados
```

---

# Exceções Previstas

```text
ConfiguracaoInvalidaError
```

---

# Garantias

O módulo garante que:

- configurações permanecem centralizadas;
- valores padrão possuem uma única definição;
- nenhuma regra de processamento é implementada.

---

# Contrato do Módulo: excecoes

## Objetivo

Definir todas as exceções específicas utilizadas pela biblioteca.

O módulo `excecoes` representa o catálogo oficial de erros do domínio.

---

# Responsabilidades

O módulo é responsável por:

- definir classes de exceção;
- padronizar erros;
- facilitar tratamento pelos consumidores.

---

# Objetos Produzidos

Exceções do domínio.

Exemplos:

```text
ParametroInvalidoError

ConfiguracaoInvalidaError

ArquivoNaoEncontradoError

ArquivoInvalidoError

AlgoritmoNaoImplementadoError

EventoDesconhecidoError

EstatisticaInconsistenteError
```

---

# Objetos Recebidos

Nenhum.

---

# Objetos Consumidos

Nenhum.

---

# Comunicação com Outros Módulos

As exceções podem ser utilizadas por qualquer módulo autorizado.

Exemplo:

```text
entradaDados

        │

        ▼

excecoes
```

---

# Dependências Permitidas

Nenhuma.

---

# Dependências Proibidas

Todos os módulos de negócio.

---

# Exceções Previstas

Não se aplica.

O próprio módulo representa as exceções arquiteturais.

---

# Garantias

O módulo garante que:

- todos os erros possuem definição única;
- não haverá duplicidade de exceções;
- os módulos utilizarão o mesmo padrão de tratamento.

---

# Considerações Parciais

Os contratos apresentados nesta seção representam os componentes estruturais da arquitetura do **LAB EDU SORT V1.0**.

O módulo `modelos` estabelece o Modelo Canônico do Domínio, sendo a referência para todos os objetos compartilhados.

Os módulos `validacoes`, `utilitarios`, `configuracoes` e `excecoes` fornecem serviços fundamentais para o funcionamento da biblioteca, mantendo responsabilidades isoladas e dependências controladas.

Com esta definição, a arquitetura garante:

- separação de responsabilidades;
- reutilização;
- baixo acoplamento;
- consistência dos objetos;
- facilidade de evolução.

---

# Fluxos, Diagramas e Evolução dos Contratos

Esta seção apresenta a visão consolidada da comunicação entre os módulos do **LAB EDU SORT V1.0**.

Os fluxos apresentados neste documento representam a arquitetura oficial da biblioteca.

Toda comunicação ocorre através de contratos definidos anteriormente e utilizando objetos do domínio pertencentes ao:

```text
02-modelo-classes.md
```

Este documento representa o **Modelo Canônico do Domínio**.

---

# Tipos de Comunicação

A arquitetura do LAB EDU SORT V1.0 utiliza três tipos fundamentais de comunicação:

- Request;
- Response;
- Event.

Cada comunicação entre módulos deverá ser classificada em uma dessas categorias.

---

# Request

## Definição

Representa uma solicitação realizada por um módulo para que outro módulo execute determinada responsabilidade.

O módulo solicitante envia um objeto contendo todas as informações necessárias para processamento.

---

## Características

Um Request:

- possui um módulo consumidor;
- inicia uma operação;
- transporta informações necessárias;
- normalmente gera uma resposta.

---

## Exemplo

```text
aplicacao

      Request

          │

          ▼

entradaDados

ConfiguracaoEntrada
```

---

# Response

## Definição

Representa o resultado produzido por um módulo após atender uma solicitação.

O Response contém informações produzidas durante o processamento.

---

## Características

Um Response:

- representa uma saída do processamento;
- contém objetos do domínio;
- preserva o encapsulamento do módulo produtor.

---

## Exemplo

```text
algoritmosOrdenacao

        Response

             │

             ▼

ResultadoOrdenacao
```

---

# Event

## Definição

Representa uma ocorrência relevante durante a execução de um módulo.

O produtor publica o evento sem conhecer seus consumidores.

---

## Características

Um Event:

- possui baixo acoplamento;
- pode possuir múltiplos consumidores;
- não exige resposta;
- permite extensibilidade.

---

## Exemplo

```text
algoritmosOrdenacao

          Event

            │

            ▼

     EventoOrdenacao

            │

     ┌──────┴──────┐

     ▼             ▼

estatisticas   Outros Observadores
```

---

# Fluxo Geral da Aplicação

O fluxo completo da execução do LAB EDU SORT V1.0 é:

```text
                    ConfiguracaoExecucao
                              │
                              ▼
                         aplicacao
                              │
                              │ Request
                              ▼
                    ConfiguracaoEntrada
                              │
                              ▼
                       entradaDados
                              │
                              │ Response
                              ▼
                       ConjuntoDados
                              │
                              ▼
                  algoritmosOrdenacao
                       │              │
                       │              │
                       │              │ Event
                       │              ▼
                       │       EventoOrdenacao
                       │              │
                       │              ▼
                       │        estatisticas
                       │              │
                       │              │ Response
                       │              ▼
                       │  EstatisticasOrdenacao
                       │
                       │ Response
                       ▼
                ResultadoOrdenacao
                              │
                              ▼
                       visualizacoes
                              │
                              ▼
                  Representação Final
```

---

# Fluxo dos Objetos do Domínio

Os objetos percorrem o seguinte ciclo de vida:

```text
ConfiguracaoExecucao

        │

        ▼

ConfiguracaoEntrada

        │

        ▼

ConjuntoDados

        │

        ▼

ResultadoOrdenacao

        │

        ▼

EstatisticasOrdenacao

        │

        ▼

Representação Final
```

A estrutura desses objetos será detalhada exclusivamente no:

```text
02-modelo-classes.md
```

---

# Fluxo da Arquitetura Orientada a Eventos

O mecanismo de coleta de estatísticas utiliza o padrão Observer.

O algoritmo publica eventos.

Os observadores processam esses eventos.

```text
              algoritmosOrdenacao

                       │

                       │ Event

                       ▼

                EventoOrdenacao

                       │

          ┌────────────┼────────────┐

          ▼            ▼            ▼

   estatisticas   auditoria     logs
                  (futuro)    (futuro)
```

Na versão 1.0:

```text
EventoOrdenacao

        │

        ▼

estatisticas

        │

        ▼

EstatisticasOrdenacao
```

---

# Matriz de Comunicação entre Módulos

A matriz abaixo representa todas as comunicações permitidas na arquitetura.

| Origem | Destino | Tipo | Objeto |
|---|---|---|---|
| aplicacao | entradaDados | Request | ConfiguracaoEntrada |
| entradaDados | algoritmosOrdenacao | Response | ConjuntoDados |
| algoritmosOrdenacao | aplicacao | Response | ResultadoOrdenacao |
| algoritmosOrdenacao | estatisticas | Event | EventoOrdenacao |
| estatisticas | aplicacao | Response | EstatisticasOrdenacao |
| aplicacao | visualizacoes | Request | ResultadoOrdenacao |
| aplicacao | visualizacoes | Request | EstatisticasOrdenacao |
| aplicacao | visualizacoes | Request | ConfiguracaoVisualizacao |

---

# Diagrama Geral das Dependências

```text
                         aplicacao
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼

   entradaDados     algoritmosOrdenacao    visualizacoes

          │                   │

          ▼                   ▼

    validacoes        PublicadorEventos

          │                   │

          ▼                   ▼

       excecoes        estatisticas


                    modelos

                      ▲

                      │

        Todos os módulos utilizam exclusivamente
        objetos definidos no domínio.


                 configuracoes

                      ▲

                      │

          Configurações compartilhadas.


                  utilitarios

                      ▲

                      │

          Serviços auxiliares reutilizáveis.
```

---

# Regras Arquiteturais da Comunicação

## Uso obrigatório de contratos

Todo relacionamento entre módulos deverá possuir um contrato definido.

---

## Comunicação exclusivamente por objetos do domínio

Nenhum módulo poderá compartilhar estruturas internas.

A comunicação deverá utilizar exclusivamente objetos definidos no modelo canônico.

---

## Proibição de dependência circular

Um módulo nunca poderá criar dependências que retornem ao próprio fluxo de execução.

---

## Independência entre camadas

Os módulos internos não devem conhecer detalhes de:

- interface gráfica;
- linha de comando;
- API;
- persistência;
- mecanismos externos.

---

## Separação entre processamento e observação

Os algoritmos nunca deverão:

- calcular estatísticas diretamente;
- conhecer observadores;
- depender do módulo estatisticas.

---

# Evolução dos Contratos

Os contratos devem permanecer estáveis durante a evolução do projeto.

Alterações deverão respeitar compatibilidade arquitetural.

---

# Alterações Compatíveis

São consideradas compatíveis:

- adicionar novos algoritmos;
- adicionar novos eventos;
- adicionar novos observadores;
- adicionar novos formatos de visualização;
- adicionar novos objetos opcionais.

---

# Alterações Incompatíveis

São consideradas incompatíveis:

- remover objetos existentes;
- alterar significado de atributos;
- modificar responsabilidades;
- alterar fluxo obrigatório de comunicação;
- substituir contratos existentes.

---

# Versionamento dos Contratos

Cada contrato possui uma versão associada.

Exemplo:

```text
Contrato:

algoritmosOrdenacao

Versão:

1.0
```

Caso ocorra uma alteração incompatível:

```text
Contrato:

algoritmosOrdenacao

Versão:

2.0
```

Alterações incompatíveis deverão gerar uma nova versão do contrato.

---

# Relação com o Modelo Canônico do Domínio

Toda evolução arquitetural deverá permanecer sincronizada com:

```text
02-modelo-classes.md
```

Alterações envolvendo:

- entidades;
- eventos;
- resultados;
- configurações;

deverão ser refletidas simultaneamente em:

- modelo de classes;
- contratos;
- testes automatizados;
- documentação arquitetural.

---

# Checklist de Conformidade Arquitetural

Antes da criação ou alteração de qualquer módulo deverá ser verificado:

| Item | Obrigatório |
|---|---|
| Possui responsabilidade única | Sim |
| Possui contrato definido | Sim |
| Utiliza objetos do domínio | Sim |
| Comunicação classificada como Request, Response ou Event | Sim |
| Respeita dependências permitidas | Sim |
| Não cria dependências circulares | Sim |
| Mantém compatibilidade de versão | Sim |
| Está alinhado ao modelo canônico | Sim |

---

# Considerações Finais

Os contratos definidos neste documento estabelecem a especificação oficial da comunicação entre os módulos do **LAB EDU SORT V1.0**.

A arquitetura adotada utiliza:

- contratos explícitos;
- objetos de domínio compartilhados;
- comunicação Request/Response;
- comunicação orientada a eventos;
- padrão Observer para coleta de estatísticas.

Essa organização permite que cada módulo evolua de forma independente, mantendo:

- baixo acoplamento;
- alta coesão;
- responsabilidade única;
- facilidade de testes;
- extensibilidade.

O documento **04-contratos-modulos.md** juntamente com:

```text
01-modelo-conceitual.md

02-modelo-classes.md

03-responsabilidades-modulos.md
```

constitui a base arquitetural do **Milestone 02 — Modelagem dos Dados e Estruturas Básicas**.

A implementação da V1.0 deverá respeitar integralmente os contratos definidos neste documento.

---
