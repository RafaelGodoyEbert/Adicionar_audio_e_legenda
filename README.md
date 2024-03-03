# Aplicar Track de Áudio e Legendas em Vídeo

Este script Python, `aplicar_track_audio.py`, e o arquivo de lote `legendas.bat` são projetados para facilitar a adição de faixas de áudio e legendas a um vídeo.

## Requisitos

- Python 3.x
- FFmpeg

Certifique-se de ter o FFmpeg instalado e configurado corretamente no seu sistema antes de usar esses scripts.
Basicamente só [baixar ](https://github.com/BtbN/FFmpeg-Builds/releases) e colocar os .exe na mesma pasta desse programa.

## Uso

 - Certifique-se que o nome do vídeo que você quer alterar esteja com o nome ``video.mp4``
 - Certifique-se que os arquivos dentro da pasta áudios sejam no formato ``.mp3``
 - Certifique-se que os arquivos de legenda dentro da pasta legendas sejam no formato ``.srt``

### Passos para Adicionar Faixas de Áudio:

1. Coloque os arquivos de áudio que deseja adicionar na pasta especificada no diretório `áudios`.
2. Execute o script Python `1- faixa_de_áudio.bat`.

### Passos para Adicionar Legendas:

1. Execute o arquivo de lote `2- legendas.bat` após ter adicionado as legendas desejadas na pasta `legendas`.
2. As legendas devem seguir o formato de nomeação: `brazilian.srt`, `english.srt`, etc.

    - **Inglês:** `english.srt`
    - **Português (Brasileiro):** `brazilian.srt`
    - **Português (Portugal):** `portuguese-PT.srt`
    - **Espanhol:** `spanish.srt`
    - **Francês:** `french.srt`
    - **Alemão:** `deutsch.srt`
    - **Italiano:** `italian.srt`
    - **Russo:** `russian.srt`

Cada legenda é mapeada para um idioma específico usando a opção `metadata:s:s:index` do FFmpeg.
Se desejar adicionar legendas em outros idiomas, será necessário atualizar o comando FFmpeg e incluir os mapeamentos correspondentes para esses idiomas adicionais.

3. Certifique-se de que as legendas correspondam aos idiomas dos arquivos de áudio adicionados anteriormente.

## Saída

- O script `aplicar_track_audio.py` combinará o vídeo original com as faixas de áudio adicionais, produzindo um novo vídeo com as faixas de áudio incluídas. O arquivo de saída será nomeado como `output-track.mp4`(Não antere o nome). 

- O arquivo de lote `legendas.bat` adicionará as legendas ao vídeo resultante, gerando um novo vídeo com as legendas incorporadas. O arquivo de saída será nomeado como `OUTPUT_leg.mp4`.

- Agora que foi colocado os áudios e as legendas, voce pode renomear o arquivo `OUTPUT_leg.mp4` e apagar o arquivo `output-track.mp4`.

## Nota

Certifique-se de que todos os arquivos necessários (vídeo, áudio e legendas) estejam presentes nos diretórios especificados antes de executar os scripts. Certifique-se também de que os nomes dos arquivos e os idiomas correspondam corretamente para uma saída adequada.

Para quaisquer dúvidas ou problemas, entre em contato comigo.