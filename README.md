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

Você pode utilizar cada script de forma independente, sem precisar seguir uma ordem específica. Basta respeitar os diretórios especificados para que tudo funcione corretamente.

### Arquivo `traduzir.bat`
1. Coloque os arquivos `.SRT` que deseja traduzir na pasta `legendas\legendas_originais`.
2. Execute o `traduzir.bat`.

### Arquivo `mesclar_com_áudios.bat`
1. Coloque todos os áudios que deseja mesclar na pasta `audio_idiomas`.
2. Deixe o arquivo `background.mp3` na mesma pasta dos arquivos `.bat`.
3. Execute o `mesclar_com_áudios.bat`.

### Arquivo `separar_legenda.bat`
1. Execute o `separar_legenda.bat` para que ele faça o backup e a separação das legendas automaticamente.
   - Lembre-se que este script não oferece suporte a idiomas asiáticos como Japonês, Chinês e Coreano.

### Arquivo `adicionar_faixa_de_legenda.bat`
1. Ao executar, o script perguntará o nome do arquivo de vídeo que está na mesma pasta dos `.bat`.
2. Escolha a pasta de legendas que deseja adicionar: `legendas\legendas_originais` ou `legendas\legendas_traduzidas`.
3. O script criará um novo vídeo com as legendas, usando os nomes dos arquivos de legenda como referência.

### Arquivo `adicionar_faixas_de_áudio.bat`
1. Ao executar, o script perguntará o nome do arquivo de vídeo na mesma pasta dos `.bat`.
   - Caso tenha adicionado legendas, você pode escolher o nome do vídeo já com as legendas.
2. O script pegará todos os arquivos de áudio da pasta `audio_idiomas` e os adicionará ao vídeo.
3. Execute o `adicionar_faixa_de_legenda.bat` para gerar o novo vídeo com os áudios.


## Nota

Certifique-se de que todos os arquivos necessários (vídeo, áudio e legendas) estejam presentes nos diretórios especificados antes de executar os scripts. Certifique-se também de que os nomes dos arquivos e os idiomas correspondam corretamente para uma saída adequada.

Para quaisquer dúvidas ou problemas, entre em contato comigo.
