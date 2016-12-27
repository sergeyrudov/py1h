from random import randint

def randomsharik():
 while True:
  a = ['слева','справа','сверху','снизу']
  b = randint(0, 3)
  print ('Шарик прилетел {}'.format(a[b]))
  d= ['влево', 'вправо', 'вверх', 'вниз']
  c = input()
  e = d.index(c)
  if b == e:
   print('ОШибка! Игра окончена!')
   break
  else:
   print('Шарик улетел {0}'.format(c))


randomsharik()