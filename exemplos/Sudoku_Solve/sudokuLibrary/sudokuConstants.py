# ----------------------------------------------------------------------
# Configurações do tabuleiro Sudoku.
TAMANHO_TABULEIRO   = 9     # Quantidade de linhas e colunas do tabuleiro.
TAMANHO_BLOCO       = 3     # Tamanho do bloco interno (3 x 3).
POSICAO_VAZIA       = 0     # Valor utilizado para representar uma posição vazia.

PRIMEIRA_LINHA      = 0     # Índice da primeira linha do tabuleiro.
PRIMEIRA_COLUNA     = 0     # Índice da primeira coluna do tabuleiro.
ULTIMA_LINHA        = TAMANHO_TABULEIRO - 1
ULTIMA_COLUNA       = TAMANHO_TABULEIRO - 1

# ----------------------------------------------------------------------
# Faixa de valores permitidos no tabuleiro.
PRIMEIRO_NUMERO     = 1     # Primeiro valor válido do Sudoku.
ULTIMO_NUMERO       = 9     # Último número válido do Sudoku.
VALOR_MINIMO        = 0     # Menor valor permitido em uma célula.
                                # O valor zero representa uma posição vazia.
VALOR_MAXIMO        = 9     # Maior valor permitido em uma célula.


# ----------------------------------------------------------------------
# Configurações de arquivos CSV.
SEPARADOR           = ";"       # Caractere utilizado para separar os valores no arquivo CSV.
ENCODING            = "utf-8"   # Codificação utilizada na leitura e gravação dos arquivos.