import math
import numpy as np

from consts import ALPHA, ITEMS_DATA, ITEMS_QUANTITY, KD, KP, S
from sklearn.metrics import silhouette_score


class ClusteringCalculator:
  def __init__(self, grid_manager, distances_table):
    self.grid_manager = grid_manager
    self.distances_table = distances_table

  def calculate_pick_probability(self, ant):
    division_value = KP/(KP + self.__calculate_density(ant))
    return pow(division_value, 2)

  def calculate_drop_probability(self, ant):
    density_value = self.__calculate_density(ant)
    division_value = density_value/(KD + density_value)
    return pow(division_value, 2)

  def __calculate_density(self, ant):
    (neighborhood_start, neighborhood_end) = self.grid_manager.calculate_neighborhood(ant.position, S)
    
    item_being_held = self.grid_manager.get_grid_value_at(ant.position)
    sum = 0.0

    for row_index in range(neighborhood_start[0], neighborhood_end[0] + 1):
      for column_index in range(neighborhood_start[1], neighborhood_end[1] + 1):
        if self.grid_manager.is_the_grid_cell_empty(row_index, column_index):
          continue

        current_item = self.grid_manager.get_grid_value_at((row_index, column_index))
        if current_item == item_being_held:
          continue

        distance = self.distances_table.get_distance_between_items(item_being_held, current_item)
        sum += 1.0 - distance / ALPHA
    
    density = sum / math.pow(S, 2)

    return density if density > 0 else 0
  
  def calculate_clusters_and_silhouette_score(self):
    clusters = self.grid_manager.find_clusters()
    (mapped_items, labels) = self.__generate_data_for_silhouette_calculation(clusters)
    score = self.__calculate_silhouette_score(mapped_items, labels)
    return (clusters, score)

  def __generate_data_for_silhouette_calculation(self, clusters):
    mapped_items = np.zeros((ITEMS_QUANTITY, 2), dtype=np.float32)
    labels = np.zeros(ITEMS_QUANTITY, dtype=np.uint16)

    for item_index in range(ITEMS_QUANTITY):
      mapped_items[item_index, 0] = ITEMS_DATA[item_index][0]
      mapped_items[item_index, 1] = ITEMS_DATA[item_index][1]
      labels[item_index] = self.__find_cluster_index_for_current_item(clusters, item_index)

    return (mapped_items, labels)

  def __find_cluster_index_for_current_item(self, clusters, item_index):
    for cluster_index in range(len(clusters)):
      for cluster_item in clusters[cluster_index]:
        if cluster_item == item_index:
          return cluster_index

  def __calculate_silhouette_score(self, items, labels):
    try:
      return silhouette_score(items, labels, metric='euclidean')
    except:
      return 'None, because only one cluster was formed.'
