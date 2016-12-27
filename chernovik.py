def multiply_and_divide(l):
    #if l.count('divide') ==0 and l.count('multiply') ==0:
       # print('опечатка в команде умножения или деления')
    #while l.count('divide')==0:
        #print('операции деления не найдено')
    #while l.count('multiply')==0:
            #print ('операции умножения не найдено')
    for l[1] in l:
        if l.count('divide')==0:
            print('операции деления не найдено')
            while l.count('divide')>0:
                 index = l.index('divide')
                 result = float(l[index-1]) / float (l[index+1])
                 del l[index-1:index+2]
                 l.insert(index-1, str(result))
            while l.count('multiply')>0:
                index = l.index('multiply')
                result = float(l[index-1]) * float (l[index+1])
                del l [index-1:index+2]
                l.insert(index-1, str(result))
    return l

def result_math(l):
    result = multiply_and_divide(l)
    return result




math = '6 divide 3'.split()
print (result_math(math))

