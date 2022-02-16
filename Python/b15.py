def solve(n):
  n_rev = 0
  while n != 0:
    m = n % 10
    n_rev = n_rev * 10 + m
    n //= 10
  return n_rev

while True:
  try:
    n = int(input('n = '))
    if n <= 100:
      raise Exception
    break
  except:
    print('n phai la so nguyen duong > 100')

print('dao nguoc cua %d la' %(n), solve(n))

