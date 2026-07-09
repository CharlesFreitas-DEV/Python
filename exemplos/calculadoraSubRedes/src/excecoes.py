"""
Projeto.....: Calculadora de Sub-redes IPv4
Arquivo.....: excecoes.py
Descrição...: Exceções personalizadas da aplicação.
Autor.......: Charles Freitas
Licença.....: MIT
"""


# --------------------------------------------------------------------------------------------------------------
# Exceção base da aplicação.
class CalculadoraSubRedeError(Exception):
    """
    Classe base para todas as exceções específicas da aplicação Calculadora de Sub-redes IPv4.
    """
    pass


# --------------------------------------------------------------------------------------------------------------
# Exceção relacionada aos arquivos de configuração.
class ConfiguracaoError(CalculadoraSubRedeError):
    """
    Exceção lançada quando ocorre algum problema durante a leitura dos arquivos de configuração.
    """
    pass


# --------------------------------------------------------------------------------------------------------------
# Exceção base para erros de validação.
class ValidacaoError(CalculadoraSubRedeError):
    """
    Exceção base para erros relacionados aos dados de entrada.
    """
    pass


# --------------------------------------------------------------------------------------------------------------
# Exceção relacionada ao endereço IPv4.
class EnderecoIPInvalidoError(ValidacaoError):
    """
    Exceção lançada quando um endereço IPv4 informado é inválido.
    """
    pass


# --------------------------------------------------------------------------------------------------------------
# Exceção relacionada à máscara de rede.
class MascaraRedeInvalidaError(ValidacaoError):
    """
    Exceção lançada quando uma máscara CIDR informada é inválida.
    """
    pass


# --------------------------------------------------------------------------------------------------------------
# Exceção relacionada ao intervalo de máscaras.
class IntervaloMascaraInvalidoError(ValidacaoError):
    """
    Exceção lançada quando o intervalo de máscaras informado é inválido.
    """
    pass


# --------------------------------------------------------------------------------------------------------------
# Exceção relacionada aos arquivos de saída.
class ArquivoResultadoError(CalculadoraSubRedeError):
    """
    Exceção lançada quando ocorre algum problema durante a criação ou gravação dos resultados.
    """
    pass