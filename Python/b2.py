while True:
  try:
    a = float(input('a: '))
    b = float(input('b: '))
    break
  except:
    print('a b phai la cac so thuc hoac nguyen')

print('nghiem pt %.2fx' % a, '-' if b < 0 else '+', '%.2f = 0 la x = %.2f' % (b if b >= 0 else b * (-1), -b/a) if a != 0 else ('vo so nghiem' if b == 0 else 'vo nghiem'))