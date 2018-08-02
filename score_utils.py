# -*- coding: utf-8 -*-
"""
@author: fr-takumaurata
@brief: utils for score
y0 is the original y value
y is the predicted y value
"""

import numpy as np
from sklearn.metrics import mean_squared_error

#Root Mean Squared Error (RMSE)
def _rmse(y, y0):
    assert len(y) == len(y0)
    return np.sqrt(mean_squared_error(y0, y))