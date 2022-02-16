def solve(n):
  s = 0
  while n != 0:
    a = n % 10
    n //= 10
    s += a ** 3
  return s


while True:
  try:
    n = int(input('n = '))
    if n <= 99 or n >= 1000:
      raise Exception
    break
  except:
    print('n phai la so nguyen duong co 3 chu so')

print('tong lap phuong cac chu so cua %d la' % n, solve(n))