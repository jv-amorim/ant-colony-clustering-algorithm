import numpy as np


S = 3
KP = 0.3
KD = 0.3
ALPHA = 0.5
ANT_QUANTITY = 1
MAX_ITERATIONS = 1000
ITEMS_DATA = np.array([[1.60, 0.70],
                       [1.64, 0.90],
                       [1.85, 0.03],
                       [1.53, 0.60],
                       [1.89, 0.10],
                       [1.83, 0.06]])


# Don't modify the following constants. They are generated in runtime according to the ITEMS_DATA above.
ITEMS_QUANTITY = GRID_SIZE = ITEMS_DATA.shape[0]
