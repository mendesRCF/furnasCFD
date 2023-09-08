# furnasCFD

# Manual de Instalação

Versão de Teste do Programa de Desenho da Turbina para Simulações em CFD

Este programa foi desenvolvido para ser executado em Python 3 no ambiente Jupyter Notebook. Caso você não tenha o Python e o Jupyter Notebook instalados em seu computador, recomendamos a instalação do pacote Anaconda, que inclui tanto o Python quanto o Jupyter Notebook. Você pode baixar o Anaconda em https://www.anaconda.com/.

Passos de Instalação:

1. Instale o Anaconda:

Após baixar o Anaconda do link fornecido, siga as instruções de instalação adequadas para o seu sistema operacional.

2. Abra um Terminal (CMD.exe Prompt):

Após a instalação do Anaconda, abra um terminal de comando. Isso pode ser feito procurando "CMD" no menu Iniciar (Windows) ou usando o terminal padrão no macOS ou Linux.

3. Instale as Bibliotecas Necessárias:

Copie e cole cada uma das seguintes linhas no terminal e pressione a tecla "ENTER" após cada linha, conforme ilustrado na Figura 1:

- pip install stl
- pip install trimesh
- pip install scipy
- pip install Pillow
  
Certifique-se de instalar todas essas bibliotecas para garantir o funcionamento adequado do programa de desenho da turbina.

![manual 1](https://github.com/mendesRCF/furnasCFD/assets/66641867/9341fbf6-73d9-4f7e-9578-5de1c73b3953)
Figura 1: Exemplo de instalação das biblioteca stl.

Nota Importante:

Certifique-se de que o Anaconda esteja corretamente instalado e configurado antes de prosseguir com a instalação das bibliotecas. Uma vez que todas as bibliotecas estejam instaladas, você estará pronto para executar o programa de desenho da turbina e realizar simulações em CFD.


# Caso teste

1. Baixe todos Arquivos:
Certifique-se de baixar todos os arquivos necessários para o mesmo diretório. 

2. Abra o Jupyter Notebook:
Abra o Jupyter Notebook em seu ambiente Anaconda. 

3. Navegue até o Diretório de Trabalho:
No Jupyter Notebook, navegue até o diretório onde você baixou os arquivos usando a interface do navegador de arquivos do Jupyter.

4. Abra o Arquivo "TurbineComplete.ipynb":
Clique no arquivo "TurbineComplete.ipynb" para abri-lo no Jupyter Notebook.

5. Execute o script:

- TurbineComplete.ipynb

6. Após a execução a seguinte tela será mostrada.

![Captura de tela 2023-09-08 181014](https://github.com/mendesRCF/furnasCFD/assets/66641867/0eae9810-4432-4199-ab7c-2b8298ac001d)

7. Aperte "Generate Turbine!" e o código irá executar, gerando o desenho de uma turbine pré-configurada.

![Captura de tela 2023-09-08 181030](https://github.com/mendesRCF/furnasCFD/assets/66641867/98dc8331-0d23-434b-a074-c768bf26e419)

# Dados de entrada

- Arquivo contendo as coordenadas adimensionais em duas dimensões (x,y) do aerofólio de desenho da pá. Baixar direto do site http://airfoiltools.com/
- Arquivo de projeto da pá contendo raio [m], corda[m] e angulação[°] (radius, chord and twist)
- Dimensões da torre: raio[m] e altura[m].
- Dimensões da fundação: raio[m] e altura[m].

# Arquivos de saída

O presente código gera 3 arquivos de geometrias "nome de saída dado pelo o usuário". 

- "nome de saída dado pelo o usuário"_rotor.stl
- "nome de saída dado pelo o usuário"_tower.stl
- "nome de saída dado pelo o usuário"_foundation.stl



Após o download, execute o arquivo "TurbineComplete.ipynb" em seu compilador Pyhton 





