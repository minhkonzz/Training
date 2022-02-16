while True:
  try:
    m = int(input('m = '))
    n = int(input('n = '))
    if m <= 0 or n <= 0:
      raise Exception
    break
  except:
    print('m hoac n phai la cac so nguyen duong')

for i in range(1, m+1):
  print('*' * n)

