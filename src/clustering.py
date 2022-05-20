import math

from consts import ALPHA, KD, KP, S


class ClusteringCalculator:
  def __init__(self, grid, distances_table):
    self.grid = grid
    self.distances_table = distances_table

  def calculate_pick_probability(self, ant):
    division_value = KP/(KP + self.__calculate_density(ant))
    return pow(division_value, 2)

  def calculate_drop_probability(self, ant):
    density_value = self.__calculate_density(ant)
    division_value = density_value/(KD + density_value)
    return pow(division_value, 2)

  def __calculate_density(self, ant):
    (neighborhood_start, neighborhood_end) = self.grid.calculate_neighborhood(ant.position, S)
    
    item_being_held = self.grid.get_grid_value_at(ant.position)
    sum = 0.0

    for row_index in range(neighborhood_start[0], neighborhood_end[0] + 1):
      for column_index in range(neighborhood_start[1], neighborhood_end[1] + 1):
        if self.grid.is_the_grid_cell_empty(row_index, column_index):
          continue

        current_item = self.grid.get_grid_value_at((row_index, column_index))
        if current_item == item_being_held:
          continue

        distance = self.distances_table.get_distance_between_items(item_being_held, current_item)
        sum += 1.0 - distance / ALPHA
    
    density = sum / math.pow(S, 2)

    return density if density > 0 else 0
