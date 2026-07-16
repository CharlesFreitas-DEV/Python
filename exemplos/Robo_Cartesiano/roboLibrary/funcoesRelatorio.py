"""
Projeto : Robô Cartesiano
Arquivo : funcoesRelatorio.py
Descrição : Geração dos relatórios da simulação do robô cartesiano.
Autor : Charles Cesar Magno de Freitas
Licença : MIT


* Responsabilidade do módulo

    Este módulo é responsável exclusivamente pela apresentação textual
    dos resultados da simulação.


* Responsabilidades

    - Formatar informações da configuração;
    - Apresentar posição final;
    - Exibir estatísticas;
    - Exibir histórico completo.


* Não é responsabilidade deste módulo:

    - Ler arquivos;
    - Executar movimentos;
    - Calcular estatísticas;
    - Alterar objetos recebidos.


* Princípios utilizados

    - Responsabilidade Única;
    - Baixo acoplamento;
    - Alta coesão;
    - Separação entre domínio e apresentação.
"""


from roboLibrary.modelos import (Configuracao, Posicao, ResultadoExecucao)


# --------------------------------------------------------------------------------------------------
# Formata uma posição cartesiana.
def _formatarPosicao(posicao: Posicao) -> str:
    return (f"({posicao.x}, {posicao.y})")


# --------------------------------------------------------------------------------------------------
# Gera o cabeçalho do relatório.
def _gerarCabecalho() -> str:
    return ("\n"
            "==================================================\n"
            "          SIMULAÇÃO DO ROBÔ CARTESIANO\n"
            "==================================================\n")


# --------------------------------------------------------------------------------------------------
# Gera a seção de configuração inicial.
def _gerarConfiguracaoInicial(configuracao: Configuracao) -> str:
    plano     = configuracao.plano
    robo      = configuracao.robo
    sequencia = configuracao.movimentos.original

    return ("\n"
            "CONFIGURAÇÃO INICIAL\n"
            "==================================================\n"
            "\n"
            "PLANO CARTESIANO\n"
            f"X mínimo ............: {plano.xMinimo}\n"
            f"X máximo ............: {plano.xMaximo}\n"
            f"Y mínimo ............: {plano.yMinimo}\n"
            f"Y máximo ............: {plano.yMaximo}\n"
            "\n"
            "ROBÔ\n"
            f"Posição inicial .....: "
            f"{_formatarPosicao(robo.posicaoInicial)}\n"
            f"Passo de movimento .: {robo.passo}\n"
            "\n"
            "SEQUÊNCIA INFORMADA\n"
            f"{sequencia}\n")


# --------------------------------------------------------------------------------------------------
# Gera o resumo estatístico da execução.
def _gerarResumoEstatistico(resultado: ResultadoExecucao) -> str:
    estatisticas        = resultado.estatisticas
    movimentosValidos   = ", ".join(estatisticas.movimentosValidos)
    movimentosInvalidos = ", ".join(estatisticas.movimentosInvalidos)

    return ("\n"
            "RESUMO ESTATÍSTICO\n"
            "==================================================\n"
            "\n"
            f"Movimentos informados .: "
            f"{estatisticas.quantidadeMovimentosInformados}\n"
            f"Movimentos realizados .: "
            f"{estatisticas.quantidadeMovimentosValidos}\n"
            f"Movimentos inválidos ..: "
            f"{estatisticas.quantidadeMovimentosInvalidos}\n"
            f"Colisões ..............: "
            f"{estatisticas.quantidadeColisoes}\n"
            "\n"
            f"Percentual realizado ..: "
            f"{estatisticas.percentualMovimentosValidos:.2f}%\n"
            f"Percentual inválido ...: "
            f"{estatisticas.percentualMovimentosInvalidos:.2f}%\n"
            "\n"
            f"Movimentos realizados .: "
            f"{movimentosValidos}\n"
            f"Movimentos inválidos ..: "
            f"{movimentosInvalidos}\n")


# --------------------------------------------------------------------------------------------------
# Gera a seção de histórico das movimentações.
def _gerarHistorico(resultado: ResultadoExecucao) -> str:
    linhas = list()
    linhas.append("\n"
                  "HISTÓRICO DE MOVIMENTAÇÕES\n"
                  "==================================================\n")

    if not resultado.historico:
        linhas.append("\nNenhuma movimentação foi executada.\n")
        return "".join(linhas)

    for movimento in resultado.historico:
        linhas.append("\n")
        linhas.append(f"Movimento {movimento.numero:03d}\n")
        linhas.append("--------------------------------------------------\n")
        linhas.append(f"Comando original ....: "
                      f"{movimento.comandoOriginal}\n")
        linhas.append(f"Comando normalizado .: "
                      f"{movimento.comandoNormalizado}\n")
        linhas.append(f"Origem ..............: "
                      f"{_formatarPosicao(movimento.origem)}\n")
        linhas.append(f"Destino pretendido ..: "
                      f"{_formatarPosicao(movimento.destinoPretendido)}\n")
        linhas.append(f"Destino final .......: "
                      f"{_formatarPosicao(movimento.destinoFinal)}\n")
        linhas.append(f"Resultado ...........: "
                      f"{movimento.resultado.name}\n")
        linhas.append(f"Colisão .............: "
                      f"{'SIM' if movimento.colisao else 'NÃO'}\n")

    return "".join(linhas)


# --------------------------------------------------------------------------------------------------
# Gera o relatório completo da execução do robô.
def gerarRelatorio(resultado: ResultadoExecucao) -> str:

    if not isinstance(resultado, ResultadoExecucao):
        raise TypeError("resultado deve ser do tipo ResultadoExecucao.")

    secoes = list()
    secoes.append(_gerarCabecalho())
    secoes.append(_gerarConfiguracaoInicial(resultado.configuracao))

    secoes.append("\n"
                  "POSIÇÃO FINAL DO ROBÔ\n"
                  "==================================================\n"
                  "\n"
                  f"{_formatarPosicao(resultado.posicaoFinal)}\n"
                  )

    secoes.append(_gerarResumoEstatistico(resultado))
    secoes.append(_gerarHistorico(resultado))

    return "".join(secoes)