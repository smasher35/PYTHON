"""
    - Pirple Python Course
    - Final Project 
    - Programmed by: Paulo Penicheiro
    - Date: January, 31th 2021
"""
from os import system, name
from time import sleep
from random import shuffle
from termcolor import colored, cprint


def CreateDeck():
    clubs = colored(u'\u2663','green')
    spades = colored(u'\u2660','green')
    diamonds = colored(u'\u2666','red')
    hearts = colored(u'\u2665','red')
    Deck = []

    faceValues = ["A","J","Q","K"]
    for i in range(4): #There are 4 differente suites
        for card in range(2,11): #addinf cards numbers
            if i == 0:
                Deck.append(str(card)+ clubs)
            elif i == 1:
                Deck.append(str(card)+ spades)
            elif i == 2:
                Deck.append(str(card)+ diamonds)
            else:
                Deck.append(str(card)+ hearts)


        for card in faceValues: #cards with figures Aces Kings Queens and jacks
            if i == 0:
                Deck.append(card + clubs)
            elif i == 1:
                Deck.append(card + spades)
            elif i == 2:
                Deck.append(card + diamonds)
            else:
                Deck.append(card + hearts)
           

    shuffle(Deck)
    return Deck

def clearTheScreen():
    # for windows f
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posixf') 
    else: 
        _ = system('clear') 



def appHeader():
    print("===========================================================")
    print("|                                                         |")
    print("|                     CARD WAR GAME                       |")
    print("|                                                         |")
    print("===========================================================")


def gameModes():
    flag = True
    while(flag):
        appHeader()
        print("")
        print("GAME MODES\n--------------------")
        print("\n1 - One Player Mode")
        print("2 - Two Player Mode")
        print("3 - Game Rules")
        print() 
        try:
            gameMode = int(input("Please choose your game mode: "))
        except Exception as e:
            print(str(e))
            gameMode = 4

        if gameMode >= 1 and gameMode <= 3:
            flag = False
            if gameMode == 1:
                playerOneMode()
            elif gameMode ==2:
                print("\n[!] - WARNING: 2 Plater Mode Option - NOT IMPLEMENTED")
            else:
                flag = True
                clearTheScreen()
                appHeader()
                GameRules()
                

        else:
            flag = True
            print("\n[-] - ERROR: please choose an option between [1-2]")
            sleep(2)
            clearTheScreen()



def GameRules():
    clearTheScreen()
    flag = True
    while(flag):
        appHeader()
        print("\n----------------------------------------------------------------------------------------------------------")
        print("The goal is to be the first player to win all 52 cards")
        print("\nTHE DEAL")
        print("The deck is divided evenly, with each player receiving 26 cards, dealt one at a time, face down. Anyone may deal first. Each player places their stack of cards face down, in front of them.")
        print("\nTHE PLAY\n")
        print("Each player turns up a card at the same time and the player with the higher card takes both cards and puts them, face down, on the bottom of his stack.")
        print("If the cards are the same rank, it is War. Each player turns 2 cards face down and one card face up. The player with the higher cards takes both piles (six cards).")
        print("If the turned-up cards are again the same rank, each player places another 2 cards face down and turns another card face up. The player with the higher card takes all 12 cards, plus the previous two cards tha led to the war,and so on")
        print("\nHOW TO KEEP SCORE\n")
        print("The game ends when one player has won all the cards")
        print("\n----------------------------------------------------------------------------------------------------------\n")

        rules = input("Type [--resume] to continue with the Game: ")
        if rules == "--resume":
            flag =  False
            

    

