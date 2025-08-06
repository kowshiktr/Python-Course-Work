import random
import sys

def dice():
    return random.randint(1,6)

def first_player_turn():
    global player1_score
    player1_status=input(f"{player1}: Want to [C]ontinue or [S]top: ").upper()
    if player1_status=='C':
        player1_turn=dice()
        player1_score+=player1_turn
        if player1_score in snakes:
            player1_score=snakes[player1_score]
            print(f"\n{player1}'s turn:\nDice: {player1_turn}\n---Snake bite---\nBoard position: {player1_score}")
        elif player1_score in ladders:
            player1_score=ladders[player1_score]
            print(f"\n{player1}'s turn:\nDice: {player1_turn}\n*****Ladder*****\nBoard position: {player1_score}")
        else:
            print(f"\n{player1}'s turn:\nDice: {player1_turn}\nBoard position: {player1_score}")
    elif player1_status=='S':
        print(f'\n{player1} quit the game.\n{player2} Won the game!!!')
        sys.exit()

def second_player_turn():
    global player2_score   
    player2_status=input(f"{player2}: Want to [C]ontinue or [S]top: ").upper()
    if player2_status=='C':
        player2_turn=dice()
        player2_score+=player2_turn
        if player2_score in snakes:
            player2_score=snakes[player2_score]
            print(f"\n{player2}'s turn:\nDice: {player2_turn}\n---Snake bite---\nBoard position: {player2_score}")
        elif player2_score in ladders:
            player2_score=ladders[player2_score]
            print(f"\n{player2}'s turn:\nDice: {player2_turn}\n*****Ladder*****\nBoard position: {player2_score}")
        else:
            print(f"\n{player2}'s turn:\nDice: {player2_turn}\nBoard position: {player2_score}")
    elif player2_status=='S':
        print(f'\n{player2} quit the game.\n{player1} Won the game!!!')
        sys.exit()



player1=input("Enter the player-1: ")
player2=input("Enter the player-2: ")

player1_score=0
player2_score=0

winning_point=100

snakes={99:23,81:17,72:64,67:14,56:32,48:12,34:3,25:19,16:9}
ladders={7:19,18:77,23:85,31:44,45:71,54:63,61:94,78:88,89:93}


while player1_score<winning_point and player2_score<winning_point:
    first_player_turn()
    second_player_turn()        
else:
    if player1_score>player2_score:
        print(f"\n\n{player1} Win the game!!!!!!")
    elif player1_score==player2_score:
        print(f"\n\nTie!!!!!!")
    else:
        print(f"\n\n{player2} Win the game!!!!!!")

'''
output:
Enter the player-1: Kowshik
Enter the player-2: Manju
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 2
Board position: 2
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 5
Board position: 5
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 4
Board position: 6
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 1
Board position: 6
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 3
Board position: 9
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 2
Board position: 8
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 1
Board position: 10
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 5
Board position: 13
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 1
Board position: 11
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 1
Board position: 14
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 1
Board position: 12
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 2
---Snake bite---
Board position: 9
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 3
Board position: 15
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 2
Board position: 11
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 4
Board position: 19
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 5
---Snake bite---
Board position: 9
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 2
Board position: 21
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 4
Board position: 13
Kowshik: Want to [C]ontinue or [S]top: c 

Kowshik's turn:
Dice: 6
Board position: 27
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 2
Board position: 15
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 2
Board position: 29
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 3
*****Ladder*****
Board position: 77
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 1
Board position: 30
Manju: Want to [C]ontinue or [S]top: c 

Manju's turn:
Dice: 2
Board position: 79
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 5
Board position: 35
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 4
Board position: 83
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 2
Board position: 37
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 3
Board position: 86
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 2
Board position: 39
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 4
Board position: 90
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 6
*****Ladder*****
Board position: 71
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 6
Board position: 96
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 4
Board position: 75
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 3
---Snake bite---
Board position: 23
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 4
Board position: 79
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 6
Board position: 29
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 6
Board position: 85
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 6
Board position: 35
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 3
Board position: 88
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 4
Board position: 39
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 2
Board position: 90
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 1
Board position: 40
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 5
Board position: 95
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 1
Board position: 41
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 1
Board position: 96
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 5
Board position: 46
Kowshik: Want to [C]ontinue or [S]top: c

Kowshik's turn:
Dice: 5
Board position: 101
Manju: Want to [C]ontinue or [S]top: c

Manju's turn:
Dice: 5
Board position: 51


Kowshik Win the game!!!!!!
'''
    

