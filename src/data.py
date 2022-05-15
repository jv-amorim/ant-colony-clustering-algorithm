import enum
import json
import numpy as np


DATA_BASE_PATH = 'data/'


class DataSources(enum.Enum):
  Genes = 1
  Players = 2


def get_items_data(data_source):
  if data_source == DataSources.Genes:
    return __get_genes_data()
  if data_source == DataSources.Players:
    return __get_players_data()


def __get_genes_data():
  file = open(DATA_BASE_PATH + 'genes.json', 'r')
  json_data = file.read()
  file.close()

  parsed_data = json.loads(json_data)
  genes_data = []

  for current_item in parsed_data:
    gene_data = (
      current_item['wnl'],
      current_item['tis'],
      current_item['gene']
    )
    genes_data.append(gene_data)

  return np.array(genes_data, dtype=[('wnl', '<f4'), ('tis', '<f4'), ('gene', 'U10')])


def __get_players_data():
  file = open(DATA_BASE_PATH + 'players.json', 'r')
  json_data = file.read()
  file.close()

  parsed_data = json.loads(json_data)
  players_data = []

  for current_item in parsed_data:
    player_data = (
      current_item['height'],
      current_item['score'],
      current_item['id']
    )
    players_data.append(player_data)

  return np.array(players_data, dtype=[('height', '<f4'), ('score', '<f4'), ('id', 'U10')])
