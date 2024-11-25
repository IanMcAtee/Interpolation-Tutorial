def bilinear_interp2(img, newShape):
  xScale = newShape[1]/img.shape[1]
  yScale = newShape[0]/img.shape[0]

  tempArr = np.zeros((img.shape[0], newShape[1]))
  for j in range(newShape[1]):
    x = (j+0.5)*(1/xScale)-0.5
    if x <= 0 or x >= img.shape[1]-1:
      tempArr[:,j] = img[:,int(x)]
      continue
    x0 = math.floor(x)
    x1 = math.ceil(x)
    if (x0 == x1):
      tempArr[:,j] = img[:,x0]
      continue
    for i in range(img.shape[0]):
      term1 = (x1-x)/(x1-x0)*img[i,x0]
      term2 = (x-x0)/(x1-x0)*img[i,x1]
      tempArr[i,j] = term1 + term2

  # Interpolate across columns
  interpImg = np.zeros((newShape[0], newShape[1]))
  for i in range(newShape[0]):
    y = (i+0.5)*(1/yScale)-0.5
    if y <= 0 or y >= img.shape[0]-1:
      interpImg[i,:] = tempArr[int(y),:]
      continue
    y0 = math.floor(y)
    y1 = math.ceil(y)
    if (y0 == y1):
      interpImg[i,:] = tempArr[y0,:]
      continue
    for j in range(newShape[1]):
      term1 = (y1-y)/(y1-y0)*tempArr[y0,j]
      term2 = (y-y0)/(y1-y0)*tempArr[y1,j]
      interpImg[i,j] = term1 + term2
  return interpImg