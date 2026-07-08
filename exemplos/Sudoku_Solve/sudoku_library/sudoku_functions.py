from sudoku_library.sudoku_constants import (PRIMEIRA_COLUNA  , PRIMEIRA_LINHA,
                                             PRIMEIRO_NUMERO  , ULTIMO_NUMERO ,
                                             POSICAO_VAZIA    , TAMANHO_BLOCO , 
                                             TAMANHO_TABULEIRO, ULTIMA_LINHA  )

from sudoku_library.validation_functions import (validarMatrizSudoku, validarTiposParametros)

# ----------------------------------------------------------------------
# Resolve um Sudoku utilizando o algoritmo de Backtracking.
def resolveSudoku(lstMatrizTabuleiro: list[list[int]]) -> bool:

    validarTiposParametros([(lstMatrizTabuleiro, list, "lstMatrizTabuleiro")])

    validarMatrizSudoku(lstMatrizTabuleiro)

    return _resolverSudokuBacktracking(lstMatrizTabuleiro, PRIMEIRA_LINHA, PRIMEIRA_COLUNA)


# ----------------------------------------------------------------------
# Verifica se um número já existe na linha informada.
def _numeroExisteNaLinha(lstMatrizTabuleiro: list[list[int]], intLinha: int,intNumero: int) -> bool:
    for intColuna in range(TAMANHO_TABULEIRO):
        if (lstMatrizTabuleiro[intLinha][intColuna] == intNumero):
            return True
    return False


# ----------------------------------------------------------------------
# Verifica se um número já existe na coluna informada.
def _numeroExisteNaColuna(lstMatrizTabuleiro: list[list[int]], intColuna: int, intNumero: int) -> bool:
    for intLinha in range(TAMANHO_TABULEIRO):
        if (lstMatrizTabuleiro[intLinha][intColuna] == intNumero):
            return True
    return False


# ----------------------------------------------------------------------
# Verifica se um número já existe no bloco 3 x 3 correspondente.
def _numeroExisteNoBloco(lstMatrizTabuleiro: list[list[int]], intLinha: int, intColuna: int, intNumero: int) -> bool:

    intPrimeiraLinhaBloco  = (intLinha - (intLinha % TAMANHO_BLOCO))
    intPrimeiraColunaBloco = (intColuna - (intColuna % TAMANHO_BLOCO))

    for intLinhaBloco in range(TAMANHO_BLOCO):
        for intColunaBloco in range(TAMANHO_BLOCO):
            if (lstMatrizTabuleiro[intPrimeiraLinhaBloco + intLinhaBloco][intPrimeiraColunaBloco + intColunaBloco] == intNumero):
                return True
    return False


# ----------------------------------------------------------------------
# Verifica se um número pode ser inserido em uma determinada posição.
def _podeInserirNumero(lstMatrizTabuleiro: list[list[int]], intLinha: int, intColuna: int, intNumero: int) -> bool:

    if _numeroExisteNaLinha(lstMatrizTabuleiro, intLinha, intNumero):
        return False

    if _numeroExisteNaColuna(lstMatrizTabuleiro, intColuna, intNumero):
        return False

    if _numeroExisteNoBloco(lstMatrizTabuleiro, intLinha, intColuna, intNumero):
        return False

    return True


# ----------------------------------------------------------------------
# Resolve o Sudoku utilizando Backtracking.
def _resolverSudokuBacktracking(lstMatrizTabuleiro: list[list[int]], intLinhaAtual: int, intColunaAtual: int) -> bool:

    # --------------------------------------------------------------
    # Se a última coluna da última linha foi ultrapassada,
    # significa que todas as posições do tabuleiro foram
    # preenchidas corretamente.
    if (intLinhaAtual == ULTIMA_LINHA and intColunaAtual == TAMANHO_TABULEIRO):
        return True

    # --------------------------------------------------------------
    # Ao terminar uma linha, continua na próxima.
    if intColunaAtual == TAMANHO_TABULEIRO:
        intLinhaAtual += 1
        intColunaAtual = PRIMEIRA_COLUNA

    # --------------------------------------------------------------
    # Caso a posição atual já esteja preenchida,
    # continua para a próxima coluna.
    if (lstMatrizTabuleiro[intLinhaAtual][intColunaAtual] != POSICAO_VAZIA):
        return _resolverSudokuBacktracking(lstMatrizTabuleiro, intLinhaAtual, intColunaAtual + 1)

    # --------------------------------------------------------------
    # Testa todos os números possíveis para a posição atual.
    for intNumero in range(PRIMEIRO_NUMERO, ULTIMO_NUMERO + 1):
        if _podeInserirNumero(lstMatrizTabuleiro, intLinhaAtual, intColunaAtual, intNumero):
            # Insere temporariamente o número na posição atual.
            lstMatrizTabuleiro[intLinhaAtual][intColunaAtual] = intNumero

            # Continua resolvendo o restante do tabuleiro.
            if _resolverSudokuBacktracking(lstMatrizTabuleiro, intLinhaAtual, intColunaAtual + 1):
                return True

            # BACKTRACK
            # O número escolhido não levou à solução.
            # Remove o valor inserido e retorna ao estado anterior para tentar outro número.
            lstMatrizTabuleiro[intLinhaAtual][intColunaAtual] = POSICAO_VAZIA


    # --------------------------------------------------------------
    # Nenhum número pôde ser inserido nesta posição.
    # Retorna para a chamada anterior da recursão para que outra
    # escolha seja realizada.
    return False