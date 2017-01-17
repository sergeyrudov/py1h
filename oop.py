from random import randint
#dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other.
#  Существующие ключи перезаписываются. Возвращает None (не новый словарь!).

char = {'position':100,'inventory':['erhreh','erehhhrhrh','erherhrehhh44']}
item = ['меч','топор','булава','цепь','книга','плащ','огнемет']

#def tratata():
#    print (char.get('inventory'))
#tratata()
#def counting_sort(sample):
#    count = {}
 #   for i in sample:
 #       count[i] = count.get(i, 0)+1
 #   print(count)
#sample = [1, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7]
#count = {1: 3, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 1}


#def look_for_inventory(command):
    if char.get('inventory') == []:
        print ('инвентарь пустой')
    else:
        print('У вас в инвентаре - {0}'.format(char.get('inventory')))

def look_for_inventory():
    a = char['inventory']
    c = 1
    for i in a:
        print("{0} | {1}  ".format(c, i))
        c = c + 1
look_for_inventory()