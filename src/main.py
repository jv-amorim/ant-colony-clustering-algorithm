from clustering import ClusteringCalculator
from colony import Colony
from consts import MAX_ITERATIONS
from distances import DistancesTable
from grid import GridManager


def main():
  grid_manager = GridManager()
  distances_table = DistancesTable()
  clustering_calculator = ClusteringCalculator(grid_manager, distances_table)
  colony = Colony(grid_manager, clustering_calculator)

  for _ in range(MAX_ITERATIONS):
    colony.perform_colony_iteration()

  write_output_file(grid_manager)


def write_output_file(grid_manager):
  output_content = \
    str(grid_manager.grid.tolist()) \
    .replace('-1', '_') \
    .replace('[', '') \
    .replace('], ', '\n') \
    .replace(']', '') \
    .replace(',', '') \
    .replace('_', '__')
  
  file = open('output/output.txt', 'w')

  for item in output_content.split(' '):
    if len(item) == 1:
      item = '0' + item
    file.write(item + ' ')

  file.close()


if __name__ == '__main__':
  main()
