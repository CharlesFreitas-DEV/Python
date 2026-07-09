"""
Projeto.....: Calculadora de Sub-redes IPv4
Arquivo.....: funcoesIP.py
Descrição...: Funções responsáveis pelos cálculos de endereçamento IPv4.
Autor.......: Charles Freitas
Licença.....: MIT
"""


from src.modelos import SubRede


# --------------------------------------------------------------------------------------------------------------
# Converte um endereço IPv4 textual para inteiro.
def _converterIPParaInteiro(strEnderecoIP: str) -> int:

    lstOctetos    = strEnderecoIP.split(".")
    intEnderecoIP = 0

    for strOcteto in lstOctetos:
        intEnderecoIP = (intEnderecoIP << 8) | int(strOcteto)

    return intEnderecoIP


# --------------------------------------------------------------------------------------------------------------
# Converte um endereço IPv4 inteiro para formato textual.
def _converterInteiroParaIP(intEnderecoIP: int) -> str:

    lstOctetos = list()

    for intPosicao in range(3, -1, -1):
        intOcteto = (intEnderecoIP >> (intPosicao * 8)) & 255
        lstOctetos.append(str(intOcteto))

    return ".".join(lstOctetos)


# --------------------------------------------------------------------------------------------------------------
# Gera uma máscara IPv4 inteira a partir do CIDR.
def _gerarMascaraInteiro(intMascaraCIDR: int) -> int:

    if intMascaraCIDR == 0:
        return 0

    return (0xFFFFFFFF << (32 - intMascaraCIDR)) & 0xFFFFFFFF


# --------------------------------------------------------------------------------------------------------------
# Converte uma máscara inteira para formato decimal.
def _converterMascaraDecimal(intMascara: int) -> str:

    return _converterInteiroParaIP(intMascara)


# --------------------------------------------------------------------------------------------------------------
# Converte uma máscara inteira para formato binário.
def _converterMascaraBinaria(intMascara: int) -> str:

    lstOctetos = list()

    for intPosicao in range(3, -1, -1):
        intOcteto = (intMascara >> (intPosicao * 8)) & 255
        lstOctetos.append(format(intOcteto, "08b"))

    return ".".join(lstOctetos)


# --------------------------------------------------------------------------------------------------------------
# Calcula o endereço de rede.
def _calcularEnderecoRede(intEnderecoIP: int, intMascara: int) -> int:

    return intEnderecoIP & intMascara


# --------------------------------------------------------------------------------------------------------------
# Calcula o endereço de broadcast.
def _calcularBroadcast(intEnderecoRede: int, intMascara: int) -> int:

    return intEnderecoRede | (~intMascara & 0xFFFFFFFF)


# --------------------------------------------------------------------------------------------------------------
# Calcula o primeiro host válido.
def _calcularPrimeiroHost(intEnderecoRede: int, intMascaraCIDR: int) -> int:

    if intMascaraCIDR >= 31:
        return intEnderecoRede

    return intEnderecoRede + 1


# --------------------------------------------------------------------------------------------------------------
# Calcula o último host válido.
def _calcularUltimoHost(intBroadcast: int, intMascaraCIDR: int) -> int:

    if intMascaraCIDR >= 31:
        return intBroadcast

    return intBroadcast - 1


# --------------------------------------------------------------------------------------------------------------
# Calcula a quantidade de hosts válidos.
def _calcularQuantidadeHosts(intMascaraCIDR: int) -> int:

    intBitsHost = 32 - intMascaraCIDR

    if intMascaraCIDR == 32:
        return 1

    if intMascaraCIDR == 31:
        return 2

    return (1 << intBitsHost) - 2


# --------------------------------------------------------------------------------------------------------------
# Gera todas as informações de uma sub-rede IPv4.
def gerarInformacoesSubRede(strEnderecoIP: str, intMascaraCIDR: int) -> SubRede:

    intEnderecoIP   = _converterIPParaInteiro(strEnderecoIP)
    intMascara      = _gerarMascaraInteiro(intMascaraCIDR)
    intEnderecoRede = _calcularEnderecoRede(intEnderecoIP, intMascara)
    intBroadcast    = _calcularBroadcast(intEnderecoRede, intMascara)
    intPrimeiroHost = _calcularPrimeiroHost(intEnderecoRede, intMascaraCIDR)
    intUltimoHost   = _calcularUltimoHost(intBroadcast, intMascaraCIDR)


    return SubRede(intCIDR           = intMascaraCIDR, 
                   strEnderecoRede   = _converterInteiroParaIP(intEnderecoRede),
                   strPrimeiroHost   = _converterInteiroParaIP(intPrimeiroHost),
                   strUltimoHost     = _converterInteiroParaIP(intUltimoHost),
                   strBroadcast      = _converterInteiroParaIP(intBroadcast),
                   strMascaraDecimal = _converterMascaraDecimal(intMascara),
                   strMascaraBinaria = _converterMascaraBinaria(intMascara),
                   intHostsValidos   = _calcularQuantidadeHosts(intMascaraCIDR)
                )