"""
Projeto : Robô Cartesiano
Arquivo : constantes.py
Descrição : Constantes utilizadas pelo projeto.
Autor : Charles Cesar Magno de Freitas
Licença : MIT
"""

# --------------------------------------------------------------------------------------------------
# SEÇÕES DO ARQUIVO INI

SECAO_PLANO      = "PLANO"
SECAO_ROBO       = "ROBO"
SECAO_MOVIMENTOS = "MOVIMENTOS"


# --------------------------------------------------------------------------------------------------
# PARÂMETROS DA SEÇÃO [PLANO]

PARAMETRO_X_MINIMO = "X_MINIMO"
PARAMETRO_X_MAXIMO = "X_MAXIMO"
PARAMETRO_Y_MINIMO = "Y_MINIMO"
PARAMETRO_Y_MAXIMO = "Y_MAXIMO"


# --------------------------------------------------------------------------------------------------
# PARÂMETROS DA SEÇÃO [ROBO]

PARAMETRO_POSICAO_INICIAL_X = "POSICAO_INICIAL_X"
PARAMETRO_POSICAO_INICIAL_Y = "POSICAO_INICIAL_Y"
PARAMETRO_PASSO             = "PASSO"


# --------------------------------------------------------------------------------------------------
# PARÂMETROS DA SEÇÃO [MOVIMENTO]

PARAMETRO_SEQUENCIA = "SEQUENCIA"


# --------------------------------------------------------------------------------------------------
# COMANDOS DE MOVIMENTAÇÃO

MOVIMENTO_NORTE    = "N"
MOVIMENTO_SUL      = "S"
MOVIMENTO_LESTE    = "L"
MOVIMENTO_OESTE    = "O"

MOVIMENTO_NOROESTE = "Q"
MOVIMENTO_NORDESTE = "E"
MOVIMENTO_SUDOESTE = "Z"
MOVIMENTO_SUDESTE  = "C"


# --------------------------------------------------------------------------------------------------
# CONJUNTO DE MOVIMENTOS VÁLIDOS

MOVIMENTOS_VALIDOS = {MOVIMENTO_NORTE, MOVIMENTO_SUL, MOVIMENTO_LESTE, MOVIMENTO_OESTE,
                      MOVIMENTO_NOROESTE, MOVIMENTO_NORDESTE, MOVIMENTO_SUDOESTE, MOVIMENTO_SUDESTE}


# --------------------------------------------------------------------------------------------------
# LIMITES

PASSO_MINIMO = 1


# --------------------------------------------------------------------------------------------------
# STATUS DA EXECUÇÃO

STATUS_MOVIMENTO_REALIZADO = "REALIZADO"
STATUS_MOVIMENTO_IGNORADO  = "IGNORADO"
STATUS_COLISAO             = "COLISAO"


# --------------------------------------------------------------------------------------------------
# FORMATAÇÃO DO RELATÓRIO

SEPARADOR_RELATORIO = "=" * 90
SEPARADOR_SECAO     = "-" * 90
TEXTO_VAZIO         = ""


# --------------------------------------------------------------------------------------------------
# MENSAGENS PADRÃO

MENSAGEM_SUCESSO            = "Simulação executada com sucesso."
MENSAGEM_COLISAO            = "Movimento não realizado: colisão com os limites do plano."
MENSAGEM_MOVIMENTO_INVALIDO = "Movimento inválido ignorado."