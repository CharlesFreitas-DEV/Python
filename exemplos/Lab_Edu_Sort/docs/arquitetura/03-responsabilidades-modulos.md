# Responsabilidades dos Módulos

## Projeto

**LAB EDU SORT V1.0**

---

# Objetivo

Este documento define as responsabilidades de cada módulo do projeto **LAB EDU SORT V1.0**.

O objetivo é estabelecer uma arquitetura baseada em alta coesão, baixo acoplamento e separação clara de responsabilidades, permitindo que cada módulo desempenhe uma função específica dentro da biblioteca.

Além de definir o papel de cada componente, este documento estabelece seus limites de atuação, suas dependências permitidas e aquilo que explicitamente não faz parte de suas responsabilidades.

---

# Princípios Arquiteturais

A organização dos módulos segue os princípios:

- SRP (Single Responsibility Principle)
- OCP (Open/Closed Principle)
- DIP (Dependency Inversion Principle)
- DRY (Don't Repeat Yourself)
- KISS (Keep It Simple)
- YAGNI (You Aren't Gonna Need It)

Cada módulo deverá possuir um único motivo para sofrer alterações.

---

# Visão Geral da Arquitetura

```text
                    +----------------------+
                    |      aplicacao       |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    |    entradaDados      |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    |      validacoes      |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    | algoritmosOrdenacao  |
                    +----------+-----------+
                               |
                 +-------------+-------------+
                 |                           |
                 ▼                           ▼
        +----------------+          +------------------+
        | estatisticas   |          |  visualizacoes   |
        +----------------+          +------------------+
                 |                           |
                 +-------------+-------------+
                               |
                               ▼
                    +----------------------+
                    |      Exportação      |
                    +----------------------+
```

---

# Módulo: algoritmosOrdenacao

## Objetivo

Implementar todos os algoritmos de ordenação disponibilizados pela biblioteca.

---

## Responsabilidades

- implementar algoritmos de ordenação;
- executar o processo de ordenação;
- manipular a coleção de dados;
- notificar eventos para coleta de estatísticas;
- devolver o conjunto de dados ordenado.

---

## Não é responsabilidade

- ler arquivos;
- validar parâmetros;
- gerar gráficos;
- exportar arquivos;
- interagir com o usuário;
- imprimir mensagens.

---

## Depende de

- modelos
- estatisticas
- utilitarios
- excecoes

---

## Utilizado por

- aplicacao
- benchmarks
- testes

---

# Módulo: estatisticas

## Objetivo

Coletar e consolidar todas as métricas produzidas durante a execução dos algoritmos.

---

## Responsabilidades

- contabilizar comparações;
- contabilizar trocas;
- medir tempo de execução;
- medir tempo de CPU;
- medir consumo de memória;
- registrar chamadas recursivas;
- consolidar estatísticas.

---

## Não é responsabilidade

- executar algoritmos;
- modificar listas;
- validar entradas;
- gerar visualizações.

---

## Depende de

- modelos

---

## Utilizado por

- algoritmosOrdenacao
- visualizacoes

---

# Módulo: visualizacoes

## Objetivo

Apresentar os resultados produzidos pela biblioteca.

---

## Responsabilidades

- apresentar tabelas;
- gerar gráficos;
- exibir comparações;
- produzir relatórios;
- organizar a saída visual dos resultados.

---

## Não é responsabilidade

- executar algoritmos;
- modificar dados;
- calcular estatísticas;
- validar entradas.

---

## Depende de

- estatisticas
- modelos

---

## Utilizado por

- aplicacao

---

# Módulo: entradaDados

## Objetivo

Construir os conjuntos de dados utilizados pelos algoritmos de ordenação.

---

## Responsabilidades

- ler arquivos;
- interpretar entradas;
- gerar listas automaticamente;
- construir listas aleatórias;
- construir listas parcialmente ordenadas;
- construir listas totalmente ordenadas;
- construir listas invertidas;
- fornecer os dados ao restante da aplicação.

---

## Não é responsabilidade

- executar algoritmos;
- calcular estatísticas;
- gerar gráficos.

---

## Depende de

- validacoes
- utilitarios
- excecoes

---

## Utilizado por

- aplicacao

---

# Módulo: validacoes

## Objetivo

Centralizar todas as validações da biblioteca.

---

## Responsabilidades

- validar tipos;
- validar parâmetros;
- validar intervalos;
- validar listas;
- validar arquivos;
- lançar exceções apropriadas quando necessário.

---

## Não é responsabilidade

- modificar dados;
- ordenar listas;
- produzir relatórios;
- gerar estatísticas.

---

## Depende de

- excecoes

---

## Utilizado por

- entradaDados
- algoritmosOrdenacao
- aplicacao

---

# Módulo: utilitarios

## Objetivo

Disponibilizar funcionalidades auxiliares reutilizáveis por toda a biblioteca.

---

## Responsabilidades

- manipulação de arquivos;
- funções auxiliares;
- conversões de dados;
- tratamento de textos;
- funcionalidades compartilhadas;
- rotinas genéricas.

---

## Não é responsabilidade

- implementar regras de negócio;
- executar algoritmos;
- validar parâmetros específicos;
- produzir estatísticas.

---

## Depende de

Nenhum módulo do domínio.

---

## Utilizado por

- entradaDados
- algoritmosOrdenacao
- visualizacoes
- estatisticas
- aplicacao

---

# Módulo: modelos

## Objetivo

Representar as entidades do domínio da biblioteca.

As classes deste módulo armazenam informações e transportam dados entre os demais componentes do sistema, sem implementar regras de negócio.

---

## Responsabilidades

- definir os modelos do domínio;
- representar entidades da aplicação;
- transportar informações entre módulos;
- manter a consistência estrutural dos dados.

---

## Não é responsabilidade

- executar algoritmos;
- validar informações;
- produzir estatísticas;
- realizar operações de entrada e saída.

---

## Depende de

Nenhum módulo do domínio.

---

## Utilizado por

- algoritmosOrdenacao
- estatisticas
- visualizacoes
- entradaDados
- aplicacao

---

# Módulo: excecoes

## Objetivo

Centralizar todas as exceções específicas da biblioteca.

---

## Responsabilidades

- definir exceções personalizadas;
- padronizar mensagens de erro;
- facilitar o tratamento de exceções;
- representar erros de domínio.

---

## Não é responsabilidade

- tratar exceções;
- registrar logs;
- executar validações;
- implementar regras de negócio.

---

## Depende de

Nenhum módulo do domínio.

---

## Utilizado por

Todos os módulos da biblioteca.

---

# Módulo: configuracoes

## Objetivo

Centralizar todas as configurações globais da biblioteca.

---

## Responsabilidades

- definir diretórios;
- armazenar constantes de configuração;
- centralizar parâmetros globais;
- disponibilizar configurações compartilhadas.

---

## Não é responsabilidade

- executar processamento;
- validar dados;
- implementar regras de negócio;
- produzir resultados.

---

## Depende de

Nenhum módulo do domínio.

---

## Utilizado por

Todos os módulos quando necessário.

---

# Módulo: aplicacao

## Objetivo

Orquestrar todo o fluxo de execução da biblioteca.

Este módulo representa a camada responsável por coordenar os demais componentes do sistema, independentemente da tecnologia utilizada para interação com o usuário.

A interface poderá ser:

- linha de comando (CLI);
- interface gráfica;
- aplicação Web;
- API;
- Jupyter Notebook;
- qualquer outra forma de integração.

---

## Responsabilidades

- iniciar a execução da aplicação;
- coordenar o fluxo entre os módulos;
- solicitar parâmetros ao usuário;
- controlar o ciclo de execução;
- encaminhar resultados para apresentação.

---

## Não é responsabilidade

- implementar algoritmos;
- calcular estatísticas;
- validar regras de negócio;
- gerar gráficos;
- manipular estruturas internas da biblioteca.

---

## Depende de

- entradaDados
- algoritmosOrdenacao
- visualizacoes

---

## Utilizado por

Representa o ponto de entrada da aplicação.

---

# Dependências Permitidas

```text
aplicacao
 │
 ├────────────► entradaDados
 │
 ├────────────► algoritmosOrdenacao
 │
 └────────────► visualizacoes

entradaDados
 │
 ├────────────► validacoes
 ├────────────► utilitarios
 ├────────────► modelos
 └────────────► excecoes

algoritmosOrdenacao
 │
 ├────────────► modelos
 ├────────────► estatisticas
 ├────────────► utilitarios
 └────────────► excecoes

estatisticas
 │
 └────────────► modelos

visualizacoes
 │
 ├────────────► estatisticas
 └────────────► modelos

validacoes
 │
 └────────────► excecoes
```

---

# Dependências Proibidas

Os seguintes relacionamentos não são permitidos pela arquitetura da biblioteca.

- visualizacoes → algoritmosOrdenacao
- visualizacoes → entradaDados
- estatisticas → algoritmosOrdenacao
- modelos → algoritmosOrdenacao
- modelos → entradaDados
- modelos → visualizacoes
- configuracoes → regras de negócio
- utilitarios → regras de negócio
- excecoes → lógica de domínio

Essas restrições preservam:

- baixo acoplamento;
- alta coesão;
- independência entre módulos;
- facilidade de manutenção;
- facilidade de testes.

---

# Resumo das Responsabilidades

| Módulo | Responsabilidade Principal |
|---------|----------------------------|
| aplicacao | Coordenar o fluxo da aplicação |
| entradaDados | Construir conjuntos de dados |
| validacoes | Validar entradas e parâmetros |
| algoritmosOrdenacao | Implementar algoritmos de ordenação |
| estatisticas | Coletar métricas da execução |
| visualizacoes | Apresentar os resultados |
| modelos | Representar entidades do domínio |
| utilitarios | Disponibilizar funcionalidades auxiliares |
| configuracoes | Centralizar configurações globais |
| excecoes | Definir exceções específicas |

---

# Diagrama Geral das Responsabilidades

```text
                     +---------------------+
                     |      aplicacao      |
                     +----------+----------+
                                |
          +---------------------+---------------------+
          |                     |                     |
          ▼                     ▼                     ▼
 +----------------+   +--------------------+   +------------------+
 | entradaDados   |   | algoritmosOrdenacao|   | visualizacoes    |
 +-------+--------+   +---------+----------+   +---------+--------+
         |                      |                        |
         ▼                      ▼                        ▼
 +----------------+     +----------------+      +----------------+
 | validacoes     |     | estatisticas   |      |    modelos     |
 +-------+--------+     +-------+--------+      +----------------+
         |                      |
         ▼                      ▼
 +----------------+     +----------------+
 | excecoes       |     | utilitarios    |
 +----------------+     +----------------+

configuracoes
      │
      └────────────► Disponível para todos os módulos
```

---

# Considerações Finais

A arquitetura definida neste documento estabelece a separação de responsabilidades entre todos os módulos da biblioteca **LAB EDU SORT V1.0**.

Essa organização proporciona:

- alta coesão entre os componentes;
- baixo acoplamento entre os módulos;
- facilidade para manutenção;
- facilidade para testes automatizados;
- extensibilidade da biblioteca;
- reutilização de componentes;
- facilidade para inclusão de novos algoritmos de ordenação;
- independência entre domínio e interface.

Este documento serve como referência arquitetural para os próximos artefatos do projeto, especialmente para o **Modelo de Classes**, os **Contratos entre Módulos** e a implementação da biblioteca na versão 1.0.

---
