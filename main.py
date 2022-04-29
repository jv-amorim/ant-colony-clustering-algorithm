import numpy as np
import random

# matriz com 30 individuos com 9 elementos, preenchida com 0
objetos = np.zeros((100, 9), dtype=int)


# Função que vai preencher a matriz de objetos com valores aleatórios.
def gera_objetos():
    # percorro cada elemento e adiciono um valor aleatório entre 0 e 15
    for x in range(len(objetos)):
        for y in range(len(objetos[x])):
            objetos[x][y] = random.randint(0, 15)

    gera_objetos()
    print("teste")