# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 09:50:08 2021

@author: Yi
"""

import numpy as np
from numpy.random import randn

N = 90000000
counter = 0

for i in randn(N):
    if (i >= -1) & (i <= 1):
        counter += 1

answer = counter / N
print(answer)