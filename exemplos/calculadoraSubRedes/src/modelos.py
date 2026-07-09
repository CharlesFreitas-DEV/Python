"""
Projeto.....: Calculadora de Sub-redes IPv4
Arquivo.....: modelos.py
Descrição...: Modelos de dados utilizados pela aplicação.
Autor.......: Charles Freitas
Licença.....: MIT
"""

from dataclasses import dataclass


# --------------------------------------------------------------------------------------------------------------
# Representa os dados de uma sub-rede IPv4 calculada pela aplicação.
@dataclass(slots=True)
class SubRede:
    intCIDR          : int  # Máscara CIDR da sub-rede.
    strEnderecoRede  : str  # Endereço de rede.
    strPrimeiroHost  : str  # Primeiro endereço IP disponível para host.
    strUltimoHost    : str  # Último endereço IP disponível para host.
    strBroadcast     : str  # Endereço de broadcast.
    strMascaraDecimal: str  # Máscara de sub-rede no formato decimal.
    strMascaraBinaria: str  # Máscara de sub-rede no formato binário.
    intHostsValidos  : int  # Quantidade de hosts válidos na sub-rede.


# --------------------------------------------------------------------------------------------------------------
# Representa as informações de entrada da aplicação.
@dataclass(slots=True)
class InformacoesRede:
    strEnderecoIP    : str  # Endereço IPv4.
    intMascaraInicial: int  # Máscara inicial em formato CIDR.
    intMascaraFinal  : int  # Máscara final em formato CIDR.