# Aplicar Track de Áudio e Legendas em Vídeo
Atualizei o programa para facilitar muito mais ainda, agora com novas funcionalidades, no que esse programa pode te ajudar?

- Traduzir arquivos `.SRT` em lote para qualquer idioma disponível no Google Tradutor. Arquivo `traduzir.bat`
- Mesclar o áudio background no seus track de áudio, caso necessário. Arquivo `mesclar_com_áudios.bat`
- Quebrar a legenda para respeitar o "padrão Netflix" de 42 caracteres por linha em lote. (Por enquanto sem suporte a idiomas asiáticos como Japones e Chines, pra isso recomendo Subtitle Edit) Arquivo `separar_legenda.bat`
- Adicionar diversos track de áudio e legenda no seu vídeo, e sem precisar especificar nada, somente por o áudio na pasta e executar o `.bat`. Arquivos `adicionar_faixa_de_legenda.bat` e `adicionar_faixas_de_áudio.bat`

## Resultado final
![image](https://github.com/RafaelGodoyEbert/Adicionar_audio_e_legenda/assets/78083427/5e4a99df-597a-4930-8e34-66f688ffaef8)

## Requisitos

- Python 3.x

## Instalação
Recomendo baixar o .zip que está pronto em releases, mas caso queira fazer.

### Crie uma venv
```python -m venv venv```
depois
```venv\Scripts\activate```

### Instale as dependencias
Com a venv ativada
```pip install -r requirements.txt```

## Uso
Obviamente você não tem uma ordem pra seguir, se quiser usar apenas um pode, um script não depende do outro, só respeite os diretórios especificados.

Arquivo `traduzir.bat`
- Você só precisa por que quer traduzir na pasta legendas\legendas_originais
- E executar o `traduzir.bat`

Arquivo `mesclar_com_áudios.bat`
- Você precisa deixar todos os áudios que você quer mesclar dentro da pasta `audio_idiomas`
- Deixar o arquivo `background.mp3` solto na pasta junto com os arquivos .bat
- E executar o `mesclar_com_áudios.bat`

Arquivo `separar_legenda.bat`
- Apenas executar o `separar_legenda.bat` e ele faz o backup e faz a separação dinamica pra você.
- Lembrando que não tem suporte a idiomas asiáticos como Japonês, Chinês e Coreano.

Arquivos `adicionar_faixa_de_legenda.bat`
- Ao executar o código ele pergunta qual o nome do arquivo de vídeo que está na pasta junto aos `.bat`.
- Ao executar o código ele pergunta qual pasta com arquivos de legenda tu quer que ele coloque, sendo `legendas\legendas_originais` ou `legendas\legendas_traduzidas`.
- Só escolher qual dessas duas pasta estão seus arquivos e executar o `adicionar_faixa_de_legenda.bat`
- Então ele criará um novo vídeo com as legendas com o próprio nome das legendas nas pastas.

Arquivos `adicionar_faixas_de_áudio.bat`
- Ao executar o código ele pergunta qual o nome do arquivo de vídeo que está na pasta junto aos `.bat`.
    - Nesse caso, se você botou as legendas, pode escolher o nome do vídeo já com legendas.
- Ao executar o código pega todos seus arquivos de áudio da pasta `audio_idiomas` e coloca no vídeo com o nome do próprio áudio.
- Só executar o `adicionar_faixa_de_legenda.bat`
- Então ele criará um novo vídeo com os áudios.

## Nota

Certifique-se de que todos os arquivos necessários (vídeo, áudio e legendas) estejam presentes nos diretórios especificados antes de executar os scripts. Certifique-se também de que os nomes dos arquivos e os idiomas correspondam corretamente para uma saída adequada.

Para quaisquer dúvidas ou problemas, entre em contato comigo.
