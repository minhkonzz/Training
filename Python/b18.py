def is_prime(n):
  if n == 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

while True:
  try:
    n = int(input('n = '))
    if n <= 0:
      raise Exception
    break
  except:
    print('n phai la so nguyen duong')

print('%d la so nguyen to' %(n) if is_prime(n) else '%d khong la so nguyen to' %(n))

