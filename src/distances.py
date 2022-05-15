import math
import numpy as np

from consts import ITEMS_DATA, ITEMS_QUANTITY


class DistancesTable:
  distances = None

  def __init__(self):
    self.__generate_distances_table()

  def __generate_distances_table(self):
    distances = np.zeros((ITEMS_QUANTITY, ITEMS_QUANTITY))
    greater_distance = 0

    for row_index in range(ITEMS_QUANTITY):
      item_1 = ITEMS_DATA[row_index]
      
      for column_index in range(ITEMS_QUANTITY):
        if row_index == column_index:
          continue

        item_2 = ITEMS_DATA[column_index]
        distance = self.__calculate_euclidian_distance(item_1, item_2)
        distances[row_index, column_index] = distance
        
        if distance > greater_distance:
          greater_distance = distance

    self.distances = distances / greater_distance

  def __calculate_euclidian_distance(self, item_1, item_2):
    pow_1 = math.pow(item_1[0] - item_2[0], 2)
    pow_2 = math.pow(item_1[1] - item_2[1], 2)
    return math.sqrt(pow_1 + pow_2)

  def get_distance_between_items(self, first_item_index, second_item_index):
    return self.distances[first_item_index, second_item_index]
