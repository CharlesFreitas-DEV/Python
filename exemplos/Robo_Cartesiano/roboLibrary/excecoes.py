"""
Projeto : Robô Cartesiano
Arquivo : excecoes.py
Descrição : Exceções personalizadas utilizadas pela aplicação.
Autor : Charles Cesar Magno de Freitas
Licença : MIT
"""


# --------------------------------------------------------------------------------------------------
# Classe base para todas as exceções da aplicação.
class RoboCartesianoException(Exception):
    def __init__(self, mensagem: str) -> None:
        super().__init__(mensagem)


# --------------------------------------------------------------------------------------------------
# Arquivo de configuração não encontrado.
class ArquivoConfiguracaoNaoEncontradoException(RoboCartesianoException):
    def __init__(self, mensagem: str = "Arquivo de configuração não encontrado.") -> None:
        super().__init__(mensagem)


# --------------------------------------------------------------------------------------------------
# Arquivo de configuração inválido.
class ArquivoConfiguracaoInvalidoException(RoboCartesianoException):
    def __init__(self, mensagem: str = "Arquivo de configuração inválido.") -> None:
        super().__init__(mensagem)

# --------------------------------------------------------------------------------------------------
# Seção obrigatória não encontrada no arquivo INI.
class SecaoObrigatoriaNaoEncontradaException(RoboCartesianoException):
    def __init__(self, mensagem: str = "Seção obrigatória não encontrada.") -> None:
        super().__init__(mensagem)


# --------------------------------------------------------------------------------------------------
# Parâmetro obrigatório ausente.
class ParametroObrigatorioNaoEncontradoException(RoboCartesianoException):
    def __init__(self, mensagem: str = "Parâmetro obrigatório não encontrado.") -> None:
        super().__init__(mensagem)


# --------------------------------------------------------------------------------------------------
# Valor inteiro inválido.
class ValorInteiroInvalidoException(RoboCartesianoException):
    def __init__(self, mensagem: str = "O valor informado deve ser inteiro.") -> None:
        super().__init__(mensagem)


# --------------------------------------------------------------------------------------------------
# Valor inteiro inválido.
class ValorStringInvalidoException(RoboCartesianoException):
    def __init__(self, mensagem: str = "O valor informado deve ser string.") -> None:
        super().__init__(mensagem)


# --------------------------------------------------------------------------------------------------
# Limites do plano inválidos.
class LimitePlanoInvalidoException(RoboCartesianoException):
    def __init__(self, mensagem: str = "Os limites do plano cartesiano são inválidos.") -> None:
        super().__init__(mensagem)


# --------------------------------------------------------------------------------------------------
# Posição inicial inválida.
class PosicaoInicialInvalidaException(RoboCartesianoException):
    def __init__(self, mensagem: str = "A posição inicial do robô é inválida.") -> None:
        super().__init__(mensagem)


# --------------------------------------------------------------------------------------------------
# Passo inválido.
class PassoInvalidoException(RoboCartesianoException):
    def __init__(self, mensagem: str = "O passo informado é inválido.") -> None:
        super().__init__(mensagem)


# --------------------------------------------------------------------------------------------------
# Movimento inválido.
class MovimentoInvalidoException(RoboCartesianoException):
    def __init__(self, mensagem: str = "Movimento inválido.") -> None:
        super().__init__(mensagem)


# --------------------------------------------------------------------------------------------------
# Erro ao gravar relatório.
class GravacaoRelatorioException(RoboCartesianoException):
    def __init__(self, mensagem: str = "Não foi possível gravar o relatório.") -> None:
        super().__init__(mensagem)