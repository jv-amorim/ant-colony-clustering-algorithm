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

  print('Result:')
  print(grid_manager.grid + 1)


if __name__ == '__main__':
  main()
