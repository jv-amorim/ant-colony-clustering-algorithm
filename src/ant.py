import random


class Ant:
  def __init__(self, position, is_holding, grid_manager):    
    self.position = position
    self.is_holding = is_holding
    self.grid_manager = grid_manager

  def __str__(self):
    return f'Ant = {{ Position: {self.position}, Is Holding: {self.is_holding} }}'

  def move(self):
    if not self.is_holding:
      return

    (neighborhood_start, neighborhood_end) = self.grid_manager.calculate_neighborhood(self.position, 3)
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

      if self.grid_manager.is_the_grid_cell_empty(x, y):
        new_position = [x, y]
    
    self.grid_manager.swap_grid_values(self.position, new_position)
    self.position = new_position

  def clone(self):
    return Ant(self.position, self.is_holding, self.grid_manager)
