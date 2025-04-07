import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.colors as mcolors

ALTURA = 5
LARGURA = 5

matriz = np.full((ALTURA + 2, LARGURA + 2), 1)
matriz[1:ALTURA + 1, 1:LARGURA + 1] = 0

num_sujeiras = random.randint(4, 6)  # Define quantidade de sujeiras
for _ in range(num_sujeiras):
    x, y = random.randint(1, ALTURA), random.randint(1, LARGURA)  # Dentro da área útil
    matriz[x, y] = 2  # Marca sujeira

# Colormap personalizado: 0 - azul, 1 - verde, 2 - amarelo
colors = [(0, 0, 1), (0, 1, 0), (1, 1, 0)]  # Azul, verde, amarelo
n_bins = 3  # Número de cores
cmap_name = 'custom_cmap'
cm = mcolors.ListedColormap(colors, name=cmap_name)

# Normalizador para o intervalo de valores (0 a 2)
bounds = [0, 1, 2, 3]
norm = mcolors.BoundaryNorm(bounds, cm.N)

# Posicionamento do agente dentro da área útil
posAPAx, posAPAy = random.randint(1, 4), random.randint(1, 4)

def agenteReativoSimples():
    global matriz
    global posAPAx, posAPAy
    global ALTURA
    global LARGURA
    retornar = False
    #acima 1, abaixo 2, esquerda 3, direita 4, aspirar 5
    alturaPar = ALTURA % 2 == 0
    while True:
      if retornar:
        posAPAx, posAPAy = mover(posAPAx, posAPAy,"esquerda")
        if posAPAy == 1:
          retornar = False
      elif posAPAy == 1:
        if posAPAx < ALTURA:
          posAPAx, posAPAy = mover(posAPAx, posAPAy,"abaixo")
        else:
          posAPAx, posAPAy = mover(posAPAx, posAPAy,"direita")

      elif posAPAy == 2:

        if posAPAx == 1:

          if (posAPAx % 2 != 0 and alturaPar) or (posAPAx % 2 == 0 and not alturaPar):
            posAPAx, posAPAy = mover(posAPAx, posAPAy,"esquerda")
          else:
            posAPAx, posAPAy = mover(posAPAx, posAPAy,"direita")

        elif (posAPAx % 2 != 0 and alturaPar) or (posAPAx % 2 == 0 and not alturaPar):
          posAPAx, posAPAy = mover(posAPAx, posAPAy,"acima")

        elif (posAPAx % 2 == 0 and alturaPar) or (posAPAx % 2 != 0 and not alturaPar):
          posAPAx, posAPAy = mover(posAPAx, posAPAy,"direita")

      elif posAPAy < LARGURA:

        if (posAPAx % 2 == 0 and alturaPar) or (posAPAx % 2 != 0 and not alturaPar):
          posAPAx, posAPAy = mover(posAPAx, posAPAy,"direita")
        else:
          posAPAx, posAPAy = mover(posAPAx, posAPAy,"esquerda")

      else:

        if (posAPAx % 2 == 0 and alturaPar) or (posAPAx % 2 != 0 and not alturaPar):
          if posAPAx != 1:
            posAPAx, posAPAy = mover(posAPAx, posAPAy,"acima")
          else:
            posAPAx, posAPAy = mover(posAPAx, posAPAy,"esquerda")
            retornar = True
        else:
          posAPAx, posAPAy = mover(posAPAx, posAPAy,"esquerda")

      exibir(matriz)

def encontrarDirecaoNaMatriz(matrizMovimentos, posX, posY):
    for item in matrizMovimentos:
        if item[0] == posX and item[1] == posY:
            return item[2]
    return None

def mover(posAPAx, posAPAy, direcao):
    match direcao:
        case "acima":
            posAPAx = posAPAx - 1
            posAPAy = posAPAy
        case "abaixo":
            posAPAx = posAPAx + 1
            posAPAy = posAPAy
        case "esquerda":
            posAPAx = posAPAx
            posAPAy = posAPAy - 1
        case "direita":
            posAPAx = posAPAx
            posAPAy = posAPAy + 1

    return posAPAx, posAPAy

# Função que exibe o ambiente na tela
def exibir(matriz):
    global posAPAx, posAPAy

    plt.imshow(matriz, cmap=cm, norm=norm, interpolation='nearest')
    plt.colorbar()  # Adiciona uma barra de cores para referência visual

    plt.plot(posAPAy, posAPAx, marker='o', color='r', markersize=10)

    plt.show(block=False)
    plt.pause(0.3)

    if matriz[posAPAx, posAPAy] == 2:
        matriz[posAPAx, posAPAy] = 0
        exibir(matriz)

agenteReativoSimples()