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

  clusters = grid_manager.find_clusters()

  write_output_file(grid_manager.grid, clusters)


def write_output_file(grid, clusters):
  grid_as_string = convert_numpy_array_to_output_string(grid)
  clusters_as_string = convert_numpy_array_to_output_string(clusters)

  file = open('output/output.txt', 'w')
  file.write(f'{grid_as_string}\n\n\n{clusters_as_string}')
  file.close()


def convert_numpy_array_to_output_string(array):
    return \
      str(array.tolist()) \
      .replace('], ', '],\n') \
      .replace('[[', '[') \
      .replace(']]', ']') \
      .replace('-1', '_')


if __name__ == '__main__':
  main()
