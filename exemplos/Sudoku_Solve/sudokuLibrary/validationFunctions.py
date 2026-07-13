from sudokuLibrary.sudokuConstants import (TAMANHO_TABULEIRO)

# ----------------------------------------------------------------------
# Valida o tipo de um único parâmetro.
def validarTipoParametro(objValor: object, clsTipoEsperado: type, strNomeParametro: str) -> None:
    if not isinstance(objValor,clsTipoEsperado):
        raise TypeError(f'O parâmetro "{strNomeParametro}" '
                        f'deve ser do tipo '
                        f'"{clsTipoEsperado.__name__}".')


# ----------------------------------------------------------------------
# Valida o tipo de vários parâmetros.
def validarTiposParametros(lstParametros: list[tuple]) -> None:
    validarTipoParametro(lstParametros,list,"lstParametros")

    for tplParametro in lstParametros:
        if len(tplParametro) != 3:
            raise ValueError("Cada parâmetro deve possuir "
                             "(valor, tipo, nome).")


        objValor         = tplParametro[0]
        clsTipoEsperado  = tplParametro[1]
        strNomeParametro = tplParametro[2]

        validarTipoParametro(objValor,clsTipoEsperado,strNomeParametro)


# ----------------------------------------------------------------------
# Valida a estrutura da matriz do Sudoku.
def validarMatrizSudoku(lstMatrizTabuleiro: list) -> None:

    validarTipoParametro(lstMatrizTabuleiro,list,"lstMatrizTabuleiro")

    if (len(lstMatrizTabuleiro) != TAMANHO_TABULEIRO):
        raise ValueError("A matriz do Sudoku deve possuir "
                         f"{TAMANHO_TABULEIRO} linhas.")

    for intLinha, lstLinha in enumerate(lstMatrizTabuleiro, start=1):
        validarTipoParametro(lstLinha, list, f"linha {intLinha}" )

        if (len(lstLinha) != TAMANHO_TABULEIRO):
            raise ValueError(f"A linha {intLinha} deve possuir "
                             f"{TAMANHO_TABULEIRO} colunas.")

        for intColuna, intValor in enumerate(lstLinha, start=1):
            validarTipoParametro(intValor, int, f"posição ({intLinha}, {intColuna})")


# ----------------------------------------------------------------------
# Valida os valores armazenados na matriz.
def validarValoresSudoku(lstMatrizTabuleiro: list[list[int]], intValorMinimo: int, intValorMaximo: int) -> None:

    validarTiposParametros([(lstMatrizTabuleiro, list, "lstMatrizTabuleiro"),
                            (intValorMinimo    , int , "intValorMinimo"    ),
                            (intValorMaximo    , int , "intValorMaximo"    )])

    for intLinha, lstLinha in enumerate(lstMatrizTabuleiro, start=1):
        for intColuna, intValor in enumerate(lstLinha, start=1):
            if (intValor < intValorMinimo or intValor > intValorMaximo):
                raise ValueError(f"Valor inválido na posição "
                                 f"({intLinha}, {intColuna}). "
                                 f"Valor encontrado: {intValor}. "
                                 f"Valores permitidos: "
                                 f"{intValorMinimo} a "
                                 f"{intValorMaximo}.")