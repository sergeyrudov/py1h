from random import randint
money_player1 = 100
money_player2 = 100

def get_rate():
    while True:
        print('Player 1 сделай свою ставку')
        stavka_player1 = int(input())
        if stavka_player1 > money_player1:
            print('Нехватает баланса')
            continue
        print('Player 2 сделай свою ставку')
        stavka_player2 = int(input())
        if stavka_player2 > money_player2:
            print('не хватает денег')
            continue
        if stavka_player1 != stavka_player2:
            print('Ставка должна быть одинакова для игроков')
            continue
        return stavka_player1


def throw_dice():
    print('для того чобы бросить кубики нажмите Энтер')
    input()
    cube1 = randint(1, 6)
    cube2 = randint(1,6)
    print( ' Кубики покатились и выпало {0} и {1}'.format(cube1, cube2))
    result =  cube1+ cube2
    print ('Результат первого раунда {0} очков'.format(result))
    print ('Для начала второго раунда нажмите Энтер')
    input()
    cube1 = randint(1, 6)
    cube2 = randint (1, 6)
    print(' Кубики покатились и выпало {0} и {1} очков'.format(cube1, cube2))
    result = result+cube1+cube2
    print('Результат второго раунда {0} очков'.format(result))
    print ('Для того чтобы начать третий раунт нажмите Энтер')
    input()
    cube1 = randint(1, 6)
    cube2 = randint(1, 6)
    print('Кубики покатились и выпало {} и {} очков'.format(cube1, cube2))
    result = result+cube1+cube2
    print('Результат третьего раунда {0} очков'.format(result))
    print('результаты игры {0}'.format(result))
    return result




def check_step(p1, p2, rate):
    global money_player1
    global money_player2

    print(' Результат первого игрока {0} очков . Результат второго игрока {1} очков'.format(p1, p2))
    if p1>p2:
         money_player1 = money_player1+(money_player2- rate)
         print('Победил игрок №1')
    elif p1<p2:
        money_player2 = money_player2+ (money_player1-rate)
        print('Победил игрок №2')
    else:
        print('Ничья!')


def main():
    while money_player1 !=0:
        rate = get_rate()
    print(' Сейчас ход игрока №1')
    p1 = throw_dice()
    print(' Сейчас ходит игрок №2')
    p2 = throw_dice()
    return (p1,p2,rate)
main()









