from data import DataSources, get_items_data


S = 3
KP = 0.3
KD = 0.3
ALPHA = 0.5
ANT_QUANTITY = 3
MAX_ITERATIONS = 500
DATA_SOURCE = DataSources.Players


# Don't modify the following constants. They are generated in runtime according to the settings above.
ITEMS_DATA = get_items_data(DATA_SOURCE)
ITEMS_QUANTITY = GRID_SIZE = ITEMS_DATA.shape[0]
