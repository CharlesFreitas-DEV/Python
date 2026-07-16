"""
Projeto : Robô Cartesiano
Arquivo : funcoesArquivo.py
Descrição : Leitura do arquivo de configuração e gravação do relatório.
Autor : Charles Cesar Magno de Freitas
Licença : MIT


* Responsabilidade do módulo

    Este módulo é responsável exclusivamente pelas operações de entrada e saída
    de arquivos da aplicação.


* Funcionalidades

    - Leitura:
        - Localização do arquivo robo_input.ini;
        - Abertura do arquivo INI;
        - Leitura das configurações;
        - Conversão dos tipos;
        - Construção dos objetos de domínio.

    - Escrita:
        - Gravação do relatório final.


* Não é responsabilidade deste módulo:

    - Validar regras de negócio;
    - Executar movimentações;
    - Gerar estatísticas;
    - Criar relatórios.


* Fluxo principal

    lerConfiguracao()
        |
        ├── _abrirArquivoConfiguracao()
        |
        ├── _criarConfiguracao()
                |
                ├── _criarPlano()
                |
                ├── _criarRobo()
                |
                └── _criarSequenciaMovimentos()


    gravarRelatorio()
        |
        ├── Criar diretório de saída
        |
        └── Escrever arquivo texto


* Princípios utilizados

    - Responsabilidade Única (SRP);
    - Alta coesão;
    - Baixo acoplamento;
    - Separação entre infraestrutura e regras de negócio.
"""


from __future__ import annotations

from configparser import (ConfigParser, SectionProxy)

from pathlib import Path

from roboLibrary.configuracoes import (ARQUIVO_INPUT, ARQUIVO_OUTPUT, ENCODING_ARQUIVOS)

from roboLibrary.constantes import (PARAMETRO_PASSO,
                                    PARAMETRO_POSICAO_INICIAL_X, PARAMETRO_POSICAO_INICIAL_Y,
                                    PARAMETRO_SEQUENCIA,
                                    PARAMETRO_X_MAXIMO, PARAMETRO_X_MINIMO,
                                    PARAMETRO_Y_MAXIMO, PARAMETRO_Y_MINIMO,
                                    SECAO_MOVIMENTOS, SECAO_PLANO, SECAO_ROBO)

from roboLibrary.excecoes import (ArquivoConfiguracaoNaoEncontradoException,
                                  ArquivoConfiguracaoInvalidoException,
                                  GravacaoRelatorioException,
                                  ParametroObrigatorioNaoEncontradoException,
                                  SecaoObrigatoriaNaoEncontradaException)

from roboLibrary.modelos import (Configuracao, Plano, Posicao, Robo, SequenciaMovimentos)

from roboLibrary.funcoesValidacao import (validarConfiguracao)


# --------------------------------------------------------------------------------------------------
# Localiza o arquivo de configuração da aplicação.
def _localizarArquivoConfiguracao() -> Path:
    caminhoArquivo = Path(ARQUIVO_INPUT)

    if not caminhoArquivo.exists():
        raise ArquivoConfiguracaoNaoEncontradoException(f"Arquivo de configuração não encontrado: {caminhoArquivo}")

    if not caminhoArquivo.is_file():
        raise ArquivoConfiguracaoNaoEncontradoException(f"O caminho informado não corresponde a um arquivo: {caminhoArquivo}")

    return caminhoArquivo


# --------------------------------------------------------------------------------------------------
# Abre e realiza a leitura do arquivo INI.
def _abrirArquivoConfiguracao() -> ConfigParser:
    parser         = ConfigParser(inline_comment_prefixes=(";", "#"), empty_lines_in_values=False)
    caminhoArquivo = _localizarArquivoConfiguracao()

    try:
        with caminhoArquivo.open(mode="r", encoding=ENCODING_ARQUIVOS) as arquivo:
            parser.read_file(arquivo)
    except OSError as erro:
        raise ArquivoConfiguracaoInvalidoException(f"Erro ao ler arquivo de configuração: {erro}") from erro

    return parser


# --------------------------------------------------------------------------------------------------
# Obtém uma seção obrigatória do arquivo INI.
def _obterSecao(parser: ConfigParser, nomeSecao: str) -> SectionProxy:
    if nomeSecao not in parser:
        raise SecaoObrigatoriaNaoEncontradaException(f"Seção obrigatória não encontrada: [{nomeSecao}]")

    return parser[nomeSecao]


# --------------------------------------------------------------------------------------------------
# Obtém um parâmetro obrigatório dentro de uma seção.
def _obterValor(secao: SectionProxy, nomeParametro: str) -> str:
    if nomeParametro not in secao:
        raise ParametroObrigatorioNaoEncontradoException(f"Parâmetro obrigatório '{nomeParametro}' "
                                                         f"não encontrado na seção [{secao.name}]")

    return secao[nomeParametro]


