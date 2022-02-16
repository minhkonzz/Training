while True:
  try:
    a = float(input('a = '))
    b = float(input('b = '))
    break
  except:
    print('a or b ko hop le')

if a > 0 and b > 0 and a == b:
  print('a b thoa man cac canh hinh vuong')
  cv = a * 4
  dt = a ** 2
  print('chu vi: %.2f\ndien tich: %.2f' %(cv, dt))
else:
  print('a b ko thoa man canh hinh vuong')