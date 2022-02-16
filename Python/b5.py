import math

while True:
  try:
    n = int(input('n = '))
    if n <= 0 or type(n) is float:
      raise Exception
    break
  except:
    print('n phai la so nguyen ko am')

print('%d! =' % n, math.factorial(n))

