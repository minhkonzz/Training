import math

while True:
  try:
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    break
  except:
    print('a b c phai la cac so thuc hoac nguyen')

if a > 0 and b > 0 and c > 0 and a+b > c and b+c > a and a+c > b:
  print('a b c la 3 canh tam giac')
  cv = a+b+c
  p = cv/2
  print('chu vi: %.2f\ndien tich: %.2f' % (cv, math.sqrt(p*(p-a)*(p-b)*(p-c))))
else:
  print('a b c ko thoa man 3 canh tam giac')