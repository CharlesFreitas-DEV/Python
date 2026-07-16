# 🤖 Robô Cartesiano

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![OOP](https://img.shields.io/badge/paradigm-Object%20Oriented%20Programming-purple)
![Config](https://img.shields.io/badge/configuration-INI-orange)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)
![Open Source](https://img.shields.io/badge/open%20source-yes-brightgreen)

Simulador de movimentação de um robô em um plano cartesiano utilizando coordenadas **X** e **Y**.

O projeto recebe uma configuração através de um arquivo `robo_input.ini`, interpreta uma sequência de comandos de movimentação e simula o deslocamento de um robô dentro de uma área delimitada.

A aplicação foi desenvolvida em Python com foco educacional, explorando conceitos de:

- Programação Orientada a Objetos;
- Modelagem de domínio;
- Organização modular;
- Separação de responsabilidades;
- Manipulação de arquivos;
- Validação de dados;
- Tratamento de exceções.

---

# 📌 Índice

- [📖 Sobre o projeto](#-sobre-o-projeto)
- [✨ Funcionalidades](#-funcionalidades)
- [📂 Estrutura do projeto](#-estrutura-do-projeto)
- [⚙️ Requisitos](#️-requisitos)
- [🚀 Como executar](#-como-executar)
- [🔄 Fluxo de execução](#-fluxo-de-execução)
- [🧪 Exemplo de entrada e saída](#-exemplo-de-entrada-e-saída)
- [🧠 Explicação técnica](#-explicação-técnica)
- [🏗️ Arquitetura e princípios utilizados](#️-arquitetura-e-princípios-utilizados)
- [📦 Organização dos módulos](#-organização-dos-módulos)
- [❓ FAQ](#-faq)
- [🚧 Melhorias futuras](#-melhorias-futuras)
- [🤝 Contribuição](#-contribuição)
- [📄 Licença](#-licença)
- [👨‍💻 Autor](#-autor)

---

# 📖 Sobre o projeto

O **Robô Cartesiano** é um simulador de movimentação bidimensional que representa um robô deslocando-se em um plano cartesiano limitado.

A aplicação recebe:

- os limites da área de movimentação;
- a posição inicial do robô;
- o deslocamento padrão;
- uma sequência de comandos.

Após o processamento, o sistema executa os movimentos válidos e gera um relatório contendo todas as informações da simulação.

O projeto utiliza uma arquitetura modular onde cada componente possui uma responsabilidade específica, facilitando manutenção, testes e futuras evoluções.

---

# ✨ Funcionalidades

O sistema possui as seguintes funcionalidades:

## 🗺️ Plano cartesiano

Permite configurar:

- limite mínimo do eixo X;
- limite máximo do eixo X;
- limite mínimo do eixo Y;
- limite máximo do eixo Y.

Validações realizadas:

- coordenadas obrigatoriamente inteiras;
- valores positivos ou negativos permitidos;
- coordenada máxima obrigatoriamente maior que a mínima.

---

## 🤖 Controle do robô

O robô possui:

- posição inicial configurável;
- posição atual durante a execução;
- deslocamento configurável;
- histórico completo dos movimentos realizados.

---

## 🎮 Movimentação

São aceitos 8 comandos direcionais:

| Comando | Direção |
|---|---|
| N | Norte |
| S | Sul |
| L | Leste |
| O | Oeste |
| NE | Nordeste |
| NO | Noroeste |
| SE | Sudeste |
| SO | Sudoeste |

Características:

- comandos podem ser informados em letras maiúsculas ou minúsculas;
- caracteres inválidos são ignorados;
- movimentos possuem deslocamento configurável;
- cada movimento válido é registrado.

---

## 🚧 Controle de limites

Quando o robô tenta ultrapassar os limites do plano:

- o movimento não é executado;
- uma colisão é registrada;
- a ocorrência é armazenada no histórico.

---

## 📊 Relatórios

Ao final da execução são apresentados:

- posição inicial;
- posição final;
- quantidade de movimentos válidos;
- sequência de movimentos executados;
- quantidade de colisões;
- histórico detalhado da movimentação.

---

# 📂 Estrutura do projeto

A organização do projeto foi planejada para separar claramente as responsabilidades de cada módulo, facilitando a manutenção, reutilização e evolução da aplicação.

```text
Robo_Cartesiano/
│
├── robo.py
├── robo_input.ini
├── robo_output.txt
│
├── README.md
├── ARQUITETURA.md
├── LICENSE
│
└── roboLibrary/
    │
    ├── __init__.py
    ├── configuracoes.py
    ├── constantes.py
    ├── enumeradores.py
    ├── excecoes.py
    ├── modelos.py
    ├── funcoesArquivo.py
    ├── funcoesMovimento.py
    ├── funcoesRelatorio.py
    └── funcoesValidacao.py
```

## Descrição dos arquivos

| Arquivo | Descrição |
|----------|-----------|
| `robo.py` | Programa principal da aplicação. |
| `robo_input.ini` | Arquivo de configuração da simulação. |
| `robo_output.txt` | Relatório gerado ao final da execução. |
| `ARQUITETURA.md` | Documentação técnica da arquitetura do projeto. |
| `README.md` | Documentação principal do repositório. |
| `LICENSE` | Licença MIT do projeto. |

## Biblioteca `roboLibrary`

| Arquivo | Responsabilidade |
|----------|------------------|
| `configuracoes.py` | Configurações gerais da aplicação. |
| `constantes.py` | Constantes utilizadas pelo sistema. |
| `enumeradores.py` | Enumerações de movimentos e estados. |
| `excecoes.py` | Exceções personalizadas da aplicação. |
| `modelos.py` | Modelos de domínio utilizando `@dataclass`. |
| `funcoesArquivo.py` | Leitura da configuração e gravação do relatório. |
| `funcoesMovimento.py` | Processamento da movimentação do robô. |
| `funcoesRelatorio.py` | Geração do relatório textual da execução. |
| `funcoesValidacao.py` | Validação das entradas e regras de negócio. |

---

# ⚙️ Requisitos

Para executar o projeto é necessário possuir:

- Python **3.10** ou superior;
- Sistema operacional:
  - Windows;
  - Linux;
  - macOS.

O projeto utiliza apenas bibliotecas da biblioteca padrão (Standard Library) do Python, não sendo necessária a instalação de dependências externas.

## Bibliotecas utilizadas

- `configparser`
- `dataclasses`
- `enum`
- `pathlib`
- `typing`

---

# 🚀 Como executar

## 1. Clone o repositório

```bash
git clone https://github.com/CharlesFreitas-DEV/Python.git
```

## 2. Acesse o diretório do projeto

```bash
cd Robo_Cartesiano
```

## 3. Configure o arquivo `robo_input.ini`

Exemplo:

```ini
[PLANO]

X_MINIMO=-10
X_MAXIMO=10

Y_MINIMO=-10
Y_MAXIMO=10


[ROBO]

POSICAO_X=0
POSICAO_Y=0

PASSO=1


[MOVIMENTO]

SEQUENCIA=NNELOSOxxNSE123SO
```

Onde:

| Parâmetro | Descrição |
|-----------|-----------|
| `X_MINIMO` | Limite inferior do eixo X. |
| `X_MAXIMO` | Limite superior do eixo X. |
| `Y_MINIMO` | Limite inferior do eixo Y. |
| `Y_MAXIMO` | Limite superior do eixo Y. |
| `POSICAO_X` | Coordenada inicial X do robô. |
| `POSICAO_Y` | Coordenada inicial Y do robô. |
| `PASSO` | Valor do deslocamento para cada movimento válido. |
| `SEQUENCIA` | Sequência de comandos de movimentação. |

---

## 4. Execute o programa

```bash
python robo.py
```

---

## 5. Resultado

Ao término da execução será gerado automaticamente o arquivo:

```text
robo_output.txt
```

Esse arquivo conterá todas as informações da simulação, incluindo configuração utilizada, estatísticas e histórico completo dos movimentos.

---

# 🔄 Fluxo de execução

A execução da aplicação segue um fluxo simples e organizado, onde cada módulo possui uma responsabilidade específica.

```text
                robo_input.ini
                       │
                       ▼
          Leitura da configuração
                       │
                       ▼
        Validação dos parâmetros
                       │
                       ▼
      Criação dos objetos do domínio
                       │
                       ▼
      Processamento dos movimentos
                       │
                       ▼
      Geração das estatísticas
                       │
                       ▼
        Geração do relatório
                       │
                       ▼
             robo_output.txt
```

Durante esse fluxo são realizadas:

- leitura do arquivo de configuração;
- validação dos parâmetros informados;
- criação dos objetos da aplicação;
- execução dos movimentos;
- controle de colisões com os limites;
- geração das estatísticas;
- criação do relatório final.

---

# 🧪 Exemplo de entrada e saída

## Arquivo de entrada

Exemplo do arquivo `robo_input.ini`:

```ini
[PLANO]

X_MINIMO=-5
X_MAXIMO=5

Y_MINIMO=-5
Y_MAXIMO=5


[ROBO]

POSICAO_X=0
POSICAO_Y=0

PASSO=1


[MOVIMENTO]

SEQUENCIA=NNEELLSOXYZnnso
```

Neste exemplo:

- os caracteres `X`, `Y` e `Z` serão ignorados;
- os comandos `nnso` serão convertidos automaticamente para maiúsculas;
- apenas movimentos válidos serão executados.

---

## Arquivo de saída

Ao término da execução será criado o arquivo `robo_output.txt`.

Exemplo simplificado:

```text
==================================================
          SIMULAÇÃO DO ROBÔ CARTESIANO
==================================================

CONFIGURAÇÃO

Plano:
X: -5 até 5
Y: -5 até 5

Posição inicial:
(0,0)

Passo:
1

--------------------------------------------------

RESULTADO

Posição final:
(2,3)

Movimentos válidos:
12

Movimentos inválidos:
3

Colisões:
1

--------------------------------------------------

HISTÓRICO

N  -> (0,1)
N  -> (0,2)
E  -> (1,2)
E  -> (2,2)
N  -> (2,3)
...
```

Os valores apresentados dependerão da configuração utilizada e da sequência de movimentos informada.

---

# 🧠 Explicação técnica

O projeto foi desenvolvido utilizando uma arquitetura baseada em objetos de domínio, separando claramente regras de negócio, infraestrutura e apresentação.

## Objetos principais

### Plano

Representa a área cartesiana onde o robô poderá se movimentar.

Responsabilidades:

- armazenar os limites do plano;
- representar a área válida da simulação.

---

### Robo

Representa o robô durante toda a execução.

Responsabilidades:

- armazenar a posição inicial;
- armazenar a posição atual;
- armazenar o valor do deslocamento.

---

### Configuracao

Agrupa todos os parâmetros necessários para executar a simulação.

Contém:

- plano cartesiano;
- robô;
- sequência de movimentos.

---

### ResultadoExecucao

Representa o resultado completo da simulação.

Contém:

- configuração utilizada;
- posição final;
- histórico da execução;
- estatísticas.

---

## Regras de movimentação

O sistema aceita oito direções de movimentação.

| Comando | Direção |
|----------|----------|
| N | Norte |
| S | Sul |
| L | Leste |
| O | Oeste |
| NE | Nordeste |
| NO | Noroeste |
| SE | Sudeste |
| SO | Sudoeste |

Características:

- letras maiúsculas e minúsculas são aceitas;
- caracteres inválidos são ignorados;
- cada movimento utiliza o valor definido em `PASSO`;
- o robô nunca ultrapassa os limites do plano.

---

## Validações implementadas

Antes da execução são verificadas diversas regras de consistência.

Entre elas:

- existência do arquivo de configuração;
- existência das seções obrigatórias;
- existência de todos os parâmetros;
- conversão correta para números inteiros;
- validação dos limites do plano;
- validação do deslocamento;
- normalização da sequência de movimentos;
- validação da posição inicial do robô.

Caso qualquer inconsistência seja encontrada, uma exceção personalizada é lançada contendo uma mensagem descritiva do problema encontrado.

---

# 🏗️ Arquitetura e princípios utilizados

O projeto foi desenvolvido seguindo princípios modernos de engenharia de software, priorizando organização, reutilização de código e facilidade de manutenção.

## Arquitetura geral

```text
                         robo.py
                            │
                            ▼
                 Leitura da configuração
                  (funcoesArquivo.py)
                            │
                            ▼
                 Objetos do domínio
                     (modelos.py)
                            │
                            ▼
                Validação dos dados
                (funcoesValidacao.py)
                            │
                            ▼
            Processamento dos movimentos
               (funcoesMovimento.py)
                            │
                            ▼
              Resultado da execução
                            │
                            ▼
              Geração do relatório
              (funcoesRelatorio.py)
                            │
                            ▼
                   robo_output.txt
```

Essa organização permite que cada módulo execute apenas uma responsabilidade específica, tornando o código mais organizado e de fácil manutenção.

---

## Princípios utilizados

Durante o desenvolvimento foram adotados os seguintes princípios:

### Responsabilidade Única (SRP)

Cada módulo possui apenas uma responsabilidade bem definida.

Exemplos:

- `funcoesArquivo.py` → leitura e gravação de arquivos;
- `funcoesMovimento.py` → execução da movimentação;
- `funcoesRelatorio.py` → geração do relatório;
- `funcoesValidacao.py` → validação dos dados.

---

### Baixo acoplamento

Os módulos possuem poucas dependências entre si.

Isso facilita:

- manutenção;
- reutilização;
- testes;
- evolução da aplicação.

---

### Alta coesão

Cada módulo reúne funções relacionadas ao mesmo assunto, evitando mistura de responsabilidades.

---

### Programação Orientada a Objetos

O domínio foi modelado utilizando classes e `@dataclass`, permitindo representar os elementos da simulação de forma clara.

---

### Encapsulamento

As funções auxiliares dos módulos utilizam o prefixo `_`, indicando que são de uso interno.

As funções públicas representam apenas os serviços oferecidos por cada módulo.

---

### Separação entre domínio e infraestrutura

Os objetos de domínio não conhecem:

- arquivos;
- relatórios;
- interface de execução.

Da mesma forma, os módulos responsáveis pela infraestrutura não implementam regras de negócio.

---

# 📦 Organização dos módulos

A biblioteca `roboLibrary` concentra toda a implementação da aplicação.

| Módulo | Responsabilidade |
|---------|------------------|
| `configuracoes.py` | Configurações gerais do projeto. |
| `constantes.py` | Constantes utilizadas pela aplicação. |
| `enumeradores.py` | Enumerações de movimentos e estados. |
| `excecoes.py` | Exceções personalizadas. |
| `modelos.py` | Classes do domínio utilizando `@dataclass`. |
| `funcoesArquivo.py` | Leitura da configuração e gravação do relatório. |
| `funcoesValidacao.py` | Validação dos dados recebidos. |
| `funcoesMovimento.py` | Processamento da movimentação do robô. |
| `funcoesRelatorio.py` | Construção do relatório textual. |

---

## Fluxo entre os módulos

```text
                robo.py
                   │
                   ▼
        funcoesArquivo.py
                   │
                   ▼
             Configuracao
                   │
                   ▼
      funcoesMovimento.py
                   │
                   ▼
       ResultadoExecucao
                   │
                   ▼
      funcoesRelatorio.py
                   │
                   ▼
          robo_output.txt
```

Essa arquitetura facilita futuras evoluções da aplicação, como interfaces gráficas, APIs ou integração com banco de dados, sem necessidade de alterar a lógica principal da simulação.

---

# ❓ FAQ

## O robô aceita letras minúsculas?

Sim.

Todos os comandos são normalizados para letras maiúsculas antes do processamento.

---

## Caracteres inválidos provocam erro?

Não.

Qualquer caractere que não represente um movimento válido é simplesmente ignorado durante a execução.

---

## O robô pode sair dos limites do plano?

Não.

Sempre que um movimento resultar em uma posição fora da área configurada, ele é cancelado e uma colisão é registrada.

---

## Posso utilizar coordenadas negativas?

Sim.

Os limites do plano e a posição inicial do robô podem possuir valores positivos ou negativos.

---

## O valor do deslocamento é fixo?

Não.

O deslocamento é definido pelo parâmetro `PASSO` presente no arquivo `robo_input.ini`.

---

## Existe limite para a quantidade de movimentos?

Não existe um limite definido pela aplicação.

A quantidade de movimentos dependerá apenas do tamanho da sequência informada no arquivo de configuração.

---

# 🚧 Melhorias futuras

O projeto foi planejado para permitir evolução incremental. Algumas funcionalidades previstas para versões futuras são apresentadas a seguir.

## Versão 2

### Interface gráfica

- Visualização do plano cartesiano;
- Representação gráfica do robô;
- Exibição da trajetória percorrida;
- Execução passo a passo;
- Controle da velocidade da animação.

### Novos formatos de saída

- Relatório em JSON;
- Relatório em HTML;
- Relatório em PDF;
- Exportação para CSV.

### Estatísticas avançadas

- Distância total percorrida;
- Quantidade de movimentos por direção;
- Percentual de movimentos válidos;
- Percentual de colisões;
- Maior distância em relação à origem;
- Quadrantes mais visitados.

### Configuração

- Múltiplos cenários no mesmo arquivo;
- Arquivos de configuração em JSON;
- Arquivos de configuração em YAML.

---

## Versão 3

### Novas funcionalidades

- Obstáculos no plano cartesiano;
- Diferentes tipos de terreno;
- Múltiplos robôs na mesma simulação;
- Execução concorrente de robôs.

### Interface

- Interface gráfica completa;
- Visualização em tempo real;
- Zoom;
- Controle por teclado;
- Reprodução da simulação.

### Persistência

- Banco de dados SQLite;
- Histórico de simulações;
- Estatísticas acumuladas;
- Reexecução de cenários anteriores.

---

# 🤝 Contribuição

Contribuições são bem-vindas.

Caso deseje colaborar com o projeto:

1. Faça um **Fork** deste repositório;
2. Crie uma nova branch para sua funcionalidade;

```bash
git checkout -b minha-feature
```

3. Realize as alterações desejadas;
4. Execute os testes do projeto;
5. Faça o commit das alterações;

```bash
git commit -m "Adiciona nova funcionalidade"
```

6. Envie para o seu repositório;

```bash
git push origin minha-feature
```

7. Abra um **Pull Request**.

---

# 📄 Licença

Repositório desenvolvido para fins educacionais em Python.

Este projeto está licenciado sob a licença **MIT**.

Consulte o arquivo `LICENSE` para mais detalhes.

---

# 👨‍💻 Autor

**Charles Cesar Magno de Freitas**

Professor • Analista de Sistemas • Desenvolvedor Back-end

- 🎓 Professor de Programação
- 🐍 Entusiasta da linguagem Python
- 🧩 Desenvolvedor de projetos educacionais
- 💻 GitHub: https://github.com/CharlesFreitas-DEV

---

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório para apoiar o desenvolvimento e incentivar a criação de novos projetos educacionais.