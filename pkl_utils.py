# -*- coding: utf-8 -*-
"""
@author: fr-takumaurata
@brief: utils for pickle
"""

import pickle
import time

def _save(fname, data, protocol=pickle.HIGHEST_PROTOCOL):
    with open(fname, "wb") as f:
        print ("pkl saving..")
        pickle.dump(data, f, protocol)
        print ("pkl saved")

def _load(fname):
    with open(fname, "rb") as f:
        print ("pkl loading..")
        return pickle.load(f)
        print ("pkl loaded")