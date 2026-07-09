"""
Projeto.....: Calculadora de Sub-redes IPv4
Arquivo.....: configuracoes.py
Descrição...: Carrega as configurações da aplicação e os dados de entrada.
Autor.......: Charles Freitas
Licença.....: MIT
"""

import configparser

from pathlib import Path

from src.excecoes import ConfiguracaoError
from src.modelos import InformacoesRede


# --------------------------------------------------------------------------------------------------------------
# Diretório raiz do projeto.
DIRETORIO_RAIZ = Path(__file__).parent.parent


# --------------------------------------------------------------------------------------------------------------
# Arquivos de configuração da aplicação.
ARQUIVO_CONFIGURACAO = DIRETORIO_RAIZ / "config.ini"
ARQUIVO_REDE         = DIRETORIO_RAIZ / "info_rede.ini"


# --------------------------------------------------------------------------------------------------------------
# Carrega um arquivo de configuração.
def _carregarArquivoConfiguracao(objArquivo: Path) -> configparser.ConfigParser:

    if not objArquivo.exists():
        raise ConfiguracaoError(f"O arquivo \"{objArquivo.name}\" não foi encontrado.")

    objConfiguracoes = configparser.ConfigParser(interpolation=None)

    objConfiguracoes.read(objArquivo, encoding="utf-8")

    return objConfiguracoes


# --------------------------------------------------------------------------------------------------------------
# Arquivos de configuração carregados.
_CONFIG = _carregarArquivoConfiguracao(ARQUIVO_CONFIGURACAO)    # Configurações do programa
_REDE   = _carregarArquivoConfiguracao(ARQUIVO_REDE)            # Dados iniciais da rede


# --------------------------------------------------------------------------------------------------------------
# Configurações da aplicação.
DIRETORIO_RESULTADOS = _CONFIG.get("ARQUIVOS", "DIRETORIO_RESULTADOS")  # Diretório onde serão gravados os arquivos de saída.
FORMATO_NOME_JSON    = _CONFIG.get("ARQUIVOS", "FORMATO_NOME_JSON")     # Formato do nome do arquivo JSON.
JSON_ENCODING        = _CONFIG.get("ARQUIVOS", "JSON_ENCODING")         # Codificação utilizada na gravação do JSON.
JSON_INDENTACAO      = _CONFIG.getint("ARQUIVOS","JSON_INDENTACAO")     # Quantidade de espaços utilizados na identação do JSON
JSON_ASCII           = _CONFIG.getboolean("ARQUIVOS","JSON_ASCII")      # Define se os caracteres Unicode serão convertidos para ASCII


# --------------------------------------------------------------------------------------------------------------
# Obtém as informações da rede.
def obterInformacoesRede() -> InformacoesRede:

    return InformacoesRede(strEnderecoIP     = _REDE.get("REDE", "ENDERECO_IP"),
                           intMascaraInicial = _REDE.getint("REDE", "MASCARA_INICIAL"),
                           intMascaraFinal   = _REDE.getint("REDE", "MASCARA_FINAL")
                           )