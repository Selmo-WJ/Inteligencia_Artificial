import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.colors as mcolors
from collections import deque

TAMANHO = 6
AMBIENTE = 4

matriz = np.full((TAMANHO, TAMANHO), 1)
matriz[1:5, 1:5] = 0

posicoes_disponiveis = [(x, y) for x in range(1, 5) for y in range(1, 5)]
num_sujeiras = random.randint(4, 6)
for x, y in random.sample(posicoes_disponiveis, num_sujeiras):
    matriz[x, y] = 2  # Marca sujeira

colors = [(0, 0, 1), (0, 1, 0), (1, 1, 0)]  # Azul, verde, amarelo
cm = mcolors.ListedColormap(colors)
norm = mcolors.BoundaryNorm([0, 1, 2, 3], cm.N)

posAPAx, posAPAy = 1, 1
pontos = 0
caminho_atual = []


def encontrar_caminho(matriz, inicio):
    global caminho_atual
    filas = deque([(inicio, [])])
    visitados = set([inicio])

    while filas:
        (x, y), caminho = filas.popleft()

        if matriz[x, y] == 2:
            caminho_atual = caminho
            return caminho

        # Movimentos possíveis: cima, baixo, esquerda, direita
        movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= 4 and 1 <= ny <= 4 and matriz[nx, ny] != 1 and (nx, ny) not in visitados:
                visitados.add((nx, ny))
                filas.append(((nx, ny), caminho + [(nx, ny)]))

    caminho_atual = []
    return []


def mover(pos, caminho):
    global pontos, posAPAx, posAPAy
    if caminho:
        posAPAx, posAPAy = caminho[0]
        pontos += 1
        return caminho[1:]
    return []


def exibir(matriz):
    global posAPAx, posAPAy, pontos, caminho_atual

    plt.clf()
    plt.imshow(matriz, cmap=cm, norm=norm, interpolation='nearest')
    plt.plot(posAPAy, posAPAx, marker='o', color='r', markersize=10)
    plt.title(f'Pontuação: {pontos}')
    plt.show(block=False)
    plt.pause(0.3  )

    if matriz[posAPAx, posAPAy] == 2:
        matriz[posAPAx, posAPAy] = 0
        pontos += 1
        caminho_atual = []
        exibir(matriz)

    if not caminho_atual:
        encontrar_caminho(matriz, (posAPAx, posAPAy))
    else:
        caminho_atual = mover((posAPAx, posAPAy), caminho_atual)


def checkObj(matriz):
    return np.any(matriz == 2)


# Loop do agente baseado em objetivo
while checkObj(matriz):
    exibir(matriz)

print(f"Pontuação final: {pontos}")