"""
Projeto.....: Calculadora de Sub-redes IPv4
Arquivo.....: funcoesArquivo.py
Descrição...: Funções responsáveis pela geração dos arquivos de saída.
Autor.......: Charles Freitas
Licença.....: MIT
"""

import json

from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from src import configuracoes

from src.excecoes import ArquivoResultadoError
from src.modelos import InformacoesRede, SubRede


# --------------------------------------------------------------------------------------------------------------
# Cria o diretório onde serão gravados os resultados.
def _criarDiretorioResultados() -> Path:

    objDiretorio = (configuracoes.DIRETORIO_RAIZ / configuracoes.DIRETORIO_RESULTADOS)

    objDiretorio.mkdir(parents=True, exist_ok=True)

    return objDiretorio


# --------------------------------------------------------------------------------------------------------------
# Gera um nome único para o arquivo JSON.
def _gerarNomeArquivo() -> str:

    return datetime.now().strftime(configuracoes.FORMATO_NOME_JSON)


# --------------------------------------------------------------------------------------------------------------
# Obtém o caminho completo do arquivo JSON.
def _obterCaminhoArquivo() -> Path:

    objDiretorio   = _criarDiretorioResultados()
    strNomeArquivo = _gerarNomeArquivo()

    return objDiretorio / strNomeArquivo


# --------------------------------------------------------------------------------------------------------------
# Converte as informações da rede para dicionário.
def _converterInformacoesRedeParaDicionario(objInformacoesRede: InformacoesRede) -> dict:

    return asdict(objInformacoesRede)


# --------------------------------------------------------------------------------------------------------------
# Converte uma lista de objetos SubRede para uma lista de dicionários.
def _converterSubRedesParaDicionarios(lstSubRedes: list[SubRede]) -> list[dict]:

    return [asdict(objSubRede) for objSubRede in lstSubRedes]


# --------------------------------------------------------------------------------------------------------------
# Monta a estrutura final do arquivo JSON.
def _montarDadosJSON(objInformacoesRede: InformacoesRede, lstSubRedes: list[SubRede]) -> dict:

    return {"data_hora"       : datetime.now().isoformat(),
            "informacoes_rede": _converterInformacoesRedeParaDicionario(objInformacoesRede),
            "subredes"        : _converterSubRedesParaDicionarios(lstSubRedes)
            }


# --------------------------------------------------------------------------------------------------------------
# Grava os dados em um arquivo JSON.
def _salvarArquivoJSON(objArquivo: Path, dictDados: dict) -> bool:

    try:
        with objArquivo.open(mode="w", encoding=configuracoes.JSON_ENCODING) as objArquivoJSON:
            json.dump(dictDados, objArquivoJSON, 
                      indent=configuracoes.JSON_INDENTACAO, ensure_ascii=configuracoes.JSON_ASCII)
    except OSError as erro:
        raise ArquivoResultadoError(f"Erro ao gravar o arquivo \"{objArquivo.name}\": {erro}")

    return True


# --------------------------------------------------------------------------------------------------------------
# Salva os resultados da aplicação em formato JSON.
def salvarResultadosJSON(objInformacoesRede: InformacoesRede, lstSubRedes: list[SubRede]) -> bool:

    objArquivo = _obterCaminhoArquivo()
    dictDados  = _montarDadosJSON(objInformacoesRede, lstSubRedes)

    _salvarArquivoJSON(objArquivo, dictDados)

    return True