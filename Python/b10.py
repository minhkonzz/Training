while True:
  try:
    n = int(input('n = '))
    if n <= 0:
      raise Exception
    break
  except:
    print('n phai la nguyen duong')

s = 0
for i in range(1, n+1):
  if n % i == 0:
    s += 1

print('%d co %d uoc so duong' % (n, s))