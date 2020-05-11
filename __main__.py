from src.polygon import Polygon
from src.path_planning import find_path
from src.concave_decomposition import decompose, combine
import numpy as np

import matplotlib.pyplot as plt

from random import randint

if __name__ == '__main__':
    #search_area = Polygon([(1.0, 1.0), (2.0, 2.0), (1.2, 3.4), (4.5, 3.2), (4.0, -1.2)])
    search_area = Polygon([(83.0, 28.0), (68.0, 0.0), (12.0, 3.0), (0.0, 58.0), (80.0, 80.0)])


    decompose(search_area)
    combine(search_area)  # not implemented yet...

    path = find_path(search_area, (1, -1), 1)