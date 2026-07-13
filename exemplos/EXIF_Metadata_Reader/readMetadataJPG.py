import sys

from metadataFunctions import *

from metadataConstants import *

# ------------------------------------------------------------------------------------------
# Nome do arquivo JPG a ser lido
strNomeArquivo = os.path.join(DIR_IMG, "presepio_natalino.jpg")


# ------------------------------------------------------------------------------------------
try:
    fileInput = open(strNomeArquivo, "rb")
except FileNotFoundError:
    sys.exit("\nERRO: Arquivo Não Existe...\n")
except Exception as erro:
    sys.exit(f"\nERRO: {erro}...\n")
else:
    # Todo arquivo JPEG inicia com o marcador SOI (Start Of Image).
    # Em seguida deve existir o segmento APP1 contendo o cabeçalho EXIF.
    if fileInput.read(2) != JPG_HEADER:
        fileInput.close()
        sys.exit("\nERRO: Arquivo informado não é JPG...\n")

    # Verificando se existe um segmento EXIF (APP1).
    # Um arquivo JPG pode conter metadados em outros formatos,
    # mas este programa interpreta apenas metadados EXIF.
    if fileInput.read(2) != EXIF_HEADER:
        fileInput.close()
        sys.exit("\nAVISO: Este arquivo não possui metadados...\n")

    # Obtendo o header do EXIF
    exifSize      = fileInput.read(2)  # Leitura sequencial do cabeçalho EXIF/TIFF.
                                       # A ordem dos bytes segue exatamente a especificação EXIF.
    exifHeader    = fileInput.read(4)  # EXIF Header (marcador EXIF)
    temp1         = fileInput.read(2)  # EXIF Header (fixo)
    endianHeader  = fileInput.read(2)  # Endian do arquivo (Big ou Little)
    temp2         = fileInput.read(2)  # TIFF Header (fixo)
    temp3         = fileInput.read(4)  # TIFF Header (fixo)
    countMetadata = fileInput.read(2)  # Metadata Count

    # Todos os valores numéricos lidos a partir deste ponto deverão respeitar
    # a ordem de bytes (Little Endian ou Big Endian) definida pelo cabeçalho TIFF.
    # (49 49: Little Endian - Intel / 4D 4D: Big Endian - Motorola)
    strOrderByte = "little" if endianHeader == b"\x49\x49" else "big"
    exifSize = int.from_bytes(exifSize, byteorder=strOrderByte)
    countMetadata = int.from_bytes(countMetadata, byteorder=strOrderByte)

    # Montando o dicionário do header do EXIF
    lstDadosEXIF = [ exifSize, exifHeader, temp1, endianHeader, temp2, temp3, countMetadata ]

    dictEXIF = dict(zip(HEADER_EXIF, lstDadosEXIF))

    # Variável para armazenar o offset do subdiretório de dados de GPS (TAG 0x8825)
    intGPSInfoOffset = None

    # A IFD principal contém todos os metadados do arquivo,
    # exceto aqueles armazenados em subdiretórios específicos,
    # como GPS, EXIF Interoperability e Maker Notes.
    lstMetadata = list()

    # Cada entrada (IFD Entry) possui exatamente 12 bytes:
    #    TAG (2) + Formato (2) + Nº Componentes (4) + Valor/Offset (4)
    for _ in range(countMetadata):
        # Identificador do Metadado
        idTAGNumber      = int.from_bytes(fileInput.read(2), byteorder=strOrderByte)
        strTagNumber     = TAG_NUMBER.get(idTAGNumber, "Unknown Tag")

        # Formato do Metadado
        idDataFormat     = int.from_bytes(fileInput.read(2), byteorder=strOrderByte)
        strDataFormat    = DATA_FORMAT.get(idDataFormat, "Unknown Format")

        # Número de Componentes do Metadado
        numberComponents = int.from_bytes(fileInput.read(4), byteorder=strOrderByte)

        # Dependendo do tamanho da informação, este campo pode armazenar:
        #   - o próprio valor do metadado; ou
        #   - um offset apontando para outra posição do arquivo.
        dataValue = int.from_bytes(fileInput.read(4), byteorder=strOrderByte)

        # A TAG 0x8825 (GPSInfo) contém o offset para o subdiretório de dados de GPS.
        if idTAGNumber == 0x8825: 
            intGPSInfoOffset = dataValue

        # Strings ASCII normalmente são armazenadas fora da IFD.
        # Nesse caso, dataValue representa um offset para o texto.
        if idDataFormat == 0x0002:
            dataValue = lerDadosASCII( fileInput, dataValue, numberComponents, CODE_PAGE )

        lstTemp = [ strTagNumber, strDataFormat, numberComponents, dataValue ]

        lstMetadata.append(dict(zip(HEADER_METADATA, lstTemp)))

    # Lendo e tratando os metadados de GPS, se existirem
    lstGpsMetadata = list()

    if intGPSInfoOffset:
        # O diretório GPS é outra IFD independente da IFD principal.
        # # A TAG 0x8825 informa onde esse diretório começa.
        fileInput.seek(intGPSInfoOffset + 12)

        countGpsMetadata = int.from_bytes(fileInput.read(2), byteorder=strOrderByte)

        # ETAPA 1: Ler todas as tags de GPS do arquivo.
        # É necessário ler todas primeiro porque o tratamento de uma tag
        # (ex: GPSLatitude) depende do valor de outra (ex: GPSLatitudeRef).
        gpsDataRaw = dict()

        # As entradas da IFD GPS possuem a mesma estrutura de 12 bytes
        # utilizada pelos metadados da IFD principal.
        for _ in range(countGpsMetadata):
            idTAGNumber = int.from_bytes(fileInput.read(2), byteorder=strOrderByte)
            strTagNumber     = GPS_TAG_NUMBER.get(idTAGNumber, "Unknown GPS Tag")

            idDataFormat     = int.from_bytes(fileInput.read(2), byteorder=strOrderByte)
            strDataFormat    = DATA_FORMAT.get(idDataFormat, "Unknown Format")

            numberComponents = int.from_bytes(fileInput.read(4), byteorder=strOrderByte)

            dataValue        = int.from_bytes(fileInput.read(4), byteorder=strOrderByte)

            # Alguns formatos (ASCII e Rational) são armazenados em outra
            # posição do arquivo e precisam ser lidos utilizando o offset.
            valorFinal = dataValue

            if strDataFormat == "ASCII String":
                valorFinal = lerDadosASCII(fileInput, dataValue, numberComponents, CODE_PAGE)
            elif strDataFormat == "Unsigned Rational":
                valorFinal = lerDadosRational(fileInput, dataValue, numberComponents, strOrderByte)

            # Armazena a "peça" bruta no dicionário de apoio
            gpsDataRaw[strTagNumber] = valorFinal

        # ETAPA 2: Imediatamente após a leitura, tratar os dados e construir a lista final.
        # Agora que temos todas as peças, podemos combiná-las.
        latRefBruto = gpsDataRaw.get("GPSLatitudeRef")
        latValor    = gpsDataRaw.get("GPSLatitude")

        lonRefBruto = gpsDataRaw.get("GPSLongitudeRef")
        lonValor    = gpsDataRaw.get("GPSLongitude")

        altRefVal   = gpsDataRaw.get("GPSAltitudeRef")
        altValor    = gpsDataRaw.get("GPSAltitude")

        timestamp   = gpsDataRaw.get("GPSTimeStamp")
        datestamp   = gpsDataRaw.get("GPSDateStamp")

        # As coordenadas GPS são armazenadas em graus, minutos e segundos.
        # Elas são convertidas para graus decimais para facilitar o uso
        # em mapas e sistemas de geolocalização.
        if latValor:
            latRef = latRefBruto if latRefBruto in ["N", "S"] else "S"
            lstGpsMetadata.append({"TAGNumber": "Latitude", "DataValue": converterGrausDecimais(latValor, latRef)})
            lstGpsMetadata.append({"TAGNumber": "Ref. Latitude", "DataValue": MAPEAMENTO_REF.get(latRef)})

        if lonValor:
            lonRef = lonRefBruto if lonRefBruto in ["E", "W"] else "W"
            lstGpsMetadata.append({"TAGNumber": "Longitude", "DataValue": converterGrausDecimais(lonValor, lonRef)})
            lstGpsMetadata.append({"TAGNumber": "Ref. Longitude","DataValue": MAPEAMENTO_REF.get(lonRef)})

        # O EXIF armazena a altitude como um valor positivo.
        # A TAG GPSAltitudeRef indica se a altitude é acima (0)
        # ou abaixo (1) do nível médio do mar.
        if altValor:
            altitude = altValor[0] if isinstance(altValor, list) else altValor
            if altRefVal == 1: altitude = -altitude
            lstGpsMetadata.append({"TAGNumber": "Altitude", "DataValue": f"{altitude:.2f} metros"})

        # O padrão EXIF armazena data e horário separadamente.
        # Aqui ambos são combinados em uma única informação.
        if timestamp and datestamp:
            hora = ( f"{int(timestamp[0]):02d}:"
                     f"{int(timestamp[1]):02d}:"
                     f"{int(timestamp[2]):02d} UTC"
                  )

            lstGpsMetadata.append({"TAGNumber": "Data e Hora (UTC)", "DataValue": f"{datestamp} {hora}"})

    # Fechando o arquivo
    fileInput.close()

    # Imprimindo o nome do arquivo lido
    print("\n\nArquivo Lido\n" + "-" * 30)
    print(strNomeArquivo)

    # Imprimindo os dados do cabeçalho EXIF
    print("\n\nDados do Cabeçalho EXIF\n" + "-" * 30)
    for key, value in dictEXIF.items(): print(f"{key:15}: {value}")

    # Imprimindo os metadados lidos
    print("\n\nMetadados Lidos\n" + "-" * 30)
    for metaData in lstMetadata: print(f"{metaData}")

    # Imprimindo os metadados de GPS lidos
    if lstGpsMetadata:
        print("\n\nMetadados de GPS Lidos\n" + "-" * 30)
        for metaData in lstGpsMetadata: print(f"{metaData}")

    print("\n\n")