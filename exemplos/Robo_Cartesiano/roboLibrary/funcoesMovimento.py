"""
Projeto : Robô Cartesiano
Arquivo : funcoesMovimento.py
Descrição : Execução da movimentação do robô no plano cartesiano.
Autor : Charles Cesar Magno de Freitas
Licença : MIT


* Responsabilidade do módulo

    Este módulo contém toda a lógica de movimentação do robô dentro do
    plano cartesiano.


* Responsabilidades

    Este módulo é responsável por:

        - Interpretar comandos de movimentação;
        - Converter comandos em movimentos válidos;
        - Calcular deslocamentos;
        - Calcular posições pretendidas;
        - Verificar colisões com os limites do plano;
        - Atualizar a posição atual do robô;
        - Registrar histórico das movimentações;
        - Atualizar estatísticas da execução.


* Não é responsabilidade deste módulo:

        - Ler arquivos de configuração;
        - Validar parâmetros iniciais;
        - Gerar arquivos de relatório;
        - Controlar o programa principal.


* Fluxo principal

            executarMovimentos()
                    ↓
        Percorrer sequência de comandos
                    ↓
            _obterMovimento()
                    |
            +────────────────────+
            |                    |
        Inválido               Válido
            ↓                    ↓
        Registrar        _calcularDestino()
                                 ↓
                        _verificarColisao()
                                 |
                         +───────+───────+
                         |               |
                      Colisão          Livre
                         ↓               ↓
                  Mantém posição   Atualiza robô
                         |               |
                         +───────+───────+
                                 ↓
                        _registrarMovimento()
                                 ↓
                      _atualizarEstatisticas()


* Princípios utilizados

    - Responsabilidade Única (SRP);
    - Separação entre regras e infraestrutura;
    - Uso de modelos de domínio;
    - Uso de Enum para comandos;
    - Histórico protegido através de cópias das posições.


* Função pública

    executarMovimentos()


* Funções privadas

    _obterMovimento()
    _calcularDestino()
    _verificarColisao()
    _registrarMovimento()
    _atualizarEstatisticas()
"""

from __future__ import annotations

from roboLibrary.enumeradores import (Movimento, ResultadoMovimento)

from roboLibrary.modelos import (Configuracao, Estatisticas, HistoricoMovimento, 
                                 Plano, Posicao, ResultadoExecucao, Robo)


# --------------------------------------------------------------------------------------------------
# Obtém o movimento correspondente ao comando informado.
def _obterMovimento(comando: str) -> Movimento | None:
    comandoNormalizado = comando.upper()

    for movimento in Movimento:
        if movimento.value == comandoNormalizado:
            return movimento

    return None


# --------------------------------------------------------------------------------------------------
# Calcula a posição pretendida após executar um movimento.
# O deslocamento utilizado é obtido através do atributo passo configurado no robô.
def _calcularDestino(robo: Robo, movimento: Movimento) -> Posicao:
    novaPosicaoX = (robo.posicaoAtual.x + (movimento.deltaX * robo.passo))
    novaPosicaoY = (robo.posicaoAtual.y + (movimento.deltaY * robo.passo))

    return Posicao(x=novaPosicaoX, y=novaPosicaoY)


# --------------------------------------------------------------------------------------------------
# Verifica se a posição pretendida ultrapassa os limites definidos pelo plano cartesiano.
def _verificarColisao(plano: Plano, destino: Posicao) -> bool:
    if destino.x < plano.xMinimo: return True

    if destino.x > plano.xMaximo: return True

    if destino.y < plano.yMinimo: return True

    if destino.y > plano.yMaximo: return True

    return False


