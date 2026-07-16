"""
Projeto : Robô Cartesiano
Arquivo : modelos.py
Descrição : Modelos de domínio utilizados pela aplicação.
Autor : Charles Cesar Magno de Freitas
Licença : MIT


* Responsabilidade do módulo

    Este módulo contém exclusivamente os modelos de domínio utilizados
    pela simulação do robô cartesiano.


* Modelos disponíveis

    - Plano:
        Representa os limites do plano cartesiano.

    - Posicao:
        Representa uma coordenada no plano.

    - Robo:
        Representa o estado atual do robô.

    - SequenciaMovimentos:
        Representa os comandos informados pelo usuário.

    - Configuracao:
        Agrupa todas as configurações da execução.

    - HistoricoMovimento:
        Representa cada movimento processado.

    - Estatisticas:
        Armazena informações quantitativas da execução.

    - ResultadoExecucao:
        Representa o resultado completo da simulação.


* Princípios utilizados

    - Separação entre domínio e infraestrutura;
    - Uso de dataclasses;
    - Objetos imutáveis quando possível;
    - Baixo acoplamento;
    - Alta coesão.
"""


from dataclasses import dataclass, field

from roboLibrary.enumeradores import ResultadoMovimento


# --------------------------------------------------------------------------------------------------
# Representa uma posição no plano cartesiano.
@dataclass(slots=True)
class Posicao:
    x: int
    y: int


# --------------------------------------------------------------------------------------------------
# Representa os limites do plano cartesiano.
@dataclass(slots=True)
class Plano:
    xMinimo: int
    xMaximo: int
    yMinimo: int
    yMaximo: int


# --------------------------------------------------------------------------------------------------
# Representa o robô durante a simulação.
@dataclass(slots=True)
class Robo:
    posicaoInicial: Posicao
    posicaoAtual  : Posicao
    passo         : int


# --------------------------------------------------------------------------------------------------
# Representa a sequência de movimentos informada.
@dataclass(slots=True)
class SequenciaMovimentos:
    original   : str
    normalizada: str


# --------------------------------------------------------------------------------------------------
# Representa toda a configuração da simulação.
@dataclass(slots=True)
class Configuracao:
    plano     : Plano
    robo      : Robo
    movimentos: SequenciaMovimentos


# --------------------------------------------------------------------------------------------------
# Representa um movimento individual executado.
@dataclass(slots=True)
class HistoricoMovimento:
    numero            : int
    comandoOriginal   : str
    comandoNormalizado: str
    origem            : Posicao
    destinoPretendido : Posicao
    destinoFinal      : Posicao
    resultado         : ResultadoMovimento
    colisao           : bool


# --------------------------------------------------------------------------------------------------
# Representa as estatísticas da execução.
@dataclass(slots=True)
class Estatisticas:
    quantidadeMovimentosInformados: int = 0
    quantidadeMovimentosValidos   : int = 0
    quantidadeMovimentosInvalidos : int = 0
    quantidadeColisoes            : int = 0
    percentualMovimentosValidos   : float = 0.0
    percentualMovimentosInvalidos : float = 0.0
    movimentosValidos             : list[str] = field(default_factory=list)
    movimentosInvalidos           : list[str] = field(default_factory=list)


# --------------------------------------------------------------------------------------------------
# Representa o resultado completo da execução.
@dataclass(slots=True)
class ResultadoExecucao:
    configuracao: Configuracao
    posicaoFinal: Posicao
    estatisticas: Estatisticas
    historico   : list[HistoricoMovimento] = field(default_factory=list)