#a = ['334','3434','345','555']
#b = []
#for i in a:
#    b.append(int(i))
#print(b)

#def mult2(x,y):
#    c = x*y
#    return c

#f = mult2(5,4)
#print (f)
import re


b = re.compile(r'[a-zA-Z][a-zA-Z0-9-]+')
c = re.compile(r'[a-zA-Z0-9]+')
d = re.compile(r'\+38-\d{3}-\d{3}-\d{2}-\d{2}')

def login(b):
    print('Введите логин')
    a = input()
    while True:
            if b.match(a):
                print('логин принят')
            else: print('логин неверный')
            break

login(b)

def password(c):
    print('\n Введите пароль')
    a = input()
    while True:
            if c.match(a):
                print('\n пароль принят')
            else: print('некорректный пароль')
            break
password(c)

def phonenumber(phone):
    print ('\n Введите телефон в формате +38-xxx-xxx-xx-xx')
    a = input()
    while True:
            if phone.match(a):
                print('номер телефона принят')
            else: print('номер некорректный')
            break
phonenumber(d)

