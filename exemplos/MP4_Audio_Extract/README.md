# 🎵 MP4 Audio Extract

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![FFmpeg](https://img.shields.io/badge/ffmpeg-required-red)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)
![Open Source](https://img.shields.io/badge/open%20source-yes-brightgreen)

---

## 📌 Índice

- [📖 Sobre o projeto](#-sobre-o-projeto)
- [✨ Funcionalidades](#-funcionalidades)
- [📂 Estrutura do projeto](#-estrutura-do-projeto)
- [⚙️ Requisitos](#️-requisitos)
- [⬇️ Instalação do FFmpeg](#️-instalação-do-ffmpeg)
- [🚀 Como executar](#-como-executar)
- [🔄 Fluxo de execução](#-fluxo-de-execução)
- [🧪 Exemplo de uso](#-exemplo-de-uso)
- [🧠 Explicação técnica](#-explicação-técnica)
- [❓ FAQ](#-faq)
- [🚧 Melhorias futuras](#-melhorias-futuras)
- [🤝 Contribuição](#-contribuição)
- [📄 Licença](#-licença)
- [👨‍💻 Autor](#-autor)

---

## 📖 Sobre o projeto

O **MP4 Audio Extract** é um utilitário em Python que automatiza a extração de áudio de arquivos de vídeo no formato **MP4**, convertendo-os para **MP3** com o auxílio do **FFmpeg**.

O objetivo é fornecer uma solução simples, portátil e eficiente para extração de áudio sem necessidade de softwares gráficos.

---

## ✨ Funcionalidades

- Extração de áudio de vídeos MP4
- Geração automática de arquivo MP3
- Manutenção do nome original do arquivo
- Salvamento na mesma pasta do vídeo
- Validação de existência de arquivos
- Verificação do FFmpeg instalado
- Execução via linha de comando
- Baixa dependência externa (apenas FFmpeg)

---

## 📂 Estrutura do projeto

```text
MP4_Audio_Extract/
│
├── extractMP3fromMP4.py
├── LICENSE
└── README.md
```

---

## ⚙️ Requisitos

- Python 3.10+
- FFmpeg instalado no sistema

O projeto NÃO requer bibliotecas externas via pip.

---

## ⬇️ Instalação do FFmpeg

### 🔹 Windows (recomendado)

Baixe em:

https://www.gyan.dev/ffmpeg/builds/

Escolha:

- `ffmpeg-*-essentials_build.zip` (suficiente)
- ou `ffmpeg-*-full_build.zip` (completo)

---

### 📦 Extração

Extraia para:

```text
C:\ffmpeg
```

Estrutura esperada:

```text
C:\ffmpeg
└── bin
    ├── ffmpeg.exe
    ├── ffplay.exe
    └── ffprobe.exe
```

---

### 🧪 Teste

No terminal:

```cmd
"C:\ffmpeg\bin\ffmpeg.exe" -version
```

---

## 🚀 Como executar

1. Coloque o vídeo MP4 na mesma pasta do script
2. Execute:

```bash
python extractMP3fromMP4.py
```

---

## 🔄 Fluxo de execução

1. Localiza o arquivo MP4
2. Verifica existência do vídeo
3. Localiza FFmpeg
4. Verifica existência do FFmpeg
5. Monta nome do arquivo MP3
6. Executa conversão via FFmpeg
7. Gera arquivo MP3 final

---

## 🧪 Exemplo de uso

### Entrada:

```text
NOME_ARQUIVO.MP4
```

### Saída:

```text
NOME_ARQUIVO.MP3
```

---

## 🧠 Explicação técnica

### 📁 Bibliotecas utilizadas

```python
import os
import sys
import subprocess
```

---

### 📂 `os` (sistema de arquivos)

Responsável por manipulação de caminhos e arquivos:

- `os.path.isfile()` → verifica existência de arquivo
- `os.path.exists()` → verifica existência de caminho
- `os.path.abspath()` → caminho absoluto
- `os.path.dirname()` → diretório do arquivo
- `os.path.join()` → concatenação segura de paths
- `os.path.splitext()` → separa nome e extensão

---

### 🧠 `sys`

Usado para encerramento controlado do programa:

```python
sys.exit("mensagem de erro")
```

---

### ⚙️ `subprocess`

Executa comandos externos (FFmpeg):

```python
subprocess.run(lstComando, check=True)
```

#### 🔎 Parâmetro `check=True`

Gera exceção se o comando falhar.

---

### 🎞️ Construção do nome do MP3

```python
strArquivoMp3 = os.path.splitext(strArquivoVideo)[0] + ".mp3"
```

Exemplo:

```text
video.mp4 → video.mp3
```

---

### 🎛️ Comando FFmpeg

```python
lstComando = [
    strFfmpeg,
    "-i", strArquivoVideo,
    "-vn",
    "-codec:a", "libmp3lame",
    "-b:a", "192k",
    "-y",
    strArquivoMp3
]
```

---

### 📌 Parâmetros do FFmpeg

| Parâmetro | Função |
|----------|--------|
| `-i` | arquivo de entrada |
| `-vn` | remove vídeo |
| `-codec:a` | define codec de áudio |
| `libmp3lame` | encoder MP3 |
| `-b:a` | bitrate |
| `-y` | sobrescreve arquivo |

---

### ⚠️ Tratamento de erros

- Arquivo não encontrado → `FileNotFoundError`
- FFmpeg não encontrado → `FileNotFoundError`
- Erros de conversão → exceção do `subprocess`

---

## ❓ FAQ

### ❓ Preciso instalar bibliotecas via pip?

Não.

---

### ❓ Funciona em Linux e macOS?

Sim, basta alterar o caminho do FFmpeg.

---

### ❓ Posso converter outros formatos?

Sim, desde que suportados pelo FFmpeg.

---

### ❓ O áudio perde qualidade?

Não necessariamente. O padrão é 192kbps.

---

## 🚧 Melhorias futuras

- Interface gráfica (Tkinter / PyQt)
- Suporte a múltiplos arquivos
- Barra de progresso
- Configuração de bitrate
- Detecção automática de FFmpeg no PATH
- Logs de execução

---

## 🤝 Contribuição

Contribuições são bem-vindas:

1. Fork do projeto
2. Criação de branch (`feature/nova-funcionalidade`)
3. Commit
4. Pull Request

---

## 📄 Licença

Repositório desenvolvido para fins educacionais em Python.

Este projeto está licenciado sob a licença MIT.

Consulte o arquivo `LICENSE` para mais detalhes.

---

# 👨‍💻 Autor

**Charles Cesar Magno de Freitas**

Professor • Analista de Sistemas • Desenvolvedor Back-end

- 🎓 Professor de Programação
- 🐍 Entusiasta da linguagem Python
- 🧩 Desenvolvedor de projetos educacionais
- 💻 GitHub: https://github.com/CharlesFreitas-DEV

---

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório para apoiar o desenvolvimento e incentivar a criação de novos projetos educacionais.