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

def nearest_neighbor(signal: np.ndarray, newLen: int) -> np.ndarray:
  interval = (len(signal)-1)/(newLen-1)
  interpSignal = np.zeros(newLen)
  for i in range(newLen):
    interpSignal[i] = signal[round(i*interval)]
  return interpSignal

def nearest_neighbor2(img: np.ndarray, newShape: tuple) -> np.ndarray:
  interpImg = np.zeros(newShape)
  xInterval = (img.shape[1])/(newShape[1])
  yInterval = (img.shape[0])/(newShape[0])
  for y in range(newShape[0]):
    for x in range(newShape[1]):
      interpImg[y,x] = img[math.floor(y*yInterval), math.floor(x*xInterval)]
  return interpImg

##### LINEAR INTERPOLATION METHODS #####

def linear(signal: np.ndarray, newLen: int) -> np.ndarray:
  interval = (len(signal)-1)/(newLen-1)
  interpSignal = np.zeros(newLen)
  for i in range(newLen):
    x = i*interval
    x0 = np.floor(x)
    x1 = np.ceil(x)
    if x0 == x1:
      interpSignal[i] = signal[int(x0)]
      continue
    y0 = signal[int(x0)]
    y1 = signal[int(x1)]
    interpSignal[i] = y0+(x-x0)*((y1-y0)/(x1-x0))
  return interpSignal

def bilinear():
  pass

##### CUBIC INTERPOLATION METHODS #####