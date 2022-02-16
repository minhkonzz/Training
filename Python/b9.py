def find_ucln(a, b):
  while b != 0:
    t = a % b
    a = b
    b = t
  return a

while True:
  try:
    a = int(input('a = '))
    b = int(input('b = '))
    if a <= 0 or b <= 0:
      raise Exception
    break
  except:
    print('a b phai la cac so nguyen duong')

uc = find_ucln(a, b)
print('%d/%d sau khi rut gon la: %d/%d' % (a, b, a/uc, b/uc))


