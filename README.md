# Aplicar Tracks de Áudio e Legendas em Vídeo

Este programa facilita a tradução e adição de faixas de áudio e legendas em vídeos, com novas funcionalidades para otimizar o processo.

## Funcionalidades:

- **Tradução em lote de arquivos `.SRT`**  
  Traduz legendas para qualquer idioma disponível no Google Tradutor. Utilize o arquivo `traduzir.bat`.
  - **Diferencial:**  
    Ao contrário de tradutores convencionais (como sites ou programas como o Subtitle Edit), este programa mantém o contexto, traduzindo o arquivo como um todo. Assim, mesmo com quebras nas legendas, a tradução preserva a continuidade, oferecendo um resultado mais fiel ao original.
  - **Observação:**  
    Traduções para idiomas asiáticos, como Japonês e Chinês, podem apresentar problemas na distribuição de caracteres, resultando em índices de legendas em branco. Para esses casos, recomendamos o uso de ferramentas como o Subtitle Edit.

- **Mescla de áudio de fundo**  
  Mescla faixas de áudio de fundo com suas tracks de áudio, se necessário. Utilize o arquivo `mesclar_com_áudios.bat`.

- **Quebra de legendas no padrão "Netflix"**  
  Quebra legendas automaticamente para respeitar o limite de 42 caracteres por linha. (Não oferece suporte a idiomas asiáticos como Japonês e Chinês; para esses casos, recomendamos o Subtitle Edit). Utilize o arquivo `separar_legenda.bat`.

- **Adição automática de tracks de áudio e legenda**  
  Adicione várias faixas de áudio e legendas ao vídeo sem precisar configurar manualmente. Basta colocar os arquivos de áudio na pasta correta e executar o `.bat`. Utilize os arquivos `adicionar_faixa_de_legenda.bat` e `adicionar_faixas_de_áudio.bat`.

## Resultado final
![image](https://github.com/RafaelGodoyEbert/Adicionar_audio_e_legenda/assets/78083427/5e4a99df-597a-4930-8e34-66f688ffaef8)

## Requisitos

- Python 3.x

## Instalação
Recomendo baixar o .zip que está pronto em releases, mas caso queira fazer.

### Crie uma venv
```
python -m venv venv
```
depois
```
venv\Scripts\activate
```

### Instale as dependencias
Com a venv ativada
```
pip install -r requirements.txt
```

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
