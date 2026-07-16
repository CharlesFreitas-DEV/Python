"""
Projeto : Robô Cartesiano
Arquivo : funcoesValidacao.py
Descrição : Funções de validação do projeto.
Autor : Charles Cesar Magno de Freitas
Licença : MIT
"""

from roboLibrary.constantes import PASSO_MINIMO

from roboLibrary.excecoes import (PassoInvalidoException, PosicaoInicialInvalidaException,
                                  ValorInteiroInvalidoException, LimitePlanoInvalidoException,
                                  ValorStringInvalidoException) 

from roboLibrary.modelos import (Configuracao, Plano, Posicao, SequenciaMovimentos)


# --------------------------------------------------------------------------------------------------
# Valida se um valor é do tipo inteiro.
def validarInteiro(valor: object, nomeParametro: str) -> None:
    if not isinstance(valor, int):
        raise ValorInteiroInvalidoException(f"O parâmetro '{nomeParametro}' deve ser um número inteiro.")


# --------------------------------------------------------------------------------------------------
# Valida os limites do plano cartesiano.
def validarPlano(plano: Plano) -> None:
    if not isinstance(plano, Plano):
        raise TypeError("plano deve ser do tipo Plano.")

    validarInteiro(plano.xMinimo, "X_MINIMO")
    validarInteiro(plano.xMaximo, "X_MAXIMO")
    validarInteiro(plano.yMinimo, "Y_MINIMO")
    validarInteiro(plano.yMaximo, "Y_MAXIMO")

    if plano.xMaximo <= plano.xMinimo:
        raise LimitePlanoInvalidoException("X_MAXIMO deve ser maior que X_MINIMO.")

    if plano.yMaximo <= plano.yMinimo:
        raise LimitePlanoInvalidoException("Y_MAXIMO deve ser maior que Y_MINIMO.")


# --------------------------------------------------------------------------------------------------
# Valida o deslocamento do robô.
def validarPasso(passo: int) -> None:
    validarInteiro(passo, "PASSO")

    if passo < PASSO_MINIMO:
        raise PassoInvalidoException("O valor de PASSO deve ser maior ou igual a 1.")


# --------------------------------------------------------------------------------------------------
# Valida se a posição inicial está dentro dos limites do plano.
def validarPosicaoInicial(posicao: Posicao, plano: Plano) -> None:
    if not isinstance(posicao, Posicao):
        raise TypeError("posicao deve ser do tipo Posicao.")

    if not isinstance(plano, Plano):
        raise TypeError("plano deve ser do tipo Plano.")

    if not (plano.xMinimo <= posicao.x <= plano.xMaximo):
        raise PosicaoInicialInvalidaException("POSICAO_X está fora dos limites do plano.")

    if not (plano.yMinimo <= posicao.y <= plano.yMaximo):
        raise PosicaoInicialInvalidaException("POSICAO_Y está fora dos limites do plano.")


# --------------------------------------------------------------------------------------------------
# Valida toda a configuração utilizada pela aplicação.
def validarConfiguracao(configuracao: Configuracao) -> None:
    if not isinstance(configuracao, Configuracao):
        raise TypeError("configuracao deve ser do tipo Configuracao.")

    validarPlano(configuracao.plano)

    validarPasso(configuracao.robo.passo)

    validarPosicaoInicial(configuracao.robo.posicaoInicial, configuracao.plano)

    if not isinstance(configuracao.movimentos, SequenciaMovimentos):
        raise TypeError("movimentos deve ser do tipo SequenciaMovimentos.")


    if not isinstance(configuracao.movimentos.original, str):
        raise ValorStringInvalidoException("A sequência de movimentos deve ser uma string.")
