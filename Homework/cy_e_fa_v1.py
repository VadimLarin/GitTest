player1, player2 = input().split(" ")
player1 = player1.lower()
player2 = player2.lower()

def winner(player1,player2):
    if (player1 == 'камень' and player2 == 'ножницы') or (player1 == 'ножницы' and player2 == 'бумага') or (player1 == 'бумага' and player2 == 'камень'):
        return 'игрок 1 выиграл'
    elif (player1 == 'камень' and player2 == 'камень') or (player1 == 'ножницы' and player2 == 'ножницы') or (player1 == 'бумага' and player2 == 'бумага'): 
        return 'ничья'
    else:
        return 'игрок 2 выиграл'
    
print(winner(player1,player2))
