import itertools
import math
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
    for row_index in range(GRID_SIZE):
      for column_index in range(GRID_SIZE):
        current_grid_value = self.get_grid_value_at((row_index, column_index))
        if current_grid_value == item_index:
          return (row_index, column_index)

  def calculate_neighborhood(self, center_coordinate, neighborhood_space):
    space_radius = math.floor(neighborhood_space / 2)

    neighborhood_start = [center_coordinate[0] - space_radius, center_coordinate[1] - space_radius]
    neighborhood_start = np.clip(neighborhood_start, [0, 0], None)

    neighborhood_end = [center_coordinate[0] + space_radius, center_coordinate[1] + space_radius]
    neighborhood_end = np.clip(neighborhood_end, None, [GRID_SIZE - 1, GRID_SIZE - 1])

    return (neighborhood_start, neighborhood_end)

  def find_clusters(self):
    neighbors_of_each_item = self.__get_neighbor_items_of_each_item_in_the_grid()
    clusters = self.__unify_neighbors_of_each_item_into_clusters(neighbors_of_each_item)
    return np.array(clusters, dtype=object)

  def __get_neighbor_items_of_each_item_in_the_grid(self):    
    neighbors_of_each_item = [None] * ITEMS_QUANTITY

    for row_index in range(GRID_SIZE):
      for column_index in range(GRID_SIZE):
        current_item = self.grid[row_index, column_index]
        if current_item == -1:
          continue        
        neighbors = self.__get_neighbor_items_for_current_item((row_index, column_index))
        neighbors_of_each_item[current_item] = neighbors

    return neighbors_of_each_item

  def __get_neighbor_items_for_current_item(self, item_coordinates):
    neighbors = []
    (neighborhood_start, neighborhood_end) = self.calculate_neighborhood(item_coordinates, 3)

    for x in range(neighborhood_start[0], neighborhood_end[0] + 1):
      for y in range(neighborhood_start[1], neighborhood_end[1] + 1):
        if self.grid[x, y] == -1:
          continue
        neighbors.append(self.grid[x, y])
    
    return neighbors

  # Solution adapted from: https://stackoverflow.com/a/47564626/12331811.
  def __unify_neighbors_of_each_item_into_clusters(self, neighbors_of_each_item):
    neighbors_set = set(itertools.chain.from_iterable(neighbors_of_each_item)) 

    for each in neighbors_set:
      components = [x for x in neighbors_of_each_item if each in x]
      for i in components:
        neighbors_of_each_item.remove(i)
      neighbors_of_each_item += [list(set(itertools.chain.from_iterable(components)))]

    return neighbors_of_each_item
