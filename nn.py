money_player1 = 100
money_player2 = 100

def get_rate():
    while True:
        print('Player 1 сделай свою ставку')
        stavka_player1 = int(input())
        print('Player 2 сделай свою ставку')
        stavka_player2 = int(input())
    if stavka_player1 <money_player1:
        print('Нехватает баланса')
        continue
    if stavka_player2 <money_player2:
        print('не хватает денег')
        continue
    if stavka_player1 != stavka_player2:
        print('Ставка должна быть одинакова для игроков')
        continue
        return stavka_player1
get_rate()
