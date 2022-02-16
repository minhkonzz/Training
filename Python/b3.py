import math

while True:
  try:
    x = int(input('x: '))
    if x < 0:
      raise Exception
    break
  except:
    print('x phai la so nguyen khong am')

y = int(math.sqrt(x))
print('%d la so chinh phuong' % x if y * y == x else '%d ko phai so chinh phuong' % x)