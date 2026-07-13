# ----------------------------------------------------------------------
# Biblioteca Sudoku_Solve
# Este arquivo define as funções públicas disponibilizadas pelo pacote.
# Funções internas dos módulos permanecem encapsuladas.


from sudokuLibrary.sudokuFunctions import (resolveSudoku)

from sudokuLibrary.fileFunctions import (lerArquivoSudoku,salvarArquivoSudoku)

from sudokuLibrary.displayFunctions import (exibeTabuleiro)


# ----------------------------------------------------------------------
# Controle da API pública do pacote.
# Define explicitamente quais elementos serão exportados quando utilizado:
# from sudoku_library import *

__all__ = [ "resolveSudoku", "lerArquivoSudoku", "salvarArquivoSudoku", "exibeTabuleiro" ]