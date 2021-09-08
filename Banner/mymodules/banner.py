import time
import sys
import os
from termcolor import colored
from datetime import date

                                                         
def banner():
    todays_date = date.today()
    for index in range(80):
        print(colored("-", "yellow"), end="")
    print("")
    print(colored("https://www.youtube.com/channel/UCLNgMNfdksu_r5cwlplenBg\t"+ todays_date.strftime("%B").upper() +" - "+ str(todays_date.year),"cyan"))
    for index in range(80):
        print(colored("-", "yellow"), end="")
    print()
    print(colored("       _                 ____ _____  __  ____            _   _       _ _ ", "red"))
    print(colored("      | |__  _   _      |  _ \___ / / _|/ ___|___  _ __ | \ | |_   _| | |", "red"))
    print(colored("      | '_ \| | | |     | | | ||_ \| |_| |   / _ \| '_ \|  \| | | | | | |", "red"))
    print(colored("      | |_) | |_| |     | |_| |__) |  _| |__| (_) | | | | |\  | |_| | | |", "red"))
    print(colored("      |_.__/ \__, |     |____/____/|_|  \____\___/|_| |_|_| \_|\__,_|_|_|", "red"))
    print(colored("              |___/ ", "red"))

    for index in range(80):
        print(colored("-", "yellow"), end="")
    print("")
    print(colored(sys.version, "cyan"))
    for index in range(80):
        print(colored("-", "yellow"), end="")
        
    print()


#banner()