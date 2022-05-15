import math
import random
import numpy as np

from consts import GRID_SIZE


class Ant:
  def __init__(self, position, is_holding, colony):    
    self.position = position
    self.is_holding = is_holding
    self.colony = colony

  def __str__(self):
    return f'Ant = {{ Position: {self.position}, Is Holding: {self.is_holding} }}'

  def calculate_neighborhood(self, neighborhood_space):
    space_radius = math.floor(neighborhood_space / 2)

    neighborhood_start = [self.position[0] - space_radius, self.position[1] - space_radius]
    neighborhood_start = np.clip(neighborhood_start, [0, 0], None)

    neighborhood_end = [self.position[0] + space_radius, self.position[1] + space_radius]
    neighborhood_end = np.clip(neighborhood_end, None, [GRID_SIZE - 1, GRID_SIZE - 1])

    return (neighborhood_start, neighborhood_end)

  def move(self):
    if not self.is_holding:
      return

    (neighborhood_start, neighborhood_end) = self.calculate_neighborhood(3)
    new_position = None
    iteration_count = 0
    
    while new_position is None:
      iteration_count += 1
      is_the_ant_cornered = iteration_count >= 100
      if is_the_ant_cornered:
        self.is_holding = False
        return

      x = random.randint(neighborhood_start[0], neighborhood_end[0])
      y = random.randint(neighborhood_start[1], neighborhood_end[1])

      if self.colony.grid.is_the_grid_cell_empty(x, y):
        new_position = [x, y]
    
    self.colony.grid.swap_grid_values(self.position, new_position)
    self.position = new_position

  def clone(self):
    return Ant(self.position, self.is_holding, self.colony)
