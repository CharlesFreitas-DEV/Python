# 🖼️ EXIF Metadata Reader

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![EXIF](https://img.shields.io/badge/metadata-EXIF-orange)
![Format](https://img.shields.io/badge/format-JPEG-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
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
- [🧪 Exemplo de saída](#-exemplo-de-saída)
- [🧠 Explicação técnica](#-explicação-técnica)
- [❓ FAQ](#-faq)
- [🚧 Melhorias futuras](#-melhorias-futuras)
- [🤝 Contribuição](#-contribuição)
- [📄 Licença](#-licença)
- [👨‍💻 Autor](#-autor)

---

## 📖 Sobre o projeto

O **EXIF Metadata Reader** é um exemplo desenvolvido em Python que demonstra como realizar a leitura manual dos metadados **EXIF** armazenados em arquivos **JPEG**, sem utilizar bibliotecas especializadas como Pillow, ExifRead ou similares.

Todo o processamento é realizado diretamente sobre os bytes do arquivo, permitindo compreender como o padrão EXIF está organizado internamente e como interpretar sua estrutura utilizando apenas recursos da biblioteca padrão do Python.

Este projeto possui finalidade **didática**, sendo indicado para o estudo de manipulação de arquivos binários, formatos de imagem, programação de baixo nível e perícia computacional.

---

## ✨ Funcionalidades

- Leitura de arquivos JPEG em modo binário
- Validação da assinatura do arquivo JPEG
- Verificação da existência do bloco EXIF
- Leitura do cabeçalho TIFF
- Identificação automática de Little Endian e Big Endian
- Leitura da IFD Principal (Image File Directory)
- Interpretação dos formatos de dados EXIF
- Leitura de valores ASCII
- Leitura de valores do tipo RATIONAL
- Leitura do diretório GPS
- Conversão de coordenadas GPS para Graus Decimais
- Exibição organizada dos metadados encontrados
- Utilização exclusiva da biblioteca padrão do Python

---

## 📂 Estrutura do projeto

```text
EXIF_Metadata_Reader/
│
├── images/
│   └── presepio_natalino.jpg
│
├── LICENSE
├── metadataConstants.py
├── metadataFunctions.py
├── README.md
└── readMetadataJPG.py
```

---

## ⚙️ Requisitos

- Python 3.10 ou superior

O projeto **não requer instalação de bibliotecas externas**.

---

## 🚀 Como executar

Coloque uma imagem JPEG na pasta indicada pelo programa e execute:

```bash
python readMetadataJPG.py
```

---

## 🔄 Fluxo de execução

1. Abre o arquivo JPEG em modo binário.
2. Verifica a assinatura do arquivo.
3. Localiza o bloco EXIF.
4. Lê o cabeçalho TIFF.
5. Identifica a ordem dos bytes (Endian).
6. Lê a IFD Principal.
7. Interpreta os metadados encontrados.
8. Localiza a IFD de GPS, caso exista.
9. Converte coordenadas GPS para Graus Decimais.
10. Exibe todas as informações obtidas.

---

## 🧪 Exemplo de saída

```text
Arquivo Lido
------------------------------
...\Python\exemplos\EXIF_Metadata_Reader\images\presepio_natalino.jpg


Dados do Cabeçalho EXIF
------------------------------
exifSize       : 11687
exifMarker     : b'Exif'
temp1          : b'\x00\x00'
tiffHeader     : b'II'
temp2          : b'*\x00'
temp3          : b'\x08\x00\x00\x00'
metaCount      : 13


Metadados Lidos
------------------------------
{'TAGNumber': 'ImageWidth', 'DataFormat': 'Unsigned Long', 'NumberComponents': 1, 'DataValue': 4080}
{'TAGNumber': 'ImageLength', 'DataFormat': 'Unsigned Long', 'NumberComponents': 1, 'DataValue': 3072}
{'TAGNumber': 'Make', 'DataFormat': 'ASCII String', 'NumberComponents': 7, 'DataValue': 'Xiaomi'}
{'TAGNumber': 'YResolution', 'DataFormat': 'ASCII String', 'NumberComponents': 9, 'DataValue': 'M2102K1G'}
{'TAGNumber': 'Orientation', 'DataFormat': 'Unsigned Short', 'NumberComponents': 1, 'DataValue': 1}
{'TAGNumber': 'XResolution', 'DataFormat': 'Unsigned Rational', 'NumberComponents': 1, 'DataValue': 186}
{'TAGNumber': 'Unknown Tag', 'DataFormat': 'Unsigned Rational', 'NumberComponents': 1, 'DataValue': 194}
{'TAGNumber': 'ResolutionUnit', 'DataFormat': 'Unsigned Short', 'NumberComponents': 1, 'DataValue': 2}
{'TAGNumber': 'Software', 'DataFormat': 'ASCII String', 'NumberComponents': 22, 'DataValue': 'HDR+ 1.0.414775603ndy'}
{'TAGNumber': 'DateTime', 'DataFormat': 'ASCII String', 'NumberComponents': 20, 'DataValue': '2022:12:19 20:21:42'}
{'TAGNumber': 'YCbCrPositioning', 'DataFormat': 'Unsigned Short', 'NumberComponents': 1, 'DataValue': 1}
{'TAGNumber': 'ExifOffset', 'DataFormat': 'Unsigned Long', 'NumberComponents': 1, 'DataValue': 244}
{'TAGNumber': 'GPSInfo', 'DataFormat': 'Unsigned Long', 'NumberComponents': 1, 'DataValue': 939}


Metadados de GPS Lidos
------------------------------
{'TAGNumber': 'Latitude', 'DataValue': -5.812361111111111}
{'TAGNumber': 'Ref. Latitude', 'DataValue': 'Sul'}
{'TAGNumber': 'Longitude', 'DataValue': -35.20316666666667}
{'TAGNumber': 'Ref. Longitude', 'DataValue': 'Oeste'}
{'TAGNumber': 'Altitude', 'DataValue': '41.20 metros'}
{'TAGNumber': 'Data e Hora (UTC)', 'DataValue': '2022:12:19 23:21:00 UTC'}
```

---

## 🧠 Explicação técnica

### 📁 Bibliotecas utilizadas

```python
import os
import sys
```

Além da biblioteca:

```python
from typing import List
```

---

### 📂 `os`

Responsável pela manipulação de caminhos de arquivos.

Principais funções utilizadas:

- `os.path.join()`
- `os.path.dirname()`
- `os.path.abspath()`

---

### 🧠 `sys`

Utilizado para encerramento controlado da aplicação.

```python
sys.exit("Mensagem de erro")
```

---

### 📦 `typing`

Utilizado para documentação dos tipos de dados.

```python
List
```

---

### 📸 Estrutura do EXIF

O padrão EXIF utiliza a estrutura TIFF para armazenar seus metadados.

O programa interpreta:

- Cabeçalho TIFF
- IFD Principal
- Diretório GPS

Cada entrada da IFD possui exatamente **12 bytes**, compostos por:

| Campo | Bytes |
|--------|------:|
| TAG | 2 |
| Tipo | 2 |
| Número de Componentes | 4 |
| Valor ou Offset | 4 |

---

### 🔄 Byte Order

O programa identifica automaticamente a ordem dos bytes utilizada pela imagem:

- Little Endian (Intel)
- Big Endian (Motorola)

garantindo a correta interpretação dos valores armazenados.

---

### 🧭 Coordenadas GPS

As coordenadas geográficas armazenadas no EXIF encontram-se no formato:

```text
Graus
Minutos
Segundos
```

O programa converte automaticamente essas informações para:

```text
Graus Decimais
```

facilitando sua utilização em sistemas de mapas e geolocalização.

---

### ⚠️ Tratamento de erros

O programa realiza validações para:

- Arquivo inexistente
- Arquivo que não seja JPEG
- Arquivo sem metadados EXIF
- Estrutura EXIF inválida
- Offsets inválidos
- Dados inconsistentes

---

## ❓ FAQ

### ❓ Utiliza Pillow?

Não.

Todo o processamento é realizado manualmente sobre os bytes do arquivo.

---

### ❓ Funciona com qualquer arquivo JPEG?

Funciona com imagens JPEG que possuam metadados EXIF.

---

### ❓ Posso utilizar em disciplinas de Perícia Computacional?

Sim.

O projeto foi desenvolvido justamente para demonstrar como interpretar metadados diretamente na estrutura binária do arquivo.

---

### ❓ O programa altera a imagem?

Não.

A leitura é realizada apenas em modo binário, sem modificar o arquivo original.

---

## 🚧 Melhorias futuras

- Suporte à leitura de arquivos TIFF
- Suporte à leitura de arquivos HEIC
- Suporte à leitura de arquivos HEIF
- Suporte ao padrão eXIf em arquivos PNG
- Leitura de metadados XMP
- Leitura de metadados IPTC
- Exportação para JSON
- Exportação para CSV
- Interface gráfica
- Escrita e edição de metadados EXIF
- Leitura de Miniaturas (Thumbnail EXIF)
- Interpretação de Maker Notes dos fabricantes

---

## 🤝 Contribuição

Contribuições são bem-vindas.

1. Faça um Fork do projeto.
2. Crie uma Branch (`feature/nova-funcionalidade`).
3. Faça seus Commits.
4. Abra um Pull Request.

---

## 📄 Licença

Repositório desenvolvido para fins educacionais em Python, com foco no estudo de:

- Manipulação de arquivos binários;
- Estrutura interna de arquivos JPEG;
- Padrão de metadados EXIF;
- Cabeçalho TIFF e organização de dados;
- Leitura e interpretação de bytes;
- Offset e ponteiros em estruturas binárias;
- Ordenação de bytes (Little Endian e Big Endian);
- Geolocalização através de metadados GPS;
- Análise de informações digitais para aplicações em perícia computacional.

Este projeto está licenciado sob a licença MIT.

Consulte o arquivo `LICENSE` para mais detalhes.

---

## 👨‍💻 Autor

**Charles Cesar Magno de Freitas**

**Contato:** <freitascharles.dev@gmail.com>

---