while True:
  try:
    a = float(input('a: '))
    b = float(input('b: '))
    break
  except:
    print('a b phai la cac so thuc hoac nguyen')

print('\nres:')
print('%.2f + %.2f = ' %(a, b), a + b)
print('%.2f - %.2f = ' %(a, b), a - b)
print('%.2f * %.2f = ' %(a, b), a * b)
print('b = 0, khong the chia' if b == 0 else '%.2f / %.2f = %.2f' %(a, b, a/b))

