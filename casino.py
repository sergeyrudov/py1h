from random import randint
money = 100

def get_result(num):
    r = randint(1,9)
    if num == r:
        print('ugadal')
    else:
        print('neugadal')
    if num !=r:
            print (money-num)
    else:
        print(money*3)



def main():
    while True:
        print('Вывести число от 1 до 9')
        num = int(input())
        get_result(num)

print(main())
