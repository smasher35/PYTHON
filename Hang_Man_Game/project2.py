  """
    - Pirple Python Course
    - Inporting Project #2
    - Programmed by: Paulo Penicheiro
    - Date: January, 20th 2021
"""
from os import system, name
import sys
from termcolor import colored, cprint
import time
import getpass


#THE HANGMAN BOARD
# 0 1 2 3 4
# _ _ _   0    
# |    |  1
# |    O  2
# |   -|- 3
# |   / \ 4

# Fail1 = currentBoard[row][column] = 

#Final Board board = [["__", "__", "_", " "," "],["|", "  ", " ", "|", " "],["|", " ", " ", "O", " "],["|", " ", "-", "|", "-"], ["|", " ", "", " " , "\\"]] 

class Player:
    def __init__(self,name, color, score=0, fails=0):
        self.name = name
        self.score = score
        self.fails = fails
        self.player1Color = color
        
    def getScore(self):
        return self.score
    
    def getFails(self):
        return self.fails
    
    def setScore(self, value):
        self.score += value
        
    def setfails(self, value):
        self.fails += value
        
        

def clearTheScreen():
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 



def DrawBoard(currentBoard,wordToDraw,Player1Score,Player2Score):
    clearTheScreen()
    print("\n******************* WORD TO GUESS *********************\n\n")
    print("\t\t",end="")
    for letter in wordToDraw:
        print(letter, end='')

            
    print("\n\n============== THE HANGMAN GALLOWES ===================\n")
    
    print("Player 1 - Score: ", Player1Score)
    print("Player 2 - Score: ", Player2Score)
    print("")
    for row in range(5):
        for column in range(5):
            if column != 4:
                print (colored(currentBoard[row][column], 'red'), end="")
            else:
                print(colored(currentBoard[row][column],'red')) 
    print(colored("-----------------", 'red'))
    

def drawWordDashes(wordList):
    for letter in wordList:
        if letter == " ":
            wordToDraw.append(" ")
        else:
            wordToDraw.append("_")
    
    return wordToDraw

def findLettersInTheWord(letter):
    countFoundLetters= 0
    iterator=0
    indexes=[]
    for l in wordToGuess:
        if l == letter:
            countFoundLetters+=1
            indexes.append(iterator)
        iterator += 1
                      
    return countFoundLetters, indexes
            

def PlayTurn(PlayerTurn, wordToGuessLen):
    global winner
    global wordLen
    global letterCount
    global wordToDraw
    global wordToGuess
    letter = input("Please Type a Letter: ")
    letter = letter.upper()
    counter, indexList = findLettersInTheWord(letter)
    
    if counter == 0:
        print ("NO LETTER FOUND")
        if PlayerTurn == 1:
            Player1.setScore(-5)
            Player1.setfails(1)
            fails = Player1.getFails()
            
        else:
            Player2.setScore(-5)
            Player2.setfails(1)
            fails = Player2.getFails()
        
        if fails == 1:
            currentBoard[2][3]="O"
            DrawBoard(currentBoard, wordToDraw, Player1.getScore(),Player2.getScore())
            return True
        elif fails == 2:
            currentBoard[3][3]="|"
            DrawBoard(currentBoard, wordToDraw, Player1.getScore(),Player2.getScore())
            return True
        elif fails == 3:
            currentBoard[3][2]="-"
            DrawBoard(currentBoard, wordToDraw, Player1.getScore(),Player2.getScore())
            return True
        elif fails == 4:
            currentBoard[3][4]="-"
            DrawBoard(currentBoard, wordToDraw, Player1.getScore(),Player2.getScore())
            return True
        elif fails == 5:
            currentBoard[4][2]="/"
            DrawBoard(currentBoard, wordToDraw, Player1.getScore(),Player2.getScore())
            return True
        elif fails == 6:
            currentBoard[4][4]="\\"
            DrawBoard(currentBoard, wordToDraw, Player1.getScore(),Player2.getScore())
            winner = 0
            return False
            
    else:
        for i in indexList:
            wordToDraw[i]= letter
        letterCount += counter   
        if PlayerTurn == 1:
            DrawBoard(currentBoard, wordToDraw, Player1.getScore(),Player2.getScore())
            counter = 0
            if letterCount == wordLen :
                winner = 1
                Player1.setScore(100)
                return False
            else:
                return True
        else:
            DrawBoard(currentBoard, wordToDraw, Player1.getScore(),Player2.getScore())
            counter = 0
            if letterCount == wordLen :
                Player2.setScore(100)
                winner = 1
                return False
            else:
                return True
        


