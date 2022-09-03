
## Rock paper scissors game
# Author : MRKN
# Purpose : A small python rock paper scissors game
# Created : 2022-03-28


import random

choises = ["r","p","s"]


while True:
    playAgain = False
    youWin = False
    compChoise = random.choice(choises)
    # print(f"Computer choise {compChoise}")

    yourChoise = input("Your choise?")

    if yourChoise not in choises:
        print("Not a valid option, try again")
        continue

    if (yourChoise == compChoise):
        print(f"You tied {yourChoise} = {compChoise}")
        continue

    if (compChoise == "r"):
        if yourChoise == "p":
            print(f"You win {yourChoise} beats {compChoise}")
            youWin = True 
            continue

    if (compChoise == "p"):
        if yourChoise == "s":
            print(f"You win {yourChoise} beats {compChoise}")
            youWin = True 
            continue

    if (compChoise == "s"):
        if yourChoise == "r":
            print(f"You win {yourChoise} beats {compChoise}")
            youWin = True 
            continue
        
    if ( not youWin):
        print(f"You loose {compChoise} beats {yourChoise}")
        
        playAgainChoise = input("Play again ?")
        if (playAgainChoise == "y"):
            playAgain = True
        else:
            break
    continue