def playerOneMode():
    playerOneDeck = []
    playerTwoDeck = []
    clearTheScreen()
    appHeader()
    isGameOn = True
    round=1
    faceCardsDictionary = {"A":15, "J":12, "Q":11, "K":13, "10":10,"9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}
    cardDeck = CreateDeck()
    print("\n[+] - Card Deck created")
    print("[+] - Card Deck Shuffled")
    for i in range(26):
        card1 = cardDeck.pop()
        playerOneDeck.append(card1)
    for i in range(26):
        card1 = cardDeck.pop()
        playerTwoDeck.append(card1)
    print("[+] - Players Decks are Created")
    name = input("Player 1 please enter your name: ")
    Player1 = Player(name, playerOneDeck)
    Player2 = Player("Cisco Bot",playerTwoDeck)
    while(isGameOn):
        print(f"\n[+] - Round {round}\n----------------------------------\n")
        if len(playerOneDeck) == 0 or len(playerTwoDeck) == 0:
            isGameOn = False
        else: 
            print(Player1.name, " Total Cards: ", len(Player1.getPlayerDeck()))
            print(Player2.name, " Total Cards: ", len(Player2.getPlayerDeck()))
            sleep(1)
            player1BattleCard = playerOneDeck.pop(0)
            computerBattleCard = playerTwoDeck.pop(0)
            print("[+]",Player1.name, "Card: ",player1BattleCard)
            key1 = player1BattleCard[0]
            if key1 == "1":
                 Player1RoundPoints = faceCardsDictionary["10"]
            else:
                Player1RoundPoints = faceCardsDictionary[key1]
            print("[+]",Player2.name, "Card : ", computerBattleCard)
            key2 = computerBattleCard[0]
            if key2 == "1":
                 Player2RoundPoints = faceCardsDictionary["10"]
            else:
                Player2RoundPoints = faceCardsDictionary[key2]
            sleep(2)
            if Player1RoundPoints > Player2RoundPoints:
                print("[+]", Player1.name, "WON THE ROUND")
                playerOneDeck.append(player1BattleCard)
                playerOneDeck.append(computerBattleCard)
                rules = input("Wish to view the game Rules? [type --help] or hit [ENTER] to start next round: ")
                if rules == "--help":
                    GameRules()
            elif Player1RoundPoints < Player2RoundPoints:
                print("[+]", Player2.name, " WON THE ROUND")
                playerTwoDeck.append(computerBattleCard)
                playerTwoDeck.append(player1BattleCard)
                rules = input("Wish to view the game Rules? [type --help] or hit [ENTER] to start next round: ")
                if rules == "--help":
                    GameRules()
            else:
                battle = True
                player1BattleDeck =[]
                computerBattleDeck = []
                while(battle):
                    print("[+] - Going To Battle")
                    for i in range(3):
                        player1BattleDeck.append(playerOneDeck.pop(0))
                        computerBattleDeck.append(playerTwoDeck.pop(0))
                    BattleCard1 = player1BattleDeck[-1]
                    BattleCard2 = computerBattleDeck[-1]
                    print("[+]",Player1.name, "Card: ",BattleCard1)
                    key1 = BattleCard1[0]
                    if key1 == "1":
                        Player1RoundPoints = faceCardsDictionary["10"]
                    else:
                        Player1RoundPoints = faceCardsDictionary[key1]
                    print("[+]",Player2.name, "Card : ", BattleCard2)
                    key2 = BattleCard2[0]
                    if key2 == "1":
                        Player2RoundPoints = faceCardsDictionary["10"]
                    else:
                        Player2RoundPoints = faceCardsDictionary[key2]
                    if  Player1RoundPoints > Player2RoundPoints:
                        print("[+]", Player1.name, "WON THE ROUND")
                        for card in player1BattleDeck:
                            playerOneDeck.append(card)
                        for card in computerBattleDeck:
                            playerOneDeck.append(card)
                        playerOneDeck.append(player1BattleCard)
                        playerOneDeck.append(computerBattleCard)
                        battle = False
                        rules = input("Wish to view the game Rules? [type --help] or hit [ENTER] to start next round: ")
                        if rules == "--help":
                            GameRules()
                        break
                    elif Player1RoundPoints < Player2RoundPoints:
                        print("[+]", Player2.name, " WON THE ROUND")
                        for card in player1BattleDeck:
                            playerTwoDeck.append(card)
                        for card in computerBattleDeck:
                            playerTwoDeck.append(card)
                        playerTwoDeck.append(player1BattleCard)
                        playerTwoDeck.append(computerBattleCard)
                        battle = False
                        rules = input("Wish to view the game Rules? [type --help] or hit [ENTER] to start next round: ")
                        if rules == "--help":
                            GameRules()
                        break
                    else:
                        battle = True
                        continue
     
        if playerOneDeck == 0:
            clearTheScreen()
            appHeader()
            print("\n[+] -", Player2.name, " WON THE WAR GAME")
            isGameOn =  False
            break
            

        if playerTwoDeck == 0:
            clearTheScreen()
            appHeader()
            print("\n[+] -", Player2.name, " WON THE WAR GAME")
            isGameOn =  False
            break
        round += 1

    

def playTurn(player1, computer):
    player1BattleCard = player1.deck.pop()
    computerBattleCard = computer.deck.pop()
    player1BattleDeck =[]
    computerBattleDeck = []
    faceCardsDictionary = {"A":15, "J":12, "Q":11, "K":13, "10":10,"9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}
    print(player1.name, "Card: ",player1BattleCard)
    key1 = player1BattleCard[0]
    Player1RoundPoints = faceCardsDictionary[key1]
    print("PLAYER1 POINTS: ", Player1RoundPoints)
    print( computer.name, "Card : ", computerBattleCard)
    key2 = computerBattleCard[0]
    Player2RoundPoints = faceCardsDictionary[key2]
    print("PLAYER2 POINTS: ", Player2RoundPoints)
    sleep(2)
    if Player1RoundPoints > Player2RoundPoints:
        player1.addCardToDeck(player1BattleCard)
        player1.addCardToDeck(computerBattleCard)
    elif Player1RoundPoints < Player2RoundPoints:
        computer.addCardToDeck(computerBattleCard)
        computer.addCardToDeck(player1BattleCard)
    else:
        battle = True
        print("[+] - Going To Battle")

    return player1.getPlayerDeck(), computer.getPlayerDeck()



class Player:
    def __init__(self, name, deck=[]):
        self.name = name
        self.deck = deck 
            
    def setPlayerDeck(self, newDeck):
        self.deck = newDeck

    def getPlayerDeck(self):
        return self.deck

    def addCardToDeck(self, card):
        self.deck.append(card)

    def resetDeck(self):
        self.deck = []


while(True): 
    gameModes()