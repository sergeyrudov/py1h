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
get_rate()

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
    cube3 = randint(1, 6)
    cube4 = randint (1,6)
    print(' Кубики покатились и выпало {0} и {1} очков'.format(cube3, cube4))
    result = result+cube3+cube4
    print('Результат второго раунда {0} очков'.format(result))
    print ('Для того чтобы начать третий раунт нажмите Энтер')
    input()
    cube5 = randint(1, 6)
    cube6 = randint(1, 6)
    print('Кубики покатились и выпало {} и {} очков'.format(cube5, cube6))
    result = result+cube5+cube6
    print('Результат третьего раунда {0} очков'.format(result))
    print('результаты игры {0}'.format(result))
throw_dice()

def check_step(stavka_player1, stavka_player2, rate):
    global money_player1
    global money_player2
    p1 =
    p2 = stavka_player2
    rate = stavka_player1
    print(' Результат первого игрока {0} очков . Результат второго игрока {1} очков'.format(p1, p2))
    if p1>p2:
         money_player1 = money_player1+p2
         print('Победил игрок №1')
    elif p1<p2:
        money_player2 = money_player2 +p1
        print('Победил игрок №2')
    else:
        print('Ничья!')


check_step(1, 1)
