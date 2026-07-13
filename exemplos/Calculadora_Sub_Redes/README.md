# 🌐 Calculadora de Sub-redes IPv4

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Algorithm](https://img.shields.io/badge/algorithm-Bitwise%20Operations-orange)
![Network](https://img.shields.io/badge/network-IPv4-green)
![Format](https://img.shields.io/badge/input%2Foutput-INI%20%7C%20JSON-purple)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Architecture](https://img.shields.io/badge/architecture-modular-purple)
![Paradigm](https://img.shields.io/badge/paradigm-Structured%20%7C%20OOP-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)
![Open Source](https://img.shields.io/badge/open%20source-yes-brightgreen)

---

## 📌 Índice

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

A **Calculadora de Sub-redes IPv4** é um projeto desenvolvido em Python que implementa o cálculo automático de informações de redes IPv4 utilizando **operações bitwise**.

O programa recebe:

- Um endereço IPv4;
- Uma máscara de rede inicial no formato CIDR;
- Uma máscara de rede final no formato CIDR;

e calcula todas as sub-redes pertencentes ao intervalo informado.

Para cada máscara de rede são geradas as seguintes informações:

- Endereço de Rede;
- Primeiro Host válido;
- Último Host válido;
- Endereço de Broadcast;
- Máscara de Sub-rede em formato decimal;
- Máscara de Sub-rede em formato binário;
- Número de Hosts válidos.

O projeto possui finalidade **didática**, sendo indicado para o estudo de:

- Redes de computadores;
- Endereçamento IPv4;
- Subnetting;
- Representação binária;
- Operações bitwise;
- Algoritmos;
- Estruturas de dados;
- Modularização em Python;
- Manipulação de arquivos;
- Organização de projetos Python.

---

A implementação foi estruturada utilizando princípios de engenharia de software, separando as responsabilidades da aplicação em módulos independentes:

- Configuração da aplicação;
- Leitura dos dados de entrada;
- Validação dos dados;
- Cálculos de endereçamento IPv4;
- Manipulação de arquivos;
- Geração dos resultados.

A arquitetura foi construída seguindo os princípios:

- **Responsabilidade Única (SRP - Single Responsibility Principle);**
- **Separação de Responsabilidades (SoC - Separation of Concerns);**
- **Encapsulamento;**
- **DRY (Don't Repeat Yourself);**
- **Modularização;**
- **Baixo acoplamento entre componentes.**

---

# ✨ Funcionalidades

- Leitura das configurações através do arquivo `config.ini`;
- Leitura dos dados de entrada através do arquivo `info_rede.ini`;
- Validação de endereço IPv4;
- Validação dos octetos;
- Validação das máscaras CIDR;
- Validação do intervalo de máscaras;
- Cálculo do endereço de rede;
- Cálculo do endereço de broadcast;
- Cálculo do primeiro host válido;
- Cálculo do último host válido;
- Cálculo da quantidade de hosts válidos;
- Conversão de IPv4 decimal para inteiro;
- Conversão de inteiro para IPv4 decimal;
- Geração de máscaras utilizando operações de bits;
- Conversão de máscaras para representação binária;
- Utilização de operações bitwise:
  - AND (`&`);
  - OR (`|`);
  - NOT (`~`);
  - Deslocamento de bits (`<<`);
- Não utiliza a biblioteca `ipaddress`;
- Exportação dos resultados para arquivo JSON;
- Criação automática do diretório de resultados;
- Tratamento de exceções personalizadas;
- Código modular e documentado;
- Utilização de `dataclass` para representação dos dados;
- Organização seguindo boas práticas de desenvolvimento Python.

---

# 📂 Estrutura do projeto

```text
Calculo_SubRede/
│
├── resultados/
│   └── subredes_YYYYMMDD_HHMMSS.json
|
├── src/
│   │
│   ├── __init__.py
│   ├── configuracoes.py
│   ├── excecoes.py
│   ├── funcoesArquivo.py
│   ├── funcoesIP.py
│   ├── funcoesValidacao.py
│   └── modelos.py
│
├── calculadoraSubRede.py
├── config.ini
├── info_rede.ini
├── LICENSE
└── README.md

# ⚙️ Requisitos

- Python 3.10 ou superior.

O projeto não utiliza bibliotecas externas.

São utilizadas apenas bibliotecas nativas do Python:

```python
from pathlib import Path
from dataclasses import dataclass
import configparser
import json
```

---

# 🚀 Como executar

Os arquivos de configuração devem estar no diretório raiz do projeto.

Estrutura esperada:

```text
Calculo_SubRede/

├── calculadoraSubRede.py
├── config.ini
├── info_rede.ini
|
├── src/
│   │
│   ├── __init__.py
│   ├── configuracoes.py
│   ├── excecoes.py
│   ├── funcoeasArquivo.py
│   ├── display_functions.py
│   └── sudoku_functions.py
|
├── LICENSE
│
└── README.md

```

Execute:

```bash
python calculadoraSubRede.py
```

O programa realizará:

1. Leitura do arquivo de configurações:

```text
config.ini
```

2. Leitura dos dados de entrada:

```text
info_rede.ini
```

3. Validação das informações fornecidas.

4. Cálculo das sub-redes utilizando operações bitwise.

5. Geração do arquivo JSON.

O resultado será salvo automaticamente no diretório:

```text
resultados/
```

---

# 🔄 Fluxo de execução

O fluxo completo da aplicação ocorre da seguinte forma:

```text
info_rede.ini
        |
        v
configuracoes.py
        |
        v
InformacoesRede
        |
        v
funcoesValidacao.py
        |
        v
funcoesIP.py
        |
        v
SubRede
        |
        v
funcoesArquivo.py
        |
        v
arquivo JSON
```

---

## Etapas do processamento

1. O programa principal inicia a aplicação.

2. O módulo `configuracoes.py` realiza a leitura dos arquivos:

```text
config.ini
info_rede.ini
```

3. Os dados de entrada são armazenados utilizando:

```python
@dataclass
class InformacoesRede
```

4. São realizadas validações:

- Estrutura do endereço IPv4;
- Quantidade de octetos;
- Valores numéricos dos octetos;
- Faixa válida dos octetos;
- Máscara CIDR;
- Intervalo entre máscaras.

5. Para cada máscara do intervalo informado:

- O endereço IPv4 é convertido para inteiro;
- A máscara CIDR é convertida para inteiro;
- São aplicadas operações bitwise;
- São calculadas as informações da sub-rede.

6. Os resultados são armazenados utilizando:

```python
@dataclass
class SubRede
```

7. O arquivo JSON é gerado no diretório:

```text
resultados/
```

---

# 🧪 Exemplo de entrada e saída

## Arquivo de configuração

`info_rede.ini`

```ini
[REDE]

ENDERECO_IP = 192.168.10.35

MASCARA_INICIAL = 24

MASCARA_FINAL = 26
```

---

## Resultado esperado

Para o endereço:

```text
192.168.10.35
```

e intervalo:

```text
/24 até /26
```

serão geradas:

```text
/24
/25
/26
```

---

## Saída JSON

Exemplo:

```json
{
    "data_hora": "2026-07-09T18:54:26.287769",
    "informacoes_rede": {
        "strEnderecoIP": "192.168.10.35",
        "intMascaraInicial": 24,
        "intMascaraFinal": 26
    },
    "subredes": [
        {
            "intCIDR": 24,
            "strEnderecoRede": "192.168.10.0",
            "strPrimeiroHost": "192.168.10.1",
            "strUltimoHost": "192.168.10.254",
            "strBroadcast": "192.168.10.255",
            "strMascaraDecimal": "255.255.255.0",
            "strMascaraBinaria": "11111111.11111111.11111111.00000000",
            "intHostsValidos": 254
        },
        {
            "intCIDR": 25,
            "strEnderecoRede": "192.168.10.0",
            "strPrimeiroHost": "192.168.10.1",
            "strUltimoHost": "192.168.10.126",
            "strBroadcast": "192.168.10.127",
            "strMascaraDecimal": "255.255.255.128",
            "strMascaraBinaria": "11111111.11111111.11111111.10000000",
            "intHostsValidos": 126
        },
        {
            "intCIDR": 26,
            "strEnderecoRede": "192.168.10.0",
            "strPrimeiroHost": "192.168.10.1",
            "strUltimoHost": "192.168.10.62",
            "strBroadcast": "192.168.10.63",
            "strMascaraDecimal": "255.255.255.192",
            "strMascaraBinaria": "11111111.11111111.11111111.11000000",
            "intHostsValidos": 62
        }
    ]
}
```

---

# 🧠 Explicação técnica

## 📁 Bibliotecas utilizadas

Principais bibliotecas utilizadas:

```python
from pathlib import Path
from dataclasses import dataclass
import configparser
import json
```

---

# 📂 pathlib

Responsável pelo gerenciamento dos caminhos dos arquivos.

Principais recursos utilizados:

- Localização da raiz do projeto;
- Construção dos caminhos dos arquivos;
- Criação do diretório de resultados;
- Compatibilidade entre sistemas operacionais.

---

# 📄 configparser

Utilizado para leitura dos arquivos:

```text
config.ini
info_rede.ini
```

Permite separar:

- Configurações da aplicação;
- Dados fornecidos pelo usuário.

---

# 🧩 dataclass

O projeto utiliza `dataclass` para representar os dados da aplicação.

Modelo utilizado para entrada:

```python
@dataclass
class InformacoesRede
```

Responsável por armazenar:

- Endereço IPv4;
- Máscara inicial;
- Máscara final.

Modelo utilizado para saída:

```python
@dataclass
class SubRede
```

Responsável por armazenar:

- CIDR;
- Endereço de rede;
- Primeiro host;
- Último host;
- Broadcast;
- Máscara decimal;
- Máscara binária;
- Quantidade de hosts.

---

# 🧮 Operações Bitwise

Todos os cálculos IPv4 são realizados sem utilização da biblioteca:

```python
ipaddress
```

A implementação utiliza manipulação direta de bits.

---

## Conversão IPv4 para inteiro

Um endereço IPv4 possui 32 bits:

```text
192.168.10.35

11000000.10101000.00001010.00100011
```

Cada octeto ocupa 8 bits.

A conversão é realizada utilizando deslocamento:

```python
<<
```

---

## Cálculo do endereço de rede

A operação utilizada é:

```python
enderecoRede = enderecoIP & mascara
```

O operador:

```text
&
```

mantém apenas os bits pertencentes à rede.

---

## Cálculo do endereço de broadcast

A operação utilizada é:

```python
broadcast = rede | (~mascara & 0xFFFFFFFF)
```

O operador:

```text
|
```

define todos os bits do host como:

```text
1
```

---

## Quantidade de hosts válidos

Calculada através de:

```text
2^(bits de host) - 2
```

Implementada utilizando:

```python
1 << bitsHost
```

# 🏗️ Arquitetura e princípios utilizados

O projeto foi desenvolvido utilizando princípios de engenharia de software com o objetivo de manter o código organizado, reutilizável, testável e de fácil manutenção.

A arquitetura adotada busca reduzir o acoplamento entre os módulos e aumentar a separação das responsabilidades.

---

# 📐 Princípios aplicados

## Responsabilidade Única (SRP - Single Responsibility Principle)

Cada módulo da aplicação possui uma responsabilidade específica.

Essa abordagem evita que um único arquivo concentre diferentes regras de negócio.

Exemplo:

| Módulo | Responsabilidade |
|---|---|
| `calculadoraSubRede.py` | Execução principal da aplicação |
| `configuracoes.py` | Leitura e gerenciamento das configurações |
| `funcoesValidacao.py` | Validação dos dados de entrada |
| `funcoesIP.py` | Cálculos relacionados ao protocolo IPv4 |
| `funcoesArquivo.py` | Manipulação de arquivos |
| `modelos.py` | Definição das estruturas de dados |
| `excecoes.py` | Exceções personalizadas |

---

## Separação de Responsabilidades (SoC - Separation of Concerns)

A aplicação foi dividida em módulos independentes, onde cada componente possui uma finalidade específica.

Benefícios:

- Código mais organizado;
- Facilidade de manutenção;
- Maior reutilização;
- Testes mais simples;
- Menor acoplamento entre componentes.

---

## Encapsulamento

Funções utilizadas internamente pelos módulos são encapsuladas seguindo a convenção:

```python
_nomeFuncao()
```

Esse padrão indica que a função possui uso privado dentro do próprio módulo.

Exemplo:

```python
_converterIPParaInteiro()

_gerarMascaraInteiro()

_calcularEnderecoRede()
```

---

## DRY (Don't Repeat Yourself)

O projeto evita duplicação de código.

Regras comuns foram centralizadas em funções específicas.

Exemplos:

- Conversão IPv4;
- Geração de máscaras;
- Validações;
- Manipulação de arquivos.

---

## Programação Orientada a Objetos

Apesar da aplicação utilizar principalmente funções, foram utilizados conceitos de orientação a objetos através de:

```python
@dataclass
```

As estruturas de dados são representadas como objetos, facilitando:

- Organização dos dados;
- Legibilidade;
- Manutenção;
- Expansão futura.

---

# 📦 Organização dos módulos

## `calculadoraSubRede.py`

Arquivo principal da aplicação.

Responsável por:

- Inicializar o programa;
- Carregar configurações;
- Executar validações;
- Coordenar os cálculos;
- Solicitar geração do arquivo JSON.

---

## `configuracoes.py`

Responsável pela leitura dos arquivos:

```text
config.ini
info_rede.ini
```

Centraliza as configurações utilizadas pela aplicação.

Responsabilidades:

- Localizar arquivos;
- Ler parâmetros;
- Criar objetos de configuração;
- Disponibilizar informações para os demais módulos.

---

## `funcoesIP.py`

Responsável pelos cálculos IPv4.

Principais funcionalidades:

- Conversão IPv4 ↔ inteiro;
- Geração de máscaras;
- Cálculo de endereço de rede;
- Cálculo de broadcast;
- Cálculo de hosts válidos;
- Geração das informações das sub-redes.

Principal função pública:

```python
gerarInformacoesSubRede()
```

Responsável por gerar as informações completas de uma sub-rede.

---

Funções internas:

```python
_converterIPParaInteiro()

_converterInteiroParaIP()

_gerarMascaraInteiro()

_converterMascaraParaBinario()

_calcularEnderecoRede()

_calcularBroadcast()

_calcularHostsValidos()
```

---

## `funcoesValidacao.py`

Responsável pelas validações da aplicação.

Realiza:

- Validação do endereço IPv4;
- Validação dos octetos;
- Validação dos valores permitidos;
- Validação das máscaras CIDR;
- Validação do intervalo de máscaras.

Em caso de erro:

- Uma exceção é lançada;
- O fluxo normal da aplicação é interrompido.

---

## `funcoesArquivo.py`

Responsável pela manipulação dos arquivos.

Realiza:

- Criação do diretório:

```text
resultados/
```

- Geração dos arquivos JSON;
- Controle da codificação;
- Tratamento de erros de gravação.

---

## `modelos.py`

Define as estruturas utilizadas na aplicação.

Modelo de entrada:

```python
@dataclass
class InformacoesRede
```

Armazena:

- Endereço IPv4;
- Máscara inicial;
- Máscara final.

---

Modelo de saída:

```python
@dataclass
class SubRede
```

Armazena:

- CIDR;
- Endereço de rede;
- Primeiro host;
- Último host;
- Broadcast;
- Máscara decimal;
- Máscara binária;
- Hosts válidos.

---

## `excecoes.py`

Centraliza as exceções personalizadas.

Exemplos:

```python
ConfiguracaoError

ValidacaoError

ArquivoResultadoError
```

O uso de exceções específicas facilita identificar problemas durante a execução.

---

# ❓ FAQ

## ❓ O projeto utiliza a biblioteca `ipaddress`?

Não.

Todos os cálculos foram implementados manualmente utilizando operações bitwise.

O objetivo é demonstrar o funcionamento interno do endereçamento IPv4 através da manipulação direta dos bits.

---

## ❓ Por que utilizar operações bitwise?

Porque o protocolo IPv4 trabalha com representação binária.

As operações bitwise permitem compreender diretamente:

- Bits de rede;
- Bits de host;
- Máscaras;
- Broadcast;
- Subdivisão de redes.

---

## ❓ O projeto utiliza bibliotecas externas?

Não.

Toda a implementação utiliza apenas bibliotecas nativas do Python.

---

## ❓ Posso alterar o endereço IP calculado?

Sim.

Basta alterar o arquivo:

```text
info_rede.ini
```

Exemplo:

```ini
ENDERECO_IP = 192.168.10.35

MASCARA_INICIAL = 24

MASCARA_FINAL = 30
```

---

## ❓ Onde ficam os resultados?

Os arquivos gerados são armazenados automaticamente no diretório:

```text
resultados/
```

Cada execução gera um novo arquivo JSON.

---

## ❓ Posso utilizar esse projeto em disciplinas?

Sim.

O projeto possui finalidade educacional e pode ser utilizado para demonstrar:

- Redes de computadores;
- IPv4;
- Representação binária;
- Operações bitwise;
- Algoritmos;
- Estruturas de dados;
- Modularização;
- Organização de projetos Python.

---

# 🚧 Melhorias futuras

- Implementação de testes automatizados utilizando `pytest`;
- Criação de testes unitários para cada módulo;
- Validação completa dos arquivos de configuração;
- Exportação dos resultados para CSV;
- Exportação dos resultados para PDF;
- Interface gráfica;
- Interface Web;
- API REST;
- Suporte ao protocolo IPv6;
- Comparação entre diferentes redes;
- Visualização gráfica das sub-redes;
- Implementação de relatórios estatísticos;
- Empacotamento como biblioteca Python.

---

# 🤝 Contribuição

Contribuições são bem-vindas.

Para contribuir:

1. Faça um Fork do projeto.

2. Crie uma nova branch:

```bash
git checkout -b feature/nova-funcionalidade
```

3. Desenvolva sua alteração.

4. Realize seus commits:

```bash
git commit -m "Adiciona nova funcionalidade"
```

5. Envie sua branch:

```bash
git push origin feature/nova-funcionalidade
```

6. Abra um Pull Request.

---

# 📄 Licença

Repositório desenvolvido para fins educacionais em Python, com foco no estudo de:

- Redes de computadores;
- Endereçamento IPv4;
- Subnetting;
- Operações bitwise;
- Algoritmos;
- Estruturas de dados;
- Programação modular;
- Organização de projetos Python.

Este projeto está licenciado sob a licença MIT.

Consulte o arquivo `LICENSE` para mais detalhes.

---

# 👨‍💻 Autor

**Charles Cesar Magno de Freitas**

**Contato:** <freitascharles.dev@gmail.com>