# --------------------------------------------------------------------------------------------------
# Converte uma string para inteiro.
def _converterInteiro(valor: str, descricao: str) -> int:
    try:
        return int(valor)
    except ValueError as erro:
        raise ArquivoConfiguracaoInvalidoException(f"O parâmetro '{descricao}' deve possuir valor inteiro.") from erro


# --------------------------------------------------------------------------------------------------
# Normaliza a sequência de movimentos.
def _normalizarSequencia(sequencia: str) -> str:
    return sequencia.strip().upper()


# --------------------------------------------------------------------------------------------------
# Cria o objeto Plano a partir das informações do arquivo INI.
def _criarPlano(parser: ConfigParser) -> Plano:
    secaoPlano = _obterSecao(parser, SECAO_PLANO)
    xMinimo    = _converterInteiro(_obterValor(secaoPlano, PARAMETRO_X_MINIMO), PARAMETRO_X_MINIMO)
    xMaximo    = _converterInteiro(_obterValor(secaoPlano, PARAMETRO_X_MAXIMO), PARAMETRO_X_MAXIMO)
    yMinimo    = _converterInteiro(_obterValor(secaoPlano, PARAMETRO_Y_MINIMO), PARAMETRO_Y_MINIMO)
    yMaximo    = _converterInteiro(_obterValor(secaoPlano, PARAMETRO_Y_MAXIMO), PARAMETRO_Y_MAXIMO)

    return Plano(xMinimo=xMinimo, xMaximo=xMaximo, yMinimo=yMinimo, yMaximo=yMaximo)


# --------------------------------------------------------------------------------------------------
# Cria o objeto Robo a partir das informações do arquivo INI.
def _criarRobo(parser: ConfigParser) -> Robo:
    secaoRobo = _obterSecao(parser, SECAO_ROBO)
    xInicial  = _converterInteiro(_obterValor(secaoRobo, PARAMETRO_POSICAO_INICIAL_X), PARAMETRO_POSICAO_INICIAL_X)
    yInicial  = _converterInteiro(_obterValor(secaoRobo, PARAMETRO_POSICAO_INICIAL_Y), PARAMETRO_POSICAO_INICIAL_Y)
    passo     = _converterInteiro(_obterValor(secaoRobo, PARAMETRO_PASSO), PARAMETRO_PASSO)

    posicaoInicial = Posicao(x=xInicial, y=yInicial)
    posicaoAtual   = Posicao(x=xInicial, y=yInicial)

    return Robo(posicaoInicial=posicaoInicial, posicaoAtual=posicaoAtual, passo=passo)


# --------------------------------------------------------------------------------------------------
# Obtém e normaliza a sequência de movimentos.
def _criarSequenciaMovimentos(parser: ConfigParser) -> str:
    secaoMovimentos   = _obterSecao(parser, SECAO_MOVIMENTOS)
    sequenciaOriginal = _obterValor(secaoMovimentos, PARAMETRO_SEQUENCIA)

    return SequenciaMovimentos(original=sequenciaOriginal, 
                               normalizada=_normalizarSequencia(sequenciaOriginal))


# --------------------------------------------------------------------------------------------------
# Cria o objeto Configuracao completo da aplicação.
def _criarConfiguracao(parser: ConfigParser) -> Configuracao:
    plano      = _criarPlano(parser)
    robo       = _criarRobo(parser)
    movimentos = _criarSequenciaMovimentos(parser)

    return Configuracao(plano=plano, robo=robo, movimentos=movimentos)


# --------------------------------------------------------------------------------------------------
# Realiza a leitura completa do arquivo de configuração.
def lerConfiguracao() -> Configuracao:
    parser       = _abrirArquivoConfiguracao()
    configuracao = _criarConfiguracao(parser)

    validarConfiguracao(configuracao)

    return configuracao


# --------------------------------------------------------------------------------------------------
# Grava o relatório da execução em arquivo texto.
def gravarRelatorio(relatorio: str, caminhoArquivo: Path | None = None) -> None:
    if not isinstance(relatorio, str):
        raise TypeError("O relatório deve ser uma string.")

    if caminhoArquivo is None:
        caminhoArquivo = Path(ARQUIVO_OUTPUT)

    try:
        caminhoArquivo.parent.mkdir(parents=True, exist_ok=True)
        with caminhoArquivo.open(mode="w", encoding=ENCODING_ARQUIVOS) as arquivo:
            arquivo.write(relatorio)
    except OSError as erro:
        raise GravacaoRelatorioException(f"Erro ao gravar o relatório: {caminhoArquivo}") from erro