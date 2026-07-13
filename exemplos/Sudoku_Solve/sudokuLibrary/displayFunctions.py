from sudokuLibrary.sudokuConstants import (TAMANHO_BLOCO,TAMANHO_TABULEIRO)

from sudokuLibrary.validationFunctions import (validarTiposParametros,validarMatrizSudoku)

# ----------------------------------------------------------------------
# Formata o tabuleiro do Sudoku.
def _formatarTabuleiro(lstMatrizTabuleiro: list[list[int]]) -> str:

    lstLinhas = list()
    for intLinha in range(TAMANHO_TABULEIRO):
        lstColunas = list()
        for intColuna in range(TAMANHO_TABULEIRO):
            lstColunas.append(str(lstMatrizTabuleiro[intLinha][intColuna]))
            if ((intColuna + 1) % TAMANHO_BLOCO == 0 and intColuna < TAMANHO_TABULEIRO - 1):
                lstColunas.append("|")
        lstLinhas.append(" ".join(lstColunas))

        if ((intLinha + 1) % TAMANHO_BLOCO == 0 and intLinha < TAMANHO_TABULEIRO - 1):
            lstLinhas.append("-" * 21)

    return "\n".join(lstLinhas)


# ----------------------------------------------------------------------
# Exibe o tabuleiro do Sudoku.
def exibeTabuleiro(lstMatrizTabuleiro: list[list[int]]) -> None:

    validarTiposParametros([(lstMatrizTabuleiro, list, "lstMatrizTabuleiro")])

    validarMatrizSudoku(lstMatrizTabuleiro)

    print(_formatarTabuleiro(lstMatrizTabuleiro))