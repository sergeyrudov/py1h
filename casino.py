from random import randint
money = 100

def get_result(num, rate):
    global money
    r = randint(1,9)
    if num == r:
        print('ugadal')
    else:
        print('neugadal')
    if num !=r:
        money = money-rate
    else:
        money = money + rate *3
    print ('На вашем балансе: {0} грн'.format(money))

def main():
    while money !=0:
        print('Вывести число от 1 до 9')
        num = int(input())
        print ('Сделайте свою ставку')
        rate = int(input())
        if rate > money:
            print('Ставка превышает баланс!')
            continue
        get_result(num, rate)

print(main())