# --------------------------------------------------------------------------------------------------
# Cria o registro de uma movimentação realizada.
# As posições são copiadas para garantir que o histórico permaneça imutável 
# mesmo após novas movimentações.
def _registrarMovimento(numero: int, comandoOriginal: str, comandoNormalizado: str,
                        origem: Posicao, destinoPretendido: Posicao, destinoFinal: Posicao, 
                        resultado: ResultadoMovimento, colisao: bool) -> HistoricoMovimento:

    return HistoricoMovimento(numero=numero, comandoOriginal=comandoOriginal,
                              comandoNormalizado=comandoNormalizado,
                              origem=Posicao(x=origem.x, y=origem.y),
                              destinoPretendido=Posicao(x=destinoPretendido.x, y=destinoPretendido.y),
                              destinoFinal=Posicao(x=destinoFinal.x, y=destinoFinal.y),
                              resultado=resultado, colisao=colisao)


# --------------------------------------------------------------------------------------------------
# Atualiza as estatísticas da execução após cada comando processado.
def _atualizarEstatisticas(estatisticas: Estatisticas, comando: str,
                           resultado: ResultadoMovimento, colisao: bool) -> None:
    estatisticas.quantidadeMovimentosInformados += 1

    if resultado == ResultadoMovimento.INVALIDO:
        estatisticas.quantidadeMovimentosInvalidos += 1
        estatisticas.movimentosInvalidos.append(comando)
    elif resultado == ResultadoMovimento.REALIZADO:
        estatisticas.quantidadeMovimentosValidos += 1
        estatisticas.movimentosValidos.append(comando)
    elif resultado == ResultadoMovimento.COLISAO:
        estatisticas.quantidadeMovimentosValidos += 1
        estatisticas.movimentosValidos.append(comando)


    if colisao: estatisticas.quantidadeColisoes += 1

    totalMovimentos = (estatisticas.quantidadeMovimentosInformados)

    if totalMovimentos > 0:
        estatisticas.percentualMovimentosValidos   = (estatisticas.quantidadeMovimentosValidos / 
                                                      totalMovimentos * 100)
        estatisticas.percentualMovimentosInvalidos = (estatisticas.quantidadeMovimentosInvalidos / 
                                                      totalMovimentos * 100)


# --------------------------------------------------------------------------------------------------
# Executa toda a sequência de movimentos do robô.
def executarMovimentos(configuracao: Configuracao) -> ResultadoExecucao:
    robo      = configuracao.robo
    plano     = configuracao.plano
    sequencia = configuracao.movimentos.normalizada

    estatisticas = Estatisticas()

    historico: list[HistoricoMovimento] = list()

    for numero, comando in enumerate(sequencia, start=1):
        origem             = Posicao(x=robo.posicaoAtual.x, y=robo.posicaoAtual.y)
        movimento          = _obterMovimento(comando)
        comandoNormalizado = comando.upper()

        if movimento is None: # Movimento inválido
            resultado         = ResultadoMovimento.INVALIDO
            destinoPretendido = Posicao(x=origem.x, y=origem.y)
            destinoFinal      = Posicao(x=origem.x, y=origem.y)
            colisao           = False
        else: # Movimento válido
            destinoPretendido = _calcularDestino(robo, movimento)
            colisao           = _verificarColisao(plano,destinoPretendido)

            if colisao: # Colisão com limite do plano
                resultado    = ResultadoMovimento.COLISAO
                destinoFinal = Posicao(x=origem.x, y=origem.y)
            else: # Movimento realizado
                resultado         = ResultadoMovimento.REALIZADO
                robo.posicaoAtual = Posicao(x=destinoPretendido.x, y=destinoPretendido.y)
                destinoFinal = Posicao(x=robo.posicaoAtual.x,y=robo.posicaoAtual.y)

        historicoMovimento = _registrarMovimento(numero=numero, comandoOriginal=comando,
                                                 comandoNormalizado=comandoNormalizado,
                                                 origem=origem, destinoPretendido=destinoPretendido,
                                                 destinoFinal=destinoFinal, resultado=resultado,
                                                 colisao=colisao)
        historico.append(historicoMovimento)

        _atualizarEstatisticas(estatisticas, comandoNormalizado, resultado, colisao)

    return ResultadoExecucao(configuracao=configuracao, 
                             posicaoFinal=Posicao(x=robo.posicaoAtual.x, y=robo.posicaoAtual.y),
                             estatisticas=estatisticas, historico=historico)
