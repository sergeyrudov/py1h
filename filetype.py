def func(path1, path2):
  try:
    f = open(path1,'r',encoding='utf-8')
    n = f.readlines()[1]
    if n != '\n':
        n2 = open(path2,'r', encoding='utf-8')
        n3 = n2.readlines()
    elif n =='\n':
        print('Файл пустой, вставлять нечего')
    if n != n3[1]:
        n3.insert(1, n)
        n2 = open(path2,'w', encoding='utf-8')
        n2.writelines(n3)
    else: print('Инсерстить или нет?')
    user = input()
    if user =='y':
        n2 = open(path2, 'w', encoding='utf-8')
        n2.writelines(n3)
        n2.close()
  except IndexError: print('Error')
  except FileNotFoundError: print('файл не найден')




func (r'd:/test/text1.txt',r'd:/test/text2.txt')







#print(f)
#print(f.read())
#print(n)