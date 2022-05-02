import numpy as np
import random

# matriz com 10 objetos e duas características, altura e média de gols
objetos = np.zeros((10, 2), dtype=int)


# Função que vai preencher a matriz de objetos com valores aleatórios
def gera_objetos():
    # percorro cada elemento e adiciono um valor aleatório entre 0 e 1
    for x in range(len(objetos)):
        for y in range(len(objetos[x])):
            if y == 0:
                objetos[x][y] = round(random.uniform(1.5, 2.10), 2)
                print("altura = ", objetos[x][y])
            else:
                objetos[x][y] = round(random.uniform(0, 1), 2)
                print("media = ", objetos[x][y])


gera_objetos()