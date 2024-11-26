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
    x0 = math.floor(x)
    x1 = math.ceil(x)
    if x0 == x1:
      interpSignal[i] = signal[x0]
      continue
    y0 = signal[x0]
    y1 = signal[x1]
    interpSignal[i] = y0+(x-x0)*((y1-y0)/(x1-x0))
  return interpSignal

def bilinear_interp2(img, newShape):
  xScale = newShape[1]/img.shape[1]
  yScale = newShape[0]/img.shape[0]

  tempArr = np.zeros((img.shape[0], newShape[1]))
  for j in range(newShape[1]):
    x = (j+0.5)*(1/xScale)-0.5
    if x <= 0 or x >= img.shape[1]-1:
      tempArr[:,j] = img[:,int(x)]
      continue
    x1 = math.floor(x)
    x2 = math.ceil(x)
    if (x1 == x2):
      tempArr[:,j] = img[:,x1]
      continue
    for i in range(img.shape[0]):
      tempArr[i,j] = (x2-x)*img[i,x1] + (x-x1)*img[i,x2]

  # Interpolate across columns
  interpImg = np.zeros((newShape[0], newShape[1]))
  for i in range(newShape[0]):
    y = (i+0.5)*(1/yScale)-0.5
    if y <= 0 or y >= img.shape[0]-1:
      interpImg[i,:] = tempArr[int(y),:]
      continue
    y1 = math.floor(y)
    y2 = math.ceil(y)
    if (y1 == y2):
      interpImg[i,:] = tempArr[y1,:]
      continue
    for j in range(newShape[1]):
      interpImg[i,j] = (y2-y)*tempArr[y1,j] + (y-y1)*tempArr[y2,j]
  return interpImg

##### CUBIC INTERPOLATION METHODS #####