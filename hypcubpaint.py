import numpy

def paint(hypcubdem):
  hypcub = numpy.array([0], float)
  partvol = 1
  i = 0
  while i < len(hypcubdem):
    l = 0
    subcub = hypcub
    while l < hypcubdem[i]-1:
      subcub = numpy.append(subcub, hypcub)
      l += 1
    hypcub = subcub
    hypcub[:partvol] += 1
    hypcub[-partvol:] += 1
    partvol = partvol*hypcubdem[i]
    i += 1
  d = 0
  while d <= len(hypcubdem):
    sCount = 0
    for i in hypcub:
      if i == d:
        sCount += 1
    print("There are " + str(sCount) + " " + str(len(hypcubdem)) + "-cubes with " + str(d) + " sides painted in a " + str(hypcubdem) + " square/cube/tesseract/other object")
    d += 1
  
paint([4, 4, 4, 4, 4, 4, 4, 4])