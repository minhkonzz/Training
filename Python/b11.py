import math

def solve(a, b, c):
  if a == 0:
    return -c/b if b != 0 else ('vo so nghiem' if c == 0 else 'vo nghiem')
  delta = b*b-4*a*c
  return -b/(2*a) if delta == 0 else ('vo nghiem' if delta < 0 else (-b - math.sqrt(delta))/(2*a), (-b + math.sqrt(delta))/(2*a))


while True:
  try:
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    break
  except:
    print('a b c phai la cac so thuc hoac nguyen')

print('nghiem pt %.2fx^2' %(a), '-' if b < 0 else '+', '%.2fx' %(b * (-1) if b < 0 else b), '-' if c < 0 else '+', '%.2f = 0 la:' %(c * (-1) if c < 0 else c), solve(a,b,c))


