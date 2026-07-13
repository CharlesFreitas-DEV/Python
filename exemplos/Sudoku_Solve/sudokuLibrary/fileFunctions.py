from pathlib import Path

from sudokuLibrary.sudokuConstants import (VALOR_MAXIMO, VALOR_MINIMO, ENCODING, SEPARADOR)

from sudokuLibrary.validationFunctions import (validarMatrizSudoku, validarTiposParametros, validarValoresSudoku)

# ----------------------------------------------------------------------
# Lê um arquivo CSV contendo um Sudoku.
def lerArquivoSudoku(pathArquivo: Path) -> list[list[int]]:

    validarTiposParametros([(pathArquivo, Path, "pathArquivo")])

    try:
        with open(pathArquivo, "r", encoding=ENCODING) as arquivo:
            lstLinhasArquivo = arquivo.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo \"{pathArquivo}\" não foi encontrado.")
    except PermissionError:
        raise PermissionError(f"Sem permissão para acessar \"{pathArquivo}\".")


    if not lstLinhasArquivo:
        raise ValueError("O arquivo informado está vazio.")

    lstMatrizTabuleiro = list()

    for intNumeroLinha, strLinha in enumerate(lstLinhasArquivo, start=1):
        lstLinha = list()
        for strValor in strLinha.strip().split(SEPARADOR):
            try:
                lstLinha.append(int(strValor.strip()))
            except ValueError:
                raise ValueError(f"A linha {intNumeroLinha} possui valores não numéricos.")


        lstMatrizTabuleiro.append(lstLinha)

    validarMatrizSudoku(lstMatrizTabuleiro)

    validarValoresSudoku(lstMatrizTabuleiro, VALOR_MINIMO, VALOR_MAXIMO)

    return lstMatrizTabuleiro


# ----------------------------------------------------------------------
# Salva um Sudoku em um arquivo CSV.
def salvarArquivoSudoku(pathArquivo: Path, lstMatrizTabuleiro: list[list[int]]) -> None:

    validarTiposParametros([(pathArquivo       , Path, "pathArquivo"       ),
                            (lstMatrizTabuleiro, list, "lstMatrizTabuleiro")])

    validarMatrizSudoku(lstMatrizTabuleiro)

    validarValoresSudoku(lstMatrizTabuleiro, VALOR_MINIMO, VALOR_MAXIMO)

    try:
        with open(pathArquivo, "w", encoding=ENCODING) as arquivo:
            for lstLinha in lstMatrizTabuleiro:
                arquivo.write(SEPARADOR.join(map(str,lstLinha)))
                arquivo.write("\n")
    except PermissionError:
        raise PermissionError(f'Sem permissão para gravar "{pathArquivo}".')