while True:
  try:
    n = int(input('n = '))
    if n <= 0 or type(n) is float:
      raise Exception
    break
  except:
    print('n phai la so nguyen ko am')

for i in range(-n, 0):
  print('*' * (-i))