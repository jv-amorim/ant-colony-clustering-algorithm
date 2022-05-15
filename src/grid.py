import random
import numpy as np

from consts import GRID_SIZE, ITEMS_QUANTITY


class GridManager:
  grid = None

  def __init__(self):
    self.__reset_grid()
    self.__assign_items_to_the_grid()
    
  def __reset_grid(self):
    self.grid = np.full((GRID_SIZE, GRID_SIZE), -1)
    
  def __assign_items_to_the_grid(self):
    for item_index in range(ITEMS_QUANTITY):
      self.__assign_item_to_the_grid(item_index)
  
  def __assign_item_to_the_grid(self, item_index):
    while True:
      x = random.randint(0, GRID_SIZE - 1)
      y = random.randint(0, GRID_SIZE - 1)

      if self.is_the_grid_cell_empty(x, y):
        self.set_grid_value_at((x, y), item_index)
        break

  def is_the_grid_cell_empty(self, x, y):
    return self.get_grid_value_at((x, y)) == -1

  def get_grid_value_at(self, coordinates):
    return self.grid[coordinates[0], coordinates[1]]

  def set_grid_value_at(self, coordinates, value):
    self.grid[coordinates[0], coordinates[1]] = value

  def swap_grid_values(self, first_value_position, second_value_position):
    first_value = self.get_grid_value_at(first_value_position)
    second_value = self.get_grid_value_at(second_value_position)
    self.set_grid_value_at(first_value_position, second_value)
    self.set_grid_value_at(second_value_position, first_value)

  def get_item_coordinates(self, item_index):
    for row_index in range(GRID_SIZE - 1):
      for column_index in range(GRID_SIZE - 1):
        current_grid_value = self.get_grid_value_at((row_index, column_index))
        if current_grid_value == item_index:
          return (row_index, column_index)
