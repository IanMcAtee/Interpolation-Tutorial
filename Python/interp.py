'''
Module: interp.py
Author: Ian McAtee
Date: November 25, 2024
Description: Provides functions for the following interpolation methods:
    - Nearest Neighbor (Single Variable and Image Variations)
    - Linear and Bilinear
    - Cubic and Bicubic
'''

# Import dependencies
import math
import numpy as np

##### NEAREST NEIGHBOR INTERPOLATION METHODS #####

def nearest_neighbor(signal: np.ndarray, newLen: tuple) -> np.ndarray:
  interval = (len(signal)-1)/(newLen-1)
  interpSignal = np.zeros(newLen)
  for i in range(newLen):
    interpSignal[i] = signal[round(i*interval)]
  return interpSignal

def nearest_neighbor2():
  pass





##### LINEAR INTERPOLATION METHODS #####









##### CUBIC INTERPOLATION METHODS #####