import math

def data(start, end, bins):#, a=1, b=-9, c=18, d=9, e=-92, f=1):
  data = []
  n = (end-start) // bins
  for x in range(start,end+1,n):
    poly = x*math.sin(x)
    data.append([x,poly])
  return data

for x in data(0,15,9):
  print(x)
