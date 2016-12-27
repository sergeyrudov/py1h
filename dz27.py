"""
В следующем фрагменте, найти информацию ip адрессов и дату:
data = 'User 123.323.121.333 connected to server 02:12:2016; Admin 22.234.156.73 connected to server 25:11:2016; Spider 255.122.11.146 connected to server 19:10:2016; ' \
       'Spider -.-.-.- TryConnected to server __:__:____'
Ip-address, может состоять из набора цифр от 1 до 3 цифр в группке, разделенные точкой. группок должно быть 4. Дата записана как число:месяц:год.
Поскольку мы не умеем группировать записи по поиску, нужно будет составить два паттерна, один для поиска ip, второй для поиска дат, получить два списка для ip и дат,
после чего соединить их при помощи zip().
Таким образом, мы получим собранные данные в виде списка кортежей попарных элементов, где в одном кортеже будет ip и соответствующая дата.
"""


import re
#data = "User 123.323.121.333 connected to server 02:12:2016; Admin 22.234.156.73 connected to server 25:11:2016; Spider 255.122.11.146 connected to server 19:10:2016; ' \
#        'Spider -.-.-.- TryConnected to server __:__:____"

#ip_address = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
#data_pattern = re.compile(r'\d{2}:\d{2}:\d{4}')
#print (list(zip(ip_address.findall(data),data_pattern.findall(data))))

#def print_numbers(limit):
#    for i in range(limit):
#        print(i)

#print_numbers(0)

#site = "http://bla.ru http://bla.blabla.com https://google.com http://ya.ru"
#email = "mail@gmail.com 12123@gmail.com djdj456@yandex.ru azaza.lul.kek@mail.ua"


#emailsearch = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9._-]+@[a-zA-Z0-9][a-zA-Z0-9.-]+\.[a-z]+$')
#search = re.compile(r'https?://\w*.\w*.?\.\w*\w+.?')
#pattern = re.compile(r'<div><b><p>text text text </p><b><')

#print(search.findall(site))
#print(emailsearch.match('bla@bla.ru'))

path_file = r'd:\vv.csv'


#f = open(path_file, 'r')
#print (list((f).split';')


def parse_csv(path):
    f = open(path, 'r')
    body = f.read().split('\n')
    result = []
    for i in body:
        if i =='':
            continue
        result.append(i.split(';'))
    return result
t = parse_csv(path_file)
print(t)
parse_csv(path_file)

def len_column(t):
    return len(t[0])

def len_lines(t):
    return len(t)

def get_headers(t):
    return t[0]

def get_line(number,t):
    return t[number-1]

#def get_cell(column,):






