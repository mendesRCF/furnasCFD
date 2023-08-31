# furnasCFD

Versão de teste do programa de desenho da turbina para simulações em CFD.

Programa desenvolvido para executar em python3 dentro da platafoma jupyter notebook, caso não possua instalado no computador recomendo a instalação do pacote Anaconda (https://www.anaconda.com/).

Com o python3 instalado, abra um terminal e instale as seguintes bibliotecas 

-  pip install tkinter
-  pip install stl
-  pip install trimesh
-  pip install subprocess
-  pip install scipy
-  pip install os
-  pip install PIL

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

# Caso teste

Para executar o caso teste, faça o download dos seguinte aquivos em um mesmo diretório 

- TurbineComplete.ipynb
- shapeTUCUNARE.dat
- NACA653618.dat

Após o download, execute o arquivo "TurbineComplete.ipynb" em seu compilador Pyhton 





