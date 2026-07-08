from pathlib import Path

import sudoku_library

# ----------------------------------------------------------------------
# Configuração dos arquivos da aplicação.
# Para resolver outro Sudoku, basta alterar os nomes dos arquivos abaixo.
NOME_ARQUIVO_ENTRADA = "sudoku_input.csv"
NOME_ARQUIVO_SAIDA   = "sudoku_output.csv"


# ----------------------------------------------------------------------
# Diretório raiz do projeto.
PATH_DIRETORIO_PROJETO = Path(__file__).resolve().parent


# ----------------------------------------------------------------------
# Caminhos completos dos arquivos.
PATH_ARQUIVO_ENTRADA = (PATH_DIRETORIO_PROJETO / NOME_ARQUIVO_ENTRADA)
PATH_ARQUIVO_SAIDA   = (PATH_DIRETORIO_PROJETO / NOME_ARQUIVO_SAIDA)


# ----------------------------------------------------------------------
# Programa Principal.
def main() -> None:
    try:
        lstMatrizTabuleiro = sudoku_library.lerArquivoSudoku(PATH_ARQUIVO_ENTRADA)
    except Exception as erro:
        print(f"\nERRO: {erro}")
    else:
        if sudoku_library.resolveSudoku(lstMatrizTabuleiro):
            print("\nSudoku resolvido:\n")
            sudoku_library.exibeTabuleiro(lstMatrizTabuleiro)
            sudoku_library.salvarArquivoSudoku(PATH_ARQUIVO_SAIDA,lstMatrizTabuleiro)
            print(f"\nArquivo gerado com sucesso: "f"{PATH_ARQUIVO_SAIDA.name}")
        else:
            print("\nERRO: O Sudoku informado não possui solução.")


# ----------------------------------------------------------------------
# Ponto de entrada da aplicação.
if __name__ == "__main__":
    main()