# furnasCFD

Versão de teste do programa de desenho da turbina para simulações em CFD.

Programa desenvolvido para executar em python3 dentro da platafoma jupyter notebook, caso não possua instalado no computador recomendo a instalação do pacote Anaconda (https://www.anaconda.com/).

Com o anaconda instalado, abra um terminal (CMD.exe Prompt).

Após a abertura, instale as bibliotecas necessárias colando cada linha individualmente no terminal e apertando ENTER (conforme ilustrado na figura 1)

-  pip install stl
-  pip install trimesh
-  pip install scipy
-  pip install Pillow

![manual 1](https://github.com/mendesRCF/furnasCFD/assets/66641867/9341fbf6-73d9-4f7e-9578-5de1c73b3953)
Figura 1 - Exemplo de instalação da biblioteca STL.

# Caso teste

Para executar o caso teste, faça o download de todos os aquivos em um mesmo diretório e exeute o arquivo 

- TurbineComplete.ipynb


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





