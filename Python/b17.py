def solve(init, n):
  if n == 0 or n == 1:
    return 1
  if n == 2:
    return 2
  res = 1
  for i in range(init, n+1, 2):
    res *= i 
  return res

while True:
  try:
    n = int(input('n = '))
    if n < 0:
      raise Exception
    break 
  except:
    print('n phai la so nguyen khong am')

print('%d!! =' %(n), solve(1,n) if n % 2 != 0 else solve(2,n))