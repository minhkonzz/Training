def is_prime(a):
  if a == 1:
    return False
  for i in range(2, a):
    if a % i == 0:
      return False
  return True

def print_primes(n): 
  for i in range(1, n+1):
    if is_prime(i):
      print(i, end=' ')

while True:
  try:
    n = int(input('n = '))
    if n <= 0:
      raise Exception
    break
  except:
    print('n phai la so nguyen duong')

print('cac so nguyen to tu 1 den %d:' %(n), end=' ')
print_primes(n)

