# ----------------------------------------------------------------------
# Biblioteca Sudoku_Solve
# Este arquivo define as funções públicas disponibilizadas pelo pacote.
# Funções internas dos módulos permanecem encapsuladas.


from sudoku_library.sudoku_functions import (resolveSudoku)

from sudoku_library.file_functions import (lerArquivoSudoku,salvarArquivoSudoku)

from sudoku_library.display_functions import (exibeTabuleiro)


# ----------------------------------------------------------------------
# Controle da API pública do pacote.
# Define explicitamente quais elementos serão exportados quando utilizado:
# from sudoku_library import *

__all__ = [ "resolveSudoku", "lerArquivoSudoku", "salvarArquivoSudoku", "exibeTabuleiro" ]