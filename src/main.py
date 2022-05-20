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

  (clusters, score) = clustering_calculator.calculate_clusters_and_silhouette_score()

  write_output_file(grid_manager.grid, clusters, score)


def write_output_file(grid, clusters, score):
  clusters_as_string = convert_numpy_array_to_output_string(clusters)
  grid_as_string = convert_numpy_array_to_output_string(grid)

  file = open('output/output.txt', 'w')
  file.write(f'Grid:\n\n{grid_as_string}\n\n\n')
  file.write(f'Clusters:\n\n{clusters_as_string}\n\n\n')
  file.write(f'Silhouette Score:\n\n{score}')
  file.close()


def convert_numpy_array_to_output_string(array):
    return \
      str(array.tolist()) \
      .replace('], ', '],\n') \
      .replace('[[', '[') \
      .replace(']]', ']') \
      .replace('-1', '_')


if __name__ == '__main__':
  print('ACC is running. Please await, it may take a few minutes to finish.')
  main()
  print('Done!')