def CreateWordToGuessList(word): 
    listOfLetters = []
    for letter in word:
        letter = letter.upper()
        listOfLetters.append(letter) 
        
    return listOfLetters        

def drawNewGameHeader():
    print("***********************************************")
    print("*                                             *")
    print("*                 NEW GAME                    *")
    print("*                                             *")
    print("***********************************************")
        
        
def drawWinnerLooserHeader(player, points):
    if winner == 0:
        print("***********************************************")
        print(f"*  {player} LOST -DID NOT GUESSED THE WORD    *")
        print(f"*   {player}: {points} points                 *")
        print("*                                             *")
        print("***********************************************\n\n")
    else:
        print("***********************************************")
        print(f"*   {player} WON -  GUESSED THE WORD           *")
        print(f"*   {player}: {points} points                 *")
        print("*                                             *")
        print("***********************************************\n\n")
        
        
def resetGame():
    global wordToGuess
    global wordToDraw
    global letterCount
    global currentBoard
    global startBoard
    global winner
    
    wordToGuess=[]
    wordToDraw=[]
    letterCount=0
    currentBoard = startBoard
    winner = 0
    
    
#----------------------------------------------------------------------- MAIN ---------------------------------------------------------------------------------------------------

startBoard = [["__", "__", "_", " "," "],["|", "  ", "|", " ", " "],["|", " ", " ", " ", " "],["|", " ", " ", " ", " "], ["|", " ", " ", " " , " "]] 
currentBoard = [["__", "__", "_", " "," "],["|", "  ", "|", " ", " "],["|", " ", " ", " ", " "],["|", " ", " ", " ", " "], ["|", " ", " ", " " , " "]] 
wordToGuess=[]
wordToDraw=[]
indexList=[]
TotFails = 6
letterCount= 0
Player1 = Player("Player1", colored(u'\u2B24','green'))
Player2 = Player("Player2", colored(u'\u2B24', 'yellow'))
Player1Score = 0
Player2Score = 0
wordLen=0
lettersFound = 0
PlayerTurn=1
winner = 0
Game = True
PlayerTurn = 1
while(Game):
    turn = True
    if PlayerTurn == 1:
        drawNewGameHeader()
        print(f"[{Player1.player1Color}] - {Player1.name} Turn: ")
        word = getpass.getpass('Please type a word [Your typing is hidden]: ')
        #word = input("Please Type a Word: ")
        print(chr(27) + "[2J") 
        wordToGuess = CreateWordToGuessList(word)
        PlayerTurn = 2
    else:
        drawNewGameHeader()
        print(f"[{Player2.player1Color}] - {Player2.name} Turn: ")
        word = getpass.getpass('Please type a word [Your typing is hidden]: ')
        print(chr(27) + "[2J") 
        wordToGuess = CreateWordToGuessList(word)
        PlayerTurn = 1
        
    wordToDraw = drawWordDashes(wordToGuess)
    DrawBoard(currentBoard, wordToDraw, Player1.getScore(),Player2.getScore())
    wordLen = len(wordToGuess)
    while(turn): 
        if PlayerTurn == 1:
            print(f"[{Player1.player1Color}] - {Player1.name} Turn: ")
            turn = PlayTurn(PlayerTurn,wordLen)
            if turn == False:
                points = Player1.getScore()
                drawWinnerLooserHeader("Player1", points)
                resetGame()
                print(f"[{Player2.player1Color}] - {Player2.name} Your Turn is Over!!")
                break
        else:
            print(f"[{Player2.player1Color}] - {Player2.name} Turn: ")
            turn = PlayTurn(PlayerTurn, wordLen)
            if turn == False:
                points = Player2.getScore()
                drawWinnerLooserHeader("Player2", points)
                resetGame()
                print(f"[{Player2.player1Color}] - {Player2.name} Your Turn is Over!!")
                break
        
        
            
        
                
                
        
        
    

    