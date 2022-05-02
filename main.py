import numpy as np
import random

# matriz com 10 objetos e duas características, altura e média de gols
objetos = np.zeros((10, 2), dtype=int)

# gera valores de média de gols
media_gols = np.random.random((10, 1))
print(media_gols)

# gera valores para altura dos jogadores
altura = [0] * 10
for i in range(10):
    altura[i] = np.random.uniform(1.5, 2.10)

print(altura)

