# 🧩 Sudoku Solve

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Algorithm](https://img.shields.io/badge/algorithm-Backtracking-orange)
![Format](https://img.shields.io/badge/input%2Foutput-CSV-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Architecture](https://img.shields.io/badge/architecture-modular-purple)
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
- [❓ FAQ](#-faq)
- [🚧 Melhorias futuras](#-melhorias-futuras)
- [🤝 Contribuição](#-contribuição)
- [📄 Licença](#-licença)
- [👨‍💻 Autor](#-autor)

---

## 📖 Sobre o projeto

O **Sudoku Solve** é um projeto desenvolvido em Python que implementa um solucionador automático de Sudoku utilizando o algoritmo de **Backtracking**.

O programa recebe um tabuleiro Sudoku no formato CSV, realiza todas as validações necessárias, aplica o algoritmo de busca recursiva para encontrar uma solução válida e gera um novo arquivo contendo o Sudoku resolvido.

O projeto possui finalidade **didática**, sendo indicado para o estudo de:

- Estruturas de dados matriciais;
- Recursividade;
- Algoritmos de busca;
- Backtracking;
- Modularização em Python;
- Manipulação de arquivos CSV;
- Organização de projetos Python.

A implementação foi estruturada utilizando separação de responsabilidades, dividindo a aplicação em módulos independentes:

- Resolução do Sudoku;
- Manipulação de arquivos;
- Validação de dados;
- Exibição dos resultados.

---

## ✨ Funcionalidades

- Leitura de Sudoku através de arquivo CSV
- Utilização do caractere `;` como separador de valores
- Validação da estrutura da matriz recebida
- Validação dos valores presentes no tabuleiro
- Resolução automática utilizando Backtracking
- Verificação de:
  - Linhas
  - Colunas
  - Blocos 3x3
- Exibição formatada do Sudoku resolvido
- Exportação do resultado para arquivo CSV
- Tratamento de exceções durante leitura e gravação
- Código organizado em módulos reutilizáveis
- Utilização de tipagem nas funções Python

---

## 📂 Estrutura do projeto

```text
Sudoku_Solve/
│
├── sudoku_input.csv
├── sudoku_output.csv
│
├── sudoku_solve.py
│
├── sudoku_library/
│   │
│   ├── __init__.py
│   ├── sudoku_constants.py
│   ├── validation_functions.py
│   ├── file_functions.py
│   ├── display_functions.py
│   └── sudoku_functions.py
│
└── README.md
```

---

## ⚙️ Requisitos

- Python 3.10 ou superior

O projeto não requer instalação de bibliotecas externas.

São utilizadas apenas bibliotecas nativas do Python:

```python
from pathlib import Path
```

---

## 🚀 Como executar

O arquivo de entrada deve estar no mesmo diretório do programa principal.

Execute:

```bash
python sudoku_solve.py
```

O programa realizará:

1. Leitura do arquivo:

```text
sudoku_input.csv
```

2. Resolução do Sudoku.

3. Geração do arquivo:

```text
sudoku_solve.csv
```

---

## 🔄 Fluxo de execução

1. O programa principal inicia a aplicação.
2. O arquivo CSV de entrada é localizado.
3. O tabuleiro Sudoku é carregado para uma matriz.
4. São realizadas validações:
   - Tipo dos dados;
   - Quantidade de linhas;
   - Quantidade de colunas;
   - Valores permitidos.
5. O algoritmo de Backtracking inicia a resolução.
6. Cada posição vazia recebe uma tentativa de valor.
7. Caso a escolha não leve a uma solução:
   - O valor é removido;
   - O algoritmo retorna ao estado anterior;
   - Uma nova tentativa é realizada.
8. Quando todas as posições são preenchidas:
   - O Sudoku está resolvido.
9. O resultado é exibido.
10. O arquivo CSV de saída é gerado.

---

## 🧪 Exemplo de entrada e saída

### Arquivo de entrada

`sudoku_input.csv`

```text
2;0;3;0;1;6;8;0;4
5;0;9;0;0;4;7;0;1
0;4;0;0;0;2;0;6;0
9;5;7;0;0;0;0;0;0
8;0;0;0;0;0;0;0;3
0;0;0;0;0;0;4;5;8
0;8;0;2;0;0;0;3;0
6;0;1;4;0;0;5;0;2
7;0;2;6;5;0;1;0;9
```

---

### Saída exibida

```text
Sudoku resolvido:

2 7 3 | 5 1 6 | 8 9 4
5 6 9 | 3 8 4 | 7 2 1
1 4 8 | 9 7 2 | 3 6 5
---------------------
9 5 7 | 8 4 3 | 2 1 6
8 2 4 | 1 6 5 | 9 7 3
3 1 6 | 7 2 9 | 4 5 8
---------------------
4 8 5 | 2 9 1 | 6 3 7
6 9 1 | 4 3 7 | 5 8 2
7 3 2 | 6 5 8 | 1 4 9

Arquivo gerado com sucesso: sudoku_output.csv
```

---

## 🧠 Explicação técnica

## 📁 Bibliotecas utilizadas

```python
from pathlib import Path
```

---

## 📂 `pathlib`

Responsável pelo gerenciamento dos caminhos dos arquivos.

Principais recursos utilizados:

- Localização do diretório do projeto;
- Construção dos caminhos dos arquivos CSV;
- Manipulação independente do sistema operacional.

---

# 🧩 Algoritmo de Backtracking

O solucionador utiliza uma estratégia de busca por tentativa e erro controlada.

O funcionamento é baseado em quatro etapas:

### 1. Escolha

Uma posição vazia do tabuleiro é selecionada.

---

### 2. Tentativa

São testados valores de:

```text
1 até 9
```

---

### 3. Verificação

Cada valor é analisado considerando:

- Não existir repetição na linha;
- Não existir repetição na coluna;
- Não existir repetição no bloco 3x3.

---

### 4. Retrocesso (Backtracking)

Caso a escolha realizada impossibilite a solução:

- O valor é removido;
- O algoritmo retorna ao estado anterior;
- Uma nova possibilidade é testada.

Esse processo continua até encontrar uma solução válida.

---

## 📦 Organização dos módulos

### `sudoku_functions.py`

Responsável pela lógica de resolução.

Principais funções:

```python
resolveSudoku()
```

Executa o processo de resolução.

```python
_resolverSudokuBacktracking()
```

Implementa o algoritmo recursivo.

---

### `file_functions.py`

Responsável pela manipulação dos arquivos.

Funções:

```python
lerArquivoSudoku()
```

Realiza a leitura do CSV.

```python
salvarArquivoSudoku()
```

Grava o Sudoku resolvido.

---

### `validation_functions.py`

Responsável pelas validações.

Realiza:

- Validação dos tipos dos parâmetros;
- Validação da estrutura da matriz;
- Validação dos valores permitidos.

---

### `display_functions.py`

Responsável pela apresentação do resultado.

Função principal:

```python
exibeTabuleiro()
```

---

### `sudoku_constants.py`

Centraliza todas as constantes utilizadas pelo projeto.

Exemplos:

```python
TAMANHO_TABULEIRO = 9

TAMANHO_BLOCO     = 3

POSICAO_VAZIA     = 0
```

---

## ❓ FAQ

### ❓ Qual algoritmo é utilizado?

O projeto utiliza **Backtracking**, um algoritmo de busca recursiva que testa possibilidades e desfaz escolhas quando necessário.

---

### ❓ O Sudoku precisa possuir uma solução única?

Não.

O algoritmo encontra uma solução válida para o tabuleiro informado.

---

### ❓ Posso alterar o arquivo de entrada?

Sim.

Basta substituir o conteúdo do arquivo:

```text
sudoku_input.csv
```

mantendo o formato:

```text
valor;valor;valor;...
```

---

### ❓ O projeto utiliza bibliotecas externas?

Não.

Toda a implementação utiliza apenas recursos nativos do Python.

---

### ❓ Posso utilizar esse projeto em disciplinas de programação?

Sim.

O projeto foi desenvolvido com finalidade educacional, podendo ser utilizado para demonstrar:

- Matrizes;
- Funções;
- Recursividade;
- Backtracking;
- Organização modular.

---

## 🚧 Melhorias futuras

- Implementação de heurísticas para otimização da busca;
- Ordenação das posições vazias utilizando estratégia MRV (Minimum Remaining Values);
- Contagem de quantidade de soluções possíveis;
- Validação de Sudoku com solução única;
- Suporte a diferentes tamanhos de Sudoku;
- Interface gráfica;
- Interface Web;
- Exportação da solução para JSON;
- Geração automática de Sudoku;
- Implementação de outros algoritmos de resolução;
- Testes automatizados utilizando `pytest`.

---

## 🤝 Contribuição

Contribuições são bem-vindas.

1. Faça um Fork do projeto.
2. Crie uma Branch:

```bash
git checkout -b feature/nova-funcionalidade
```

3. Faça seus Commits.
4. Abra um Pull Request.

---

## 📄 Licença

Repositório desenvolvido para fins educacionais em Python, com foco no estudo de:

- Algoritmos;
- Estruturas de dados;
- Recursividade;
- Backtracking;
- Organização de projetos.

Este projeto está licenciado sob a licença MIT.

Consulte o arquivo `LICENSE` para mais detalhes.

---

## 👨‍💻 Autor

**Charles Cesar Magno de Freitas**

**Contato:** <freitascharles.dev@gmail.com>