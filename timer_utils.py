# -*- coding: utf-8 -*-
"""
@author: fr-takumaurata
@brief: utils for timer
"""

import time
from contextlib import contextmanager

@contextmanager
def _timer(name):
    t0 = time.time()
    print (f'"{name}" started at {time.strftime("%d %b %Y %H:%M:%S", time.localtime())}')
    yield
    print (f'"{name}" done in {time.time() - t0:.1f} secs')