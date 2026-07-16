"""
Projeto : Robô Cartesiano
Arquivo : enumeradores.py
Descrição : Enumerações utilizadas pelo projeto.
Autor : Charles Cesar Magno de Freitas
Licença : MIT


* Responsabilidade do módulo

    Este módulo contém as enumerações utilizadas pelo domínio da aplicação.


* Enumerações disponíveis

    - Movimento:
        - Representa os comandos de movimentação do robô.
        - Cada movimento possui:
            - comando textual;
            - deslocamento no eixo X;
            - deslocamento no eixo Y.
    
    - ResultadoMovimento:
        - Representa o resultado da execução de um comando.

    - Eixo:
        - Representa os eixos do plano cartesiano.


* Convenções adotadas

    - Os comandos seguem o padrão definido no arquivo robo_input.ini.
    - Coordenadas utilizam o sistema cartesiano tradicional.
    - Movimentos diagonais possuem alteração simultânea nos eixos X e Y.


* Mapeamento dos movimentos

             N
             |
        Q    |    E
             |
    O -------+------- L
             |
        Z    |    C
             |
             S

"""


from enum import Enum


# --------------------------------------------------------------------------------------------------
# Representa os movimentos possíveis do robô.
class Movimento(Enum):

    NORTE    = ("N", 0, 1)
    SUL      = ("S", 0, -1)
    LESTE    = ("L", 1, 0)
    OESTE    = ("O", -1, 0)
    NOROESTE = ("Q", -1, 1)
    NORDESTE = ("E", 1, 1)
    SUDOESTE = ("Z", -1, -1)
    SUDESTE  = ("C", 1, -1)

    # Inicializa os atributos do movimento.
    def __init__(self, comando: str, deltaX: int, deltaY: int) -> None:
        self._comando = comando
        self._deltaX = deltaX
        self._deltaY = deltaY

    # Retorna o comando textual do movimento.
    @property
    def value(self) -> str:
        return self._comando

    # Retorna o deslocamento no eixo X.
    @property
    def deltaX(self) -> int:
        return self._deltaX

    # Retorna o deslocamento no eixo Y.
    @property
    def deltaY(self) -> int:
        return self._deltaY


# --------------------------------------------------------------------------------------------------
# Representa o resultado da execução de um movimento.
class ResultadoMovimento(Enum):

    REALIZADO = "REALIZADO"
    COLISAO   = "COLISAO"
    INVALIDO  = "INVALIDO"


# --------------------------------------------------------------------------------------------------
# Representa os eixos do plano cartesiano.
class Eixo(Enum):

    X = "X"
    Y = "Y"