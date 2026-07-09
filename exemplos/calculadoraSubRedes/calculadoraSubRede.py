"""
Projeto.....: Calculadora de Sub-redes IPv4
Arquivo.....: calculadoraSubRede.py
Descrição...: Programa principal.
Autor.......: Charles Freitas
Licença.....: MIT
"""

from src import configuracoes

from src.funcoesArquivo import salvarResultadosJSON
from src.funcoesIP import gerarInformacoesSubRede
from src.funcoesValidacao import validarEntradas


# --------------------------------------------------------------------------------------------------------------
# Executa o cálculo das sub-redes IPv4.
def executarCalculadoraSubRede() -> bool:

    objInformacoesRede = configuracoes.obterInformacoesRede()

    validarEntradas(objInformacoesRede.strEnderecoIP, 
                    objInformacoesRede.intMascaraInicial, 
                    objInformacoesRede.intMascaraFinal
                    )

    lstSubRedes = list()

    for intMascaraCIDR in range(objInformacoesRede.intMascaraInicial, objInformacoesRede.intMascaraFinal + 1):
        objSubRede = gerarInformacoesSubRede(objInformacoesRede.strEnderecoIP, intMascaraCIDR)

        lstSubRedes.append(objSubRede)

    salvarResultadosJSON(objInformacoesRede, lstSubRedes)

    return True


# --------------------------------------------------------------------------------------------------------------
# Programa principal.
def main() -> None:

    executarCalculadoraSubRede()

    print("\nCálculo das sub-redes realizado com sucesso.")
    print("Arquivo JSON gerado na pasta resultados.\n")


# --------------------------------------------------------------------------------------------------------------
# Ponto de entrada da aplicação.
if __name__ == "__main__":
    main()