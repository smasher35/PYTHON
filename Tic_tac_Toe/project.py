import random
from typing import ValuesView

def game_header():
    print('***************************************')
    print('*    X         O             X        *')
    print('*  O     X        X      O      O     *')
    print('*                                     *')
    print('*   WELCOME TO THE TIK TAK TOE GAME   *')
    print('*                                     *')
    print('*    X         O             X        *')
    print('*  O     X        X      O      O     *')
    print('***************************************')

def display_board(board):
    print('\n'*100)
    print('X  THE TIK TAK TOE BOARD   O')
    print('----------------------------\n')
    print('      |       |       ')
    print(' ', board[7],' ', '|',' ', board[8],' ','|', ' ', board[9], ' ')
    print('      |       |       ')
    print('----------------------')
    print('      |       |       ')
    print(' ', board[4],' ', '|', ' ', board[5],' ','|', ' ', board[6], ' ')
    print('      |       |       ')
    print('----------------------')
    print('      |       |       ')
    print(' ', board[1], ' ', '|', ' ', board[2], ' ', '|', ' ', board[3], ' ')
    print('      |       |       ')
    


def player_input():
    validChoice=['X','O']
    choice = 'wrong'
    while choice not in validChoice:
        choice = input("Please pick a marker 'X' or 'O': ").upper()

        if choice not in validChoice:
            print("Please just use 'X' or 'O'")

    return choice


def place_marker(game_board, marker, position):
    
   
    game_board[int(position)] = marker
    return game_board

def player_choice(game_board):
    validPositions = ['1','2','3','4','5','6','7','8','9']
    position = 'wrong'
    freeSpot =  False
    
    demo_board()

    while position not in validPositions or position.isdigit() == False or freeSpot == False:
        position = input('Please insert the position to insert the marker (1-9): ')

        print(position)
        if position.isdigit() == False:
            print("Please insert a valid position (1-9)")
        

        if position not in validPositions:
            print('Please insert valid position between 1 - 9!!')

        freeSpot = space_Check(game_board,position)
        if freeSpot:
            freeSpot = True
        else:
            freeSpot = False
            print("The current Position is not empty, please choose another position")

    return position


def win_check(gameBoard, marker):
    
    if gameBoard[1] == marker and gameBoard[2] == marker and gameBoard[3]== marker:
        return True
    elif gameBoard[4] == marker and gameBoard[5] == marker and gameBoard[6]== marker:
        return True
    elif gameBoard[7] == marker and gameBoard[8] == marker and gameBoard[9]== marker:
        return True
    elif gameBoard[1] == marker and gameBoard[4] == marker and gameBoard[7]== marker:
        return True
    elif gameBoard[2] == marker and gameBoard[5] == marker and gameBoard[8]== marker:
        return True
    elif gameBoard[3] == marker and gameBoard[6] == marker and gameBoard[9]== marker:
        return True
    elif gameBoard[1] == marker and gameBoard[5] == marker and gameBoard[9]== marker:
        return True
    elif gameBoard[3] == marker and gameBoard[5] == marker and gameBoard[7]== marker:
        return True
    else:
        return False


def choose_first():
    player =  random.randint(1,2)

    if player == 1:
        return "Player 1"
    else:
        return "Player 2"
    


def space_Check(gameBoard, position):
    position = int(position)
    if gameBoard[position] == ' ':
        return True
    else:
        return False

def full_board_check(gameBoard):
    isBoardFull = False

    if ' ' in gameBoard:
        return False
    else:
        return  True


def replay():
    validChoices=['Y','N']
    choice = 'Wrong'
    while choice not in validChoices:
        choice = input("Do You want to play again?? (Y or N): ").upper()

        if choice not in validChoices:
            print("Please shoose Y or N")

    if choice == 'Y':
        return True
    else: 
        return False
        
def demo_board():
    print("\n[+] - Board Positions -")
    print("7|8|9")
    print('-----')
    print("4|5|6")
    print('-----')
    print("1|2|3\n")

while True:
    game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    game_on = True
    game_header()
    playerTurn = choose_first()
    print(playerTurn, "is the first to Play")
    p1marker=''
    p2marker=''
    turn=0
    fullBoard= False
    if playerTurn == 'Player 1':
        turn=1
        p1marker = player_input()
        if p1marker == 'X':
            p2marker = 'O'
        else:
            p2marker ='X'
    else:
        p2marker = player_input()
        turn = 2
        if p2marker == 'X':
            p1marker = 'O'
        else:
            p1marker = 'X'

    while game_on:
        #Player1 Turn
        if turn == 1:
            fullBoard = full_board_check(game_board)
            if fullBoard == False:
                print("[+] Player 1")
                p1Position =  player_choice(game_board)
                game_board = place_marker(game_board,p1marker,p1Position)
                display_board(game_board)
                win1 = win_check(game_board,p1marker)
                if win1 == True:
                    print("[+] PLAYER 1 IS THE CHAMPION")
                    game_on = False
                turn = 2
            else:
                print("The Gabe Board is Full - GAME OVER!!")
                game_on = False
        #player2 turn
        else:
            fullBoard = full_board_check(game_board)
            if fullBoard == False:
                print("[+] Player 2")
                p2Position =  player_choice(game_board)
                game_board = place_marker(game_board,p2marker,p2Position)
                display_board(game_board)
                win2 = win_check(game_board,p2marker)
                if win2 == True:
                    print("[+] PLAYER 2 IS THE CHAMPION")
                    game_on = False
                turn = 1
            else:
                print("The Gabe Board is Full - GAME OVER!!")
                game_on = False
            
    if not replay(): 
        break

        









