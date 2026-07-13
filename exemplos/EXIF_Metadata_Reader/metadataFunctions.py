from typing import List

# ----------------------------------------------------------------------
# Função para ler uma string ASCII a partir de um offset.
def lerDadosASCII(file_handle, offset: int, num_components: int, code_page: str, base_offset:int = 0) -> str:
    # Salva a posição atual do arquivo para que ela possa ser restaurada
    # após a leitura do dado localizado em outro ponto do arquivo.
    current_pos = file_handle.tell()
    # O offset armazenado na estrutura EXIF é relativo ao início do
    # cabeçalho TIFF. Por isso é necessário acrescentar 12 bytes,
    # correspondentes ao início do bloco EXIF.
    file_handle.seek(base_offset + offset + 12)
    val = file_handle.read(num_components).decode(code_page).rstrip('\x00')
    file_handle.seek(current_pos)
    return val


# ----------------------------------------------------------------------
# Função para ler ou mais valores no formato RATIONAL (numerador/denominador)
# e retornar uma lista de números float.
def lerDadosRational(file_handle, offset: int, num_components: int, byte_order: str, base_offset:int = 0) -> List[float]:
    # Guarda a posição atual para que a função seja transparente,
    # ou seja, não altere a posição do cursor para quem a chamou.
    current_pos = file_handle.tell()
    file_handle.seek(base_offset + offset + 12)
    
    valores = list()

    # Cada valor RATIONAL é armazenado por dois inteiros sem sinal de 32 bits: numerador e denominador.
    for _ in range(num_components):
        numerador   = int.from_bytes(file_handle.read(4), byteorder=byte_order)
        denominador = int.from_bytes(file_handle.read(4), byteorder=byte_order)
        if denominador == 0:
            valores.append(0.0)
        else:
            valores.append(numerador / denominador)
            
    file_handle.seek(current_pos)
    return valores


# ----------------------------------------------------------------------
# Função para converter graus, minutos e segundos em graus decimais
def converterGrausDecimais(graus_min_seg: List[float], ref: str) -> float:
    if len(graus_min_seg) != 3:
        return 0.0

    # O padrão EXIF armazena coordenadas geográficas no formato Graus, Minutos e Segundos (DMS).        
    graus    = graus_min_seg[0]
    minutos  = graus_min_seg[1]
    segundos = graus_min_seg[2]
    
    # Conversão de Graus, Minutos e Segundos (DMS) para Graus Decimais (Decimal Degrees).
    decimal_degrees = graus + (minutos / 60.0) + (segundos / 3600.0)
    
    # Coordenadas localizadas ao Sul ou Oeste são representadas por valores negativos.
    if ref in ['S', 'W']:
        return -decimal_degrees
    
    return decimal_degrees


