import numpy as np

def without_numpy(n):
  r = range(2, n+2 if n % 2 == 0 else n, 2)
  return sum(r)/len(r)

def use_numpy(n):
  return 2.0 if n == 2 or n == 4 else np.arange(2, n+2 if n % 2 == 0 else n, 2).mean()

while True:
  try:
    n = int(input('n = '))
    if n < 2:
      raise Exception
    break
  except:
    print('n phai la so nguyen > 2')

# ko sử dụng numpy
print('mean ko su dung numpy:', without_numpy(n))

# sử dụng numpy
print('mean su dung numpy:', use_numpy(n))