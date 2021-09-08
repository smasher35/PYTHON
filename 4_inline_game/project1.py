"""
    - Pirple Python Course
    - Input and Output PROJECT #1
    - Programmed by: Paulo Penicheiro
    - Date: January, 19th 2021
"""

import sys
from termcolor import colored, cprint


def drawBoard(currentBoard):
    player1Piece = colored(u'\u2B24','green')
    player2Piece = colored(u'\u2B24', 'red')
    # Game Piece - print(u'\u2B24')
    #14 Columns
    #12cl Rows
    #012345678910111213
    # | | | | | | | 0
    #-------------- 1
    # | | | | | | | 2
    #-------------- 3
    # | | | | | | | 4
    #-------------- 5
    # | | | | | | | 6
    #-------------- 7
    # | | | | | | | 8
    #-------------- 9
    # | | | | | | | 10
    #-------------- 11

    for row in range(12):
        if row % 2 == 0:
            praticalRow = int(row/2)
            for column in range(14):
                if column % 2 == 0:
                    praticalColumn = int(column /2)
                    print(currentBoard[praticalRow][praticalColumn], end="")
                else:
                    if column != 13:
                        print(colored("|",'yellow'), end="")
                    else:
                        print(colored("|",'yellow'))
        else:
            print(colored("--------------", 'yellow'))
            
            
def detectFreePosition(currentBoard, selectedColumn):
    freeCell = 5
    
    for row in range(6):
        for column in range(7):
            if column == selectedColumn:
                if currentBoard[row][column] != " ":
                    freeCell -= 1
                                
    return freeCell
                    
    
def checkForWinner(winnerBoard):
    currentWinner=0
    global Game
    
    for row in range(6):
        for column in range(7):
            #VERTICAL CHECK
            if row <= 2:
                if winnerBoard[row][column] == winnerBoard[row+1][column]  and winnerBoard[row+2][column] == winnerBoard[row][column] and winnerBoard[row][column] == winnerBoard[row+3][column]:
                    if winnerBoard[row][column] == 1:
                        currentWinner = 1;
                        break
                        
                    if winnerBoard[row][column] == 2:
                        currentWinner = 2
                        break
            
            #HORIZONTAL CHECK
            if column <= 3: 
                if winnerBoard[row][column] == winnerBoard[row][column+1]  and winnerBoard[row][column] == winnerBoard[row][column+2] and winnerBoard[row][column] == winnerBoard[row][column+3]:
                    if winnerBoard[row][column] == 1:
                        currentWinner = 1;
                        break
                    
                    if winnerBoard[row][column] == 2:
                        currentWinner = 2
                        break
    #DIAGONAL RIGHT CHECK              
    for row in range(5,0, -1):
        for column in range(7):
            if row >= 3 and column <= 3: 
                if winnerBoard[row][column] == winnerBoard[row-1][column+1]  and winnerBoard[row][column] == winnerBoard[row-2][column+2] and winnerBoard[row][column] == winnerBoard[row-3][column+3]:
                    if winnerBoard[row][column] == 1:
                        currentWinner = 1;
                        break
                    
                    if winnerBoard[row][column] == 2:
                        currentWinner = 2
                        break
                    
    #DIAGONAL LEFT CHECK              
    for row in range(5,0, -1):
        for column in range(6,0,-1):
            if row >= 3 and column >= 3: 
                if winnerBoard[row][column] == winnerBoard[row-1][column-1]  and winnerBoard[row][column] == winnerBoard[row-2][column-2] and winnerBoard[row][column] == winnerBoard[row-3][column-3]:
                    if winnerBoard[row][column] == 1:
                        currentWinner = 1;
                        break
                    
                    if winnerBoard[row][column] == 2:
                        currentWinner = 2
                        break
                
                 
    return currentWinner                  

                
                

Game = True
Player = 1

currentBoard = [[" ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " "]]
winnerBoard = [[" ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " "]]

drawBoard(currentBoard)
player1Piece = colored(u'\u2B24','green')
player2Piece = colored(u'\u2B24', 'red')
freeCell = 0
winner = 0;
Game = True
while(Game):
    flag = True
    while(flag or freeCell == -1):
        print("[",end="")
        if Player == 1:
            print(player1Piece, end="")
        else:
            print(player2Piece, end="")
        print(f"] - Player {Player} Turn: ")
        selectedColumn = int(input("Please enter de column [1 - 7]: "))
        if(selectedColumn < 1 or selectedColumn > 7):
            print("[-] ERROR - the column must be between [1-7]")
            flag = True
        else: 
            flag = False
            
        freeCell = detectFreePosition(currentBoard, selectedColumn-1)
        if freeCell == -1 :
            print("[-] ERROR - the column is FULL, please choose another column!!")
    
            
    if Player == 1:
        # Make move for player ones
        currentBoard[freeCell][selectedColumn-1] = player1Piece
        winnerBoard[freeCell][selectedColumn-1] = 1
        Player = 2
    else:
        #make move for player topdown
        currentBoard[freeCell][selectedColumn-1] = player2Piece
        winnerBoard[freeCell][selectedColumn-1] = 2
        Player = 1
        

    drawBoard(currentBoard)
    winner = checkForWinner(winnerBoard)
    if winner == 1:
        print(colored("=============================================\n", 'magenta'))
        print(colored("      [",'magenta'),end="")
        print(player1Piece, end="")
        print(colored("] - Player 1 is the WINNER: ",'magenta'))
        print(colored("\n=============================================", 'magenta'))
        Game = False
        flag = False
    elif winner == 2:
        print(colored("=============================================\n", 'magenta'))
        print(colored("      [",'magenta'),end="")
        print(player2Piece, end="")
        print(colored("] - Player 2 is the WINNER: ",'magenta'))
        print(colored("\n=============================================", 'magenta'))
        Game = False
        flag = False
        
        
        
    #print(winnerBoard)
