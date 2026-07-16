"""
Projeto : Robô Cartesiano
Arquivo : configuracoes.py
Descrição : Configurações gerais do projeto.
Autor : Charles Cesar Magno de Freitas
Licença : MIT
"""

from pathlib import Path


# --------------------------------------------------------------------------------------------------
# DIRETÓRIOS

# Diretório raiz do projeto.
DIRETORIO_PROJETO    = Path(__file__).resolve().parent.parent  

# Diretório destinado aos arquivos gerados pela aplicação."""
DIRETORIO_RESULTADOS = (DIRETORIO_PROJETO / "resultados").resolve() 


# --------------------------------------------------------------------------------------------------
# ARQUIVOS

# Arquivo de configuração da simulação.
ARQUIVO_INPUT = (DIRETORIO_PROJETO / "robo_input.ini").resolve()

# Arquivo contendo o relatório da execução.
ARQUIVO_OUTPUT = (DIRETORIO_RESULTADOS / "robo_output.txt").resolve()


# --------------------------------------------------------------------------------------------------
# CODIFICAÇÃO

# Codificação utilizada na leitura e gravação dos arquivos.
ENCODING_ARQUIVOS = "utf-8"


# --------------------------------------------------------------------------------------------------
# EXTENSÕES PADRÃO

# Extensão do arquivo de configuração.
EXTENSAO_ARQUIVO_CONFIGURACAO = ".ini"

# Extensão do relatório gerado.
EXTENSAO_ARQUIVO_RELATORIO = ".txt"
