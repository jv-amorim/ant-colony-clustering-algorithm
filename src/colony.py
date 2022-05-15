import random

from ant import Ant
from consts import ANT_QUANTITY, GRID_SIZE, ITEMS_QUANTITY


class Colony:
  ants = None

  def __init__(self, grid, clustering_calculator):
    self.grid = grid
    self.clustering_calculator = clustering_calculator
    self.__generate_colony_ants()

  def __generate_colony_ants(self):
    self.ants = []
    for _ in range(ANT_QUANTITY):
      self.ants.append(self.__generate_ant_in_the_grid())

  def __generate_ant_in_the_grid(self):
    for row_index in range(GRID_SIZE):
      for column_index in range(GRID_SIZE):
        is_valid_position = \
          not self.grid.is_the_grid_cell_empty(row_index, column_index) \
          and \
          not self.__does_grid_cell_already_have_an_ant((row_index, column_index))
        if is_valid_position:
          return Ant((row_index, column_index), True, self)
  
  def __does_grid_cell_already_have_an_ant(self, cell_coordinates):
    for ant in self.ants:
      if ant.position == cell_coordinates:
        return True
    return False

  def perform_colony_iteration(self):
    for ant in self.ants:
      if ant.is_holding:
        ant.move()
        if ant.is_holding:
          self.__make_the_ant_try_to_drop_her_current_item(ant)
      else:
        while not ant.is_holding:
          self.__make_the_ant_try_to_pick_a_random_item(ant)

  def __make_the_ant_try_to_drop_her_current_item(self, ant):
      random_value = random.random()
      drop_probability = self.clustering_calculator.calculate_drop_probability(ant)
      ant.is_holding = drop_probability < random_value

  def __make_the_ant_try_to_pick_a_random_item(self, ant):
    item_random_index = random.randint(0, ITEMS_QUANTITY - 1)
    item_coordinates = self.grid.get_item_coordinates(item_random_index)

    if self.__does_grid_cell_already_have_an_ant(item_coordinates):
      return

    for row_index in range(GRID_SIZE):
      for column_index in range(GRID_SIZE):
        if self.grid.get_grid_value_at((row_index, column_index)) != item_random_index:
          continue
        self.__make_the_ant_try_to_pick_a_item(ant, (row_index, column_index))

  def __make_the_ant_try_to_pick_a_item(self, ant, item_position): 
      ant_clone = ant.clone()
      ant_clone.position = item_position

      random_value = random.random()
      pick_probability = self.clustering_calculator.calculate_pick_probability(ant_clone)

      if pick_probability >= random_value:
        ant.position = ant_clone.position
        ant.is_holding = True
