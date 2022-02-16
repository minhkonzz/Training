def find_ucln(a, b):
  for i in range(-a if a < b else -b, -1):
    if a % (-i) == 0 and b % (-i) == 0:
      return -i
  return 1

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
print('ucln cua %d va %d la:' %(a, b), uc)
print('bcnn cua %d va %d la:' %(a, b), (a * b)/uc)


