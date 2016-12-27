#math =(input().split(' '))

def plus_and_minus(l):
    try:
        while len(l)!=1:
            if l[1] == 'plus':
                result = float(l[0]) + float(l[2])
                del l[0:3]
                l.insert (0, str(result))
            elif l[1] == 'minus':
                result = float(l[0])- float(l[2])
                del l[0:3]
                l.insert(0, str(result))
            else:
                print('ошибка данных')
                return
    except ValueError: print('Какулькулятор принимает только числовые значения')
    except ZeroDivisionError: print('нельзя делить на ноль')
    except IndexError: print('Должно быть два числа')
    return l





def multiply_and_divide(l):
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
    result = plus_and_minus(result)
    return result

math = '5 multiply 3 divide 3 plus 3'.split()
print (result_math(math))