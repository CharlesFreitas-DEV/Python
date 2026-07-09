"""
Projeto.....: Calculadora de Sub-redes IPv4
Arquivo.....: funcoesValidacao.py
Descrição...: Funções responsáveis pela validação dos dados de entrada.
Autor.......: Charles Freitas
Licença.....: MIT
"""

from src.excecoes import (EnderecoIPInvalidoError, IntervaloMascaraInvalidoError, MascaraRedeInvalidaError)


# --------------------------------------------------------------------------------------------------------------
# Valida a quantidade de octetos do endereço IPv4.
def validarQuantidadeOctetos(lstOctetos: list[str]) -> bool:

    if len(lstOctetos) != 4:
        raise EnderecoIPInvalidoError("O endereço IP deve possuir exatamente quatro octetos.")

    return True


# --------------------------------------------------------------------------------------------------------------
# Valida se um octeto possui somente caracteres numéricos.
def validarOctetoNumerico(strOcteto: str) -> bool:

    if not strOcteto.isdigit():
        raise EnderecoIPInvalidoError("Todos os octetos do endereço IP devem ser numéricos.")

    return True


# --------------------------------------------------------------------------------------------------------------
# Valida a faixa de valores de um octeto IPv4.
def validarFaixaOcteto(intOcteto: int) -> bool:

    if intOcteto < 0 or intOcteto > 255:
        raise EnderecoIPInvalidoError("Cada octeto do endereço IP deve estar entre 0 e 255.")

    return True


# --------------------------------------------------------------------------------------------------------------
# Valida um endereço IPv4.
def validarEnderecoIP(strEnderecoIP: str) -> bool:

    lstOctetos = strEnderecoIP.strip().split(".")

    validarQuantidadeOctetos(lstOctetos)

    for strOcteto in lstOctetos:
        validarOctetoNumerico(strOcteto)
        validarFaixaOcteto(int(strOcteto))

    return True


# --------------------------------------------------------------------------------------------------------------
# Valida uma máscara de rede no formato CIDR.
def validarMascaraRede(intMascara: int) -> bool:

    try:
        intMascara = int(intMascara)
    except ValueError:
        raise MascaraRedeInvalidaError("A máscara de rede deve ser um valor inteiro.")


    if intMascara < 0 or intMascara > 32:
        raise MascaraRedeInvalidaError("A máscara de rede deve estar entre /0 e /32.")

    return True


# --------------------------------------------------------------------------------------------------------------
# Valida o intervalo entre as máscaras inicial e final.
def validarIntervaloMascaras(intMascaraInicial: int, intMascaraFinal: int) -> bool:

    validarMascaraRede(intMascaraInicial)

    validarMascaraRede(intMascaraFinal)


    if intMascaraInicial > intMascaraFinal:
        raise IntervaloMascaraInvalidoError("A máscara inicial deve ser menor ou igual à máscara final.")

    return True


# --------------------------------------------------------------------------------------------------------------
# Executa todas as validações dos dados de entrada.
def validarEntradas(strEnderecoIP: str, intMascaraInicial: int, intMascaraFinal: int) -> bool:

    validarEnderecoIP(strEnderecoIP)

    validarIntervaloMascaras(intMascaraInicial, intMascaraFinal)

    return True