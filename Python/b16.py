def sum_uc(n):
  s = 0
  for i in range(1,n):
    if n % i == 0:
      s += i 
  return s

while True:
  try:
    n = int(input('n = '))
    if n <= 0:
      raise Exception
    break
  except:
    print('n phai la so nguyen duong')

print('%d la so hoan hao' %(n) if sum_uc(n) == n else '%d ko phai so hoan hao' %(n))

