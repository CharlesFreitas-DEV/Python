import os, sys
import subprocess


# --------------------------------------------------------------------------------
# Extraindo o áudio de um vídeo MP4 para MP3
def extrairAudio(strArquivoVideo: str) -> str:
    if not os.path.isfile(strArquivoVideo):
        raise FileNotFoundError(f"ARQUIVO -> {strArquivoVideo}")

    strArquivoMp3 = os.path.splitext(strArquivoVideo)[0] + ".mp3"

    strFfmpeg = r"C:\ffmpeg\bin\ffmpeg.exe"

    if not os.path.isfile(strFfmpeg):
        raise FileNotFoundError(f"ARQUIVO -> {strFfmpeg}")

    lstComando = [  strFfmpeg   , "-i"  , strArquivoVideo, "-vn", "-codec:a",
                    "libmp3lame", "-b:a", "192k"         , "-y" , strArquivoMp3, ]

    subprocess.run(lstComando, check=True)

    return strArquivoMp3


# --------------------------------------------------------------------------------
# Bloco principal do programa
def main() -> None:
    # Obtendo o diretório do vídeo (considerando que o vídeo está 
    # no mesmo diretório do programa 
    strDiretorioVideo = os.path.dirname(os.path.abspath(__file__))

    # Informando o arquivo MP4. Substituir "seu_video.mp4" pelo nome do arquivo4
    # a ter o áudio extraído
    strArquivoVideo   = os.path.join(strDiretorioVideo, "seu_video.mp4")

    print(f"\nExtraindo áudio do arquivo:\n{strArquivoVideo}")
    
    try:
        strArquivoMp3 = extrairAudio(strArquivoVideo)
    except FileNotFoundError as erro:
        sys.exit(f"\nERRO: Arquivo não encontrado.\n{erro}")
    except Exception as erro:
        sys.exit(f"\nERRO: Ocorreu um erro durante a conversão.\nERRO -> {erro}")
    else:
        print("\nConversão concluída com sucesso!")
        print(f"Arquivo MP3: {strArquivoMp3}")


# --------------------------------------------------------------------------------
# Chamando o bloco principal do programa
if __name__ == "__main__":
    main()